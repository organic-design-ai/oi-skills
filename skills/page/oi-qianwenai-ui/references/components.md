# 千问云 — Components

Tokens: `references/tokens.md` (`--pt-*`). Page-level composition: **`references/layouts.md`**. Icons/images: `references/assets.md`.

Section numbers match `Guideline.html` TOC (01–14).

## Principles

**Tone:** 简洁 · 平白 · 弱描边 · 淡阴影. Flat surfaces; default `shadow: none`. Weak borders on outline controls and featured pricing rim. One accent per view: near-black CTA, one gradient word, or purple hover.

**Panel-as-card** (`layouts.md` §11.6): list-style panels are borderless outer + typography + hairline rows — no nested grey sub-cards.

**Visual QA:** CDN `Guideline.html` §08 (`组件与基础模块`); styles in `#ui-components` + `Scripts/ui.js`.

---

## §01 Hero Images

Grid: 3 × 2. Assets: `qwen-model-01` – `qwen-model-06` from `Images.json` (PNG).

- Frame: `radius-md`, `16:10`, `object-fit: cover`
- No border, no shadow
- One model poster per page in the **visual paragraph** below the title — never behind H1 (`layouts.md` §2)

Mobile: 1 column.

---

## §04 Buttons

Pill (`radius-full`). No default border on primary / secondary.

| Variant | Fill | Notes |
|---------|------|-------|
| `btn--primary` | `cta-fill` → hover `primary-550` | Light: black rest |
| `btn--secondary` | `primary-50` | Soft fill |
| `btn--outline` | transparent | Only variant with `line-200` border |
| `btn--text` | transparent | Ink → purple hover |

CTA icon: **`arrow-up-right-outlined`** via `.qc-icon`.

---

## §05 Gradients

9 tokens (`--pt-gradient-1` … `9`). Text clip only. One word per screen. **默认 `gradient-1`（蓝绿青）**；`gradient-9` 仅 CN。详见 `tokens.md` 渐变表。

---

## §06 Featured Model Card

Same as international kit: `model-feature-card-grid` · `model-feature-card` · `model-feature-card--secondary`.

| | Primary | Secondary |
|---|---------|-----------|
| Background | `gradient-card-bg` | `neutral-50` |
| Border | optional `line-100` | same |
| Shadow | none | none |
| Padding / radius | 32 px · `radius-md` | same |

Inner: `mf-name` · `mf-desc` · `mf-tag` · `mf-price-row` · `mf-divider` · `mf-stats` · `mf-cta`.

Pricing checkmarks: **`check-mark-outlined`** (not `check-outlined`).

营销 **3-up 模型行**（无 hover-reveal）：`layouts.md` **§4.6 变体 B** + **R11** — `line-100`、`radius-sm`、pad 24、`price-text` §8.18、`modality-chip` §8.19、分隔线、双列 metrics。

**Logo 楼层：** `layouts.md` **§4.8** — **A：** `.logo-matrix-tile`（R14，`line-100`）。**B：** `.logo-strip` / `.logo-strip-item`（R19，无边透明横排，logo h 40–48）。

**页尾大视觉 + Footer：** `layouts.md` **§4.9–§4.10** — `.tail-visual`（790/370 px，R15）+ `.page-footer`（35/65，R16，§8.24）。页面级 chrome，非 §08 卡片标本。

**横滑切换楼层：** `layouts.md` **§4.11** + **§8.26** — `.carousel-card`、100vw `.carousel-floor-track`、R17/R18、`.carousel-pager` ‹›。

**FAQ 楼层：** `layouts.md` **§4.12** + **§8.27** — `.faq-layout`、`.faq-item`/R20；外壳 A（inner）或 B（`.faq-panel`）。§08 `ui-accordion` 标本对齐 token，营销页须接 §8.27 互斥单开。

**Arena 联动楼层：** `layouts.md` **§4.13** + **§8.28** — `.arena-sync-layout`、`.arena-sync-item`/R21、`.arena-sync-visual` 面板切换。

---

## §07 Pricing Tiers

3-up or **4-up** card row — floor spec: `layouts.md` **§4.4** (R9 zones, §8.16 icon rows).

