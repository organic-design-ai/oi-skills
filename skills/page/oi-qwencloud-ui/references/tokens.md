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

### Font families

| Token | Role |
|-------|------|
| `--pt-font-base` | Inter + system sans |
| `--pt-font-mono` | Roboto Mono — labels, pricing |
| `--pt-font-code` | Consolas stack |
| `--pt-font-{thin,light,regular,medium,semibold,bold}` | Weighted Inter families |

### Tracking
`--pt-letter-spacing-tight` `-0.02em` (headings) · `--pt-letter-spacing-normal` `0` (titles) · `--pt-letter-spacing-loose` `0.02em` (body, caption).

### Size scale (size / line-height; px)
| Token | Size | Use |
|-------|-----:|-----|
| `--pt-heading-font-size-3xl` | 96 | Hero display (rare) |
| `--pt-heading-font-size-2xl` | 72 | Marketing hero h1 |
| `--pt-heading-font-size-xl` | 64 | Tagline split hero (home) |
| `--pt-heading-font-size-lg` | 60 | Centered intro hero (coding-plan, skills-detail) |
| `--pt-heading-font-size-md` | 44 | Section heads, marketplace hero |
| `--pt-heading-font-size-sm` | 36 | Legal page title, docs hero, compact h1 |
| `--pt-title-font-size-lg` | 28 | Sub-section title |
| `--pt-title-font-size-md` | 24 | Card title, legal subtitle |
| `--pt-title-font-size-sm` | 20 | Legal sub-subtitle |
| `--pt-body-font-size-lg` | 18 | Hero/section subtitle |
| `--pt-body-font-size-md` | 16 | Body |
| `--pt-body-font-size-sm` | 14 | Card meta, filter pills |
| `--pt-body-font-size-xs` | 13 | Caption mono labels |

Each size has a matching `--pt-{heading|title|body}-line-height-*` and `--pt-{heading|title|body}-letter-spacing-*`.

### Fluid
`--pt-heading-font-size-fluid-md: clamp(36px, 8vw, 52px)` · `--pt-title-font-size-fluid-md: clamp(28px, 6vw, 40px)`. Use for responsive section titles.

---

## Spacing

**2-px rhythm.** Prefer `--pt-spacing-N` tokens (N × 2 px) or semantic aliases; literal px from the working set is still valid when no token exists.

### Spacing scale (`--pt-spacing-N` = N × 2 px)

| Token | px | Token | px | Token | px |
|-------|---:|-------|---:|-------|---:|
| `--pt-spacing-1` | 2 | `--pt-spacing-8` | 16 | `--pt-spacing-20` | 40 |
| `--pt-spacing-2` | 4 | `--pt-spacing-9` | 18 | `--pt-spacing-22` | 44 |
| `--pt-spacing-3` | 6 | `--pt-spacing-10` | 20 | `--pt-spacing-24` | 48 |
| `--pt-spacing-4` | 8 | `--pt-spacing-11` | 22 | `--pt-spacing-28` | 56 |
| `--pt-spacing-5` | 10 | `--pt-spacing-12` | 24 | `--pt-spacing-32` | 64 |
| `--pt-spacing-6` | 12 | `--pt-spacing-13` | 26 | `--pt-spacing-36` | 72 |
| `--pt-spacing-7` | 14 | `--pt-spacing-14` | 28 | `--pt-spacing-40` | 80 |
| | | `--pt-spacing-15` | 30 | `--pt-spacing-44` | 88 |
| | | `--pt-spacing-16` | 32 | `--pt-spacing-48` | 96 |
| | | `--pt-spacing-18` | 36 | `--pt-spacing-57` | 114 |
| | | | | `--pt-spacing-61` | 122 |
| | | | | `--pt-spacing-69` | 138 |
| | | | | `--pt-spacing-77` | 154 |

### Semantic aliases (prefer in component CSS)

| Token | Resolves to |
|-------|-------------|
| `--pt-margin-sm` / `md` / `lg` | `spacing-12` / `spacing-18` / `spacing-24` |
| `--pt-padding-sm` / `md` / `lg` | `14px` / `18px` / `spacing-12` |
| `--pt-gap-sm` / `md` / `lg` | `spacing-6` / `14px` / `spacing-9` |

Typical defaults (full table in `layouts.md` §9):

