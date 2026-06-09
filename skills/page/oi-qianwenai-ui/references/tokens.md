# 千问云 — Design Tokens

Source: brand guideline (`:root` / `html[data-prefers-color='dark']`). All variables use `--pt-*`. No semantic alias layer.

## Design stance

扁平、克制、安静。层级靠 **neutral 色阶**（`50` ↔ `100` ↔ `150`）区分，不靠阴影。边框极少——仅在结构必须时用 `line-100` 发丝线。

**营销长页默认 `box-shadow: none`** — 与 Guideline Token Plan / 首页 / Hackathon 参考一致。`--pt-shadow-*` 仅用于：分段控件选中 thumb、卡片 hover lift（数据页）、compare bar、FAB、搜索下拉。

**千问云 vs 国际站色感：** 交互主色为 **蓝紫** `primary-550`；标题渐变优先 **蓝绿青** 谱系（`gradient-1/2/3/8/9`），而非国际站的纯紫粉渐变。

---

## Colors

### Primary (`--pt-color-primary-*`) — 蓝紫主色

10 stops（Guideline 注释：Primary blue-violet ramp CN）。

| Stop | Light hex | Role |
|------|-----------|------|
| `50` | `#F0F3FF` | Secondary CTA 浅底、链接 hover 衬底 |
| `150` | `#E7EAFF` | Secondary hover |
| `550` | `#5B58FF` | **默认强调** — 链接、hover、`+` 图标、chip tint |
| `650` | `#4500F3` | Link hover |
| `950` | `#000153` | 深色文字上的反色场景 |

Dark mode remaps: `550` → `#714FFC` · `650` → `#653AFF`.

### Neutral (`--pt-color-neutral-*`)

19 stops. **Light 与 Guideline 一致**；dark mode 角色反转（`50` 近黑画布 ↔ `950` 近白字）。

| Stop | Light hex | Marketing role |
|------|-----------|----------------|
| **`50`** | **`#FFFFFF`** | **画布 canvas** — 页面底、默认楼层、卡片内底 |
| **`100`** | **`#F9FAFD`** | **Tinted floor** — 每隔 1–2 楼层、FAQ 宽面板、bulletin |
| `150` | `#F2F4F8` | Segmented track、chip、legal note |
| `200` | `#E6E9EF` | → `line-100` 发丝线 |
| `300` | `#D1D7E2` | → `line-200` outline 按钮 |
| `650`–`750` | — | 副文案 `body` secondary |
| `950` | `#0B0C0F` | 主标题、primary CTA 填充（light） |

**常见误用：** 不要把 `neutral-100` 当画布 — 画布是 **`neutral-50`（白）**；`100` 是极浅灰台阶。

### Lines (use sparingly)

| Token | Resolves to (light) |
|-------|---------------------|
| `--pt-color-line-100` | `neutral-200` — card hairline |
| `--pt-color-line-200` | `neutral-300` — outline button, input |
| `--pt-color-line-300` | `neutral-350` — hover border |

### Supporting pairs (badges / chips only)

bg + tint: gray · red · orange · green · blue · purple. Not for large surfaces.

### Functional

`--pt-color-func-success` `#0DA740` · `--pt-color-func-warning` `#FF7931` · `--pt-color-func-danger` `#F33939` · `--pt-color-func-emphasize` `#277FE4`

Links: `--pt-color-link-default` → `primary-550` · hover → `primary-650`

### Accent decoration

`mint` · `orchid` · `electric-blue` · `sky` · `rose` · `emerald` · `apricot` — stat dots only.

### CTA inversion

| Token | Light | Dark |
|-------|-------|------|
| `--pt-cta-color-fill` | `neutral-950` | `primary-550` |
| `--pt-cta-color-fill-hover` | `primary-550` | `primary-650` |
| `--pt-cta-color-font-fill` | `primary-50` | `primary-50` |
| `--pt-cta-secondary-color-fill` | `primary-50` | `neutral-400` |
| `--pt-cta-secondary-color-fill-hover` | `primary-150` | `primary-850` |
| `--pt-cta-secondary-color-font-fill` | `primary-550` | `neutral-800` |

