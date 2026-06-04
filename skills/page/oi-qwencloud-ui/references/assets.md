# Qwen Cloud — Remote brand assets

Brand kit files are **not** bundled in the skill.

**Required:** all **icons** and **photography** must be taken from the manifests below (`Icons.json` → `href`; `Images.json` → JPG URL). No stock, placeholders, or invented paths.

**Visual tone:** 简洁、平白、弱描边、淡阴影 — see `SKILL.md` §核心约束.

**Base:** `https://acd-assets.alicdn.com/acd_work/skills/qwencloud/`

| Resource | URL |
|----------|-----|
| Guideline (visual reference + live demos) | https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Guideline.html |
| Icons manifest (48 SVGs, full `href` per icon) | https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Icons.json |
| Images manifest (JPG URLs) | https://acd-assets.alicdn.com/acd_work/skills/qwencloud/Images.json |

## Usage

1. **Tokens / components** — use installed `tokens.md` and `components.md`.
2. **Visual QA** — open or fetch `Guideline.html` before implementing unfamiliar sections (hero, model cards, pricing rim, customer card).
3. **Icons** — fetch `Icons.json`; use each `href` for static HTML (`<img class="qc-icon-img" src="…">`). React: prefer `@ali/qwen-cloud-icons` when available.
4. **Photography** — fetch `Images.json`; **one** `flower_01–06` per hero; `card_1–4` for customer stories.

## Image filenames (from manifest)

| Key | Role |
|-----|------|
| `flower_01.jpg` – `flower_06.jpg` | Hero floral backdrops |
| `card_1.jpg` – `card_4.jpg` | Customer card full-bleed art |

## Logo

Defined in `Guideline.html`. Use the guideline wordmark — do not invent alternate logos.
