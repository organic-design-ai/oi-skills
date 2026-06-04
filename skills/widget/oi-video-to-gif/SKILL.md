---
name: oi-video-to-gif
description: >-
  Convert local MP4/MOV to high-quality GIF: frame-drop levels, optional crop, per-frame
  delay, proportional resize, loss control (0=best). TRIGGER when user converts video to
  GIF, oi-video-to-gif, mp4 to gif, or Video2Gif. NOT for AI-generated video or online-only
  URLs without download.
---
# Oi Video to GIF

**Author:** Shicheng, Haihang, Alibaba Cloud Design

Convert **local** `.mp4` / `.mov` (and `.m4v` / `.webm`) to animated GIF via **ffmpeg** (palettegen + lanczos, optional transdiff). Optional **crop** (same rules as `oi-video-crop`) runs in the same pass before scaling.

**Skill path**: `<skill-dir>/` (e.g. `~/.agents/skills/oi-video-to-gif/widget/oi-video-to-gif`).

**Scripts** (absolute paths): `<skill-dir>/scripts/check_env.py`, `.../video_to_gif.py`. Foreground only.

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-video-to-gif` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-video-to-gif`), then ask what they want to accomplish.

**Triggers:** `oi-video-to-gif`, mp4/mov to gif, 视频转 GIF, Video2Gif.

**Quick start**
1. `python3 <skill-dir>/scripts/check_env.py --json` → `--install` if needed.
2. `--info-only` / `--preview` before encode.
3. Convert: `--sample-every` (抽帧等级 1=不抽帧), `--frame-delay`, `--scale`, `--loss`; optional crop flags like `oi-video-crop`.

**Example prompts**
- 「抽帧 2，scale 0.7，转 gif」（默认不调速）
- 「delay 0.05，再转 gif」（需显式要速度时）
- 「CENTER TOP 高度裁 340 再转 gif，scale 0.7」
- 「这个文件夹批量转 gif」

**Do not use for:** online-only URLs without local file; AI video generation; **image sequences** → `oi-images-to-gif`.

## Defaults (use unless user overrides)

| Option | Default | Meaning |
|--------|---------|---------|
| `--sample-every` | `2` | 抽帧等级（见下） |
| `--frame-delay` | `0.01` | 每帧显示时长（秒），**只改播放速度、不改变帧数**；`0` = 不调速 |
| `--scale` | `1` | Proportional width scale (`0.6`, `0.7`, `1`, …) |
| `--loss` | `0` | Quality: `0` = high quality / near-lossless palette, `1` = max loss / smallest file |

Output width = `round(cropped_or_source_width × scale)` unless `--width` is set explicitly.

---

## 抽帧 (`--sample-every`)

抽帧是**重复执行**同一规则，而不是「每 N 帧保留 1 帧」：

| 等级 | 含义 |
|------|------|
| `1` | **不抽帧**（不做 `select` 丢帧） |
| `2` | 执行 **1 次**：每连续 3 帧里去掉第 3 帧（保留 2、去掉 1） |
| `3` | 执行 **2 次**（在上一步结果上再跑一遍同样规则） |
| `4` | 执行 **3 次** |
| `N` | 执行 **N−1 次** |

单次规则在 ffmpeg 中为：`select='not(eq(mod(n,3),2))'` + `setpts`。多次则链式重复。

抽帧**只**做丢帧，不改编速。`N≥2` 且 `--frame-delay 0` 时，时间轴约为 `source_fps × (2/3)^(N−1)`；默认 `0.01` 会在最后统一调速。

---

## 滤镜顺序（ffmpeg `-vf`）

固定流水线（无对应参数的步骤会跳过）：

1. **抽帧** — `--sample-every`（`select` + `setpts` 链）
2. **裁切** — crop 参数（若有）
3. **缩放** — `--scale` / `--width`
4. **调色** — `palettegen` + `paletteuse`（受 `--loss` 影响）
5. **调速** — `--frame-delay > 0` 时在最后用 `setpts` 拉开帧间隔（**不丢帧、不补帧**）；默认 `0.01`（约 100fps 等效间隔）

---

## 裁切 (crop)

与 `widget/oi-video-crop` 相同语义：在转 GIF 前用 `crop=w:h:x:y` 裁切，**不**先导出中间 MP4。

| User says | Maps to |
|-----------|---------|
| 宽度裁 200 | `--crop-width 200` |
| 高度裁 340 | `--crop-height 340` |
| 宽高各裁 100 | `--crop-width 100 --crop-height 100` 或 `--dimension both --pixels 100` |

### Axis（轴心）

| Token | Width | Height |
|-------|-------|--------|
| `LEFT` / `RIGHT` / `CENTER` | 靠左 / 靠右 / 两侧均分 | — |
| `TOP` / `BOTTOM` / `CENTER` | — | 靠顶 / 靠底 / 上下均分 |

组合示例：`CENTER TOP`, `LEFT BOTTOM`.

裁切、抽帧、缩放与调速在同一次 ffmpeg 中完成，顺序见上节。

---

## Step 0 — Environment check & auto-install (MANDATORY, first)

```bash
python3 <skill-dir>/scripts/check_env.py --json
```

| `ready` | Action |
|---------|--------|
| `true` | Confirm environment ready, continue |
| `false` | Run auto-install below; do not wait for a manual menu first |

```bash
python3 <skill-dir>/scripts/check_env.py --install --json
```

