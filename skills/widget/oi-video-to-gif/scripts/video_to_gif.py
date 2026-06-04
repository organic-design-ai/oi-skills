#!/usr/bin/env python3
"""Convert local MP4/MOV to high-quality GIF (palettegen + lanczos scale)."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

VIDEO_SUFFIXES = frozenset({".mp4", ".mov", ".m4v", ".webm"})

DEFAULT_SAMPLE_EVERY = 2
DEFAULT_FRAME_DELAY = 0
DEFAULT_SCALE = 1.0
DEFAULT_LOSS = 0.0


@dataclass(frozen=True)
class CropPlan:
    out_w: int
    out_h: int
    x: int
    y: int


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    creationflags = 0
    if sys.platform == "win32":
        creationflags = subprocess.CREATE_NO_WINDOW  # type: ignore[attr-defined]
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=creationflags,
    )


def resolve_tool(name: str, explicit: str | None) -> str:
    if explicit:
        p = Path(explicit).expanduser()
        if p.is_file():
            return str(p.resolve())
        raise SystemExit(f"{name} not found: {explicit}")
    found = shutil.which(name)
    if found:
        return found
    raise SystemExit(f"{name} not found on PATH. Install ffmpeg (includes ffprobe).")


def probe_video(ffprobe: str, path: Path) -> dict[str, Any]:
    cmd = [
        ffprobe,
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,duration,r_frame_rate",
        "-of",
        "json",
        str(path),
    ]
    proc = _run(cmd)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout or "ffprobe failed").strip())
    data = json.loads(proc.stdout or "{}")
    streams = data.get("streams") or []
    if not streams:
        raise RuntimeError("no video stream")
    s = streams[0]
    width = int(s.get("width") or 0)
    height = int(s.get("height") or 0)
    duration = float(s.get("duration") or 0)
    rate = s.get("r_frame_rate") or "0/1"
    if "/" in str(rate):
        num, den = str(rate).split("/", 1)
        fps_src = float(num) / float(den) if float(den) else 0.0
    else:
        fps_src = float(rate)
    return {
        "width": width,
        "height": height,
        "duration": duration,
        "source_fps": round(fps_src, 3),
    }


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
    if crop_width < 0 or crop_height < 0:
        raise ValueError("Crop pixels must be non-negative")

    out_w = src_w - crop_width if out_width is None else out_width
    out_h = src_h - crop_height if out_height is None else out_height

    if out_w <= 0 or out_h <= 0:
        raise ValueError(
            f"Output size invalid: {out_w}x{out_h}. "
            f"Source is {src_w}x{src_h}; reduce crop amount."
        )
    if out_w > src_w or out_h > src_h:
        raise ValueError(f"Output {out_w}x{out_h} exceeds source {src_w}x{src_h}.")

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


def apply_dimension_preset(
    dimension: str | None,
    pixels: int | None,
    crop_width: int,
    crop_height: int,
) -> tuple[int, int]:
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
    raise ValueError(f"Unknown --dimension {dimension!r}; use width, height, or both")


def crop_requested(args: argparse.Namespace) -> bool:
    return bool(
        args.crop_width
        or args.crop_height
        or args.dimension
        or args.out_width is not None
        or args.out_height is not None
    )


def resolve_crop_plan(
    src_w: int,
    src_h: int,
    args: argparse.Namespace,
) -> CropPlan | None:
    if not crop_requested(args):
        return None
    crop_width, crop_height = apply_dimension_preset(
        args.dimension,
        args.pixels,
        args.crop_width,
        args.crop_height,
    )
    if (
        crop_width == 0
        and crop_height == 0
        and args.out_width is None
        and args.out_height is None
    ):
        raise SystemExit(
            "Crop requested but no amount set. Use --crop-width / --crop-height, "
            "--dimension + --pixels, or --out-width / --out-height."
        )
    h_align, v_align = parse_axis(args.axis)
    return compute_crop(
        src_w,
        src_h,
        crop_width=crop_width,
        crop_height=crop_height,
        out_width=args.out_width,
        out_height=args.out_height,
        h_align=h_align,
        v_align=v_align,
    )


def crop_summary_dict(
    *,
    source_w: int,
    source_h: int,
    plan: CropPlan,
    axis: str,
    crop_width: int,
    crop_height: int,
) -> dict[str, Any]:
    return {
        "axis": axis,
        "crop_width_px": crop_width,
        "crop_height_px": crop_height,
        "source_size": f"{source_w}x{source_h}",
        "output_size": f"{plan.out_w}x{plan.out_h}",
        "crop_filter": f"crop={plan.out_w}:{plan.out_h}:{plan.x}:{plan.y}",
        "crop_offset": {"x": plan.x, "y": plan.y},
    }


def playback_fps(frame_delay: float) -> float:
    """Target GIF display rate (1/delay); informational only — does not resample frames."""
    if frame_delay <= 0:
        raise ValueError("frame_delay must be > 0")
    return 1.0 / frame_delay


def timing_applied(frame_delay: float) -> bool:
    return frame_delay > 0


def output_width(src_width: int, scale: float, explicit_width: int | None) -> int:
    if explicit_width is not None and explicit_width > 0:
        return explicit_width
    return max(2, int(round(src_width * scale)))


def sample_drop_cycles(sample_every: int) -> int:
    """抽帧 N: apply「每连续两帧保留、去掉一帧」cycle (N-1) times; N=1 => 0."""
    return max(0, sample_every - 1)


def frame_keep_ratio(sample_every: int) -> float:
    """Approximate fraction of source frames kept after drop cycles."""
    cycles = sample_drop_cycles(sample_every)
    if cycles == 0:
        return 1.0
    return (2.0 / 3.0) ** cycles


def loss_palette_settings(loss: float) -> tuple[int, str, str]:
    loss = max(0.0, min(1.0, loss))
    max_colors = int(round(256 - loss * (256 - 48)))
    max_colors = max(16, min(256, max_colors))

    if loss <= 0.05:
        palettegen = f"palettegen=max_colors={max_colors}:stats_mode=full"
        paletteuse = "paletteuse=dither=none"
    elif loss <= 0.45:
        bayer = max(1, int(round(1 + loss * 4)))
        palettegen = f"palettegen=max_colors={max_colors}:stats_mode=full"
        paletteuse = f"paletteuse=dither=bayer:bayer_scale={bayer}"
    else:
        bayer = max(3, int(round(3 + loss * 2)))
        palettegen = f"palettegen=max_colors={max_colors}"
        paletteuse = f"paletteuse=dither=bayer:bayer_scale={bayer}"

    return max_colors, palettegen, paletteuse


# One cycle: among each block of 3 source frames, drop the 3rd (keep 2, drop 1).
_DROP_ONE_EVERY_THREE = "select='not(eq(mod(n\\,3),2))',setpts=N/FRAME_RATE/TB"


def build_drop_filters(sample_every: int) -> str:
    """Step 1: drop cycles only (no timing / fps)."""
    cycles = sample_drop_cycles(sample_every)
    if cycles == 0:
        return ""
    return ",".join([_DROP_ONE_EVERY_THREE] * cycles) + ","


def build_timing_filter(frame_delay: float) -> str:
    """Step 5 (last): stretch PTS so each frame lasts frame_delay seconds (no drop/duplicate)."""
    if not timing_applied(frame_delay):
        return ""
    # After drop step, frames are spaced 1/FRAME_RATE apart; scale to frame_delay per frame.
    return f"setpts=N*({frame_delay:.9f}*FRAME_RATE)/TB,"


def build_vf(
    *,
    sample_every: int,
    frame_delay: float,
    width: int,
    loss: float,
    crop_plan: CropPlan | None = None,
) -> str:
    """Filter order: drop → crop → scale → palette → setpts speed (last)."""
    _, palettegen, paletteuse = loss_palette_settings(loss)
    crop = (
        f"crop={crop_plan.out_w}:{crop_plan.out_h}:{crop_plan.x}:{crop_plan.y},"
        if crop_plan
        else ""
    )
    scale = f"scale={width}:-1:flags=lanczos,"
    palette = f"split[s0][s1];[s0]{palettegen}[p];[s1][p]{paletteuse},"
    return (
        f"{build_drop_filters(sample_every)}"
        f"{crop}"
        f"{scale}"
        f"{palette}"
        f"{build_timing_filter(frame_delay)}"
    ).rstrip(",")


def is_video(path: Path) -> bool:
    return path.suffix.lower() in VIDEO_SUFFIXES


def collect_videos(root: Path, recursive: bool) -> list[Path]:
    it = root.rglob("*") if recursive else root.glob("*")
    seen: set[Path] = set()
    out: list[Path] = []
    for f in it:
        if not f.is_file() or not is_video(f):
            continue
        try:
            key = f.resolve()
        except OSError:
            key = f
        if key in seen:
            continue
        seen.add(key)
        out.append(f)
    out.sort(key=lambda p: str(p).lower())
    return out


def unique_output(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suf, parent = path.stem, path.suffix, path.parent
    for i in range(1, 10000):
        candidate = parent / f"{stem}_{i}{suf}"
        if not candidate.exists():
            return candidate
    return path


def convert_one(
    ffmpeg: str,
    src: Path,
    out: Path,
    *,
    sample_every: int,
    frame_delay: float,
    width: int,
    loss: float,
    crop_plan: CropPlan | None = None,
) -> dict[str, Any]:
    vf = build_vf(
        sample_every=sample_every,
        frame_delay=frame_delay,
        width=width,
        loss=loss,
        crop_plan=crop_plan,
    )
    cmd = [
        ffmpeg,
        "-hide_banner",
        "-y",
        "-i",
        str(src),
        "-vf",
        vf,
        "-loop",
        "0",
        "-gifflags",
        "+transdiff",
        str(out),
    ]
    proc = _run(cmd)
    if proc.returncode != 0:
        tail = (proc.stderr or "").strip().splitlines()[-8:]
        msg = "\n".join(tail) if tail else f"exit {proc.returncode}"
        raise RuntimeError(msg)
    meta: dict[str, Any] = {
        "input": str(src),
        "output": str(out),
        "width": width,
        "sample_every": sample_every,
        "drop_cycles": sample_drop_cycles(sample_every),
        "frame_keep_ratio": round(frame_keep_ratio(sample_every), 4),
        "frame_delay": frame_delay,
        "playback_fps": round(playback_fps(frame_delay), 4) if timing_applied(frame_delay) else None,
        "timing": "setpts" if timing_applied(frame_delay) else "source",
        "loss": loss,
        "vf": vf,
    }
    if crop_plan:
        meta["crop"] = {
            "output_width": crop_plan.out_w,
            "output_height": crop_plan.out_h,
            "x": crop_plan.x,
            "y": crop_plan.y,
        }
    return meta


def gather_inputs(paths: list[str], recursive: bool) -> list[Path]:
    out: list[Path] = []
    for raw in paths:
        p = Path(raw).expanduser()
        if not p.exists():
            raise SystemExit(f"Not found: {p}")
        if p.is_file():
            if is_video(p):
                out.append(p)
            else:
                print(f"skip (not a supported video): {p}", file=sys.stderr)
        elif p.is_dir():
            out.extend(collect_videos(p, recursive))
    seen: set[Path] = set()
    unique: list[Path] = []
    for f in out:
        try:
            key = f.resolve()
        except OSError:
            key = f
        if key in seen:
            continue
        seen.add(key)
        unique.append(f)
    return unique


def add_crop_args(ap: argparse.ArgumentParser) -> None:
    ap.add_argument(
        "--axis",
        default="CENTER CENTER",
        help='Crop pivot, e.g. "CENTER TOP" (default: CENTER CENTER)',
    )
    ap.add_argument(
        "--crop-width",
        type=int,
        default=0,
        metavar="PX",
        help="Pixels to remove from width before GIF encode",
    )
    ap.add_argument(
        "--crop-height",
        type=int,
        default=0,
        metavar="PX",
        help="Pixels to remove from height before GIF encode",
    )
    ap.add_argument(
        "--dimension",
        choices=["width", "height", "both"],
        help="Shorthand: apply --pixels to width, height, or both",
    )
    ap.add_argument(
        "--pixels",
        type=int,
        metavar="PX",
        help="Pixel amount for --dimension",
    )
    ap.add_argument("--out-width", type=int, help="Explicit cropped width (overrides --crop-width)")
    ap.add_argument(
        "--out-height",
        type=int,
        help="Explicit cropped height (overrides --crop-height)",
    )
    ap.add_argument(
        "--preview",
        action="store_true",
        help="Show conversion/crop plan only; do not encode GIF",
    )


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Convert MP4/MOV to high-quality GIF (oi-video-to-gif skill)."
    )
    ap.add_argument("inputs", nargs="*", help="Video file(s) or folder(s)")
    ap.add_argument(
        "--sample-every",
        type=int,
        default=DEFAULT_SAMPLE_EVERY,
        help=(
            "抽帧等级 (default %(default)s): 1=不抽帧; "
            "N≥2=重复 (N-1) 次「每连续两帧保留、去掉一帧」"
        ),
    )
    ap.add_argument(
        "--frame-delay",
        type=float,
        default=DEFAULT_FRAME_DELAY,
        help=(
            f"Seconds per GIF frame at playback (default {DEFAULT_FRAME_DELAY:g} = "
            "keep timing; >0 uses setpts last — speed only, same frame count)"
        ),
    )
    ap.add_argument(
        "--scale",
        type=float,
        default=DEFAULT_SCALE,
        help=f"Proportional resize vs cropped/source width (default {DEFAULT_SCALE})",
    )
    ap.add_argument(
        "--width",
        type=int,
        default=None,
        help="Explicit output width in px (overrides --scale)",
    )
    ap.add_argument(
        "--loss",
        type=float,
        default=DEFAULT_LOSS,
        help=f"Quality loss 0=best, 1=max compression (default {DEFAULT_LOSS})",
    )
    ap.add_argument("-o", "--output-dir", type=Path, default=None, help="Output directory")
    ap.add_argument("-r", "--recursive", action="store_true", help="Scan subfolders")
    ap.add_argument("--ffmpeg", default=None, help="Path to ffmpeg")
    ap.add_argument("--ffprobe", default=None, help="Path to ffprobe")
    ap.add_argument("--info-only", action="store_true", help="Probe input only, no convert")
    ap.add_argument("--check-env", action="store_true", help="Run env check and exit")
    ap.add_argument(
        "--self-test",
        action="store_true",
        help="Run built-in filter-chain checks and exit",
    )
    ap.add_argument("--json", action="store_true", help="JSON stdout for plans/results")
    add_crop_args(ap)
    return ap


def run_self_test() -> None:
    drop = build_drop_filters(2)
    assert _DROP_ONE_EVERY_THREE in drop
    assert build_drop_filters(1) == ""
    assert build_timing_filter(0) == ""
    timing = build_timing_filter(0.1)
    assert timing == "setpts=N*(0.100000000*FRAME_RATE)/TB,"
    assert "fps=" not in timing

    vf = build_vf(sample_every=2, frame_delay=0.1, width=320, loss=0)
    assert vf.index("select=") < vf.index("scale=") < vf.index("palettegen") < vf.rindex("setpts=N*")

    vf_crop = build_vf(
        sample_every=2,
        frame_delay=0.05,
        width=160,
        loss=0,
        crop_plan=CropPlan(out_w=100, out_h=80, x=10, y=5),
    )
    assert vf_crop.index("paletteuse") < vf_crop.rindex("setpts=N*")

    vf_source = build_vf(sample_every=2, frame_delay=0, width=320, loss=0)
    assert vf_source.count("setpts=") == 1  # only inside drop chain


def plan_row(
    src: Path,
    info: dict[str, Any],
    args: argparse.Namespace,
    crop_plan: CropPlan | None,
) -> dict[str, Any]:
    base_w = crop_plan.out_w if crop_plan else info["width"]
    w = output_width(base_w, args.scale, args.width)
    row: dict[str, Any] = {
        "file": str(src.resolve()),
        **info,
        "output_width": w,
        "sample_every": args.sample_every,
        "drop_cycles": sample_drop_cycles(args.sample_every),
        "frame_keep_ratio": round(frame_keep_ratio(args.sample_every), 4),
        "frame_delay": args.frame_delay,
        "playback_fps": (
            round(playback_fps(args.frame_delay), 4) if timing_applied(args.frame_delay) else None
        ),
        "timing": "setpts" if timing_applied(args.frame_delay) else "source",
        "scale": args.scale,
        "loss": args.loss,
    }
    if crop_plan:
        cw, ch = apply_dimension_preset(
            args.dimension, args.pixels, args.crop_width, args.crop_height
        )
        row["crop"] = crop_summary_dict(
            source_w=info["width"],
            source_h=info["height"],
            plan=crop_plan,
            axis=args.axis,
            crop_width=cw,
            crop_height=ch,
        )
    return row


def main() -> int:
    args = build_parser().parse_args()

    if args.self_test:
        run_self_test()
        print("self-test ok")
        return 0

    if args.check_env:
        skill_dir = Path(__file__).resolve().parent
        check = skill_dir / "check_env.py"
        cmd = [sys.executable, str(check)]
        if "--json" in sys.argv or "-j" in sys.argv:
            cmd.append("--json")
        return subprocess.call(cmd)

    if args.sample_every < 1:
        raise SystemExit("sample-every must be >= 1 (1 = 不抽帧 / no drop cycles)")
    if args.scale <= 0:
        raise SystemExit("scale must be > 0")
    if not 0 <= args.loss <= 1:
        raise SystemExit("loss must be between 0 and 1")
    if args.frame_delay < 0:
        raise SystemExit("frame-delay must be >= 0 (0 = keep timing after drop/crop/scale)")

    ffmpeg = resolve_tool("ffmpeg", args.ffmpeg)
    ffprobe = resolve_tool("ffprobe", args.ffprobe)

    if not args.inputs:
        build_parser().print_help()
        return 0

    sources = gather_inputs(args.inputs, args.recursive)
    if not sources:
        raise SystemExit("No supported video files found (.mp4, .mov, .m4v, .webm).")

    if args.info_only or args.preview:
        rows = []
        for src in sources:
            info = probe_video(ffprobe, src.resolve())
            try:
                crop_plan = resolve_crop_plan(info["width"], info["height"], args)
            except ValueError as e:
                raise SystemExit(str(e)) from e
            rows.append(plan_row(src, info, args, crop_plan))
        payload = {"preview": args.preview, "videos": rows}
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            for row in rows:
                name = Path(row["file"]).name
                crop_note = ""
                if row.get("crop"):
                    crop_note = f" | crop {row['crop']['source_size']} -> {row['crop']['output_size']}"
                print(
                    f"{name}: {row['width']}x{row['height']} "
                    f"-> GIF width {row['output_width']}{crop_note} | "
                    f"抽帧={row['sample_every']} (cycles={row['drop_cycles']}, "
                    f"keep≈{row['frame_keep_ratio']:.0%}) | "
                    f"delay={row['frame_delay']}s ({row['timing']}) | loss={row['loss']}"
                )
                if args.preview and row.get("crop"):
                    print(f"  crop filter: {row['crop']['crop_filter']}")
        if args.preview:
            print("(preview only — no GIF written)")
        return 0

    if args.output_dir is not None:
        out_dir = args.output_dir.expanduser().resolve()
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = None

    results: list[dict[str, Any]] = []
    failed = 0
    for i, src in enumerate(sources, start=1):
        src = src.resolve()
        info = probe_video(ffprobe, src)
        try:
            crop_plan = resolve_crop_plan(info["width"], info["height"], args)
        except ValueError as e:
            raise SystemExit(str(e)) from e

        base_w = crop_plan.out_w if crop_plan else info["width"]
        width = output_width(base_w, args.scale, args.width)
        if out_dir is None:
            out = unique_output(src.with_suffix(".gif"))
        else:
            out = unique_output(out_dir / f"{src.stem}.gif")

        crop_tag = ""
        if crop_plan:
            crop_tag = f", crop={crop_plan.out_w}x{crop_plan.out_h}"
        label = (
            f"[{i}/{len(sources)}] {src.name} -> {out.name} "
            f"(w={width}, 抽帧={args.sample_every}{crop_tag}, "
            f"delay={args.frame_delay}s ({'setpts' if timing_applied(args.frame_delay) else 'source'}), "
            f"loss={args.loss})"
        )
        if not args.json:
            print(label)

        try:
            meta = convert_one(
                ffmpeg,
                src,
                out,
                sample_every=args.sample_every,
                frame_delay=args.frame_delay,
                width=width,
                loss=args.loss,
                crop_plan=crop_plan,
            )
            meta["output_size_bytes"] = out.stat().st_size if out.is_file() else 0
            results.append(meta)
        except RuntimeError as e:
            failed += 1
            err = {"input": str(src), "error": str(e)}
            results.append(err)
            print(f"  failed: {e}", file=sys.stderr)

    summary = {
        "ok": failed == 0,
        "converted": len(sources) - failed,
        "failed": failed,
        "defaults": {
            "sample_every": DEFAULT_SAMPLE_EVERY,
            "frame_delay": DEFAULT_FRAME_DELAY,
            "scale": DEFAULT_SCALE,
            "loss": DEFAULT_LOSS,
        },
        "results": results,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    elif failed:
        print(f"Done with {failed} failure(s).", file=sys.stderr)
        return 1
    else:
        print("Done.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
