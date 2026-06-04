---
name: oi-images-to-gif
description: >-
  Combine local images into animated GIF: per-frame delay (default 1s), canvas from first
  image or explicit size, proportional resize with #000000 pad, overall scale. Default output
  on Desktop as oi-images-to-gif-<uuid>.gif. TRIGGER when user stitches images/photos to gif,
  oi-images-to-gif, or multi-image slideshow. NOT for video sources (use oi-video-to-gif) or
  online-only URLs without download.
---
# Oi Images to GIF

**Author:** Haihang, Alibaba Cloud Design

Stitch **local** images (`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.gif`, `.tif`) into one animated GIF via **ffmpeg**. Each frame keeps aspect ratio; smaller images are **letterboxed** on a fixed canvas with **black** (`#000000`) padding.

**Skill path**: `<skill-dir>/` (e.g. `~/.agents/skills/oi-images-to-gif/widget/oi-images-to-gif`).

**Scripts** (absolute paths): `<skill-dir>/scripts/check_env.py`, `.../images_to_gif.py`. Foreground only.

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-images-to-gif` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-images-to-gif`), then ask what they want to accomplish.

**Triggers:** `oi-images-to-gif`, images/photos to gif, 多图转 GIF, 图片合成动图.

**Quick start**
1. `python3 <skill-dir>/scripts/check_env.py --json` → `--install` if needed.
2. `--info-only` / `--preview` before encode.
3. Encode: ordered image paths or a folder; `--delay`, `--width`/`--height`, `--scale`.
4. GIF lands on **Desktop** by default — no need to pass `--output` unless the user specifies a path.

**Example prompts**
- 「这三张图合成 gif，每张 1 秒」
- 「文件夹里图片转 gif，间隔 0.5 秒，整体 scale 0.6」
- 「画布 1280x720，2 秒一帧，导出到桌面」
- 「输出到 ~/Exports/out.gif」

**Do not use for:** video → GIF (`oi-video-to-gif`); remote URLs without a local file path.

## Defaults (use unless user overrides)

| Option | Default | Meaning |
|--------|---------|---------|
| `--delay` | `1` | Seconds each frame is shown |
| `--scale` | `1` | Scale final canvas (`0.6`, `0.7`, …) |
| `--width` / `--height` | — | Canvas size; if omitted, **first image** width × height |
| `--loss` | `0` | Palette quality: `0` best, `1` smallest file |
| **Output** | `~/Desktop/oi-images-to-gif-<uuid>.gif` | Desktop (`桌面` on zh-CN macOS); UUID avoids collisions |
| `--output` | — | Exact file path (overrides default name/location) |
| `-o` / `--output-dir` | — | Directory only; still uses `oi-images-to-gif-<uuid>.gif` inside |

**Canvas rules**
- User sets `--width` and `--height` → that canvas.
- User sets only `--width` → height derived from first image aspect ratio.
- User sets only `--height` → width derived from first image aspect ratio.
- Neither set → first image dimensions.
- Each frame: `scale` (decrease, lanczos) + `pad` to canvas with `color=0x000000`, centered.
- Final GIF size = canvas × `--scale` (rounded, min 2 px per side).

**Frame order**
- Explicit file list → CLI order.
- Folder → natural sort by filename (`img2` before `img10`).

---

## Step 0 — Environment check & auto-install (MANDATORY, first)

```bash
python3 <skill-dir>/scripts/check_env.py --json
```

| `ready` | Action |
|---------|--------|
| `true` | Continue |
| `false` | `python3 .../check_env.py --install --json` |

Or:

```bash
python3 <skill-dir>/scripts/images_to_gif.py --check-env --json
```

---

## Step 1 — Input images

Collect **local absolute paths** (or `~/...`). Minimum **1** image; typical use is **2+**.

Supported: `.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.gif`, `.tif`, `.tiff`.

---

## Step 2 — Plan (recommended)

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --info-only --json \
  --delay 1 --scale 1 \
  img1.png img2.jpg img3.png
```

Folder:

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --preview --json \
  --delay 0.5 --scale 0.6 \
  "/path/to/frames/"
```

Report: frame count, per-image size, canvas, output GIF size, delay, scale, **planned output path** (includes generated UUID).

---

## Step 3 — Confirm options (if unclear)

- **间隔** `--delay`（默认 `1` 秒；`0.5`、`2` 等）
- **画布** `--width` / `--height`（默认第一张图尺寸）
- **整体缩放** `--scale`（如 `0.6`）
- **画质** `--loss` `0`–`1`
- **输出**：默认桌面 + UUID 文件名；仅当用户指定路径时用 `--output` / `-o`

---

## Step 4 — Encode

Default (Desktop + UUID filename, 1 s per frame):

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --delay 1 --scale 1 --loss 0 --json \
  ~/Pictures/a.png ~/Pictures/b.png ~/Pictures/c.png
```

Fixed canvas, custom path:

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --delay 0.5 --width 1280 --height 720 --scale 1 \
  --output ~/Desktop/my-deck.gif --json \
  ~/Pictures/frames/
```

Output directory only (UUID filename inside that folder):

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --delay 2 -o ~/Exports --json \
  ~/Pictures/*.png
```

### CLI reference

| Argument | Default | Description |
|----------|---------|-------------|
| `--delay` | `1` | Seconds per frame |
| `--scale` | `1` | Multiply canvas width/height |
| `--width` | — | Canvas width (px) |
| `--height` | — | Canvas height (px) |
| `--loss` | `0` | `0` high quality; `1` max compression |
| *(output)* | Desktop + UUID | `oi-images-to-gif-<uuid>.gif` |
| `--output` | — | Exact output `.gif` path |
| `-o` / `--output-dir` | — | Output directory (UUID filename) |
| `-r` / `--recursive` | off | Scan subfolders when input is a directory |
| `--info-only` / `--preview` | — | Plan only |
| `--check-env` | — | Dependency check |
| `--json` | — | Machine-readable output |

---

## Step 5 — Verify

- Exit code `0`
- Output `.gif` exists and size > 0
- Report path, dimensions, frame count, delay, scale, file size

---

## Error handling

| Symptom | Action |
|---------|--------|
| `check_env` exit 2 | Step 0 → `--install` |
| `ffmpeg not found` | Step 0 |
| `No supported images` | Check paths and extensions |
| `too many images (max 128)` | Split into smaller batches |
| Huge GIF | Lower resolution (`--width`/`--height`), lower `--scale`, or `--loss` toward `1` |

## Output rules

- Never write into the `skills/` install tree
- **Default:** `~/Desktop/oi-images-to-gif-<uuid>.gif` (or `~/桌面/` when present)
- User says「导出到桌面」→ omit `--output` (default already Desktop)
- User gives a filename → `--output ~/Desktop/name.gif`
- Explicit `--output` that already exists → suffix `_1`, `_2`, … before encode

## Examples

默认：桌面 + UUID、1 秒、第一张图尺寸：

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --json frame_01.png frame_02.png frame_03.png
```

0.5 秒间隔 + 整体 60%：

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --delay 0.5 --scale 0.6 --json \
  ~/Design/storyboard/
```

1280×720 画布、2 秒一帧（仍默认桌面输出）：

```bash
python3 <skill-dir>/scripts/images_to_gif.py \
  --width 1280 --height 720 --delay 2 --json \
  ~/Exports/*.png
```
