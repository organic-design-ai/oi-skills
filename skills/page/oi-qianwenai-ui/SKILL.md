---
name: oi-qianwenai-ui
description: >-
  千问云 brand UI: simple flat surfaces, weak borders, light shadow; CN typography
  (Inter + PingFang SC + Roboto Mono). Icons and photos MUST come from CDN Icons.json /
  Images.json manifests. TRIGGER for 千问云, qianwenai, oi-qianwenai-ui, or 千问云 landing/product UI.
  NOT for generic UI, Qwen Cloud international kit, or video/media tools.
---
# Oi 千问云 UI — Qianwen AI Design System

**Author:** Alibaba Cloud Design

**Skill path:** `<skill-dir>/` (e.g. `~/.cursor/skills/oi-qianwenai-ui`).

Reference specs: `references/` (`tokens.md`, `components.md`, `layouts.md`, `icons.md`, `assets.md`). Brand kit on CDN — see `assets.md`.

---

## 核心约束（Agent 必守）

### ★ 头号铁律 — 大标题永远不要压在视觉元素上

**标题 + 副标题是画布上的独立段落（`--pt-cn-color-neutral-50`）。模型配图 / 视频 / 渐变是下方或侧边的独立面板。两段式，绝不合一。**

- ❌ 错误：`<div class="hero-panel" style="background-image: qwen-model-01.png"><h1>千问驱动的…</h1></div>`
- ✅ 正确：`<header><h1>…</h1><p>subtitle</p><CTAs/></header>` 在 `neutral-50` 上，**再**用独立 `<div class="hero-panel">` 放配图，间距 48–64 px
- 禁止 `text-shadow`、暗色遮罩「为了可读性」—— 标题需要遮罩说明位置错了
- 图像上文字上限：**title-lg 28 px**（指标 chip、说明）。≥36 px 必须在画布段落
- 唯一例外：收尾 CTA hero（`layouts.md` §2.5）

完整规则：`references/layouts.md` §2。

### 视觉气质：简洁 · 平白 · 弱描边 · 淡阴影

- **简洁** — Inter + PingFang SC 排版为主；图标小而稀（76 个 manifest SVG）。
- **平白** — `neutral-50` / `150` / `100` 色阶；默认无装饰投影。
- **弱描边** — 仅 outline、表单、pricing featured rim 等必要处 `line-200` 1px。
- **淡阴影** — 默认 flat；仅 token 级轻阴影。

### 配图与图标：只从 manifest 抽取

**禁止** stock 图、占位图、自造 URL、emoji、Lucide 与 manifest 混用。

| 类型 | 做法 |
|------|------|
| **配图** | fetch `Images.json` → **绝对 URL**（`qwen-model-*` 每页一张 hero；`card-*` 客户/条带；`agent-*` 智能体卡） |
| **图标** | fetch `Icons.json`（76 个）→ 静态页用 CDN **`href`**；无 npm 包 |

详见 `references/assets.md`.

### 面板即卡片：外不描边 · 内不嵌灰底  ★

与 Qwen Cloud 国际站相同规则，token 前缀为 `--pt-cn-*`。详见 `layouts.md` §11.6。

---

## Usage

> **Agent:** 用户问 `usage` / `怎么用` / `help` / `@oi-qianwenai-ui` 且无具体任务时，**回复本节**，然后询问目标。

**Triggers:** `oi-qianwenai-ui`, `qianwenai-ui`, **千问云**, 千问云风格, 千问云设计系统, qianwenai style/design.

**Quick start**
1. Read this `SKILL.md`.
2. Load `<skill-dir>/references/{tokens,components,layouts,icons,assets}.md`.
3. Inject Inter `@font-face`（见下）；`--pt-cn-font-base` 含 PingFang SC；Roboto Mono 见 `tokens.md`。询问 light/dark，用 `--pt-cn-*` 实现。

**Example prompts**
- 「用 oi-qianwenai-ui 做千问云产品页」
- 「千问云 model feature 双卡 + agent 卡片」
- 「千问云浅色 pricing + qwen-model hero」

**Do not use for:** 未点名千问云/qianwenai 的通用 UI；国际站 `oi-qwencloud-ui`；视频工具。

## When to use

- 用户要 **千问云** 品牌 UI（国内模型营销、控制台、定价、客户案例）
- 需要 **model-strip**、**agent-card** 玻璃面板、9 个渐变字、CN 行高排版
- Token 级表单、标签、扁平层级规范

---

## 1. Design philosophy

