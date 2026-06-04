# Nameslink — Remote brand assets

Brand kit files are **not** bundled in the skill.

**Required:** all **icons** and **photography** must be taken from the manifests below (`Icons.json` → `href`; `Images.json` → JPG URL). No stock, placeholders, or invented paths.

**Visual tone:** 简洁、平白、弱描边、淡阴影 — see `SKILL.md` §核心约束.

**Base:** `https://acd-assets.alicdn.com/acd_work/skills/nameslink/`

| Resource | URL |
|----------|-----|
| Guideline (visual reference + live demos) | https://acd-assets.alicdn.com/acd_work/skills/nameslink/Guideline.html |
| Icons manifest (67 SVGs, full `href` per icon) | https://acd-assets.alicdn.com/acd_work/skills/nameslink/Icons.json |
| Images manifest (JPG URLs) | https://acd-assets.alicdn.com/acd_work/skills/nameslink/Images.json |

## Usage

1. **Tokens / components** — use installed `tokens.md` and `components.md` (distilled from Guideline).
2. **Visual QA** — open or fetch `Guideline.html` for layout, spacing, and component appearance; do not duplicate its CSS in new pages unless matching a demo section.
3. **Icons** — fetch `Icons.json`; use each entry’s `href` (absolute CDN URL to `Icons/{id}.svg`). Static HTML: `<use href="…#id">` or `<img src="…">` without the fragment.
4. **Photography** — fetch `Images.json` (array of absolute JPG URLs). Pick **one** `light_hero_*` or `dark_hero_*` per page; use `img_01–03`, `card_bg` per `tokens.md` §7.

## Image filenames (from manifest)

| Key | Role |
|-----|------|
| `light_hero_1.jpg` – `light_hero_3.jpg` | Hero poster (light) |
| `dark_hero_1.jpg` – `dark_hero_3.jpg` | Hero poster (dark) |
| `img_01.jpg` – `img_03.jpg` | Quick-nav / mini-card |
| `card_bg.jpg` | Plan Pro background |

## Logo

Wordmark and nib are defined in `Guideline.html` (gradient nib, `currentColor` wordmark). Inline SVG from the guideline nav — do not substitute a generic mark.
