# 千问云 — Design Tokens

Source: brand guideline (`:root` / `html[data-prefers-color='dark']`). All variables use `--pt-cn-*`. No semantic alias layer.

## Design stance

扁平、克制、安静。层级靠背景色阶区分，不靠阴影。边框极少——仅在结构必须时用发丝线。品牌色只在交互态出现（hover、链接、渐变文字），不作为默认装饰。

Default shadows exist but marketing surfaces stay flat — use `--pt-cn-shadow-*` only when Guideline specimens require legibility.

---

## Colors

### Primary (`--pt-cn-color-primary-*`)

10 stops. Accent: `550` `#5B58FF` (light). Dark remaps `550` → `#714FFC`.

Key stops: `50` `#F0F3FF` · `550` `#5B58FF` · `650` `#4500F3` · `950` `#000153`

### Neutral (`--pt-cn-color-neutral-*`)

19 stops. Roles invert in dark mode (`50` canvas ↔ near-black, `950` ink ↔ near-white).

Common roles: canvas `100` · surface `50` / `150` · text `950` · secondary `650`/`600` · placeholder `450`

### Lines (use sparingly)

| Token | Resolves to (light) |
|-------|---------------------|
| `--pt-cn-color-line-100` | `neutral-200` — card hairline |
| `--pt-cn-color-line-200` | `neutral-300` — outline button, input |
| `--pt-cn-color-line-300` | `neutral-350` — hover border |

### Supporting pairs (badges / chips only)

bg + tint: gray · red · orange · green · blue · purple. Not for large surfaces.

### Functional

`--pt-cn-color-func-success` `#0DA740` · `--pt-cn-color-func-warning` `#FF7931` · `--pt-cn-color-func-danger` `#F33939` · `--pt-cn-color-func-emphasize` `#277FE4`

Links: `--pt-cn-color-link-default` → `primary-550` · hover → `primary-650`

### Accent decoration

`mint` · `orchid` · `electric-blue` · `sky` · `rose` · `emerald` · `apricot` — stat dots only.

### CTA inversion

| Token | Light | Dark |
|-------|-------|------|
| `--pt-cn-cta-color-fill` | `neutral-950` | `primary-550` |
| `--pt-cn-cta-color-fill-hover` | `primary-550` | `primary-650` |
| `--pt-cn-cta-color-font-fill` | `primary-50` | `primary-50` |
| `--pt-cn-cta-secondary-color-fill` | `primary-50` | `neutral-400` |
| `--pt-cn-cta-secondary-color-fill-hover` | `primary-150` | `primary-850` |
| `--pt-cn-cta-secondary-color-font-fill` | `primary-550` | `neutral-800` |

Light primary button: near-black rest, purple hover.

### Gradients

9 tokens (`--pt-cn-gradient-1` … `9`). Text-fill only — one word per screen. `gradient-9` is CN-only. Not for buttons, cards, or backgrounds.

Card wash: `--pt-cn-gradient-card-bg` — `135deg`, `neutral-150` → `neutral-50`.

---

## Typography

### Font families

| Token | Role |
|-------|------|
| `--pt-cn-font-base` | Inter, **PingFang SC**, system sans |
| `--pt-cn-font-mono` | **Roboto Mono**, PingFang SC, system sans |
| `--pt-cn-font-code` | Consolas stack |

千问云 vs 国际站：行高更大（中文排版）、标题字距用固定 px、部分标题字重 600。

### Size scale (size / line-height; px)

| Token | Size | Line | Use |
|-------|-----:|-----:|-----|
| `--pt-cn-heading-font-size-3xl` | 78 | 94 | Hero display (CN-only step) |
| `--pt-cn-heading-font-size-2xl` | 72 | 86 | Marketing hero h1 |
| `--pt-cn-heading-font-size-xl` | 64 | 84 | Tagline split hero |
| `--pt-cn-heading-font-size-lg` | 60 | 78 | Centered intro hero |
| `--pt-cn-heading-font-size-md` | 44 | 58 | Section heads |
| `--pt-cn-heading-font-size-sm` | 36 | 46 | Compact h1 / legal |
| `--pt-cn-title-font-size-lg` | 28 | 36 | Sub-section title |
| `--pt-cn-title-font-size-md` | 24 | 36 | Card title |
| `--pt-cn-title-font-size-sm` | 20 | 30 | Card headline |
| `--pt-cn-title-font-size-xs` | 18 | 28 | Agent glass panel title |
| `--pt-cn-body-font-size-lg` | 18 | 28 | Hero/section subtitle |
| `--pt-cn-body-font-size-md` | 16 | 24 | Body |
| `--pt-cn-body-font-size-sm` | 14 | 20 | Card meta |
| `--pt-cn-body-font-size-xs` | 13 | 20 | Caption |

