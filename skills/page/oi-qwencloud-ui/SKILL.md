---
name: oi-qwencloud-ui
description: >-
  Qwen Cloud brand UI: simple flat surfaces, weak borders, light shadow only, purple-on-hover CTAs,
  Inter + Roboto Mono. Icons and photos MUST come from CDN Icons.json / Images.json manifests.
  TRIGGER for Qwen Cloud style, oi-qwencloud-ui, qwencloud-ui, or Qwen Cloud landing/product UI.
  NOT for generic UI, other brands, or video/media tools.
---
# Oi Qwen Cloud UI — Qwen Cloud Design System

**Author:** Alibaba Cloud Design

**Skill path:** `<skill-dir>/` (e.g. `~/.cursor/skills/oi-qwencloud-ui`).

Reference specs: `references/` (`tokens.md`, `components.md`, `layouts.md`, `icons.md`, `assets.md`). Brand kit on CDN — see `assets.md`.

---

## 核心约束（Agent 必守）

### ★ 头号铁律 — 大标题永远不要压在视觉元素上

**Title + subtitle are their own clean paragraph on white (`--pt-color-neutral-50`). The image/video/flower/gradient is a SEPARATE panel below or beside. Two paragraphs, never one box.**

- ❌ Wrong: `<div class="hero-panel" style="background-image: flower.jpg"><h1>AI 驱动的…</h1></div>` — heading sitting over the flower
- ✅ Right: `<header><h1>Ship the next</h1><p>subtitle</p><CTAs/></header>` on `neutral-50`, **then** a separate `<div class="hero-panel">image/video</div>` below with 48–64 px whitespace between
- No `text-shadow`, no dark overlay "for legibility" — if a heading needs help reading, it's in the wrong place; move it up to the canvas paragraph
- Upper bound for text on imagery: **title-lg 28 px** (small metric chips, captions). Anything ≥36 px belongs in the title paragraph on canvas
- Only exception: era closing-CTA hero (`layouts.md` §2.5) — has an art-directed quiet video backdrop and centered 72 px h2. Don't generalize this to other heroes

Full rule + DO/DON'T diagrams: `references/layouts.md` §2.

### 视觉气质：简洁 · 平白 · 弱描边 · 淡阴影

- **简洁** — 克制组件数量；营销页以 Inter 排版为主，图标小而稀。
- **平白** — `neutral-50` / `150` / `100` 面色阶分层；卡片与 hero 框架默认无装饰投影。
- **弱描边** — 仅 outline 按钮、表单、pricing featured  rim 等必要处使用 `line-200` 1px；不靠粗框线分区。
- **淡阴影** — 新页面默认 flat（`shadow: none`）；若需可读性分层，仅用 token 阴影且极轻，禁止厚重 drop-shadow / 发光底。

### 配图与图标：只从 manifest 抽取

**禁止** stock 图、占位图、自造 URL、Lucide/emoji、与 kit 混用的随机 SVG。

| 类型 | 做法 |
|------|------|
| **配图** | fetch `Images.json` → 使用数组中的 **绝对 URL**（`flower_*` 每页一张 hero；`card_1–4` 客户故事） |
| **图标** | fetch `Icons.json` → 按场景选 `id`，静态页用条目 **`href`**；React 优先 `@ali/qwen-cloud-icons` 同名组件 |

实现前若未读 manifest，先 fetch 再写 markup。详见 `references/assets.md`.

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-qwencloud-ui` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-qwencloud-ui`), then ask what they want to accomplish.

**Triggers:** `oi-qwencloud-ui`, `qwencloud-ui`, qwen cloud ui, qwen cloud / qwencloud / Qwen Cloud / QwenCloud style & design, Qwen Cloud 风格 / 设计系统.

**Quick start**
1. Read this `SKILL.md` (philosophy, workflow, anti-patterns).
2. Load specs: `<skill-dir>/references/tokens.md`, `components.md`, `layouts.md`, `icons.md`, `assets.md`.
3. Declare Inter + Roboto Mono, ask light/dark, implement with `--pt-*` tokens.

**Example prompts**
- 「用 oi-qwencloud-ui 做 Qwen Cloud 产品页」
- 「按 Qwen Cloud tokens 做 model feature 双卡」
- 「Qwen Cloud 浅色 pricing + floral hero」

**Do not use for:** generic UI without explicit Qwen Cloud request; other brand kits; ffmpeg / video (`widget/*`).

## When to use