- **Simple, flat, quiet.** 色阶与留白优先。
- **Purple on interaction.** Light CTA：近黑默认 → hover `primary-550`（`#5B58FF`）。
- **One accent per view.** 黑 CTA / 一个渐变词 / 紫 hover — 三选一。
- **CN typography.** 更大行高；标题字距 0.25px；`heading-3xl` 78px 为 CN 独有档位。
- **Gradients text-only.** 9 个 `--pt-cn-gradient-*`；featured tier 仅 1px rim。
- **Model posters as hero.** 每页一张 `qwen-model-*`；客户卡 `card-*`；智能体 `agent-*`。

**Fonts:**

```css
@font-face {
    font-family: 'Inter';
    src: url('https://acd-assets.alicdn.com/acd_work/web-fonts/inter/Inter-Variable.ttf') format('truetype');
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
}
```

`--pt-cn-font-base`: Inter, PingFang SC, system sans. `--pt-cn-font-mono`: Roboto Mono, PingFang SC.

**Reset** — 与 `oi-qwencloud-ui` 相同（`em,i,cite… { font-style: normal }` 等），紧接 `@font-face` 之后注入。

---

## 2. Craft rules

### 2.1 Token namespace

使用 `--pt-cn-*`（`references/tokens.md`）。间距优先 `--pt-cn-spacing-N`（N×2 px）及语义别名。

### 2.2 Signature patterns

| Pattern | Rule |
|---------|------|
| Primary button | Pill; black rest → purple hover; icon **`arrow-up-right-outlined`** |
| Model cards | 2-col; `gradient-card-bg` vs `neutral-50` |
| Model strip | 横向 `model-strip` + `model-card`; FAB `arrow-up-right-outlined` |
| Agent cards | 2-col `agent-card`; 底部 glass 四层面板 |
| Pricing | 3-up; featured gradient-1 rim; `check-mark-outlined` |
| Hero | `qwen-model-*` 在视觉段落；标题 72/86 on canvas |
| Reader | **640 px** (`--pt-cn-layout-max-read-box`) |

### 2.3 Layout

`references/layouts.md` — 三层容器、heroes A–I、§08/§19 组件画廊、§11 卡片体系、§17 数据页交互。桌面留白 **70px**，移动 **10px**。

### 2.4 Icons & assets (CDN)

Base: `https://acd-assets.alicdn.com/acd_work/skills/qianwenai/`

| Asset | Source |
|-------|--------|
| Guideline | `…/qianwenai/Guideline.html` |
| Icons (76) | `…/qianwenai/Icons.json` |
| Images (PNG) | `…/qianwenai/Images.json` |
| §08 bundle | `…/qianwenai/Scripts/ui.js` |

Tabler outlined 仅作 manifest 缺失时的回退。见 `references/icons.md`。

---

## 3. Anti-patterns

- 国际站 token（`--pt-*` 无 `-cn-`）与千问云混用
- 使用 `flower_*` / `card_1.jpg` 等国际站素材命名
- `arrow-up-outlined` 作主 CTA（应使用 `arrow-up-right-outlined`）
- 面板即卡片外描边 / 内嵌灰底子卡
- stock 图、占位图、manifest 外图标
- 同屏多个渐变词、渐变按钮底、重阴影

---

## 4. Workflow

1. **Fonts** — Inter + PingFang SC + Roboto Mono
2. **Mode** — light / dark
3. **Tokens** — `references/tokens.md`
4. **Layout** — `references/layouts.md`
5. **Components** — `references/components.md`（含 model-strip、agent-card、§08 画廊）
6. **Manifests** — fetch `Icons.json` + `Images.json`
7. **Guideline** — `Guideline.html` §08 组件与基础模块
8. **Review** — §6 + `layouts.md` §18

---

## 5. Reference files

| File | Scope |
|------|-------|
| `tokens.md` | `--pt-cn-*` 颜色、排版、间距、z-index |
| `components.md` | §01–10 + model-strip + agent-card |
| `layouts.md` | 页面构图、hero、网格、§19 画廊 |
| `icons.md` | 76 SVG + Tabler 回退 |
| `assets.md` | CDN URL |

---

## 6. Review checklist

- [ ] Inter `@font-face` + reset
- [ ] 全部 `--pt-cn-*`；读者栏 640 px
- [ ] Light CTA：黑默认 → 紫 hover；`arrow-up-right-outlined`
- [ ] ≤1 渐变词；卡片 flat
- [ ] 面板即卡片规则（§11.6）
- [ ] 配图仅 `Images.json`：`qwen-model-*` / `card-*` / `agent-*`
- [ ] 图标仅 `Icons.json`（76）或 Tabler 回退
- [ ] 标题在画布上，不在配图之上
- [ ] model-strip / agent-card 符合 `components.md` 玻璃与滚动规范
- [ ] `layouts.md` §18 通过