`.card-row-item` / `.tier`: `neutral-50`, `line-100`, `radius-sm`, pad 32, **no shadow**. Featured: gradient rim; CTA `btn--secondary` → featured `btn--primary`. Features: `check-mark-outlined` + §8.16.

### §07a 紧凑型模型卡片

定价区块下方的 **半宽 + 四分之一宽** 非对称行 — Guideline §07 标本；线上首页对应 `.afm-bottom-grid` + `.afm-card-half` / `.afm-card-quarter`。楼层规范：`layouts.md` **§4.6 变体 C**。

| 区块 | Guideline 类名 | 线上别名 |
|------|----------------|----------|
| 网格 | `.compact-cards-grid` | `.afm-bottom-grid` |
| 卡片 | `.compact-card` | `.afm-card.afm-card-compact` |
| 半宽 | `.compact-card--half` | `.afm-card-half` |
| 四分之一 | `.compact-card--quarter` | `.afm-card-quarter` |

**外壳：** `neutral-50` · `1px line-100` · `radius-xs` · 内边距 28 · 桌面固定高 **294** · **无阴影** · 无 hover 上浮。

**内部自上而下：**

1. `.compact-card__title-row` — `h4` `body-lg` 加粗 + 可选 `.model-tag.is-hot`（`gradient-6` 胶囊，40×22）
2. `.compact-card__desc` — `body-sm` `neutral-650` · **2 行截断**
3. `.model-tags` — 横向换行 gap 8：
   - `.model-tag` — `supporting-gray` 填充
   - `.model-tag.is-special` — `gradient-7` 描边（「开源」「优选」）
4. `.card-metrics-wrap` — `margin-top: auto`
   - `.card-metrics-note` — 等宽字体备注 `neutral-450`；价格用 `.price-text` + `¥`（§8.18）
   - `.card-metrics` — 顶部分割 `line-200`；2 列 `max-content`，间距 18 / 64
   - `.card-metric` — `strong` `title-sm` + `span` `body-sm` 标签

**数据：** 精选模型楼层 `halfCard` + 前两张 `quarterCards`（Featured 标签页）。卡内无 CTA。

### §07b 行业模型卡片

带标签页的 **4 列行业行** — Guideline `.industry-cards`；线上 `.afm-industry` + `.afm-industry-card`。楼层规范：`layouts.md` **§4.7 变体 A**（完整版）。

| 区块 | Guideline 类名 | 线上别名 |
|------|----------------|----------|
| 楼层 | `.industry-cards` | `.afm-industry` |
| 标题区 | `.industry-cards__head` | `.afm-head.afm-head-industry` |
| 标签 | `.industry-tabs` · `.industry-tab.is-active` | `.afm-tabs` · `.afm-tab.is-active` |
| 网格 | `.industry-cards__grid` | `.afm-industry-grid` |
| 卡片 | `.industry-card` | `.afm-industry-card.afm-card-compact` |
| 底栏 CTA | `.industry-cards__cta` | `.afm-browse-cta` |

**标题：** Pattern B 左对齐 — `h3` `heading-sm`；**一词**渐变高亮「行业」（`gradient-3` `.grad-word`）。标签：胶囊行，选中项 `neutral-150` 底 + 6 px `primary-550` 圆点 `::before`。

**卡片外壳：** **无四边描边** — 仅 `border-bottom: 1px line-200`；内边距 `4 4 20`；桌面 min-h 200；透明底。

**内部：**

1. `.industry-card__title-row` — `.industry-card__logo` 24×24 清单图标 + `h4` `body-lg` + 可选 `.model-tag.is-hot`
2. `.industry-card__desc` — `body-sm` `neutral-750` · 2 行截断
3. `.model-tags` — 能力标签
4. `.industry-card__arrow` — `arrow-up-outlined` 12×12；`margin-top: auto`

**底栏：** 居中 `btn--outline btn--xl`（宽 220 px）—「浏览全部模型」。不用 `btn--primary`。

### §07c 智能体构建卡片

**双列构建者楼层** — Guideline `.agent-builder-section`；线上同名。楼层规范：`layouts.md` **§4.5**（营销页视觉区无边框）；Guideline §07 标本的 `.agent-builder-visual` **带描边**，仅供设计规范展示。

