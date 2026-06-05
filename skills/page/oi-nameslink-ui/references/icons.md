# Nameslink Icons

**Manifest required.** Fetch https://acd-assets.alicdn.com/acd_work/skills/nameslink/Icons.json — every glyph URL from an entry’s `href`; do not invent paths.

**Minimalism.** Simple line icons. One color (`currentColor`). No fills, badges, or backgrounds on glyphs.

Three sources, in priority order:

1. **App** — `nsiconfont`, project `5164327` (production React app only)
2. **Brand kit** — 67 outlined SVGs on CDN; manifest: `assets.md` → Icons.json (default for static / generated pages)
3. **Lucide (fallback only)** — open-source line icons from https://lucide.dev. Use **only** when neither manifest above contains the glyph; never as a convenience replacement

Same names; pick one system per surface. Do not mix in one control.

---

## 0. Fallback to Lucide

If after fetching `Icons.json` you cannot find a matching `id` / `component` for the concept (e.g., a niche product mark, a chart-type glyph, an audio waveform), fall back to Lucide.

```html
<!-- Static HTML / vanilla -->
<img
  src="https://unpkg.com/lucide-static@latest/icons/waveform.svg"
  alt=""
  style="width: 1em; height: 1em; color: currentColor;"
/>
```

```tsx
// React
import { Waveform } from 'lucide-react'
<Waveform size={16} strokeWidth={1.5} aria-hidden />
```

Rules when using Lucide:

- `stroke-width: 1.5` (match brand-kit visual weight; default Lucide is 2)
- `currentColor` only — no Lucide-default colors
- Outlined only — no filled / duotone variants
- Same size scale as brand kit: 14 / 16 inline, 30 service card, 64 empty state
- One system per control: a button using Lucide must not also embed a brand-kit `<use>` — pick Lucide or brand kit, not both
- Document the gap: if you reach for Lucide more than 2× on a single page, the manifest is probably missing the icon set — flag it for the brand team rather than scattering Lucide everywhere

---

## 1. CDN SVG kit

Fetch: https://acd-assets.alicdn.com/acd_work/skills/nameslink/Icons.json

Each entry: `component`, `id`, `href` (absolute URL to `Icons/{id}.svg`).

```html
<svg viewBox="0 0 24 24" width="1em" height="1em" aria-hidden="true">
  <use href="https://acd-assets.alicdn.com/acd_work/skills/nameslink/Icons/arrow-right-outlined.svg#arrow-right-outlined" />
</svg>
```

Or `<img src="…/Icons/search-outlined.svg" alt="" />` with `currentColor` via CSS on parent.

- Color: `currentColor` only
- Size: `1em` with text, or 14 / 16 / 30 / 64 px per `components.md`
- File name: `{name}-outlined.svg`
- React: `ArrowRightOutlined` · lookup `href` in Icons.json

Do not thicken, shadow, or encircle icons for emphasis.

---

## 2. Iconfont (production)

```tsx
<i className="iconfont" aria-hidden>&#xe632;</i>
```

| Glyph | Use |
|-------|-----|
| `&#xe632;` | Chevron / link |
| `&#xe63c;` | Dropdown |
| `&#xe63f;` | External / chip arrow |
| `&#xe63d` / `&#xe63b;` | Sun / moon |
| `&#xe616;` / `&#xe620;` | Check |
| `&#xe63a;` | Sparkles |
| `&#xe625;` | Mail |
| `&#xe61b;` | User |
| `&#xe619;` | Wallet |
| `&#xe618;` | Logout |
| `&#xe61c;` | Bids |
| `&#xe60d;` | Domains |
| `&#xe602;` / `&#xe63e;` / `&#xe603;` | Search modes |
| `&#xe607;` / `&#xe629;` / `&#xe627;` | Services |
| `&#xe623;` / `&#xe615;` / `&#xe638;` / `&#xe639;` | Social / pay — SVG kit has no replacement |

**Static HTML** — use CDN SVG column above instead of iconfont.

---

## 3. New icons

24×24, `-outlined` name; add to brand kit Icons.json on CDN. Match existing weight. Log new iconfont code if added to `5164327`.
