# Qwen Cloud Icons

**Manifest required.** Fetch https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Icons.json — use each `href` (or `@ali/qwen-cloud-icons` matching `component`). No Lucide/stock SVGs.

48 outlined SVGs on CDN.

Runtime apps: `@ali/qwen-cloud-icons` (internal docs: qwen-cloud-icons.io.alibaba-inc.com).

See `assets.md` for Guideline and image URLs.

## Rules

- `currentColor` only — no purple on the glyph itself
- Small and sparse — text carries the page
- One kit per screen
- Flat wrapper — no box, border, or shadow on the icon cell

## Static HTML

Fetch `Icons.json`; use each entry’s `href`:

```html
<span class="qc-icon" aria-hidden="true">
  <img class="qc-icon-img" src="https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Icons/check-outlined.svg" alt="" />
</span>
```

Sizing: `1em` on the wrapper. Typical: 14 px in buttons, 16 px in `btn--xl`.

Dark mode in Guideline: `filter: invert(1)` on `.qc-icon-img`. Primary CTA also inverts `arrow-up-outlined`.

## Naming

| | Pattern | Example |
|---|---------|---------|
| File | `{name}-outlined.svg` | `check-outlined.svg` |
| id | same stem | `check-outlined` |
| React | PascalCase + Outlined | `CheckOutlined` |

## Guideline usage

| Surface | Icon |
|---------|------|
| Primary CTA | `arrow-up-outlined` |
| Theme | `sun-outlined` · `moon-outlined` |
| Pricing list | `check-outlined` |

Full list: fetch Icons.json (`icons[]`).

## React

```tsx
import { CheckOutlined } from '@ali/qwen-cloud-icons';
<CheckOutlined size={16} />
```

Props: `size` · `spin` · `className` · `style` · SVG attrs pass through.

Lucide: fallback only when the package is unavailable. Never mix with this kit.