Or via main script:

```bash
python3 <skill-dir>/scripts/video_to_gif.py --check-env --json
```

---

## Step 1 — Input video

Ask for a **local absolute path** (or `~/...`) to a video file or folder. Verify the file exists.

---

## Step 2 — Plan (recommended)

Probe and show the conversion plan before encoding:

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  --info-only --json \
  "<VIDEO_PATH>"
```

With crop, add crop flags and use `--preview` to confirm filter without encoding:

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  --preview --json \
  --axis "CENTER TOP" --crop-height 340 \
  "<VIDEO_PATH>"
```

Report source resolution, crop output size (if any), planned GIF width, 抽帧等级 / `drop_cycles`, `frame_delay`, `loss`.

---

## Step 3 — Confirm options (if unclear)

Clarify with the user when not already stated:

- **抽帧** `--sample-every`（默认 `2`；`1` = 不抽帧）
- **速度** `--frame-delay`（默认 `0.01`；`0` = 沿用抽帧后时间轴；更慢可加大如 `0.05`）
- **缩放** `scale` e.g. `0.6` / `0.7` / `1` (default `1`)
- **裁切** width / height / both + **轴心** `axis`（若需要）
- **画质** `loss` from `0` (high quality) to `1` (smallest file)
- Output directory (default: same folder as source, `.gif` beside video)

---

## Step 4 — Convert

Single file (no crop):

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  --sample-every 2 \
  --scale 1 \
  --loss 0 \
  --json \
  "<VIDEO_PATH>"
```

Crop + GIF（例：高度裁 340，`CENTER TOP`）:

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  --axis "CENTER TOP" --crop-height 340 \
  --sample-every 2 --scale 0.7 --loss 0 \
  --json \
  "<VIDEO_PATH>"
```

Folder batch:

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  -r -o "<OUTPUT_DIR>" \
  --sample-every 2 --scale 0.7 --loss 0 \
  "<FOLDER_PATH>"
```

### CLI reference

| Argument | Default | Description |
|----------|---------|-------------|
| `--sample-every` | `2` | 抽帧等级：`1`=不抽帧；`N≥2` 重复 `N−1` 次「2 留 1 丢」 |
| `--frame-delay` | `0.01` | 每帧显示秒数；`>0` 时调色后 `setpts` 调速（帧数不变） |
| `--scale` | `1` | Scale width after crop (or source if no crop) |
| `--width` | — | Fixed output width (overrides `--scale`) |
| `--loss` | `0` | `0` high quality; `1` max loss |
| `--axis` | `CENTER CENTER` | Crop pivot |
| `--crop-width` / `--crop-height` | `0` | Pixels removed from each dimension |
| `--dimension` + `--pixels` | — | Shorthand: `width` \| `height` \| `both` |
| `--out-width` / `--out-height` | — | Explicit crop output size |
| `--preview` | — | Plan only; no GIF |
| `-o` / `--output-dir` | beside source | Output directory |
| `-r` / `--recursive` | off | Scan subfolders when input is a directory |
| `--info-only` | — | Probe only |
| `--check-env` | — | Dependency check |
| `--json` | — | Machine-readable output |

### Quality notes

- **`--frame-delay`**: 只控制 GIF **播放快慢**（每帧停留多久），**与帧数无关**；不要用 `fps` 滤镜（会改帧数）。
- **`--frame-delay 0`**: 不调速，沿用抽帧后的时间轴。
- **`--frame-delay > 0`**: `paletteuse` 之后 `setpts=N*(delay*FRAME_RATE)/TB`，总时长变、帧数不变。
- **`--sample-every`**: 只决定保留哪些帧；与 `--frame-delay` 独立。
- **loss=0**: up to 256 palette colors, `stats_mode=full`, no dither.
- **loss=1**: fewer colors + stronger bayer dither.
- **`-gifflags +transdiff`**: lossless frame differencing when possible.
- **scale** uses `lanczos`; height keeps aspect ratio.

---

## Step 5 — Verify

- Exit code `0`
- Output `.gif` exists and size > 0
- Report path, output width, 抽帧等级, crop size (if any), `frame-delay`, `loss`, file size

---

## Error handling

| Symptom | Action |
|---------|--------|
| `check_env` exit 2 | Step 0 → `--install` |
| `ffmpeg not found` | Step 0 |
| `Output size invalid` (crop) | Reduce crop pixels or fix axis |
| Huge GIF | Raise `--sample-every`, lower `--scale`, or raise `--loss` toward `1` |
| Too blurry | Use `--sample-every 1`, raise `--scale`, set `--loss 0` |

## Output rules

- Never write into the `skills/` install tree
- Default output: `{stem}.gif` next to the source video

## Examples

不抽帧 + 调速（最后一步 setpts，帧数不变）：

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  --sample-every 1 --frame-delay 0.03 --scale 1 --loss 0 \
  --json ~/Movies/clip.mp4
```

抽帧 2（默认，不调速）+ 缩小宽度：

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  --sample-every 2 --scale 0.7 --loss 0 \
  --json ~/Movies/clip.mp4
```

裁切后转 GIF：

```bash
python3 <skill-dir>/scripts/video_to_gif.py \
  --axis "CENTER TOP" --crop-height 340 \
  --sample-every 2 --scale 0.7 --loss 0 \
  --json ~/Movies/vertical.mp4
```
