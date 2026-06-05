# Qwen Cloud — Components

Tokens: `references/tokens.md` (`--pt-*`). Page-level composition (page shell, hero variants, section headers, grid tables, sidebar/reader patterns, sub-block vocabulary): **`references/layouts.md`** — read it before placing any component. Icons/images: `references/assets.md`.

## Principles

**Tone:** 简洁 · 平白 · 弱描边 · 淡阴影. Flat surfaces; default `shadow: none` (淡阴影 token only when Guideline needs legibility). Weak 1px borders on outline controls and featured pricing rim — otherwise `neutral-50` / `150` / `100` and whitespace. One accent per view: near-black CTA, or one gradient word, or purple on hover — not all three competing.

**Panel-as-card composition** (`layouts.md` §11.6): when a card hosts a list of repeated rows (recommended models, cost summary, plan benefits, FAQ, bundle items), the outer panel is **borderless** (`gradient-card-bg` or `neutral-100` step, no 1px hairline, no shadow) and interior rows separate via **typography + a single hairline** — never nested grey-bg sub-cards.

---

## §01 Hero Images

Grid: 3 × 2. Assets: `flower_01` – `flower_06`.

- Frame: `radius-md`, `16:10`, `object-fit: cover`
- No border, no shadow on frame
- One floral per page, full-bleed behind headline

Mobile: 1 column.

> Pick the appropriate **hero variant (A–H)** from `layouts.md` §2 before composing — the floral grid only applies to hero variants B and showcase blocks.

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

**If a model card hosts a sub-list** (recommended models, related items, included assets), treat the card as a panel-as-card (`layouts.md` §11.6): drop the optional `line-100` outer hairline and lay rows directly on the panel with `border-b 1px line-100` between rows. Do **not** wrap each row in its own `neutral-100/150` filled rounded sub-card.

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

Page-level composition lives in **`layouts.md`** — page shell, container utilities (`.layout-max-wide` / `.layout-max-inner`), hero variants A–H, section header patterns A/B/C, grid table, filter rail, reader column, sub-block vocabulary, and the layout review checklist (§13).

Quick pointers when assembling a page:

- **Nav:** sticky, frosted, no bottom border. Height 84 px desktop / 62 px mobile (`--pt-nav-backdrop-offset`).
- **Section background steps:** alternate `neutral-50` ↔ `neutral-100` for visual rhythm — not bordered boxes.
- **Theme toggle:** `sun-outlined` · `moon-outlined`.
- **Breakpoint:** 1024 px; grids collapse to `1fr`; gutters 36 → 20 px (utilities handle it).

---

## Assets

**Images:** CDN `Images.json` — `card_1–4.jpg` · `flower_01–06.jpg` (`assets.md`)

**Icons:** CDN `Icons.json` — 48 outlined SVGs; Tabler outlined as fallback for missing glyphs (`icons.md`)
