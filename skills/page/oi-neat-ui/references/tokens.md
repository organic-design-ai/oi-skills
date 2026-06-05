# Neat — Design Tokens

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

**Style:** all Playfair headings (hero H1, every `home-section-title`, plan/dock price, FAQ Q-label) default to `font-style: normal` — **upright, never italic**. Italic Playfair is reserved for a deliberate inline emphasis span only.

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

Manifest: https://acd-assets.alicdn.com/acd_work/skills/neat/Images.json (absolute JPG URLs). See `assets.md`.

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

---

## 10. Dark / Light mode

Both modes are first-class. Token blocks live in `neat/src/css/token.css:2-94`. Mode is set on `<html data-prefers-color='light'|'dark'>`.

```css
html[data-prefers-color='dark']  { /* …tokens… */ }
html[data-prefers-color='light'] { /* …tokens… */ }
:root { /* mode-independent tokens (radius, spacing, gradients, fonts) */ }
```

### What inverts vs what stays constant

| Group | Light | Dark | Behavior |
|-------|-------|------|----------|
| Neutral 50 | `#ffffff` (card surface) | `#000000` (card surface) | **Ladder inverts** — 50 stays "card surface" in both modes; hex flips |
| Neutral 100 | `#f7f7f9` (canvas) | `#0d0d0e` (canvas) | Same — role preserved (Neat uses 100 as canvas, 50 as card; the opposite of most kits) |
| Neutral 950 | `#000000` (ink) | `#ffffff` (ink) | Role preserved, hex flips |
| Primary 50–950 | identical hex in both modes | identical | **Brand purple ramp is mode-constant** — `primary-50: #edefff` stays lavender wash in dark too |
| `--pt-color-line1` | `#e9eaee` (light hairline) | `#1e1e20` (dark hairline) | Auto-inverts |

### CTA inversion — the signature move

| Token | Light | Dark |
|-------|-------|------|
| `--pt-cta-color-fill` | `neutral-950` (black) | `primary-550` (purple) |
| `--pt-cta-color-fill-hover` | `primary-650` (purple) | `primary-650` (deeper purple) |
| `--pt-cta-color-font-fill` | `neutral-50` (white) | `neutral-950` (white) |
| `--pt-cta-secondary-color-fill` | `neutral-950` | `neutral-400` |
| `--pt-cta-secondary-color-fill-hover` | `primary-150` (lavender wash) | `primary-850` (very dark purple) |
| `--pt-cta-secondary-color-font-fill` | `primary-550` | `neutral-800` |

**Light primary CTA:** black at rest → purple on hover. **Dark primary CTA:** purple at rest → deeper purple on hover. The "purple-on-interaction" feel is preserved across modes.

### Shadow tokens differ per mode

| Token | Light | Dark |
|-------|-------|------|
| `--pt-shadow-light` | `0 8px 24px rgba(83,91,107,0.04)` | `0 8px 24px rgba(0,0,0,0.22)` |
| `--pt-shadow-normal` | `0 16px 40px rgba(83,91,107,0.10)` | `0 16px 40px rgba(0,0,0,0.38)` |

Dark mode shadows are ~5× stronger (higher α) to remain visible against a near-black canvas. Don't use a single shadow value across modes.

### Floor-bg specifics that flip per mode

These are surface choices the audit found, not tokens — but they need explicit per-mode handling:

| Surface | Light | Dark |
|---------|-------|------|
| Services floor bg | `bg-primary-50` (lavender wash, `#edefff`) | `bg-neutral-50` (no lavender on dark — would clash) |
| Steps "lavender" card | `bg-primary-50` | `bg-primary-450` (`#7039f9` — bright purple card) |
| Steps lavender card primary CTA | `bg-neutral-950 text-neutral-50` (black on lavender) | `bg-func-black text-func-white` (black on bright-purple — explicit override) |
| Nav dropdown link color | `--pt-nav-dropdown-link-color: #0d0d0e` | `#ffffff` (explicit token override) |

### Mode-constant tokens (do not depend on mode)

These live in `:root` and resolve identically in both modes:

- All radii (`--pt-radius-3xs … 2xl … full`)
- All gradients (`--pt-gradient-1/2/3/nav-link/home-search-border/home-search-placeholder/card-bg`)
- Type tokens (sizes + line-heights)
- Layout widths (`--pt-layout-max-width`, `--pt-layout-max-inner`, `--pt-layout-max-read-box`)
- Motion (`--pt-motion-fast: 0.25s`)
- Footer height (`--pt-footer-bottom-height`)

### Imagery per mode

- **Hero JPG per mode:** `light_hero_1–3.jpg` ↔ `dark_hero_1–3.jpg` — pick the one matching `data-prefers-color`. The brand kit ships both light and dark posters specifically so heroes look right in both modes without overlay tricks.
- **`card_bg.jpg`** (plan-pro background art) is mode-constant — works on both light and dark plan cards.
- Inside-card photos / mini-card `img_01–03.jpg` are mode-constant.

### Surface mapping (both modes)

| Plane | `neutral-*` step | Used for |
|-------|-----------------|----------|
| Canvas | 100 | `.page` body; default floor bg |
| Card surface | 50 | Borderless content cards (hero, services, plan, quick-nav, dock, steps) |
| Subtle surface | 150 | Pill segmented track, chip bg, dropdown item hover |
| Accent wash (light only) | `primary-50` | Services floor; mode-pill rack |

The card surface uses `neutral-50` and the canvas uses `neutral-100` — that's the inverse of most kits. The visual rhythm (canvas → step up to card surface) survives in dark because the ramp flips correctly.

### Implementation rules

1. **Always implement both modes.** Ask which mode if not specified; verify in both before considering it done.
2. **Use tokens, not raw hex.** Every `--pt-color-*` resolves correctly in both modes automatically. The few raw hexes in the codebase (mobile profile chip border `#E6E8EB`, user-menu trigger `#6940FF`) are tech debt — prefer tokens.
3. **Don't hard-code light-mode literals in dark-mode overrides.** Trust the cascade.
4. **Test contrast in both modes.** A `bg-primary-50` + `text-primary-550` chip must read in dark — primary-50 stays lavender (`#edefff`) and primary-550 stays brand purple, so contrast holds.
5. **Borders use `--pt-color-line1` or the line tokens** which auto-invert. Don't reach for raw `neutral-200`.
6. **Heading-on-canvas rule (`layouts.md` §2) holds in both modes.** Canvas means `neutral-100` — `#f7f7f9` in light, `#0d0d0e` in dark. The rule never overlays a giant heading on imagery in either mode.
7. **For `prefers-color-scheme: dark` system preference:** mirror the `data-prefers-color='dark'` attribute on `<html>` to match. The brand kit doesn't expose a `@media (prefers-color-scheme)` block — the attribute is the single source of truth.