| Context | px / token |
|---------|---:|
| Chip / inline gap | 8 (`spacing-4`) |
| Card inner row gap | 12 / 14 (`spacing-6` / `spacing-7`) |
| Grid card gap | 24 (`spacing-12`) · 18 · 36 |
| Card padding | 24 / 28 / 32 |
| Panel padding (gradient-card) | 60 44 desktop · 32 20 mobile |
| Heading → grid | 48 / 60 |
| Section → next section | 96 / 122 / 138 (`spacing-48` / `61` / `69`) |
| Outer page gutter | 36 desktop · 20 mobile (utilities) |
| Preview gallery gap | 32 (`spacing-16`) |

---

## Radius

Working set (use these five):

| Token | px | Typical use |
|-------|---:|-------------|
| `--pt-radius-full` | 999 | Buttons, inputs, tags, FABs, dots |
| `--pt-radius-xs` | 12 | Inner panels, tool tiles, command boxes, notices |
| `--pt-radius-sm` | 18 | Mid cards (marketplace, compare, pricing offer) |
| `--pt-radius-md` | 24 | Standard cards, hero frames, gradient panels |
| `--pt-radius-lg` | 36 | Full-bleed heroes, signup brand panel, era CTA |

Also defined but rarely used: `--pt-radius-xl` 42 · `--pt-radius-2xl` 48 · `--pt-radius-2xs` 8 · `--pt-radius-3xs` 6 · `--pt-radius-4xs` 2. Don't reach for these unless the Guideline calls for them.

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

| Token | Value | Use |
|-------|-------|-----|
| `--pt-layout-limit-width` | 1920px | Absolute cap |
| `--pt-layout-max-width` | `min(100vw - 140px, 1920px)` | Outer / full-bleed (`.layout-max-wide`) |
| `--pt-layout-max-inner` | `min(100vw - 280px, 1780px)` | Inner content (`.layout-max-inner`) |
| `--pt-layout-max-read-box` | 768px | Reader column (legal, docs body, skills-detail) |
| `--pt-nav-backdrop-offset` | 84px desktop · 62px mobile | Sticky offset for rails/heads |
| `--pt-bulletin-height` / `--pt-bulletin-padding` | 306 / 70 (24 mobile) | Bulletin block only |

Breakpoint: 1024px. Mobile gutters 20 px via the container utilities.

### Z-index stack (`--pt-z-*`)

Use tokenized layers — do not invent z-index literals on overlays.

| Token | Value | Use |
|-------|------:|-----|
| `--pt-z-hide` | -1 | Hidden layers |
| `--pt-z-base` | 0 | Default |
| `--pt-z-popup-inline` | 50 | Inline popovers |
| `--pt-z-sticky` | 100 | Sticky section heads |
| `--pt-z-fixed` | 200 | Fixed bars |
| `--pt-z-sidebar` | 300 | Side rails |
| `--pt-z-float-widget` | 500 | FABs |
| `--pt-z-sub-nav` | 900 | Sub-navigation |
| `--pt-z-top-nav` | 1000 | Guideline / site nav |
| `--pt-z-top-banner` | 1050 | Announcement strip |
| `--pt-z-dropdown` | 1100 | Menus |
| `--pt-z-popover` | 1200 | Popovers |
| `--pt-z-tooltip` | 1300 | Tooltips |
| `--pt-z-drawer-backdrop` | 1400 | Drawer scrim |
| `--pt-z-drawer` | 1410 | Drawer panel |
| `--pt-z-dialog-backdrop` | 1500 | Modal scrim |
| `--pt-z-dialog` | 1510 | Modal content |
| `--pt-z-notification` | 1600 | Toasts |
| `--pt-z-max` | 2000 | Hard cap |

Full page-composition spec — including hero variants A–I, section header patterns A/B/C, the grid table, sidebar widths, reader column, preview gallery (§19), and sub-block vocabulary — lives in `layouts.md`.

---

## Images (CDN)

Manifest: https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Images.json

- `card_1.jpg` – `card_4.jpg` — customer cards
- `flower_01.jpg` – `flower_06.jpg` — hero backdrops (one per page)

See `assets.md`.

---

## Icons

48 SVGs on CDN. Manifest: https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Icons.json — see `icons.md`.

---

## Dark / Light mode

Both modes are first-class. Token blocks live in `qwencloud-v1/src/css/token.scss:4-145`. Mode is set on `<html data-prefers-color='light'|'dark'>`.

```scss
html[data-prefers-color='dark']  { /* …tokens… */ }
html[data-prefers-color='light'] { /* …tokens… */ }
```

### What inverts vs what stays constant

