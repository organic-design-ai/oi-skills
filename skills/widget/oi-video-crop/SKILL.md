---
name: oi-video-crop
description: >-
  Crop local videos with ffmpeg: width, height, or both; pivot axis (CENTER TOP, etc.);
  auto-install ffmpeg via brew/apt when missing. TRIGGER when user crops/trims local video,
  mentions oi-video-crop, axis, or pixel trim on width/height. NOT for AI video generation.
---
# Oi Video Crop

**Author:** Haihang, Alibaba Cloud Design

Crop a **local** video with **ffmpeg** (width / height / both).

**Package path**: `<pkg-dir>/widget/oi-video-crop/` (e.g. `~/.cursor/skills/oi-skills/widget/oi-video-crop`).

**Scripts** (absolute paths): `<pkg-dir>/widget/oi-video-crop/scripts/check_env.py`, `.../video_crop.py`. Foreground only.

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-video-crop` without a concrete task), **reply with this section** (replace `<pkg-dir>` with the installed package path, e.g. `~/.agents/skills/oi-skills`), then ask what they want to accomplish.

**Triggers:** `oi-video-crop`, 裁切/裁剪视频, crop width/height, ffmpeg crop, axis.

**Quick start**
1. `python3 <pkg-dir>/widget/oi-video-crop/scripts/check_env.py --json` → `--install` if needed.
2. `--info-only` for source size; `--preview` to confirm crop plan.
3. Crop with `--input`, `--axis`, `--crop-width` / `--crop-height` (or `--dimension` + `--pixels`).

**Example prompts**
- 「宽度裁 200，轴心 CENTER CENTER」
- 「高度裁 340，CENTER TOP，输出到桌面」
- 「preview 一下裁完多大」

**Do not use for:** GIF export → `oi-video-to-gif` (can crop during GIF in one pass).

## Step 0 — Environment check & auto-install (MANDATORY, first)

Before asking for a video, run:

```bash
python3 <pkg-dir>/widget/oi-video-crop/scripts/check_env.py --json
```

| `ready` | Action |
|---------|--------|
| `true` | Briefly confirm「环境就绪」, go to Step 1 |
| `false` | **Auto-install** (see below). Do **not** wait for the user to pick a menu option |

### Auto-install (default when `ready: false`)

1. Tell the user briefly, e.g.「检测到未安装 ffmpeg，正在自动安装…」
2. Run in **foreground**:

```bash
python3 <pkg-dir>/widget/oi-video-crop/scripts/check_env.py --install --json
```

This runs the platform’s preferred command (e.g. `brew install ffmpeg` on macOS). Re-check is included; stop when `ready: true`.

3. If still `ready: false` after `--install`:
   - If `auto_install.available` was `false` (no brew / no supported package manager), show `agent_prompt` menu and wait for user choice
   - If install failed, report stderr/exit code, then show `agent_menu` as fallback

**Do not** ask「是否安装 ffmpeg？」before running `--install`. Only fall back to the manual menu when auto-install cannot run or fails.

Or check only (no install):

```bash
python3 <pkg-dir>/widget/oi-video-crop/scripts/video_crop.py --check-env --json
```

---

## Step 1 — Input video

> 请先提供要裁切的**视频文件路径**（本地绝对路径或 `~/...`）。

Verify file exists.

---

## Step 2 — Current dimensions

```bash
python3 <pkg-dir>/widget/oi-video-crop/scripts/video_crop.py --input "<VIDEO_PATH>" --info-only
```

Report e.g. **1080×1920** px, plus duration/codec if helpful.

---

## Step 3 — Crop dimension & amount (MANDATORY clarify)

**Must ask** which edge(s) to trim unless user already stated clearly:

> 要裁切的是 **宽度**、**高度**，还是 **宽和高都要**？各裁多少像素？

| User says | Maps to |
|-----------|---------|
| 宽度裁 200 / 裁宽度 200 | `--crop-width 200` |
| 高度裁 340 / 裁高度 340 | `--crop-height 340` |
| 宽高各裁 100 | `--crop-width 100 --crop-height 100` or `--dimension both --pixels 100` |
| 只裁 340（未说明方向） | **Ask** width vs height vs both — do not assume height only |

### Axis

> **轴心**？例如 `CENTER TOP` = 宽居中、高顶对齐（裁高度时从底部去掉）。

| Token | Width | Height |
|-------|-------|--------|
| `LEFT` / `RIGHT` / `CENTER` | 靠左 / 靠右 / 两侧均分 | — |
| `TOP` / `BOTTOM` / `CENTER` | — | 靠顶 / 靠底 / 上下均分 |

组合：`CENTER TOP`, `LEFT BOTTOM`, `RIGHT CENTER`.

### Confirm output size (preview)

Run **preview** before final crop:

```bash
python3 <pkg-dir>/widget/oi-video-crop/scripts/video_crop.py \
  --input "<VIDEO_PATH>" \
  --axis "<AXIS>" \
  --crop-width <W> \
  --crop-height <H> \
  --preview --json