- User wants **Qwen Cloud** brand UI (cloud product marketing, model cards, pricing tiers, customer stories)
- Pages needing floral hero grids, near-black light-mode CTAs, and sparse outlined icons
- Token-level specs for forms, tags, gradients-as-text-only, and flat elevation

**Do not use** unless the user names Qwen Cloud or this skill.

---

## 1. Design philosophy

- **Simple, flat, quiet.** 简洁平白：弱描边、淡阴影（见核心约束）；色阶与留白优先于装饰。
- **Quiet and flat.** Background steps (`neutral-50` / `150` / `100`) replace heavy shadows; hairlines only when structure is unclear.
- **Purple on interaction.** Light primary CTA: near-black at rest, `primary-550` on hover — not purple fill at rest.
- **One accent per view.** Pick among: black CTA, one gradient word, or purple hover — do not compete.
- **Typography-led.** Inter for all marketing type; Roboto Mono for labels, pricing, uppercase captions.
- **Gradients are text-only.** Eight `--pt-gradient-*` tokens clip to single words; featured tier may use 1px gradient border rim only.
- **Photography as hero.** One `flower_*` per page behind headline; customer cards use `card_1–4` full-bleed art.

**Fonts (declare before coding):**

```html
<link rel="stylesheet" href="https://acd-assets.alicdn.com/acd_work/web-fonts/inter/inter.css" />
```

Roboto Mono: see `references/tokens.md` § Typography.

---

## 2. Craft rules

### 2.1 Token namespace

Use `--pt-*` from `references/tokens.md` verbatim. **Spacing is literal px on a 2-px rhythm** — there is no `--pt-spacing-N` ladder. Pick from: `4 · 6 · 8 · 10 · 12 · 14 · 16 · 18 · 20 · 24 · 28 · 32 · 36 · 40 · 44 · 48 · 56 · 64 · 72 · 96 · 122 · 138`. See `references/layouts.md` §10.

### 2.2 Signature patterns

| Pattern | Rule |
|---------|------|
| Primary button | Pill; light: `neutral-950` fill → hover `primary-550`; icon `arrow-up-outlined` |
| Secondary | `primary-50` soft fill, no border |
| Outline | Only variant with `line-200` border |
| Model cards | 2-col grid; primary uses `gradient-card-bg`; secondary `neutral-50`; no shadow |
| Pricing | 3-up; featured tier gradient-1 **border rim** only |
| Hero | `neutral-100` flat; title up to 72/76; one `.grad` word |
| Customer card | Full-bleed image + white typographic panel, `radius-md` / `radius-xs` |
| Theme toggle | `sun-outlined` · `moon-outlined` |

### 2.3 Layout

Page-level composition lives in `references/layouts.md`. Highlights:

- **Three container layers** (§1): `.layout-max-wide` (outer, ~140 px viewport gutter, for framed visuals) → `.layout-max-inner-wrap > .layout-max-inner` (inner, ~280 px gutter, **default** for headings/grids/copy) → reader (768 px cap, for prose). Never bypass.
- **Heading on white, never on imagery** (§2): giant H1/H2 sits on `--pt-color-neutral-50` (canvas) or `--pt-color-neutral-100` (tinted floor). Photos/videos sit in their *own* framed panel below or beside. Only exception: era closing CTA (§2.3).
- **9 hero variants A–I** (§3); **3 floor-head patterns A/B/C** + asymmetric D (§5); grid table at §7 — pull a row, don't invent.
- **Card system** (§11): two equally first-class flavors — bordered (hairline `--pt-color-line-100` on canvas) and **borderless** (bg-step separation when sitting on a stepped panel). Decision tree §11.4. Eight internal recipes §11.2. Ten clean-flat signals §11.3.
- **Radius vocabulary (5):** `full · xs · sm · md · lg` → 999 / 12 / 18 / 24 / 36 (§15).
- **Section rhythm:** top-of-floor `96 / 122 / 138`; heading→body `48 / 60 / 64` (§1.5).
- **Sticky offset:** `calc(var(--pt-nav-backdrop-offset) + 12px)` for rails; nav is 84 px desktop / 62 px mobile.
- **Data-page interaction** (§17): models toolbar shares `height: 40 + radius-full` across all controls; search uses gradient mask-composite focus rim; popovers are borderless + `--pt-shadow-light`.
- **Breakpoint:** 1024 px; mobile gutters 20 px (utilities handle it); grids collapse to `1fr`.

