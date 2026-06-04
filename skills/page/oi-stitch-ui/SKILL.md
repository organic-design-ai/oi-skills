---
name: oi-stitch-ui
description: >-
  Landing-page design workflows: 12 local styles for DESIGN.md, static HTML capture,
  prompt enhancement, multi-page loops, React/shadcn build, and Remotion. TRIGGER when
  user says oi-stitch-ui, design/DESIGN.md, code-to-design, or multi-page site build.
  No external design APIs required.
---
# Oi Stitch UI — Design Workflow Library

**Author:** Google Stitch

**Skill path:** `<skill-dir>/` (e.g. `~/.cursor/skills/oi-stitch-ui`).

**12** workflow styles under `styles/`. Catalog: `styles/index.json`.

Project artifacts live in **`design/`** (e.g. `design/DESIGN.md`, `design/pages/`, `design/next-prompt.md`).

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-stitch-ui` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-stitch-ui`), then ask what they want to accomplish.

**Triggers:** `oi-stitch-ui`, `design/DESIGN.md`, code-to-design, multi-page build, 设计工作流.

**Quick start**
1. Choose workflow **slug** from `styles/index.json` (e.g. `generate-design`, `code-to-design`, `stitch-loop`).
2. Read `<skill-dir>/styles/<slug>/SKILL.md`.
3. Write artifacts under project `design/` (`DESIGN.md`, `pages/`, `next-prompt.md`).

**Example prompts**
- 「oi-stitch-ui 从现有 React 项目导出 DESIGN.md」→ `extract-design-md`
- 「多页站点 baton 循环」→ `stitch-loop`
- 「HTML 转 React 组件」→ `react-components`

**Do not use for:** video crop/GIF; style-only token libraries → `oi-awesome-ui`.

## When to use

- Capture or document UI from an existing codebase
- Build landing pages with a shared design system
- Convert HTML mockups to React or shadcn/ui
- Iterative multi-page site construction
- Polish UI prompts before implementation

**Do not use** for ffmpeg/video widget tasks (`oi-video-crop`, `oi-video-to-gif`).

---

## Step 1 — Choose a style slug

| Goal | Slug |
|------|------|
| New page from prompt / image | `generate-design` |
| Export app → `design/` package | `code-to-design` |
| DESIGN.md from source code | `extract-design-md` |
| Static HTML snapshot | `extract-static-html` |
| DESIGN.md from HTML/screenshots | `design-md` |
| Maintain tokens in repo | `manage-design-system` |
| Premium DESIGN.md spec | `taste-design` |
| Polish user prompt | `enhance-prompt` |
| Multi-page baton loop | `stitch-loop` |
| HTML → React | `react-components` |
| Screenshot walkthrough video | `remotion` |
| shadcn/ui setup | `shadcn-ui` |

List catalog:

```bash
python3 -c "import json; d=json.load(open('<skill-dir>/styles/index.json')); [print(k,'-',v['summary']) for k,v in sorted(d.items())]"
```

Default for full capture: **`code-to-design`**. Default for new pages: **`generate-design`**.

---

## Step 2 — Load the style guide (MANDATORY)

| File | Path |
|------|------|
| Rules | `<skill-dir>/styles/<slug>/SKILL.md` |
| References | `<skill-dir>/styles/<slug>/references/` |
| Resources | `<skill-dir>/styles/<slug>/resources/` |
| Examples | `<skill-dir>/styles/<slug>/examples/` |

Read the style `SKILL.md` end-to-end before running scripts or editing the repo.

**Scripts** (when defined):

```bash
bash <skill-dir>/styles/<slug>/scripts/<script>
python3 <skill-dir>/styles/<slug>/scripts/<script>
npx tsx <skill-dir>/styles/<slug>/scripts/<script>
```

---

## Step 3 — Common orchestration

**Code → design package** (`code-to-design`):

1. `extract-static-html` → `design/pages/*.html`
2. `extract-design-md` → `design/DESIGN.md`
3. `manage-design-system` → map tokens in Tailwind/CSS

**New UI** (`generate-design`):

1. Ensure `design/DESIGN.md` (`manage-design-system` / `taste-design`)
2. Optional: `enhance-prompt`
3. Implement in the project stack

**Multi-page** (`stitch-loop`):

- Requires `design/DESIGN.md`, `design/SITE.md`, `design/next-prompt.md`

---

## Step 4 — Delivery checklist

- [ ] Artifacts under agreed `design/` paths
- [ ] `DESIGN.md` tokens applied in theme config, not duplicated ad hoc
- [ ] No emoji as structural icons
- [ ] Responsive and accessible contrast
- [ ] React output validated when using `react-components`

---

## Path convention

| Placeholder | Example |
|-------------|---------|
| `<skill-dir>` | `~/.agents/skills/oi-stitch-ui` |
| Catalog | `<skill-dir>/styles/index.json` |
| Style rules | `<skill-dir>/styles/<slug>/SKILL.md` |
