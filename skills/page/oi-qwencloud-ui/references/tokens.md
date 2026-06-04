# Qwen Cloud — Design Tokens

Source: brand guideline (`:root` / `html[data-prefers-color='dark']`). All variables use `--pt-*`. No semantic alias layer.

## Design stance

Minimal, flat, quiet. Surfaces differ by background step, not shadow. Borders are rare — a hairline only when structure needs it. Purple appears on interaction (hover, link, one gradient word), not as default chrome.

Default in the guideline preview: `--pt-shadow-light: none`, `--pt-shadow-normal: none`.

---

## Colors

### Primary (`--pt-color-primary-*`)

10 stops. Accent: `550` `#653AFF` (light). Dark remaps `550` → `#714FFC`.

Key stops: `50` `#F1EDFF` · `550` `#653AFF` · `650` `#5229E6` · `950` `#110442`

### Neutral (`--pt-color-neutral-*`)

19 stops. Same hex ladder; roles invert in dark mode (`50` white → near-black canvas, `950` ink → near-white text).

Full ramp in `Guideline.html`. Common roles:

- Canvas: `100` / body bg
- Surface: `50`, `150`
- Text primary: `950`
- Text secondary: `650`, `600`
- Placeholder: `450`

### Lines (use sparingly)

| Token | Resolves to (light) |
|-------|---------------------|
| `--pt-color-line-100` | `neutral-200` — card hairline when needed |
| `--pt-color-line-200` | `neutral-300` — outline button, input |
| `--pt-color-line-300` | `neutral-350` — hover border |

Prefer spacing and background step over new borders.

### Supporting pairs (badges / chips only)

bg + tint: gray · red · orange · green · blue · purple. Not for large surfaces.

### Functional

`--pt-color-func-success` `#0DA740` · `--pt-color-func-warning` `#FF7931` · `--pt-color-func-danger` `#F33939` · `--pt-color-func-emphasize` `#277FE4`

Links: `--pt-color-link-default` → `primary-550` · hover → `primary-650`

### CTA inversion

| Token | Light | Dark |
|-------|-------|------|
| `--pt-cta-color-fill` | `neutral-950` | `primary-550` |
| `--pt-cta-color-fill-hover` | `primary-550` | `primary-650` |
| `--pt-cta-color-font-fill` | `primary-50` | `primary-50` |
| `--pt-cta-secondary-color-fill` | `primary-50` | `neutral-400` |
| `--pt-cta-secondary-color-fill-hover` | `primary-150` | `primary-850` |
| `--pt-cta-secondary-color-font-fill` | `primary-550` | `neutral-800` |

Light primary button: near-black rest, purple hover. No purple fill at rest in light mode.

### Gradients

8 tokens (`--pt-gradient-1` … `8`). Text-fill only — one word per screen. Not for buttons, cards, or backgrounds.

Card wash: `--pt-gradient-card-bg` — `135deg`, `neutral-150` → `neutral-50`. Almost flat; no visible gradient band.

Decoration accents (`--pt-color-accent-mint` etc.): stat dots only.

---

## Typography

| Token | Role |
|-------|------|
| `--pt-font-base` | Inter + system sans |
| `--pt-font-mono` | Roboto Mono — labels, pricing |
| `--pt-font-code` | Consolas stack |

Tracking: tight `-0.02em` (headings) · normal `0` · loose `0.02em` (body).

Scale (size / line-height): heading-2xl 72/76 · heading-md 44/50 · title-lg 28/34 · title-md 24/30 · body-lg 18/24 · body-md 16/22 · body-sm 14/20 · caption-md 12/16

Fluid: `--pt-heading-font-size-fluid-md`, `--pt-title-font-size-fluid-md` for responsive section titles.

---

## Spacing

2 px base. `--pt-spacing-N` = N × 2 px (e.g. `12` = 24 px).

Common: `8` 16 px · `12` 24 px · `16` 32 px · `24` 48 px

Aliases (prefer these):

| | sm | md | lg |
|---|----|----|-----|
| `--pt-margin-*` | 24 | 36 | 48 |
| `--pt-padding-*` | 14 | 18 | 24 |
| `--pt-gap-*` | 12 | 14 | 18 |

---

## Radius

| Token | px | Typical use |
|-------|----|-------------|
| `--pt-radius-md` | 24 | Cards, hero frames |
| `--pt-radius-xs` | 12 | Inner panels |
| `--pt-radius-full` | 999 | Buttons, inputs, tags |

Soft corners, not sharp. Pill for all CTAs.

---

## Borders & elevation

Line widths: `thin` 0.5 px · `normal` 1 px · `thick` 1.5 px.

Default: no border. When required: `1px solid var(--pt-color-line-100)`.

Shadows exist as tokens but guideline runs flat (`none`). If depth is needed, step the surface (`50` → `150`) before adding shadow. Production reference values in Guideline §13 — use lightly.

---

## Motion

`--pt-motion-fast` 0.25s · `--pt-motion-slow` 0.7s · ease-in-out default. Color and opacity only. No bounce.

---

## Layout

`--pt-layout-limit-width` 1920px · max-width `min(100vw - 140px, 1920px)` · inner `min(100vw - 280px, 1780px)` · read box 640px

Breakpoint: 1024px. Mobile gutters 10px.

---

## Images (CDN)

Manifest: https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Images.json

- `card_1.jpg` – `card_4.jpg` — customer cards
- `flower_01.jpg` – `flower_06.jpg` — hero backdrops (one per page)

See `assets.md`.

---

## Icons

48 SVGs on CDN. Manifest: https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Icons.json — see `icons.md`.