### 2.4 Icons & assets (CDN)

All brand assets live on CDN — **not** in `<skill-dir>`. See `references/assets.md`.

| Asset | Source |
|-------|--------|
| Guideline | `…/qwencloud/Guideline.html` |
| Icons (48) | `…/qwencloud/Icons.json` → `Icons/*.svg` |
| Images | `…/qwencloud/Images.json` → absolute JPG URLs |
| Logo | Inline in Guideline |

**Mandatory:** every JPG from `Images.json` — no substitutes. Icons: prefer `Icons.json` / `@ali/qwen-cloud-icons`; when a needed glyph is **not** in the 48-icon manifest, fall back to **Tabler outlined** (`stroke: 1.5`, `currentColor`). One kit per screen — manifest **or** Tabler, never mixed. See `references/icons.md`.

**Dark mode icons in static HTML:** `filter: invert(1)` on `.qc-icon-img` where guideline specifies.

---

## 3. Anti-patterns

- No purple glyph fill on icons (`currentColor` only)
- No stock/placeholder images; no icons outside `Icons.json` or Tabler-outlined fallback
- No heavy shadow on cards; new work stays flat — 淡阴影 token only when Guideline requires legibility
- No gradient button or card backgrounds
- No multiple gradient words per screen
- No badges + chips on the same card
- No bounce easing; opacity/color only
- Do not mix icon kits on the same screen (manifest **or** Tabler, never both, never with Lucide/Heroicons/Feather)
- No orphan spacing — values must land on the 2-px rhythm (`layouts.md` §9)
- No invented column counts/gaps — pull from `layouts.md` §4 grid table
- No new radius values outside the 5-token vocabulary (`layouts.md` §8)

---

## 4. Workflow

1. **Declare fonts** — Inter, Roboto Mono
2. **Ask mode** — light or dark
3. **Load tokens** — `references/tokens.md`
4. **Pick layout** — `references/layouts.md`: page shell (§1) → hero variant (§2) → section header pattern (§3) → grid from the §4 table → filter/reader if needed (§5–6)
5. **Compose components** — `references/components.md` (buttons, model card, pricing, forms, customer card, sub-blocks)
6. **Manifests** — fetch `Icons.json` + `Images.json`; bind all photos to manifest URLs (required); icons from manifest or Tabler fallback
7. **Guideline** — open `Guideline.html` for visual QA on unfamiliar sections
8. **Review** — checklist below + `layouts.md` §18

---

## 5. Reference files

| File | Path | Scope |
|------|------|-------|
| Tokens | `<skill-dir>/references/tokens.md` | Color, type, radius, motion, width tokens (`--pt-*`) |
| Components | `<skill-dir>/references/components.md` | Buttons, cards, pricing, forms, customer card |
| Layouts | `<skill-dir>/references/layouts.md` | Container layers, heading-on-white rule, heroes A–I, floor taxonomy, headers A/B/C, grids, sub-blocks, typography, card archetypes (bordered/borderless/featured-rim/media/tile/composite/form/overlay), data-page interaction |
| Icons | `<skill-dir>/references/icons.md` | Manifest + Tabler fallback rules |
| CDN assets | `<skill-dir>/references/assets.md` | Image / icon manifest URLs |

---

## 6. Review checklist

- [ ] Light CTA: black rest, purple hover — not purple at rest
- [ ] ≤1 gradient text word per screen (plus allowed tier border rim)
- [ ] Cards and hero frames flat — no decorative shadow
- [ ] Model primary vs secondary card backgrounds distinct
- [ ] `arrow-up-outlined` on primary CTA
- [ ] `flower_*` / `card_*` URLs from `Images.json` only; one floral hero per page
- [ ] Icons from `Icons.json` / `@ali/qwen-cloud-icons` first; Tabler outlined only as fallback
- [ ] 简洁平白：弱描边、无重阴影、无渐变按钮/卡片底
- [ ] Spacing values land on the 2-px rhythm; grids/radii pull from `layouts.md` vocabulary
- [ ] Heading sits on canvas/tinted floor — **never** on imagery (only exception: era closing CTA per `layouts.md` §2.3)
- [ ] Card chosen via the §11.4 decision tree (bordered vs borderless; A–H archetypes); padding + radius from §11.5
- [ ] Data-page (if applicable) passes the `layouts.md` §17.14 interaction-layer checklist
- [ ] Page passes the layout checklist in `layouts.md` §18
