---
name: oi-skills
description: >-
  Oi Skills collection. Trigger when user says oi-skills, Oi Skills, 设计技能,
  or wants a capability from this package without naming a child skill. Routes to
  widget/* or page/* or ppt/* or animation/* skills.
---

# Oi Skills

**Author:** Alibaba Cloud Design

Package root: `<pkg-dir>/` (e.g. `~/.agents/skills/oi-skills`).

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-skills` without a concrete task), **reply with this section** (replace `<pkg-dir>` with the installed package path, e.g. `~/.agents/skills/oi-skills`), then ask what they want to accomplish.

**Triggers:** `oi-skills`, `Oi Skills`, `设计技能`, or vague design/media task without naming a child.

### Quick start

1. Infer intent: **widget** (video/GIF) vs **ppt** (HTML slides) vs **page** (UI/design) vs **animation** (motion/animation workflows).
2. Open only the child `SKILL.md` listed below — do not merge unrelated workflows.
3. If unclear, ask which row fits best.

Child paths:

- `oi-video-crop`: `<pkg-dir>/widget/oi-video-crop/SKILL.md`
- `oi-video-to-gif`: `<pkg-dir>/widget/oi-video-to-gif/SKILL.md`
- `oi-images-to-gif`: `<pkg-dir>/widget/oi-images-to-gif/SKILL.md`
- `oi-html-ppt`: `<pkg-dir>/ppt/oi-html-ppt/SKILL.md`
- `oi-guizang-ppt`: `<pkg-dir>/ppt/oi-guizang-ppt/SKILL.md`
- `oi-hue-ui`: `<pkg-dir>/page/oi-hue-ui/SKILL.md`
- `oi-awesome-ui`: `<pkg-dir>/page/oi-awesome-ui/SKILL.md`
- `oi-taste-ui`: `<pkg-dir>/page/oi-taste-ui/SKILL.md`
- `oi-nothing-ui`: `<pkg-dir>/page/oi-nothing-ui/SKILL.md`
- `oi-pro-ui`: `<pkg-dir>/page/oi-pro-ui/SKILL.md`
- `oi-stitch-ui`: `<pkg-dir>/page/oi-stitch-ui/SKILL.md`
- `oi-text-effect`: `<pkg-dir>/animation/oi-text-effect/SKILL.md`

### Example prompts

- 「用 oi-skills 裁视频」→ `oi-video-crop`
- 「设计技能，做玻璃态落地页」→ `oi-awesome-ui` → style slug
- 「怎么用 oi-pro-ui？」→ read `oi-pro-ui/SKILL.md` Usage
- 「做打字机文字动效」→ `oi-text-effect`（`textType`）

**Do not use for:** tasks that already name a child skill — go straight to that child.

## Choose a skill (when intent is unclear)

- `oi-video-crop` (`<pkg-dir>/widget/oi-video-crop/SKILL.md`): Local video crop, ffmpeg, 裁切/裁剪视频
- `oi-video-to-gif` (`<pkg-dir>/widget/oi-video-to-gif/SKILL.md`): Local MP4/MOV → GIF, 抽帧/速度/缩放/loss
- `oi-images-to-gif` (`<pkg-dir>/widget/oi-images-to-gif/SKILL.md`): Local images → GIF, delay/canvas/pad/scale
- `oi-html-ppt` (`<pkg-dir>/ppt/oi-html-ppt/SKILL.md`): Static HTML deck — themes, layouts, presenter mode
- `oi-guizang-ppt` (`<pkg-dir>/ppt/oi-guizang-ppt/SKILL.md`): Single-file swipe PPT — magazine or Swiss style
- `oi-hue-ui` (`<pkg-dir>/page/oi-hue-ui/SKILL.md`): 生成/改造设计语言 skill（`styles/references/` + `styles/examples/`）
- `oi-awesome-ui` (`<pkg-dir>/page/oi-awesome-ui/SKILL.md`): 62 design style guides (glassmorphism, minimal, …)
- `oi-taste-ui` (`<pkg-dir>/page/oi-taste-ui/SKILL.md`): Premium anti-slop frontend + 12 styles
- `oi-nothing-ui` (`<pkg-dir>/page/oi-nothing-ui/SKILL.md`): Nothing-inspired monochrome UI (`styles/references/`; explicit trigger only)
- `oi-pro-ui` (`<pkg-dir>/page/oi-pro-ui/SKILL.md`): UI/UX BM25 search + design-system generator
- `oi-stitch-ui` (`<pkg-dir>/page/oi-stitch-ui/SKILL.md`): Local design workflows — DESIGN.md, HTML, React, 12 styles
- `oi-text-effect` (`<pkg-dir>/animation/oi-text-effect/SKILL.md`): Text effects for React/HTML — entrance, sweep, scramble, flip, morph, shimmer, typewriter

Ask the user which skill they need, or infer from their message, then **read and follow that skill's SKILL.md only**.

## Path convention

- `<pkg-dir>`: `~/.agents/skills/oi-skills`
- Child scripts: `<pkg-dir>/widget/oi-video-crop/scripts/...`
