# 千问云 — Components

Tokens: `references/tokens.md` (`--pt-cn-*`). Page-level composition: **`references/layouts.md`**. Icons/images: `references/assets.md`.

Section numbers match `Guideline.html` TOC (01–14).

## Principles

**Tone:** 简洁 · 平白 · 弱描边 · 淡阴影. Flat surfaces; default `shadow: none`. Weak borders on outline controls and featured pricing rim. One accent per view: near-black CTA, one gradient word, or purple hover.

**Panel-as-card** (`layouts.md` §11.6): list-style panels are borderless outer + typography + hairline rows — no nested grey sub-cards.

**Visual QA:** CDN `Guideline.html` §08 (`组件与基础模块`); styles in `#ui-components` + `Scripts/ui.js`.

---

## §01 Hero Images

Grid: 3 × 2. Assets: `qwen-model-01` – `qwen-model-06` from `Images.json` (PNG).

- Frame: `radius-md`, `16:10`, `object-fit: cover`
- No border, no shadow
- One model poster per page in the **visual paragraph** below the title — never behind H1 (`layouts.md` §2)

Mobile: 1 column.

---

## §04 Buttons

Pill (`radius-full`). No default border on primary / secondary.

| Variant | Fill | Notes |
|---------|------|-------|
| `btn--primary` | `cta-fill` → hover `primary-550` | Light: black rest |
| `btn--secondary` | `primary-50` | Soft fill |
| `btn--outline` | transparent | Only variant with `line-200` border |
| `btn--text` | transparent | Ink → purple hover |

CTA icon: **`arrow-up-right-outlined`** via `.qc-icon`.

---

## §05 Gradients

9 tokens (`--pt-cn-gradient-1` … `9`). Text clip only. One word per screen. `gradient-9` is CN-only.

---

## §06 Featured Model Card

Same as international kit: `model-feature-card-grid` · `model-feature-card` · `model-feature-card--secondary`.

| | Primary | Secondary |
|---|---------|-----------|
| Background | `gradient-card-bg` | `neutral-50` |
| Border | optional `line-100` | same |
| Shadow | none | none |
| Padding / radius | 32 px · `radius-md` | same |

Inner: `mf-name` · `mf-desc` · `mf-tag` · `mf-price-row` · `mf-divider` · `mf-stats` · `mf-cta`.

Pricing checkmarks: **`check-mark-outlined`** (not `check-outlined`).

---

## §07 Pricing Tiers

3-up grid. Featured `.tier.is-featured`: gradient-1 border rim only.

---

## §08 组件与基础模块 (Components & Primitives)

Guideline §08 mounts the **live preview gallery** (`comp-primitives-mount[data-ui-style="qianwenai"]`) — same 53 production cards + `ui-*` primitives as the international bundle, with CN copy in specimens.

### 08.1 Gallery shell

| Piece | Rule |
|-------|------|
| Mount | `.comp-primitives-mount[data-ui-style="qianwenai"]` |
| Masonry | `.preview-grid` · `--columns: 4` · `--gap: 32px` |
| Card shell | `ui-card` — `radius-sm`, `neutral-50`, hairline rim |

See `layouts.md` §19.

### 08.2 UI primitives

`ui-button` · `ui-dialog` · `ui-sheet` · `ui-select` · `ui-checkbox` · `ui-radio-group` · `ui-switch` · `ui-slider` · `ui-progress` · `ui-spinner` · `ui-table` · `ui-accordion` · `ui-breadcrumb` · `ui-calendar` · `ui-chart` · `ui-tooltip` · `ui-sidebar` · `ui-models-filter-*` · `ui-price-text` · `ui-unit-text` · `ui-field-separator` · `ui-style-switch`

Forms: `forms-specimen` — pill inputs, `line-200` border, focus `primary-550`.

### 08.3 Production card catalog (53)

Same BEM roots as Qwen Cloud international kit — see `oi-qwencloud-ui/references/components.md` §08.3 for the full root → title table. Specimens use Chinese labels where applicable (`kitchen-island` → 模型 Playground, `notification-settings` → 通知, etc.).

Domains: foundation · models/playground · usage/analytics · billing · workspace · integrations · support.

### 08.4 Card rules

Header (`ha` + `ma`) · body · optional footer. Flat hairline rim. Manifest icons only. No stock art.

---

## §09 Tags & Badges

`.badge.is-*` (2 px radius, 10 px caps) · `.chip.is-*` (pill, 11 px).

Do not put badges and chips on the same card.

---

## §10 客户案例卡片 (Customer Card Grid)

2 × 2. Assets: `card-01` – `card-04` (or `card-06` for extended strip) from `Images.json`.

- Full-bleed PNG, `radius-md`
- White typographic panel `radius-xs`, right-aligned
- Quote · headline · body · name + title

---

## 模型卡片带 (Model strip) — 千问云营销组件

Horizontal scroll. Assets: `card-01` – `card-06`. Classes: `model-strip` · `model-card`.

- Container: `neutral-50`, `scroll-snap-type: x mandatory`, hidden scrollbar
- Card: `clamp(240px, …, 440px)` wide, no border/shadow
- Image: `radius-sm`, 250 px tall, `object-fit: cover`, hover `scale(1.04)`
- FAB: 36 px circle, white fill, bottom-right, hover fade-in, `arrow-up-right-outlined`
- Content: title `title-sm` 20px/600 · desc `body-sm` `neutral-650` · default CTA

Mobile: dual-column card width.

---

## Agent 卡片 (Agent card grid) — 千问云营销组件

2-col grid. Assets: `agent-01` – `agent-04`. Classes: `agent-card-grid` · `agent-card`.

- Card: `radius-md`, `aspect-ratio: 16/10`, full-bleed `agent-*.png`
- Glass panel (bottom-anchored, `border-radius: 18px`):
  - **blur:** `backdrop-filter: blur(1px) saturate(1.35)` + `color-mix(in srgb, neutral-50 22%, transparent)`
  - **tint:** `color-mix(in srgb, neutral-50 6%, transparent)`
  - **rim:** `inset 0 1px rgba(255,255,255,.38), inset 0 0 0 1px rgba(255,255,255,.1), inset 0 -1px 4px rgba(0,0,0,.03)`
  - **content:** z-index 3, padding `22px 16px`
  - Dark: stronger neutral mixes on blur/tint/rim (see `dev/qianwenai` References)
- Title `title-xs` 500 · body `body-sm` `neutral-650` 2-line clamp

Mobile: 1 column.

---

## Page chrome

- **Nav:** sticky, frosted, 84 px / 62 px mobile
- **Floors:** alternate `neutral-50` ↔ `neutral-100`
- **Theme:** sun/moon outlined icons from manifest
- **Breakpoint:** 1024 px; gutters 70 → 10 px

---

## Assets

**Images:** `qwen-model-*` · `card-*` · `agent-*` — `assets.md`

**Icons:** 76 SVGs — `icons.md`

**Live bundle:** `Guideline.html` + `Scripts/ui.js` — `assets.md`