| 区块 | Guideline 类名 | 线上别名 |
|------|----------------|----------|
| 区块 | `.agent-builder-section` | `.agent-builder-section` |
| 标题 | `.agent-builder-head` | `.agent-builder-head` |
| 网格 | `.agent-builder-grid` | `.agent-builder-grid` |
| 卡片 | `.agent-builder-card` | `.agent-builder-card` |
| 视觉 | `.agent-builder-visual` | `.agent-builder-visual` |
| 文案 | `.agent-builder-copy` | `.agent-builder-copy` |

**标题：** Pattern A 居中 — `h3` `heading-md`；高亮词「智能体构建者」`.grad-word`（`gradient-2`）；描述 `body-md` `neutral-750` 最大宽 640 px。

**单卡（视觉 → 文案，间距 48）：**

1. `.agent-builder-visual` — Guideline：`radius-xs` · `1px line-100` · 高 **248** · 铺满 `img`/`video` · 左上 `.agent-builder-visual__icon` 20×20 白色图标（`code-brackets-outlined` / `device-desktop-code-outlined`）。**营销页：** 去掉描边，对齐 §4.5 `.media-duo-visual`（`radius-md` 无边框）。
2. `.agent-builder-copy` — `h4` `title-md` · `p` `body-md` `neutral-550` · CTA `btn--text`（「开始构建」「探索文档」）— **不用** 胶囊按钮。

**素材：** `Images/card-01.png`、`card-02.png`（或 `Images.json` CDN）。

---

## Coding Plan 页面（Token Plan）

线上四层内容 + footer。完整楼层规范：`layouts.md` **§4.0.1**。页尾仅 **§4.10 `<Footer />`**（无尾部大视觉、无 FooterBottom）。

| # | 区块 | 根类名 | 布局 § |
|---|------|--------|--------|
| 1 | 介绍 + 展示 | `.coding-plan-intro-section` · `.coding-plan-intro-showcase` | §4.0.1 · §8.29 |
| 2 | 限时优惠价目 | `.coding-plan-offer-section` · `.coding-plan-offer-card` | §4.4 · R9 |
| 3 | 支持的 AI 工具 | `.coding-plan-tools-section` · `.coding-plan-tools-item` | §4.8 A |
| 4 | 常见问题 | `.coding-plan-faq-section` · `.coding-plan-faq-panel` | §4.12 B-wash · §8.27 |

### Intro 展示（楼层 1）

- **标题区**（inner）：`h1` + `.coding-plan-intro-title-gradient`（`gradient-1`）· `.heading-desc-lg` 居中 · 描述内可嵌 `TextLink`。
- **面板**（wide）：`gradient-card-bg`、`radius-md`、高 **380**、内边距 `60 44`、双列间距 **64**。
- **折叠行：** `.coding-plan-feature-item` — 图标 + 标题 + `IconModelsPlusSvg`；展开隐藏加号；§8.29 互斥单开 + 右侧预览联动。
- **预览：** `.coding-plan-preview-panel.is-active`；桌面右栏叠放；移动仅在展开行内显示。

### FAQ 面板（楼层 4）

- **外壳：** `.coding-plan-faq-panel` — `gradient-card-bg`（非 `neutral-100` 平面板）、间距 **154**、内边距 `60 44`。
- **左栏：** 双行标题 + `.coding-plan-faq-gradient`（`gradient-2` 高亮第二行）。
- **右栏：** `.coding-plan-faq-item` — `title-md` 问题 + 加号图标；§8.27 互斥单开；收起行 `min-height: 100px`。

### 价目 + 工具（楼层 2–3）

- **价目：** `.coding-plan-offer-card` — 同 §07 定价卡；`check-mark-outlined` 特性行；`¥` 价格；一张 `.is-featured` 渐变 rim。
- **工具：** `.coding-plan-tools-grid` 四列矩阵 — `line-100` 描边瓦片；深浅色 Logo 切换。

---

## §08 组件与基础模块 (Components & Primitives)

Guideline §08 mounts the **live preview gallery** (`comp-primitives-mount[data-ui-style="qianwenai"]`) — same 53 production cards + `ui-*` primitives as the international bundle, with CN copy in specimens.

### 08.1 Gallery shell

