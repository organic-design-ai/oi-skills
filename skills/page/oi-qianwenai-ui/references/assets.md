# 千问云 — Remote brand assets

Brand kit files are **not** bundled in the skill.

**Required:** all **icons** and **photography** must be taken from the manifests below (`Icons.json` → `href`; `Images.json` → PNG URL). No stock, placeholders, or invented paths.

**Visual tone:** 简洁、平白、弱描边、淡阴影 — see `SKILL.md` §核心约束.

**Base:** `https://acd-assets.alicdn.com/acd_work/skills/qianwenai/`

| Resource | URL |
|----------|-----|
| Guideline (visual reference + live demos) | https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Guideline.html |
| Icons manifest (76 SVGs) | https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Icons.json |
| Images manifest (PNG URLs) | https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Images.json |
| UI bundle (§08 component gallery) | https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Scripts/ui.js |
| Shared vendor chunks | `Scripts/base-ui.js` · `Scripts/react-vendor.js` · `Scripts/recharts.js` |

## Usage

1. **Tokens / components** — use installed `tokens.md` and `components.md`.
2. **Visual QA** — open `Guideline.html` before unfamiliar sections (hero, model cards, pricing, **§08 组件与基础模块**).
3. **Icons** — fetch `Icons.json`; static HTML uses each `href` under the CDN base (`<img class="qc-icon-img" src="…">`). No external icon npm package — manifest only.
4. **Photography** — fetch `Images.json`; **one** `qwen-model-*` per hero; `card-*` for customer / strip cards; `agent-*` for agent grid.
5. **§08 gallery** — `Guideline.html` mounts `comp-primitives-mount[data-ui-style="qianwenai"]`; replicate BEM roots from `components.md` §08.

## Image filenames (from manifest)

| Key | Role |
|-----|------|
| `qwen-model-01.png` – `qwen-model-06.png` | Hero model posters (one per page) |
| `card-01.png` – `card-06.png` | Customer cards · model-strip cards |
| `agent-01.png` – `agent-05.png` | Agent card backgrounds |

## Logo

Defined in `Guideline.html`. Use the guideline wordmark — do not invent alternate logos.
