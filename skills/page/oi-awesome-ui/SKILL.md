---
name: oi-awesome-ui
description: >-
  62 curated design-system style guides for landing pages and web UI (glassmorphism,
  minimal, bento, brutalism, etc.). TRIGGER when user picks a visual style, asks for
  oi-awesome-ui, or needs token-level design rules for a page. NOT for video/media tools.
---
# Oi Awesome UI — Design Style Library

**Author:** Bergside

**Package path:** `<pkg-dir>/page/oi-awesome-ui/` (e.g. `~/.cursor/skills/oi-skills/page/oi-awesome-ui`).

This skill bundles **62** self-contained style guides. Each style has agent instructions (`SKILL.md`) and a human companion (`DESIGN.md`). Catalog: `styles/index.json`.

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-awesome-ui` without a concrete task), **reply with this section** (replace `<pkg-dir>` with the installed package path, e.g. `~/.agents/skills/oi-skills`), then ask what they want to accomplish.

**Triggers:** `oi-awesome-ui`, named visual style (glassmorphism, minimal, bento, …), 设计风格 / 设计系统风格.

**Quick start**
1. Map user intent to a **slug** (kebab-case) or list catalog: `page/oi-awesome-ui/styles/index.json`.
2. Read `<pkg-dir>/page/oi-awesome-ui/styles/<slug>/SKILL.md` (+ optional `DESIGN.md`).
3. Implement UI in the user's stack using that style's tokens and rules.

**Example prompts**
- 「用 glassmorphism 做 SaaS 落地页」
- 「oi-awesome-ui 里适合 B2B 的三种风格？」
- 「Review 这页是否符合 minimal tokens」

**Do not use for:** ffmpeg / GIF / video (`widget/*`).

## When to use

- Building or restyling a **landing page**, marketing site, or product UI with a named aesthetic
- User names a style (e.g. glassmorphism, bento, neobrutalism) or asks for a design-system look
- You need **tokens, do/don't rules, accessibility gates**, and component expectations for one visual direction

**Do not use** for ffmpeg/video, GIF conversion, or unrelated widget tasks.

---

## Step 1 — Choose a style slug

1. If the user named a style, map it to a **slug** (kebab-case, e.g. `glassmorphism`, `minimal`, `shadcn`).
2. Otherwise, read the catalog:

```bash
python3 -c "import json; d=json.load(open('<pkg-dir>/page/oi-awesome-ui/styles/index.json')); print('\n'.join(sorted(d)))"
```

3. Offer **2–3** slugs that fit the product (SaaS → `clean`, `professional`, `shadcn`; creative → `artistic`, `expressive`; luxury → `luxury`, `elegant`).
4. Confirm one slug before implementation.

**Available slugs (62):** agentic, ant, application, artistic, bento, bold, brutalism, cafe, claymorphism, claude, clean, codex, colorful, contemporary, corporate, cosmic, creative, dashboard, doodle, dramatic, editorial, elegant, energetic, enterprise, expressive, fantasy, fiction, flat, futuristic, glassmorphism, gradient, impeccable, levels, lingo, luxury, material, matrix, minimal, modern, mono, neon, neobrutalism, neumorphism, pacman, paper, premium, professional, publication, refined, retro, riso, sega, shadcn, simple, skeumorphism, sleek, spacious, storytelling, terracotta, tetris, vibrant, vintage.

---

## Step 2 — Load the style guide (MANDATORY)

Read and follow **only** the selected style files:

| File | Path |
|------|------|
| Agent rules | `<pkg-dir>/page/oi-awesome-ui/styles/<slug>/SKILL.md` |
| Design intent (optional) | `<pkg-dir>/page/oi-awesome-ui/styles/<slug>/DESIGN.md` |

**Rules:**

- Treat the style `SKILL.md` as the **source of truth** for tokens, tone, do/don't, and quality gates.
- Do **not** mix multiple slugs in one page unless the user explicitly asks for a hybrid; if hybrid, state trade-offs.
- Strip any stale third-party install hints (e.g. external CLI pull commands); implement in the user's stack.

---

## Step 3 — Implement

1. Restate design intent in one sentence (from the style guide Mission).
2. Map **color, type, spacing** tokens from Style Foundations to CSS/Tailwind/theme variables.
3. Build sections/components per Required Output Structure in the style `SKILL.md`.
4. Run the style **Quality Gates** and **QA checklist** before delivery.

---

## Step 4 — Review checklist

- [ ] WCAG 2.2 AA contrast and visible focus (per style Accessibility section)
- [ ] Semantic tokens, not random hex per component
- [ ] No emoji as structural icons (use SVG icon sets)
- [ ] Responsive: mobile-first, no horizontal scroll on small viewports
- [ ] Writing tone matches the style guide

---

## Path convention

| Placeholder | Example |
|-------------|---------|
| `<pkg-dir>` | `~/.agents/skills/oi-skills` |
| Style catalog | `<pkg-dir>/page/oi-awesome-ui/styles/index.json` |
| Style rules | `<pkg-dir>/page/oi-awesome-ui/styles/<slug>/SKILL.md` |
