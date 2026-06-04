#!/usr/bin/env python3
"""Combine local images into an animated GIF (pad + scale via ffmpeg)."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any

IMAGE_SUFFIXES = frozenset({".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff"})

DEFAULT_DELAY = 1.0
DEFAULT_SCALE = 1.0
DEFAULT_LOSS = 0.0
PAD_COLOR = "0x000000"


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


def probe_image(ffprobe: str, path: Path) -> dict[str, int]:
    cmd = [
        ffprobe,
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height",
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
        raise RuntimeError("no image stream")
    s = streams[0]
    width = int(s.get("width") or 0)
    height = int(s.get("height") or 0)
    if width <= 0 or height <= 0:
        raise RuntimeError(f"invalid dimensions for {path.name}")
    return {"width": width, "height": height}


def is_image(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_SUFFIXES


def natural_sort_key(path: Path) -> list[Any]:
    parts = re.split(r"(\d+)", path.name.lower())
    return [int(p) if p.isdigit() else p for p in parts]


def collect_images(root: Path, recursive: bool) -> list[Path]:
    it = root.rglob("*") if recursive else root.glob("*")
    files = [f for f in it if f.is_file() and is_image(f)]
    files.sort(key=natural_sort_key)
    return files


def gather_inputs(paths: list[str], recursive: bool) -> list[Path]:
    out: list[Path] = []
    for raw in paths:
        p = Path(raw).expanduser()
        if not p.exists():
            raise SystemExit(f"Not found: {p}")
        if p.is_file():
            if is_image(p):
                out.append(p.resolve())
            else:
                print(f"skip (not a supported image): {p}", file=sys.stderr)
        elif p.is_dir():
            found = collect_images(p, recursive)
            if not found:
                print(f"skip (no images in folder): {p}", file=sys.stderr)
            out.extend(f.resolve() for f in found)
    seen: set[Path] = set()
    unique: list[Path] = []
    for f in out:
        if f in seen:
            continue
        seen.add(f)
        unique.append(f)
    return unique


def resolve_canvas(
    first: dict[str, int],
    width: int | None,
    height: int | None,
) -> tuple[int, int]:
    fw, fh = first["width"], first["height"]
    if width is not None and height is not None:
        return width, height
    if width is not None:
        return width, max(2, int(round(fh * width / fw)))
    if height is not None:
        return max(2, int(round(fw * height / fh))), height
    return fw, fh


def apply_scale(canvas_w: int, canvas_h: int, scale: float) -> tuple[int, int]:
    return (
        max(2, int(round(canvas_w * scale))),
        max(2, int(round(canvas_h * scale))),
    )


def loss_palette_settings(loss: float) -> tuple[str, str]:
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
    return palettegen, paletteuse


def frame_filter(out_w: int, out_h: int) -> str:
    return (
        f"scale={out_w}:{out_h}:force_original_aspect_ratio=decrease:flags=lanczos,"
        f"pad={out_w}:{out_h}:(ow-iw)/2:(oh-ih)/2:color={PAD_COLOR},"
        "setsar=1,format=rgb24"
    )


def build_filter_complex(n: int, out_w: int, out_h: int, loss: float) -> str:
    ff = frame_filter(out_w, out_h)
    parts: list[str] = []
    labels: list[str] = []
    for i in range(n):
        parts.append(f"[{i}:v]{ff}[v{i}]")
        labels.append(f"[v{i}]")
    concat_in = "".join(labels)
    palettegen, paletteuse = loss_palette_settings(loss)
    parts.append(f"{concat_in}concat=n={n}:v=1:a=0,format=rgb24,split[s0][s1]")
    parts.append(f"[s0]{palettegen}[p]")
    parts.append(f"[s1][p]{paletteuse}")
    return ";".join(parts)


def _default_desktop() -> Path:
    home = Path.home()
    for name in ("Desktop", "桌面"):
        p = home / name
        if p.is_dir():
            return p
    return home


def default_gif_basename() -> str:
    return f"oi-images-to-gif-{uuid.uuid4()}.gif"


def default_output_path(output_dir: Path | None = None) -> Path:
    parent = output_dir.expanduser().resolve() if output_dir is not None else _default_desktop()
    return parent / default_gif_basename()


def unique_output(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suf, parent = path.stem, path.suffix, path.parent
    for i in range(1, 10000):
        candidate = parent / f"{stem}_{i}{suf}"
        if not candidate.exists():
            return candidate
    return path


def build_plan(
    ffprobe: str,
    images: list[Path],
    args: argparse.Namespace,
) -> dict[str, Any]:
    probes = []
    for img in images:
        info = probe_image(ffprobe, img)
        probes.append({"file": str(img.resolve()), **info})

    canvas_w, canvas_h = resolve_canvas(probes[0], args.width, args.height)
    out_w, out_h = apply_scale(canvas_w, canvas_h, args.scale)

    if args.output is not None:
        out_path = args.output.expanduser().resolve()
    else:
        out_dir = args.output_dir.expanduser().resolve() if args.output_dir is not None else None
        out_path = default_output_path(out_dir)

    return {
        "frame_count": len(images),
        "images": probes,
        "canvas": {"width": canvas_w, "height": canvas_h},
        "output_size": {"width": out_w, "height": out_h},
        "delay_seconds": args.delay,
        "scale": args.scale,
        "loss": args.loss,
        "pad_color": PAD_COLOR,
        "output": str(out_path),
        "filter_complex": build_filter_complex(len(images), out_w, out_h, args.loss),
    }


def convert(
    ffmpeg: str,
    images: list[Path],
    out: Path,
    *,
    out_w: int,
    out_h: int,
    delay: float,
    loss: float,
) -> dict[str, Any]:
    n = len(images)
    if n == 0:
        raise ValueError("no images")
    if n > 128:
        raise ValueError("too many images (max 128 per GIF); split into batches")

    fc = build_filter_complex(n, out_w, out_h, loss)
    cmd: list[str] = [ffmpeg, "-hide_banner", "-y"]
    for img in images:
        cmd.extend(["-loop", "1", "-t", f"{delay:.6f}", "-i", str(img)])
    cmd.extend(
        [
            "-filter_complex",
            fc,
            "-an",
            "-gifflags",
            "+transdiff",
            str(out),
        ]
    )
    proc = _run(cmd)
    if proc.returncode != 0:
        tail = (proc.stderr or "").strip().splitlines()[-12:]
        msg = "\n".join(tail) if tail else f"exit {proc.returncode}"
        raise RuntimeError(msg)

    return {
        "output": str(out),
        "frame_count": n,
        "output_width": out_w,
        "output_height": out_h,
        "delay_seconds": delay,
        "loss": loss,
        "filter_complex": fc,
    }


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Combine local images into GIF (oi-images-to-gif skill)."
    )
    ap.add_argument(
        "inputs",
        nargs="*",
        help="Image file(s) and/or folder(s); folder images sorted by natural name",
    )
    ap.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY,
        help=f"Seconds each frame is shown (default {DEFAULT_DELAY})",
    )
    ap.add_argument(
        "--scale",
        type=float,
        default=DEFAULT_SCALE,
        help=f"Scale final canvas size (default {DEFAULT_SCALE})",
    )
    ap.add_argument(
        "--width",
        type=int,
        default=None,
        help="Canvas width in px (default: first image width)",
    )
    ap.add_argument(
        "--height",
        type=int,
        default=None,
        help="Canvas height in px (default: first image height)",
    )
    ap.add_argument(
        "--loss",
        type=float,
        default=DEFAULT_LOSS,
        help="Palette quality 0=best, 1=smallest (default 0)",
    )
    ap.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: Desktop; filename oi-images-to-gif-<uuid>.gif)",
    )
    ap.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Exact output .gif path (overrides default Desktop + UUID name)",
    )
    ap.add_argument("-r", "--recursive", action="store_true", help="Scan subfolders")
    ap.add_argument("--ffmpeg", default=None, help="Path to ffmpeg")
    ap.add_argument("--ffprobe", default=None, help="Path to ffprobe")
    ap.add_argument("--info-only", action="store_true", help="Plan only, no encode")
    ap.add_argument("--preview", action="store_true", help="Alias for --info-only")
    ap.add_argument("--check-env", action="store_true", help="Run env check and exit")
    ap.add_argument(
        "--self-test",
        action="store_true",
        help="Run built-in checks and exit",
    )
    ap.add_argument("--json", action="store_true", help="JSON stdout")
    return ap


def run_self_test() -> None:
    w, h = apply_scale(800, 600, 0.6)
    assert w == 480 and h == 360
    cw, ch = resolve_canvas({"width": 1920, "height": 1080}, 800, None)
    assert cw == 800 and ch == 450
    fc = build_filter_complex(2, 320, 240, 0)
    assert "concat=n=2" in fc and PAD_COLOR in fc
    assert "force_original_aspect_ratio=decrease" in fc
    name = default_gif_basename()
    assert name.startswith("oi-images-to-gif-") and name.endswith(".gif")
    assert len(name) > len("oi-images-to-gif-.gif")


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

    if args.delay <= 0:
        raise SystemExit("--delay must be > 0")
    if args.scale <= 0:
        raise SystemExit("--scale must be > 0")
    if not 0 <= args.loss <= 1:
        raise SystemExit("--loss must be between 0 and 1")
    if args.width is not None and args.width < 2:
        raise SystemExit("--width must be >= 2")
    if args.height is not None and args.height < 2:
        raise SystemExit("--height must be >= 2")

    ffmpeg = resolve_tool("ffmpeg", args.ffmpeg)
    ffprobe = resolve_tool("ffprobe", args.ffprobe)

    if not args.inputs:
        build_parser().print_help()
        return 0

    images = gather_inputs(args.inputs, args.recursive)
    if not images:
        raise SystemExit("No supported images found (.png, .jpg, .jpeg, .webp, .bmp, .gif, .tif).")

    plan = build_plan(ffprobe, images, args)
    out_path = Path(plan["output"])

    if args.info_only or args.preview:
        if args.json:
            print(json.dumps({"preview": True, **plan}, ensure_ascii=False, indent=2))
        else:
            print(
                f"Frames: {plan['frame_count']} | canvas {plan['canvas']['width']}x"
                f"{plan['canvas']['height']} -> GIF {plan['output_size']['width']}x"
                f"{plan['output_size']['height']} | delay={plan['delay_seconds']}s | "
                f"scale={plan['scale']}"
            )
            for row in plan["images"]:
                print(f"  - {Path(row['file']).name}: {row['width']}x{row['height']}")
            print(f"Output: {plan['output']}")
            print("(preview only — no GIF written)")
        return 0

    out_path.parent.mkdir(parents=True, exist_ok=True)
    if args.output is not None:
        out_path = unique_output(out_path)
        plan["output"] = str(out_path)
    if not args.json:
        print(
            f"Encoding {plan['frame_count']} frames -> {out_path.name} "
            f"({plan['output_size']['width']}x{plan['output_size']['height']}, "
            f"delay={args.delay}s, scale={args.scale})"
        )

    try:
        meta = convert(
            ffmpeg,
            images,
            out_path,
            out_w=plan["output_size"]["width"],
            out_h=plan["output_size"]["height"],
            delay=args.delay,
            loss=args.loss,
        )
        meta["output_size_bytes"] = out_path.stat().st_size if out_path.is_file() else 0
        meta["canvas"] = plan["canvas"]
        meta["scale"] = args.scale
        meta["images"] = [row["file"] for row in plan["images"]]
        payload = {"ok": True, **meta}
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"Done: {out_path} ({meta['output_size_bytes']} bytes)")
        return 0
    except RuntimeError as e:
        if args.json:
            print(json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False, indent=2))
        else:
            print(f"failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