Light primary button: near-black rest, purple hover.

### Gradients — 9 个签名渐变（千问云独有 `gradient-9`）

**用途：** 仅 **标题 clip 一词/短语**（`background-clip: text`）；每屏 ≤1 处。禁止用于按钮底、卡片底、大面积背景（背景用 `gradient-card-bg` 或 neutral 台阶）。

| Token | 色感 | 典型场景 |
|-------|------|----------|
| **`gradient-1`** | 蓝 → 青绿 → 紫 `#4897FE → #40EBDA → #14C8C7 → #5B58FF` | **默认营销标题**、hero 渐变词、featured pricing rim |
| **`gradient-2`** | 紫 → 蓝 → 青 `#5B58FF → #4897FE → #14C8C7` | 次级标题、pricing rim 备选 |
| **`gradient-3`** | 蓝 → 青 → 绿 `#4897FE → #67E9E9 → #40DB5F` | 偏 **蓝绿** 的 campaign 标题 |
| `gradient-4` | 紫 → 品红 → 橙 | 高饱和促销（慎用） |
| `gradient-5` | 品红 → 紫 | 偏紫粉强调 |
| `gradient-6` | 锥形 青 → 紫 | 动效 rim（featured、搜索 focus） |
| `gradient-7` | 径向蓝紫 | 装饰 / era 视觉 |
| **`gradient-8`** | 径向 **青 → 绿** `#14C8C7 → #22CA95 → #008D26` | **蓝绿** tail visual、自然/增长主题 |
| **`gradient-9`** | 青 → 绿 → 金 **（仅 CN）** | 国内专属标题、活动 kicker |

Card wash: `--pt-gradient-card-bg` — `135deg`, `neutral-150` → `neutral-50` — hero showcase、panel-as-card；几乎看不出色带。

**与国际站差异：** 国际站 `oi-qwencloud-ui` 渐变偏紫粉（`#653AFF` 系）；千问云优先 **蓝绿青**（`#14C8C7` / `#4897FE` / `#40EBDA`）混入 `gradient-1–3/8/9`。

---

## Typography

### Font families

| Token | Role |
|-------|------|
| `--pt-font-base` | Inter, **PingFang SC**, system sans |
| `--pt-font-mono` | **Roboto Mono**, PingFang SC, system sans |
| `--pt-font-code` | Consolas stack |

千问云 vs 国际站：行高更大（中文排版）、标题字距用固定 px、部分标题字重 600。

### Size scale (size / line-height; px)

| Token | Size | Line | Use |
|-------|-----:|-----:|-----|
| `--pt-heading-font-size-3xl` | 78 | 94 | Hero display (CN-only step) |
| `--pt-heading-font-size-2xl` | 72 | 86 | Marketing hero h1 |
| `--pt-heading-font-size-xl` | 64 | 84 | Tagline split hero |
| `--pt-heading-font-size-lg` | 60 | 78 | Centered intro hero |
| `--pt-heading-font-size-md` | 44 | 58 | Section heads |
| `--pt-heading-font-size-sm` | 36 | 46 | Compact h1 / legal |
| `--pt-title-font-size-lg` | 28 | 36 | Sub-section title |
| `--pt-title-font-size-md` | 24 | 36 | Card title |
| `--pt-title-font-size-sm` | 20 | 30 | Card headline |
| `--pt-title-font-size-xs` | 18 | 28 | Agent glass panel title |
| `--pt-body-font-size-lg` | 18 | 28 | Hero/section subtitle |
| `--pt-body-font-size-md` | 16 | 24 | Body |
| `--pt-body-font-size-sm` | 14 | 20 | Card meta |
| `--pt-body-font-size-xs` | 13 | 20 | Caption |

Letter-spacing: headings `0.25px` · body `0.4px` (lg `0.5px`) · titles `0`.

