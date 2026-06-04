# Qwen Cloud Icons

**Manifest first.** Fetch https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Icons.json — use each `href` (or `@ali/qwen-cloud-icons` matching `component`). When a needed glyph is **not** in the 48-icon manifest, fall back to **Tabler Icons** (open-source, outlined, matches the kit's stroke). Never Lucide/Heroicons/Feather/stock SVGs.

48 outlined SVGs on CDN.

Runtime apps: `@ali/qwen-cloud-icons` (internal docs: qwen-cloud-icons.io.alibaba-inc.com).

See `assets.md` for Guideline and image URLs.

## Rules

- `currentColor` only — no purple on the glyph itself
- Small and sparse — text carries the page
- One kit per screen — pick manifest **or** Tabler for a given page; do not mix on the same screen
- Flat wrapper — no box, border, or shadow on the icon cell
- Tabler is **fallback only** — if the glyph exists in the manifest, use the manifest

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

## Tabler (fallback for missing glyphs)

Use only when the needed glyph isn't in `Icons.json` and there's no near-equivalent (e.g. `chart-line`, `chevron-down-outlined` exist — don't reach for Tabler for those).

| Mode | How |
|------|-----|
| Static HTML | `<img class="qc-icon-img" src="https://unpkg.com/@tabler/icons@latest/icons/outline/<name>.svg" alt="" />` inside the same `.qc-icon` wrapper |
| React | `import { Icon<Name> } from '@tabler/icons-react'` — pass `size={16}` and `stroke={1.5}` to match the kit's line weight |

**Match the kit:** outline only (not filled), `stroke-width: 1.5`, `currentColor`, 14–16 px in body/CTAs. Same dark-mode rule — `filter: invert(1)` on `.qc-icon-img` where the Guideline inverts.

Never mix Tabler with Lucide, Heroicons, Feather, or other icon sets on the same page.
