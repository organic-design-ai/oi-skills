# Nameslink — Design Tokens

Source: brand guideline (`:root` / `html[data-prefers-color='dark']`). Namespace: `--pt-*`. Copy values as-is. Full token ramp: see installed `references/tokens.md` (extracted from guideline).

**Minimalism.** Flat surfaces. Separation comes from neutral steps and space, not borders or shadows. Color and type do the work. Gradients only where the brand already defines them (logo, hero highlight, search accent).

---

## 1. Colors

### Primary (10 stops)

Same ramp in light and dark; roles change. Accent: **550** (`#6940FF`).

| Token | Hex | Notes |
|-------|-----|-------|
| `--pt-color-primary-50` | `#EDEFFF` | Light wash |
| `--pt-color-primary-150` | `#E0D7FF` | Secondary CTA (light) |
| `--pt-color-primary-250` | `#BCABFC` | Secondary hover (light) |
| `--pt-color-primary-350` | `#9478FF` | Dark muted text |
| `--pt-color-primary-450` | `#7039F9` | — |
| `--pt-color-primary-550` | `#6940FF` | Links, focus, dark CTA |
| `--pt-color-primary-650` | `#542EDE` | CTA hover |
| `--pt-color-primary-750` | `#391AAB` | — |
| `--pt-color-primary-850` | `#281276` | Secondary hover (dark) |
| `--pt-color-primary-950` | `#150A41` | — |

### Neutral (20 stops)

Light values below; dark mode inverts the ladder (50 ↔ black canvas, 950 ↔ white text).

| Token | Light |
|-------|-------|
| `--pt-color-neutral-50` | `#FFFFFF` |
| `--pt-color-neutral-100` | `#F7F7F9` |
| `--pt-color-neutral-150` | `#F2F4F8` |
| `--pt-color-neutral-200` | `#E6E9EF` |
| `--pt-color-neutral-250` | `#DEE2E9` |
| `--pt-color-neutral-300` | `#D1D7E2` |
| `--pt-color-neutral-350` | `#AEB7C8` |
| `--pt-color-neutral-400` | `#9FA7B7` |
| `--pt-color-neutral-450` | `#8E96A7` |
| `--pt-color-neutral-500` | `#7F8798` |
| `--pt-color-neutral-550` | `#707889` |
| `--pt-color-neutral-600` | `#626A7A` |
| `--pt-color-neutral-650` | `#535B6B` |
| `--pt-color-neutral-700` | `#3C424F` |
| `--pt-color-neutral-750` | `#242933` |
| `--pt-color-neutral-800` | `#1D2129` |
| `--pt-color-neutral-850` | `#0F1115` |
| `--pt-color-neutral-900` | `#0D0D0E` |
| `--pt-color-neutral-950` | `#000000` |

**Lines.** Use sparingly. Prefer adjacent neutrals over rules.

| Token | Light | Dark |
|-------|-------|------|
| `--pt-color-line1` | `#E9EAEE` | `#1E1E20` |
| `--pt-color-line-100` | `neutral-200` | (flips) |
| `--pt-color-line-300` | `neutral-450` | (flips) |

### Brand & functional

| Token | Hex |
|-------|-----|
| `--pt-color-brand-600` / `--pt-color-accent-a1` | `#2C56FF` |
| `--pt-color-accent-a2` | `#01B853` |
| `--pt-color-func-success` | `#0DA740` |
| `--pt-color-func-warning` | `#FF7931` |
| `--pt-color-func-danger` | `#F33939` |

### CTA

| Role | Light | Dark |
|------|-------|------|
| Fill | `neutral-950` | `primary-550` |
| Fill hover | `primary-650` | `primary-650` |
| Text | `neutral-50` | `neutral-950` |
| Secondary fill | `primary-150` | `neutral-400` |
| Secondary text | `primary-550` | `neutral-800` |

### Gradients (fixed slots only)

Not for page backgrounds or buttons.

| Token | Use |
|-------|-----|
| `--pt-gradient-1` | Logo nib, hero highlight text |
| `--pt-gradient-2` | Search placeholder text |
| `--pt-gradient-3` | Optional text flash |
| `--pt-gradient-nav-link` | AI Tools link |
| `--pt-gradient-home-search-border` | Search shell accent only |
| `--pt-gradient-card-bg` | Soft card wash (`neutral-150` → `neutral-50`) |

Text fill: `background-image` + `background-clip: text` + transparent fill.

---

## 2. Typography

| Token | Role |
|-------|------|
| `--pt-font-regular` | Inter — UI and body |
| `--pt-font-playfair` | Floor titles only |
| `--pt-font-mono` | Labels, code |

| Scale | Size / lh | Weight |
|-------|-----------|--------|
| Hero | 60 / 64 | 700 |
| Sub-display | 44 / 50 | 600 |
| Floor (Playfair) | 40 / 54 | 600 |
| Title md / sm | 24 / 30 · 20 / 26 | 500 |
| Body lg / md / sm | 18 / 28 · 16 / 22 · 14 / 20 | 400 |
| Plan price | 56 / 60 Playfair | 700 |

Tracking: slight negative on large type only (`-0.02em` display, `-0.01em` floor). Body stays normal.

---

## 3. Space & shape

- Grid: **4 px**
- Guideline gutters: **70 px** desktop, **20 px** ≤1024 px
- Radii: pills `999` for CTA and tags; cards often **10 px** or **20 px**; search shell **18 px**
- Default: generous padding, clear gaps. Do not pack components to mimic depth.

---

## 4. Depth (minimal)

**Do not use shadow** to separate blocks. If something feels weak, step the background (`neutral-50` on `neutral-100`) or add space.

Tokens exist for legacy overlays only — treat as near-zero in new UI:

| Token | Note |
|-------|------|
| `--pt-shadow-light` | Avoid on cards |
| `--pt-shadow-normal` | Modal only if required |
| `--pt-shadow-card` | Prefer flat plan cards |

**Do not add** box-shadow, drop-shadow, or inset rims for decoration.

---

## 5. Motion

| Token | Value |
|-------|-------|
| `--pt-motion-fast` | `0.25s` |
| `--pt-ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` |

Color and opacity only. No bounce, stagger, or parallax. Respect `prefers-reduced-motion`.

---

## 6. Layout

| Token | Value |
|-------|-------|
| `--pt-layout-limit-width` | `1920px` |
| `--pt-layout-max-width` | `min(calc(100vw - 140px), 1920px)` |

Breakpoint **1024 px**: single column, tighter vertical rhythm.

---

## 7. Images (CDN)

Manifest: https://acd-assets.alicdn.com/acd_work/skills/nameslink/Images.json (absolute JPG URLs). See `assets.md`.

| File | Use |
|------|-----|
| `img_01.jpg` – `img_03.jpg` | Quick-nav / mini-card |
| `card_bg.jpg` | Plan Pro background |
| `light_hero_1–3.jpg` | Hero poster (light) — one per page |
| `dark_hero_1–3.jpg` | Hero poster (dark) — one per page |

---

## 8. Icons

Production: iconfont `5164327`. Brand kit: 67 CDN SVGs — see `icons.md` / `assets.md`.

---

## 9. Logo

Wordmark uses `currentColor`. Nib uses `--pt-gradient-1` only. Do not flatten the nib to a solid.
