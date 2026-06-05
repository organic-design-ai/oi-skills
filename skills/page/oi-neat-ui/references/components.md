# Neat — Components

Tokens: `references/tokens.md`. Icons/images: **manifest only** — `references/assets.md` (`Icons.json`, `Images.json`).

**Tone:** 简洁 · 平白 · 弱描边 · 淡阴影. Solid fills; hierarchy = type, neutral steps, whitespace. Hairline borders only where listed (tertiary, outline cases). Default **no** card shadow; if needed, token shadow only, very light.

---

## 1. Buttons

Pill shape (`--pt-radius-full`). Flat color transitions at `0.25s`.

| Size | H | px | Font |
|------|---|-----|------|
| xs | 30 | 14 | 14 |
| sm | 36 | 18 | 14 |
| md | 40 | 20 | 14 |
| md-plus | 44 | 30 | 14 |
| lg | 48 | 22 | 14 |
| xl | 54 | 26 | 16 |
| 2xl | 60 | 32 | 16 |

| Variant | Fill | Text | Hover |
|---------|------|------|-------|
| primary | `--pt-cta-color-fill` | `--pt-cta-color-font-fill` | `--pt-cta-color-fill-hover` |
| secondary | `--pt-cta-secondary-color-fill` | `--pt-cta-secondary-color-font-fill` | secondary hover token |
| tertiary | transparent | `neutral-950` | border only (see below) |
| plan-lite | `accent-a1` | white | slight brightness |
| plan-pro | `primary-550` | white | `primary-650` |

**tertiary** — only variant with a visible edge: 1 px `line-100`, hover `line-300`. No fill.

Disabled: `neutral-400` / `neutral-550`, no interaction.

**Text link** — not a button. Color `primary-550`, weight 500, no underline. Optional 12 px chevron. No border.

---

## 2. Cards

All flat. **No shadow. No grey-bg inset sub-cards** — when listing items inside a card (recommended models, included specs, cost summary rows, benefit groups), keep the card interior on `neutral-50` and divide rows with `border-b border-line1` only. See `layouts.md` §5.6.

### Hero

- Bg `neutral-50`
- Radius 20 px
- One hero JPG, `cover`, `right center`
- Content + search; open layout

### Services (`feature-card`)

- Bg `neutral-50` (or `primary-50` wash in app — still flat)
- Radius 10 px, pad 24 px, min-h 240 px
- Icon 30 px, title 18/28, body 14/20 `neutral-600`
- Action chip: solid circle `neutral-950` → hover `primary-550` (no ring)

### Plan

- Bg `neutral-50`; Pro may use `card_bg.jpg`
- Radius 10 px, max width 590 px
- Playfair price 56/60
- Full-width plan CTA, no elevation

### Mini-card

- Media: `img_01` – `img_03`
- Mono eyebrow 12 px uppercase
- Flat image block, no frame

---

## 3. Inputs

### Glass search

- Radius 18 px
- Flat `neutral-50` shell in guideline; production may blur behind — still no shadow
- Gradient accent on placeholder and rim token only (not a box border stack)
- Mode pills: flat `neutral-150` track, active `neutral-950` / `neutral-50`
- Inner field: avoid double borders; one calm edge or none

### Text field

- Bg `neutral-50`, radius 8 px
- Default: **no border** or hairline `line1` if required for affordance
- Focus: `primary-550` — prefer color shift over thick ring

---

## 4. Tags

Pill, flat fill only.

| Type | Bg | Text |
|------|-----|------|
| default | `neutral-150` | `neutral-650` |
| featured | `accent-a2` | white |
| status | light tint | func color |

No outline tags. No gradient borders on chips.

---

## 5. Nav & footer

**Nav (guideline)** — sticky, h 72 px, bg `neutral-100`, flat. Links body-sm, hover `primary-550`. AI Tools: gradient text only. Sign in tertiary, sign up primary.

**Footer** — flat columns, text links. No divider lines between groups unless `line1` is unavoidable.

Production nav may use light blur; keep it subtle, no heavy glass rim.

---

## 6. Overlays

Menus and modals: flat panel on `neutral-50`, radius 24 px. **No shadow** in new work; separate from page with background tint (`rgba(0,0,0,.45)`) only.

List hover: `neutral-150` fill, not a border row.

---

## 7. States

| State | Treatment |
|-------|-----------|
| Empty | Large icon, short copy, secondary CTA — all flat |
| Loading | Small spinner icon, no skeleton chrome |
| Error | Tinted chip, no red border box |
| Disabled | Muted fill, reduced contrast |

---

## 8. Layout patterns

- Floor: Playfair title + plain subtitle + body grid
- Services: 4 → 1 col at 1024 px
- Plans: 2 × 590 px centered → 1 col
- Section spacing: wide `mt` (e.g. 80–280 px), not boxed sections

---

## 9. Images

```
img_01.jpg  img_02.jpg  img_03.jpg  card_bg.jpg
light_hero_1–3.jpg  dark_hero_1–3.jpg
```

One hero image per screen. Cards use photography as content, not as a framed asset with borders.

---

## 10. Icons

`currentColor`. Sizes: 14–16 inline, 30 on service cards, 64 empty state. Guideline = SVG. App = iconfont. Do not mix in one control. See `icons.md`.