| Group | Light | Dark | Behavior |
|-------|-------|------|----------|
| Neutral 50 | `#ffffff` (canvas) | `#09090a` (near-black canvas) | **Ladder inverts** — 50 is canvas in both modes; 950 is ink in both modes; the hex flips |
| Neutral 950 | `#0b0c0f` (ink) | `#f9fafc` (near-white ink) | Same — role preserved, hex flips |
| Primary 550 (accent) | `#653aff` | `#714ffc` | Slightly different hex; both are the brand purple |
| Primary 650 (hover) | `#5229e6` | `#653aff` | Different |
| Line 100 | → `neutral-200` | → `neutral-250` | Both stay desaturated; auto-inverts via the neutral ramp |
| Supporting bg (red/orange/green/blue/purple) | very light tint (`#fff2f0`, `#ecfaed`, …) | very dark tint (`#360002`, `#001f06`, …) | Bg inverts; the `-tint` color (used for text/icon) stays the same hue |

### CTA inversion — the signature move

| Token | Light | Dark |
|-------|-------|------|
| `--pt-cta-color-fill` | `neutral-950` (black) | `primary-550` (purple) |
| `--pt-cta-color-fill-hover` | `primary-550` (purple) | `primary-650` (deeper purple) |
| `--pt-cta-color-font-fill` | `primary-50` | `primary-50` |
| `--pt-cta-secondary-color-fill` | `primary-50` (lavender wash) | `neutral-400` |
| `--pt-cta-secondary-color-fill-hover` | `primary-150` | `primary-850` (very dark purple) |
| `--pt-cta-secondary-color-font-fill` | `primary-550` | `neutral-800` |

**Light primary CTA:** black at rest → purple on hover. **Dark primary CTA:** purple at rest → deeper purple on hover. The "purple-on-interaction" feel is preserved across modes.

### Shadow tokens differ per mode

| Token | Light | Dark |
|-------|-------|------|
| `--pt-shadow-light` | `0 8px 24px rgba(83,91,107,0.06)` | `0 8px 24px rgba(0,0,0,0.28)` |
| `--pt-shadow-normal` | `0 16px 40px rgba(83,91,107,0.10)` | `0 16px 40px rgba(0,0,0,0.38)` |

Dark mode shadows are stronger (higher α). Don't use a single shadow value across modes.

### Component colors that flip explicitly

- `--pt-color-models-compare-bar-bg`: light `rgba(13,15,18,0.92)` (dark glass) → dark `rgba(255,255,255,0.92)` (light glass). The compare bar always contrasts with the page canvas.

### Imagery per mode

- Use the **same** `flower_*.jpg` poster in both modes. Test legibility — most floral hero JPGs work in both because the heading is NOT on top of them (§2 rule).
- **Icon dark-mode inversion:** static HTML icons from `Icons.json` use `filter: invert(1)` on `.qc-icon-img` when in dark mode (the manifest SVGs were authored on a light background). React `@ali/qwen-cloud-icons` components auto-handle this.
- **Primary CTA arrow icon** also inverts via `filter: invert(1)` so the white-on-black light CTA becomes black-on-purple in dark.

### Surface mapping in both modes

| Plane | Light (`neutral-*`) | Dark (`neutral-*`) | Use |
|-------|---------------------|---------------------|-----|
| Canvas | 50 `#ffffff` | 50 `#09090a` | `.page` body |
| Tinted floor | 100 `#f9fafd` | 100 `#0f1115` | Every 2nd/3rd floor |
| Subtle surface | 150 `#f2f4f8` | 150 `#16191d` | Pill track, chips, disabled input |
| Card wash | gradient-card-bg | (auto-inverts via neutrals) | Tinted card-as-floor panel |

### Implementation rules

1. **Always implement both modes.** When asked to build a page, ask which mode if not specified; verify the design in both before considering it done.
2. **Use tokens, not raw hex.** Every `--pt-color-*` resolves correctly in both modes automatically.
3. **Don't hard-code light-mode literals in dark-mode overrides.** Trust the cascade.
4. **Test contrast in both modes.** The same component (e.g. soft `primary-50` bg + `primary-550` text) must pass legibility in both.
5. **Borders use line tokens** (`--pt-color-line-100/200/300`), which auto-invert via the neutral ramp. Don't reach for raw `neutral-200`.
6. **Heading-on-canvas rule (§2 of `layouts.md`) holds in both modes.** Canvas just means "neutral 50" — it's white in light, near-black in dark. The rule never overlays a giant heading on imagery in either mode.
