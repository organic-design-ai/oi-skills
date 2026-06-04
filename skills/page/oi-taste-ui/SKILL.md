---
name: oi-taste-ui
description: >-
  Premium page frontend taste: anti-slop layout/typography/motion rules with
  adjustable dials and 12 styles (default, GPT-strict, minimal, brutalist, redesign,
  image-to-code, imagegen, brandkit, output enforcement, stitch). TRIGGER when user
  wants high-end UI, oi-taste-ui, or anti-generic AI design. NOT for video/media tools.
---
# Oi Taste UI — Premium Frontend Taste

**Author:** Leonxlnx

**Skill path:** `<skill-dir>/` (e.g. `~/.cursor/skills/oi-taste-ui`).

This skill bundles **12** specialized style guides under `styles/`. Catalog: `styles/index.json`.

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-taste-ui` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-taste-ui`), then ask what they want to accomplish.

**Triggers:** `oi-taste-ui`, anti-slop, 高级感 / 品味 UI, or a named sub-style slug.

**Quick start**
1. Pick a **slug** under `styles/` (default: `taste-skill`) — see `styles/index.json`.
2. Read `<skill-dir>/styles/<slug>/SKILL.md`.
3. Apply premium layout, typography, and motion rules when building or reviewing UI.

**Example prompts**
- 「oi-taste-ui 做高端 landing」
- 「用 image-to-code-skill 从设计图写网站」
- 「redesign-skill 升级现有首页」

**Do not use for:** ffmpeg / video widgets; pure BM25 search → `oi-pro-ui`.

## When to use

- Landing pages or product UI that must feel **premium**, not generic AI output
- User asks for oi-taste-ui, anti-slop, high-end visual design, or a named sub-style
- Image-first pipelines (comps → code) or redesign of existing UI

**Do not use** for ffmpeg/video or unrelated widget tasks.

---

## Step 1 — Choose a style slug

1. If the user named a workflow, map to a **slug** (folder name below).
2. Otherwise read the catalog:

```bash
python3 -c "import json; d=json.load(open('<skill-dir>/styles/index.json')); print('\n'.join(sorted(d)))"
```

3. If unclear, default to **`taste-skill`**.

| User intent | Slug |
|-------------|------|
| Default premium landing / general UI | `taste-skill` |
| Stricter GPT/Codex, more motion/layout variance | `gpt-tasteskill` |
| Image → analyze → code | `image-to-code-skill` |
| Improve existing codebase UI | `redesign-skill` |
| Soft, calm, expensive feel | `soft-skill` |
| Force complete deliverables | `output-skill` |
| Editorial / Notion-Linear minimal | `minimalist-skill` |
| Industrial brutalist (experimental) | `brutalist-skill` |
| Premium DESIGN.md (also in **`oi-stitch-ui`** → `styles/taste-design`) | `taste-design` or use **`oi-stitch-ui`** |
| Images only: web comps | `imagegen-frontend-web` |
| Images only: mobile flows | `imagegen-frontend-mobile` |
| Images only: brand kit boards | `brandkit` |

---

## Step 2 — Load the style guide (MANDATORY)

Read and follow **only** the selected style files:

| File | Path |
|------|------|
| Agent rules | `<skill-dir>/styles/<slug>/SKILL.md` |
| Design intent (optional) | `<skill-dir>/styles/<slug>/DESIGN.md` |

Do **not** mix multiple slugs unless the user explicitly requests it.

---

## Step 3 — Baseline dials (`taste-skill` / `gpt-tasteskill`)

When the active style defines **DESIGN_VARIANCE**, **MOTION_INTENSITY**, **VISUAL_DENSITY** (1–10):

- Default baseline: **8 / 6 / 4** unless the user overrides in chat.
- Do **not** ask the user to edit skill files; override via conversation only.
- Use dial definitions in the style `SKILL.md` for layout, motion, and density.

---

## Step 4 — Global rules (code styles)

Apply unless the style `SKILL.md` explicitly relaxes them:

1. **Dependency check:** Verify `package.json` before importing UI libraries; output install commands if missing.
2. **Anti-emoji:** No emojis in UI or as icons; use SVG icon sets.
3. **Viewport:** Use `min-h-[100dvh]` instead of `h-screen` for full-height heroes.
4. **Layout:** Prefer CSS Grid over fragile flex percentage math.
5. **Purple-ban:** Avoid generic AI purple/blue gradients unless requested.
6. **Performance:** Animate `transform` and `opacity` only.

---

## Step 5 — Image-first workflows

For `imagegen-*` or `image-to-code-skill` slugs:

1. Generate or receive reference images per style instructions.
2. Analyze hierarchy, spacing, type, and color before coding.
3. Implement in the user's stack; match references.

---

## Step 6 — Delivery checklist

- [ ] Full interaction states (loading, empty, error) where UI is interactive
- [ ] Mobile fallback for asymmetric layouts (style-specific)
- [ ] One accent color discipline; neutral bases
- [ ] No truncated output when `output-skill` is active

---

## Path convention

| Placeholder | Example |
|-------------|---------|
| `<skill-dir>` | `~/.agents/skills/oi-taste-ui` |
| Style catalog | `<skill-dir>/styles/index.json` |
| Style rules | `<skill-dir>/styles/<slug>/SKILL.md` |