Fluid: `--pt-heading-font-size-fluid-md: clamp(36px, 8vw, 52px)` · `--pt-title-font-size-fluid-md: clamp(28px, 6vw, 40px)`

---

## Spacing

**2-px rhythm.** `--pt-spacing-N` = N × 2 px.

Scale: `1` 2px · `2` 4px · `3` 6px · `4` 8px · `5` 10px · `6` 12px · `7` 14px · `8` 16px · `9` 18px · `10` 20px · `11` 22px · `12` 24px · `13` 26px · `14` 28px · `15` 30px · `16` 32px · `18` 36px · `20` 40px · `22` 44px · `24` 48px · `28` 56px · `32` 64px · `36` 72px · `40` 80px · `44` 88px · `48` 96px · `57` 114px · `61` 122px · `69` 138px · `77` 154px

Semantic: `--pt-margin-sm/md/lg` → `spacing-12/18/24` · `--pt-padding-sm/md/lg` → `14px/18px/spacing-12` · `--pt-gap-sm/md/lg` → `spacing-6/14px/spacing-9`

---

## Radius

Working set: `full` 999 · `xs` 12 · `sm` 18 · `md` 24 · `lg` 36. Also `2xs` 8 · `3xs` 6 · `4xs` 2 for badges.

---

## Borders & elevation

Line widths: `thin` 0.5 px · `normal` 1 px · `thick` 1.5 px.

| Token | Light | Dark |
|-------|-------|------|
| `--pt-shadow-light` | `0 8px 24px rgba(83,91,107,.06)` | `0 8px 24px rgba(0,0,0,.28)` |
| `--pt-shadow-normal` | `0 16px 40px rgba(83,91,107,.10)` | `0 16px 40px rgba(0,0,0,.38)` |

---

## Motion

`--pt-motion-fast` 0.25s · `--pt-motion-slow` 0.7s · ease-in-out. Color and opacity only.

---

## Z-index (`--pt-z-*`)

`hide` -1 · `base` 0 · `popup-inline` 50 · `sticky` 100 · `fixed` 200 · `sidebar` 300 · `float-widget` 500 · `sub-nav` 900 · `top-nav` 1000 · `top-banner` 1050 · `dropdown` 1100 · `popover` 1200 · `tooltip` 1300 · `drawer-backdrop` 1400 · `drawer` 1410 · `dialog-backdrop` 1500 · `dialog` 1510 · `notification` 1600 · `max` 2000

---

## Layout

| Token | Value | Use |
|-------|-------|-----|
| `--pt-layout-limit-width` | 1920px | Absolute cap |
| `--pt-layout-max-width` | `min(100vw - 140px, 1920px)` | Outer (`.layout-max-wide`) |
| `--pt-layout-max-inner` | `min(100vw - 280px, 1780px)` | Inner (`.layout-max-inner`) |
| `--pt-layout-max-read-box` | **640px** | Reader column (CN prose) |
| `--pt-nav-backdrop-offset` | 84px desktop · 62px mobile | Sticky offset |

Breakpoint: 1024px. Desktop gutters **70px**; mobile **10px**.

Full page composition: `layouts.md`.

---

## Images (CDN)

Manifest: https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Images.json

| Key | Role |
|-----|------|
| `qwen-model-01.png` – `qwen-model-06.png` | Hero / model imagery (one per page) |
| `card-01.png` – `card-06.png` | Customer / model-strip cards |
| `agent-01.png` – `agent-05.png` | Agent cards |

See `assets.md`.

---

## Icons

76 SVGs on CDN. Manifest: https://acd-assets.alicdn.com/acd_work/skills/qianwenai/Icons.json — see `icons.md`.

---

## Dark / Light mode

Set `<html data-prefers-color='light'|'dark'>`. Use tokens — do not hard-code light literals in dark overrides.

- Light CTA: black rest → purple hover; dark CTA: purple rest → deeper purple hover
- Static icons: `filter: invert(1)` on `.qc-icon-img` in dark mode where Guideline specifies
- Primary CTA uses `arrow-up-right-outlined`
