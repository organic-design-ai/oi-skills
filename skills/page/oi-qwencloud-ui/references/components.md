# Qwen Cloud — Components

Tokens: `references/tokens.md` (`--pt-*`). Icons/images: **manifest only** — `references/assets.md`.

## Principles

**Tone:** 简洁 · 平白 · 弱描边 · 淡阴影. Flat surfaces; default `shadow: none` (淡阴影 token only when Guideline needs legibility). Weak 1px borders on outline controls and featured pricing rim — otherwise `neutral-50` / `150` / `100` and whitespace. One accent per view: near-black CTA, or one gradient word, or purple on hover — not all three competing.

---

## §01 Hero Images

Grid: 3 × 2. Assets: `flower_01` – `flower_06`.

- Frame: `radius-md`, `16:10`, `object-fit: cover`
- No border, no shadow on frame
- One floral per page, full-bleed behind headline

Mobile: 1 column.

---

## §04 Buttons

Pill (`radius-full`). No default border on primary / secondary.

| Variant | Fill | Notes |
|---------|------|-------|
| `btn--primary` | `cta-fill` → hover `primary-550` | Light: black rest |
| `btn--secondary` | `primary-50` | Soft fill, no outline |
| `btn--outline` | transparent | Only variant with border (`line-200`) |
| `btn--text` | transparent | Ink → purple hover |

Sizes: default 14 px · `btn--sm` · `btn--xl` 54 px height.

CTA icon: `arrow-up-outlined` via `.qc-icon`.

---

## §06 Model Card

Grid: 2 columns. Classes: `model-feature-card-grid` · `model-feature-card` · `model-feature-card--secondary`.

| | Primary | Secondary |
|---|---------|-----------|
| Background | `gradient-card-bg` | `neutral-50` |
| Border | optional `line-100` hairline | same |
| Shadow | none | none |
| Padding | 32 px | 32 px |
| Radius | `radius-md` | `radius-md` |

Inner: `mf-name` · `mf-desc` (2-line clamp) · `mf-tag` (pill, purple outline) · `mf-price-row` · `mf-divider` (`line-100`) · `mf-stats` · `mf-cta`.

Primary CTAs: primary + outline. Secondary card: secondary + text.

---

## §07 Pricing

3-up grid. Tier: `neutral-50` fill, `line-100` hairline, `radius-md`, no shadow.

Featured (`.tier.is-featured`): gradient-1 border rim only — no ribbon, no extra shadow. Checkmarks: `check-outlined`.

---

## §08 Forms

Pill inputs. Border `line-200`; focus → `primary-550` (no glow ring in guideline). Disabled: `neutral-150` bg. Error: danger border + hint.

Labels: 12 px uppercase mono tone.

---

## §09 Tags & Badges

Small pills. Supporting bg + tint pairs. No border on filled variants. `is-outline` badge is the only outlined tag.

Do not put badges and chips on the same card.

---

## §10 Customer Card

2 × 2. Assets: `card_1` – `card_4`.

- Card: full-bleed image, `radius-md`, no outer border
- Panel: white fill, `radius-xs`, right-aligned — typography only, no logo
- Prefer flat panel (no shadow) in new work; guideline demo uses a light shadow for legibility on busy art

Quote · headline · body · name + title (bottom-right).

---

## §05 Gradients

8 tokens. Text clip only. One word per screen. Featured tier border is the exception (1 px rim, not a fill).

---

## Page chrome

**Hero:** `neutral-100` bg, flat. Title 72/76; one `.grad` word.

**Nav:** sticky, light frosted bar. No bottom border.

**Sections:** `.numbered` / `.numbered.is-tinted` alternate — tint is a subtle bg step, not a bordered box.

**Theme toggle:** `sun-outlined` · `moon-outlined`.

---

## Responsive

1024px breakpoint. Desktop gutter 140px; mobile 10px. Grids collapse to 1 column.

Max width 1920px.

---

## Assets

**Images:** CDN `Images.json` — `card_1–4.jpg` · `flower_01–06.jpg` (`assets.md`)

**Icons:** CDN `Icons.json` — 48 outlined SVGs (`icons.md`)