```

Omit `--crop-width` or `--crop-height` when zero. Shorthand:

```bash
# width only
--dimension width --pixels 200 --axis "CENTER CENTER" --preview

# height only
--dimension height --pixels 340 --axis "CENTER TOP" --preview
```

Tell user the planned `output_size` and `crop_filter`. Ask「确认执行吗？」.

**Examples**

| Source | Params | Output |
|--------|--------|--------|
| 1080×1920 | height 340, `CENTER TOP` | 1080×1580 |
| 1920×1080 | width 200, `CENTER CENTER` | 1720×1080 |
| 1080×1920 | width 100 + height 340, `LEFT TOP` | 980×1580 |

---

## Step 4 — Output location (menu)

Default: **Desktop** (`~/Desktop` / `~/桌面`).

Ask:

> 输出保存到哪里？
> 1) **桌面**（默认）
> 2) 指定文件夹（请给路径）
> 3) 指定完整文件路径

| Choice | CLI |
|--------|-----|
| 1 | omit `--output-dir` |
| 2 | `--output-dir "<DIR>"` |
| 3 | `--output "<FULL_PATH>"` |

---

## Step 5 — Encoding option (menu)

Ask before crop (unless user already chose):

> 编码方式？
> 1) **重新编码**（默认，兼容性最好）
> 2) 流复制 `--copy`（更快，裁切时可能失败）

| Choice | CLI |
|--------|-----|
| 1 | default (no `--copy`) |
| 2 | `--copy` |

---

## Step 6 — Execute crop

```bash
python3 <pkg-dir>/widget/oi-video-crop/scripts/video_crop.py \
  --input "<VIDEO_PATH>" \
  --axis "<AXIS>" \
  --crop-width <W> \
  --crop-height <H> \
  --output-dir "<DIR>"
```

Only include non-zero crop flags. Width-only example:

```bash
--axis "CENTER CENTER" --dimension width --pixels 200
```

### CLI reference

| Argument | Description |
|----------|-------------|
| `--check-env` | Env check only (no `--input`) |
| `--install` (check_env.py) | Auto-install missing deps, then re-check |
| `--info-only` | Probe size only |
| `--preview` | Plan only; no ffmpeg |
| `--crop-width` | Pixels removed from **width** |
| `--crop-height` | Pixels removed from **height** |
| `--dimension` | `width` \| `height` \| `both` + `--pixels` |
| `--axis` | Pivot, e.g. `CENTER TOP`, `LEFT CENTER` |
| `--out-width` / `--out-height` | Explicit output size |
| `--output-dir` / `--output` | Save location |
| `--copy` | Stream copy instead of re-encode |
| `--json` | Machine-readable stdout |

---

## Step 7 — Verify

- Exit code `0`
- Output file exists, size > 0
- Report final path and **width×height**

---

## Error handling

| Symptom | Action |
|---------|--------|
| `check_env` exit 2 | Step 0 → run `--install`; if still failing, manual menu |
| `ffprobe not found` | Step 0 → `--install` (ffprobe ships with ffmpeg) |
| `Output size invalid` | Recompute; one dimension may exceed source |
| `ffmpeg failed` with `--copy` | Retry without `--copy` |

## Output rules

- Never write into `skills/` install tree
- Filename: `{stem}_crop_{W}x{H}.mp4`

## Example dialogues

**Width crop**

- User: 宽度裁 200，轴心 CENTER CENTER
- Agent: Preview 1920×1080 → 1720×1080 → confirm → crop → Desktop

**Height crop**

- User: 高度裁 340，CENTER TOP
- Agent: Preview 1080×1920 → 1080×1580 → confirm → crop

**Env**

- Agent: `check_env` → missing ffmpeg → `--install` → `brew install ffmpeg` → ready → continue