| Piece | Rule |
|-------|------|
| Mount | `.comp-primitives-mount[data-ui-style="qianwenai"]` |
| Masonry | `.preview-grid` · `--columns: 4` · `--gap: 32px` |
| Card shell | `ui-card` — `radius-sm`, `neutral-50`, hairline rim |

See `layouts.md` §19.

### 08.2 UI primitives

`ui-button` · `ui-dialog` · `ui-sheet` · `ui-select` · `ui-checkbox` · `ui-radio-group` · `ui-switch` · `ui-slider` · `ui-progress` · `ui-spinner` · `ui-table` · `ui-accordion` · `ui-breadcrumb` · `ui-calendar` · `ui-chart` · `ui-tooltip` · `ui-sidebar` · `ui-models-filter-*` · `ui-price-text` · `ui-unit-text` · `ui-field-separator` · `ui-style-switch`

Forms: `forms-specimen` — pill inputs, `line-200` border, focus `primary-550`.

### 08.3 Production card catalog (53)

Same BEM roots as Qwen Cloud international kit — see `oi-qwencloud-ui/references/components.md` §08.3 for the full root → title table. Specimens use Chinese labels where applicable (`kitchen-island` → 模型 Playground, `notification-settings` → 通知, etc.).

Domains: foundation · models/playground · usage/analytics · billing · workspace · integrations · support.

### 08.4 Card rules

Header (`ha` + `ma`) · body · optional footer. Flat hairline rim. Manifest icons only. No stock art.

---

## §09 Tags & Badges

`.badge.is-*` (2 px radius, 10 px caps) · `.chip.is-*` (pill, 11 px).

Do not put badges and chips on the same card.

---

## §10 客户案例卡片 (Customer Card Grid)

2 × 2. Assets: `card-01` – `card-04` (or `card-06` for extended strip) from `Images.json`.

- Full-bleed PNG, `radius-md`
- White typographic panel `radius-xs`, right-aligned
- Quote · headline · body · name + title

---

## 模型卡片带 (Model strip) — 千问云营销组件

Horizontal scroll. Assets: `card-01` – `card-06`. Classes: `model-strip` · `model-card`.

- Container: `neutral-50`, `scroll-snap-type: x mandatory`, hidden scrollbar
- Card: `clamp(240px, …, 440px)` wide, no border/shadow
- Image: `radius-sm`, 250 px tall, `object-fit: cover`, hover `scale(1.04)`
- FAB: 36 px circle, white fill, bottom-right, hover fade-in, `arrow-up-right-outlined`
- Content: title `title-sm` 20px/600 · desc `body-sm` `neutral-650` · default CTA

Mobile: dual-column card width.

---

## Agent 卡片 (Agent card grid) — 千问云营销组件

2-col grid. Assets: `agent-01` – `agent-04`. Classes: `agent-card-grid` · `agent-card`.

- Card: `radius-md`, `aspect-ratio: 16/10`, full-bleed `agent-*.png`
- Glass panel (bottom-anchored, `border-radius: 18px`):
  - **blur:** `backdrop-filter: blur(1px) saturate(1.35)` + `color-mix(in srgb, neutral-50 22%, transparent)`
  - **tint:** `color-mix(in srgb, neutral-50 6%, transparent)`
  - **rim:** `inset 0 1px rgba(255,255,255,.38), inset 0 0 0 1px rgba(255,255,255,.1), inset 0 -1px 4px rgba(0,0,0,.03)`
  - **content:** z-index 3, padding `22px 16px`
  - Dark: stronger neutral mixes on blur/tint/rim (see `dev/qianwenai` References)
- Title `title-xs` 500 · body `body-sm` `neutral-650` 2-line clamp

Mobile: 1 column.

---

## Page chrome

- **Nav:** sticky, frosted, 84 px / 62 px mobile
- **Floors:** alternate `neutral-50` ↔ `neutral-100`
- **Theme:** sun/moon outlined icons from manifest
- **Breakpoint:** 1024 px; gutters 70 → 10 px

---

## Assets

**Images:** `qwen-model-*` · `card-*` · `agent-*` — `assets.md`

**Icons:** 76 SVGs — `icons.md`

**Live bundle:** `Guideline.html` + `Scripts/ui.js` — `assets.md`
