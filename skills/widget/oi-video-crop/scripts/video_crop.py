#!/usr/bin/env python3
"""Crop a local video with ffmpeg using a pivot axis and pixel trim.

Examples:
  python3 video_crop.py --input ~/Movies/clip.mp4 --info-only
  python3 video_crop.py --input clip.mp4 --axis "CENTER TOP" --crop-height 340
  python3 video_crop.py --input clip.mp4 --axis "LEFT CENTER" --crop-width 200
  python3 video_crop.py --input clip.mp4 --axis "CENTER TOP" --crop-width 100 --crop-height 340 --preview
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


MIN_PYTHON = (3, 9)


@dataclass(frozen=True)
class VideoInfo:
    path: Path
    width: int
    height: int
    duration_sec: float | None
    codec: str | None


@dataclass(frozen=True)
class CropPlan:
    out_w: int
    out_h: int
    x: int
    y: int


def _require_python() -> None:
    if sys.version_info < MIN_PYTHON:
        ver = ".".join(map(str, sys.version_info[:3]))
        print(
            f"Error: Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ required (found {ver}).",
            file=sys.stderr,
        )
        sys.exit(1)


def _which(cmd: str) -> str | None:
    return shutil.which(cmd)


def _default_desktop() -> Path:
    home = Path.home()
    for name in ("Desktop", "桌面"):
        p = home / name
        if p.is_dir():
            return p
    return home


def _expand_path(raw: str) -> Path:
    return Path(os.path.expanduser(raw)).resolve()


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def probe_video(path: Path) -> VideoInfo:
    if not path.is_file():
        raise FileNotFoundError(f"Video not found: {path}")

    ffprobe = _which("ffprobe")
    if not ffprobe:
        raise RuntimeError("ffprobe not found. Install ffmpeg: https://ffmpeg.org/download.html")

    cmd = [
        ffprobe,
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,codec_name",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(path),
    ]
    proc = _run(cmd)
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "unknown error").strip()
        raise RuntimeError(f"ffprobe failed: {err}")

    data = json.loads(proc.stdout or "{}")
    streams = data.get("streams") or []
    if not streams:
        raise RuntimeError("No video stream found in file")

    stream = streams[0]
    width = int(stream["width"])
    height = int(stream["height"])
    codec = stream.get("codec_name")
    duration_raw = (data.get("format") or {}).get("duration")
    duration = float(duration_raw) if duration_raw not in (None, "N/A") else None

    return VideoInfo(path=path, width=width, height=height, duration_sec=duration, codec=codec)


def parse_axis(axis: str) -> tuple[str, str]:
    """Parse axis like 'CENTER TOP' -> (horizontal, vertical)."""
    tokens = [t.strip().upper() for t in axis.replace(",", " ").split() if t.strip()]
    if not tokens:
        raise ValueError("Axis must not be empty")

    horiz = {"LEFT", "CENTER", "CENTRE", "RIGHT"}
    vert = {"TOP", "CENTER", "CENTRE", "BOTTOM"}

    h_align: str | None = None
    v_align: str | None = None
    for t in tokens:
        if t == "CENTRE":
            t = "CENTER"
        if t in horiz:
            h_align = t
        elif t in vert:
            v_align = t
        else:
            raise ValueError(f"Unknown axis token: {t}")

    if h_align is None:
        h_align = "CENTER"
    if v_align is None:
        v_align = "CENTER"

    return h_align, v_align


def compute_crop(
    src_w: int,
    src_h: int,
    *,
    crop_width: int = 0,
    crop_height: int = 0,
    out_width: int | None = None,
    out_height: int | None = None,
    h_align: str = "CENTER",
    v_align: str = "CENTER",
) -> CropPlan:
    """Compute ffmpeg crop rectangle from trim pixels or explicit output size."""
    if crop_width < 0 or crop_height < 0:
        raise ValueError("Crop pixels must be non-negative")

    if out_width is None:
        out_w = src_w - crop_width
    else:
        out_w = out_width

    if out_height is None:
        out_h = src_h - crop_height
    else:
        out_h = out_height

    if out_w <= 0 or out_h <= 0:
        raise ValueError(
            f"Output size invalid: {out_w}x{out_h}. "
            f"Source is {src_w}x{src_h}; reduce crop amount."
        )
    if out_w > src_w or out_h > src_h:
        raise ValueError(
            f"Output {out_w}x{out_h} exceeds source {src_w}x{src_h}."
        )

    trim_w = src_w - out_w
    trim_h = src_h - out_h

    if h_align == "LEFT":
        x = 0
    elif h_align == "RIGHT":
        x = trim_w
    else:
        x = trim_w // 2

    if v_align == "TOP":
        y = 0
    elif v_align == "BOTTOM":
        y = trim_h
    else:
        y = trim_h // 2

    return CropPlan(out_w=out_w, out_h=out_h, x=x, y=y)


def format_info(info: VideoInfo) -> str:
    dur = f"{info.duration_sec:.2f}s" if info.duration_sec is not None else "unknown"
    codec = info.codec or "unknown"
    return (
        f"File: {info.path}\n"
        f"Size: {info.width}x{info.height} px\n"
        f"Duration: {dur}\n"
        f"Codec: {codec}"
    )


def crop_video(
    info: VideoInfo,
    plan: CropPlan,
    output_path: Path,
    *,
    reencode: bool = True,
) -> None:
    ffmpeg = _which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg not found. Install ffmpeg: https://ffmpeg.org/download.html")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    vf = f"crop={plan.out_w}:{plan.out_h}:{plan.x}:{plan.y}"

    cmd: list[str] = [ffmpeg, "-y", "-i", str(info.path), "-vf", vf]
    if reencode:
        cmd += ["-c:v", "libx264", "-preset", "fast", "-crf", "18", "-c:a", "copy"]
    else:
        cmd += ["-c", "copy"]
    cmd.append(str(output_path))

    proc = _run(cmd)
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "unknown error").strip()
        raise RuntimeError(f"ffmpeg failed: {err[-2000:]}")


def default_output_path(input_path: Path, out_dir: Path, plan: CropPlan) -> Path:
    stem = input_path.stem
    suffix = input_path.suffix or ".mp4"
    name = f"{stem}_crop_{plan.out_w}x{plan.out_h}{suffix}"
    return out_dir / name


def apply_dimension_preset(
    dimension: str | None,
    pixels: int | None,
    crop_width: int,
    crop_height: int,
) -> tuple[int, int]:
    """Map --dimension + --pixels into crop_width / crop_height."""
    if dimension is None:
        return crop_width, crop_height
    if pixels is None or pixels <= 0:
        raise ValueError("--dimension requires --pixels > 0")

    dim = dimension.strip().lower()
    if dim in ("width", "w", "horizontal", "x"):
        return pixels, crop_height
    if dim in ("height", "h", "vertical", "y"):
        return crop_width, pixels
    if dim in ("both", "all", "wh", "xy"):
        return pixels, pixels
    raise ValueError(
        f"Unknown --dimension {dimension!r}; use width, height, or both"
    )


def build_crop_summary(
    info: VideoInfo,
    plan: CropPlan,
    *,
    axis: str,
    crop_width: int,
    crop_height: int,
    output_path: Path | None,
    preview: bool,
) -> dict[str, object]:
    trim_w = info.width - plan.out_w
    trim_h = info.height - plan.out_h
    parts: list[str] = []
    if crop_width > 0 or trim_w > 0:
        parts.append(f"width −{crop_width or trim_w}px → {plan.out_w}px")
    if crop_height > 0 or trim_h > 0:
        parts.append(f"height −{crop_height or trim_h}px → {plan.out_h}px")
    return {
        "preview": preview,
        "input": str(info.path),
        "source_width": info.width,
        "source_height": info.height,
        "source_size": f"{info.width}x{info.height}",
        "axis": axis,
        "crop_width_px": crop_width,
        "crop_height_px": crop_height,
        "trim_width_px": trim_w,
        "trim_height_px": trim_h,
        "output_width": plan.out_w,
        "output_height": plan.out_h,
        "output_size": f"{plan.out_w}x{plan.out_h}",
        "crop_filter": f"crop={plan.out_w}:{plan.out_h}:{plan.x}:{plan.y}",
        "crop_offset": {"x": plan.x, "y": plan.y},
        "changes": parts,
        "output": str(output_path) if output_path else None,
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Probe and crop local videos with ffmpeg.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Axis examples:\n"
            "  CENTER TOP     — width centered, height anchored to top\n"
            "  LEFT BOTTOM    — width left, height anchored to bottom\n"
            "  CENTER CENTER  — trim evenly on both sides\n"
        ),
    )
    p.add_argument("--input", "-i", help="Path to input video")
    p.add_argument(
        "--check-env",
        action="store_true",
        help="Check Python/ffmpeg (no input required)",
    )
    p.add_argument(
        "--install",
        action="store_true",
        help="With --check-env: auto-install missing deps then re-check",
    )
    p.add_argument(
        "--info-only",
        action="store_true",
        help="Only print video dimensions (no crop)",
    )
    p.add_argument(
        "--preview",
        action="store_true",
        help="Compute crop plan and output path without running ffmpeg",
    )
    p.add_argument(
        "--axis",
        default="CENTER CENTER",
        help='Pivot for crop window, e.g. "CENTER TOP" (default: CENTER CENTER)',
    )
    p.add_argument(
        "--crop-height",
        type=int,
        default=0,
        metavar="PX",
        help="Pixels to remove from height (output height = source - PX)",
    )
    p.add_argument(
        "--crop-width",
        type=int,
        default=0,
        metavar="PX",
        help="Pixels to remove from width (output width = source - PX)",
    )
    p.add_argument(
        "--dimension",
        choices=["width", "height", "both"],
        help="Shorthand: apply --pixels to width, height, or both axes",
    )
    p.add_argument(
        "--pixels",
        type=int,
        metavar="PX",
        help="Pixel amount for --dimension (width / height / both)",
    )
    p.add_argument("--out-width", type=int, help="Explicit output width (overrides crop-width)")
    p.add_argument("--out-height", type=int, help="Explicit output height (overrides crop-height)")
    p.add_argument(
        "--output-dir",
        "-o",
        help="Output directory (default: Desktop)",
    )
    p.add_argument("--output", help="Full output file path (overrides --output-dir)")
    p.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON on stdout",
    )
    p.add_argument(
        "--copy",
        action="store_true",
        help="Stream copy when possible (may fail for crop; default re-encodes)",
    )
    return p


def _run_check_env(json_out: bool, install: bool = False) -> int:
    check_script = Path(__file__).resolve().parent / "check_env.py"
    if not check_script.is_file():
        print("Error: check_env.py not found beside video_crop.py", file=sys.stderr)
        return 1
    cmd = [sys.executable, str(check_script)]
    if install:
        cmd.append("--install")
    if json_out:
        cmd.append("--json")
    proc = _run(cmd)
    if proc.stdout:
        print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n")
    if proc.stderr:
        print(proc.stderr, file=sys.stderr, end="" if proc.stderr.endswith("\n") else "\n")
    return proc.returncode if proc.returncode is not None else 1


def main(argv: list[str] | None = None) -> int:
    _require_python()
    args = build_parser().parse_args(argv)

    if args.check_env:
        return _run_check_env(json_out=args.json, install=args.install)

    if not args.input:
        print("Error: --input is required unless using --check-env.", file=sys.stderr)
        return 1

    input_path = _expand_path(args.input)
    try:
        info = probe_video(input_path)
    except (FileNotFoundError, RuntimeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if args.info_only:
        payload = {
            "input": str(info.path),
            "width": info.width,
            "height": info.height,
            "duration_sec": info.duration_sec,
            "codec": info.codec,
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(format_info(info))
        return 0

    try:
        crop_width, crop_height = apply_dimension_preset(
            args.dimension,
            args.pixels,
            args.crop_width,
            args.crop_height,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if (
        crop_height == 0
        and crop_width == 0
        and args.out_width is None
        and args.out_height is None
    ):
        print(
            "Error: specify crop via --crop-width / --crop-height, "
            "--dimension + --pixels, or --out-width / --out-height.",
            file=sys.stderr,
        )
        return 1

    try:
        h_align, v_align = parse_axis(args.axis)
        plan = compute_crop(
            info.width,
            info.height,
            crop_width=crop_width,
            crop_height=crop_height,
            out_width=args.out_width,
            out_height=args.out_height,
            h_align=h_align,
            v_align=v_align,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if args.output:
        output_path = _expand_path(args.output)
    else:
        out_dir = _expand_path(args.output_dir) if args.output_dir else _default_desktop()
        output_path = default_output_path(input_path, out_dir, plan)

    summary = build_crop_summary(
        info,
        plan,
        axis=args.axis,
        crop_width=crop_width,
        crop_height=crop_height,
        output_path=output_path,
        preview=args.preview,
    )

    if args.preview:
        if args.json:
            print(json.dumps(summary, ensure_ascii=False, indent=2))
        else:
            print("Crop plan (preview — ffmpeg not run):")
            print(f"  Source:  {summary['source_size']} px")
            if crop_width:
                print(f"  Width:   remove {crop_width} px → {plan.out_w} px")
            if crop_height:
                print(f"  Height:  remove {crop_height} px → {plan.out_h} px")
            print(f"  Axis:    {args.axis}")
            print(f"  Output:  {summary['output_size']} px")
            print(f"  Filter:  {summary['crop_filter']}")
            print(f"  Save to: {output_path}")
        return 0

    try:
        crop_video(info, plan, output_path, reencode=not args.copy)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    summary["preview"] = False
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print("Crop complete.")
        print(f"  Source:  {info.width}x{info.height} px")
        if crop_width:
            print(f"  Width:   −{crop_width} px")
        if crop_height:
            print(f"  Height:  −{crop_height} px")
        print(f"  Axis:    {args.axis}")
        print(f"  Output:  {plan.out_w}x{plan.out_h} px")
        print(f"  File:    {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
