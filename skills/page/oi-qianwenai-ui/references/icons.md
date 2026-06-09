# 千问云 Icons

**Manifest first.** Fetch https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Icons.json — use each CDN `href`. When a glyph is missing, fall back to **Tabler Icons** (outlined, `stroke: 1.5`, `currentColor`). Never Lucide/Heroicons/Feather/stock SVGs.

76 outlined SVGs on CDN (`Icons/`).

See `assets.md` for Guideline and image URLs.

## Rules

- `currentColor` only — no purple on the glyph itself
- Small and sparse — text carries the page
- One kit per screen — manifest **or** Tabler for a page; never mixed
- Flat wrapper — no box, border, or shadow on the icon cell
- Tabler is **fallback only**

## Static HTML

Fetch `Icons.json`; rewrite `./Icons/` paths to the CDN base:

```html
<span class="qc-icon" aria-hidden="true">
  <img class="qc-icon-img" src="https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Icons/check-mark-outlined.svg" alt="" />
</span>
```

Sizing: `1em` on the wrapper. Typical: 14 px in buttons, 16 px in `btn--xl`.

Dark mode: `filter: invert(1)` on `.qc-icon-img` where Guideline specifies. Primary CTA also inverts `arrow-up-right-outlined`.

## Naming

| | Pattern | Example |
|---|---------|---------|
| File | `{name}-outlined.svg` | `check-mark-outlined.svg` |
| id | same stem | `check-mark-outlined` |
| React (if wrapping) | PascalCase + Outlined | `CheckMarkOutlined` |

Special: `-filled` (e.g. `sparkle-4-filled`) · `-mini` (e.g. `chevron-left-mini`).

## Guideline usage

| Surface | Icon |
|---------|------|
| Primary CTA | `arrow-up-right-outlined` |
| Theme | `sun-outlined` · `moon-outlined` (if in manifest) |
| Pricing list | `check-mark-outlined` |
| Model strip FAB | `arrow-up-right-outlined` |

Full list: fetch `Icons.json` (`icons[]`). 76 entries including `qianwen-search-outlined`, `brain-ai-outlined`, `sparkle-4-filled`, etc.

## Tabler (fallback)

Static HTML: `https://unpkg.com/@tabler/icons@latest/icons/outline/<name>.svg` inside `.qc-icon`.

Match kit: outline only, `stroke-width: 1.5`, 14–16 px. Same dark-mode invert rule.

Never mix Tabler with manifest icons on the same screen.
