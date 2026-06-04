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

Reference specs: `references/` (`tokens.md`, `components.md`, `icons.md`, `assets.md`). Brand kit on CDN — see `assets.md`.

---

## 核心约束（Agent 必守）

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

**Triggers:** `oi-qwencloud-ui`, `qwencloud-ui`, Qwen Cloud style, Qwen Cloud design, 千问云 / Qwen Cloud 风格.

**Quick start**
1. Read this `SKILL.md` (philosophy, workflow, anti-patterns).
2. Load specs: `<skill-dir>/references/tokens.md`, `components.md`, `icons.md`, `assets.md`.
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

Use `--pt-*` from `references/tokens.md` verbatim. Spacing base: **2px** (`--pt-spacing-N` = N × 2px).

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

- Radius: cards/hero `24px` (`--pt-radius-md`); pills `999`
- Max width `min(100vw - 140px, 1920px)`; inner `min(100vw - 280px, 1780px)`
- Breakpoint **1024px**; mobile gutters **10px**

### 2.4 Icons & assets (CDN)

All brand assets live on CDN — **not** in `<skill-dir>`. See `references/assets.md`.

| Asset | Source |
|-------|--------|
| Guideline | `…/qwencloud/Guideline.html` |
| Icons (48) | `…/qwencloud/Icons.json` → `Icons/*.svg` |
| Images | `…/qwencloud/Images.json` → absolute JPG URLs |
| Logo | Inline in Guideline |

**Mandatory:** every icon and JPG from `Icons.json` / `Images.json` — no substitutes. React: `@ali/qwen-cloud-icons` when available; static HTML: CDN `href` from manifest. See `references/icons.md`.

**Dark mode icons in static HTML:** `filter: invert(1)` on `.qc-icon-img` where guideline specifies.

---

## 3. Anti-patterns

- No purple glyph fill on icons (`currentColor` only)
- No stock/placeholder images or icons outside `Images.json` / `Icons.json`
- No heavy shadow on cards; new work stays flat — 淡阴影 token only when Guideline requires legibility
- No gradient button or card backgrounds
- No multiple gradient words per screen
- No badges + chips on the same card
- No bounce easing; opacity/color only
- Do not mix Lucide with this kit on the same screen

---

## 4. Workflow

1. **Declare fonts** — Inter, Roboto Mono
2. **Ask mode** — light or dark
3. **Load tokens** — `references/tokens.md`
4. **Compose** — `references/components.md` (hero, buttons, model card, pricing, forms, customer card)
5. **Manifests** — fetch `Icons.json` + `Images.json`; bind all icons/photos to manifest URLs (required)
6. **Guideline** — open `Guideline.html` for visual QA on unfamiliar sections
7. **Review** — checklist below

---

## 5. Reference files

| File | Path |
|------|------|
| Tokens | `<skill-dir>/references/tokens.md` |
| Components | `<skill-dir>/references/components.md` |
| Icons | `<skill-dir>/references/icons.md` |
| CDN assets | `<skill-dir>/references/assets.md` |

---

## 6. Review checklist

- [ ] Light CTA: black rest, purple hover — not purple at rest
- [ ] ≤1 gradient text word per screen (plus allowed tier border rim)
- [ ] Cards and hero frames flat — no decorative shadow
- [ ] Model primary vs secondary card backgrounds distinct
- [ ] 48-icon kit only; `arrow-up-outlined` on primary CTA
- [ ] `flower_*` / `card_*` URLs from `Images.json` only; one floral hero per page
- [ ] Icons from `Icons.json` / `@ali/qwen-cloud-icons` only
- [ ] 简洁平白：弱描边、无重阴影、无渐变按钮/卡片底
- [ ] Spacing uses `--pt-spacing-*` / margin-padding aliases