Letter-spacing: headings `0.25px` · body `0.4px` (lg `0.5px`) · titles `0`.

Fluid: `--pt-cn-heading-font-size-fluid-md: clamp(36px, 8vw, 52px)` · `--pt-cn-title-font-size-fluid-md: clamp(28px, 6vw, 40px)`

---

## Spacing

**2-px rhythm.** `--pt-cn-spacing-N` = N × 2 px.

Scale: `1` 2px · `2` 4px · `3` 6px · `4` 8px · `5` 10px · `6` 12px · `7` 14px · `8` 16px · `9` 18px · `10` 20px · `11` 22px · `12` 24px · `13` 26px · `14` 28px · `15` 30px · `16` 32px · `18` 36px · `20` 40px · `22` 44px · `24` 48px · `28` 56px · `32` 64px · `36` 72px · `40` 80px · `44` 88px · `48` 96px · `57` 114px · `61` 122px · `69` 138px · `77` 154px

Semantic: `--pt-cn-margin-sm/md/lg` → `spacing-12/18/24` · `--pt-cn-padding-sm/md/lg` → `14px/18px/spacing-12` · `--pt-cn-gap-sm/md/lg` → `spacing-6/14px/spacing-9`

---

## Radius

Working set: `full` 999 · `xs` 12 · `sm` 18 · `md` 24 · `lg` 36. Also `2xs` 8 · `3xs` 6 · `4xs` 2 for badges.

---

## Borders & elevation

Line widths: `thin` 0.5 px · `normal` 1 px · `thick` 1.5 px.

| Token | Light | Dark |
|-------|-------|------|
| `--pt-cn-shadow-light` | `0 8px 24px rgba(83,91,107,.06)` | `0 8px 24px rgba(0,0,0,.28)` |
| `--pt-cn-shadow-normal` | `0 16px 40px rgba(83,91,107,.10)` | `0 16px 40px rgba(0,0,0,.38)` |

---

## Motion

`--pt-cn-motion-fast` 0.25s · `--pt-cn-motion-slow` 0.7s · ease-in-out. Color and opacity only.

---

## Z-index (`--pt-cn-z-*`)

`hide` -1 · `base` 0 · `popup-inline` 50 · `sticky` 100 · `fixed` 200 · `sidebar` 300 · `float-widget` 500 · `sub-nav` 900 · `top-nav` 1000 · `top-banner` 1050 · `dropdown` 1100 · `popover` 1200 · `tooltip` 1300 · `drawer-backdrop` 1400 · `drawer` 1410 · `dialog-backdrop` 1500 · `dialog` 1510 · `notification` 1600 · `max` 2000

---

## Layout

| Token | Value | Use |
|-------|-------|-----|
| `--pt-cn-layout-limit-width` | 1920px | Absolute cap |
| `--pt-cn-layout-max-width` | `min(100vw - 140px, 1920px)` | Outer (`.layout-max-wide`) |
| `--pt-cn-layout-max-inner` | `min(100vw - 280px, 1780px)` | Inner (`.layout-max-inner`) |
| `--pt-cn-layout-max-read-box` | **640px** | Reader column (CN prose) |
| `--pt-cn-nav-backdrop-offset` | 84px desktop · 62px mobile | Sticky offset |

Breakpoint: 1024px. Desktop gutters **70px**; mobile **10px**.

Full page composition: `layouts.md`.

---

## Images (CDN)

Manifest: https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Images.json

| Key | Role |
|-----|------|
| `qwen-model-01.png` – `qwen-model-06.png` | Hero / model imagery (one per page) |
| `card-01.png` – `card-06.png` | Customer / model-strip cards |
| `agent-01.png` – `agent-05.png` | Agent cards |

See `assets.md`.

---

## Icons

76 SVGs on CDN. Manifest: https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Icons.json — see `icons.md`.

---

## Dark / Light mode

Set `<html data-prefers-color='light'|'dark'>`. Use tokens — do not hard-code light literals in dark overrides.

- Light CTA: black rest → purple hover; dark CTA: purple rest → deeper purple hover
- Static icons: `filter: invert(1)` on `.qc-icon-img` in dark mode where Guideline specifies
- Primary CTA uses `arrow-up-right-outlined`
