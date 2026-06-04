---
name: oi-nameslink-ui
description: >-
  Nameslink brand UI: simple flat surfaces, weak borders, light shadow only, purple accent,
  Inter + Playfair. Icons and photos MUST come from CDN Icons.json / Images.json manifests.
  TRIGGER for Nameslink style, oi-nameslink-ui, nameslink-ui, or Nameslink landing/product UI.
  NOT for generic UI, other brand kits, or video/media tools.
---
# Oi Nameslink UI — Nameslink Design System

**Author:** Alibaba Cloud Design

**Skill path:** `<skill-dir>/` (e.g. `~/.cursor/skills/oi-nameslink-ui`).

Reference specs: `references/` (`tokens.md`, `components.md`, `icons.md`, `assets.md`). Brand kit on CDN — see `assets.md`.

---

## 核心约束（Agent 必守）

### 视觉气质：简洁 · 平白 · 弱描边 · 淡阴影

- **简洁** — 少装饰、少层级嵌套；信息靠字号、字重、中性色阶和留白分区，不靠框线堆叠。
- **平白** — 大面积扁平面色（`neutral-50` / `100` / `150`）；默认无卡片投影、无渐变铺底。
- **弱描边** — 描边仅用于 tertiary 按钮、必要分隔或结构不清时；用 `line-100` / `line-200` 1px 发丝线，禁止粗边框当主分隔。
- **淡阴影** — 默认 **无** 装饰阴影；若 Guideline 场景必须分层，仅用 `--pt-shadow-*` token 且保持极轻，禁止重投影、发光、多层 shadow stack。

### 配图与图标：只从 manifest 抽取

**禁止** 使用 stock 图、占位图、自造 CDN、Lucide/emoji 或随意 SVG。

| 类型 | 做法 |
|------|------|
| **配图** | 先 fetch `Images.json`（见 `assets.md`），从返回的 **绝对 URL** 中选文件名（如 `light_hero_2.jpg`）；`<img src>` 必须用 manifest 中的 URL |
| **图标** | 先 fetch `Icons.json`，按 `id` / `component` 匹配场景，`<use href>` 或 `<img src>` 必须用条目里的 **`href`**（CDN 绝对路径） |

实现前若未读 manifest，先 fetch 再写 markup。详见 `references/assets.md`。

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-nameslink-ui` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-nameslink-ui`), then ask what they want to accomplish.

**Triggers:** `oi-nameslink-ui`, `nameslink-ui`, Nameslink style, Nameslink design, Nameslink 风格 / 设计系统.

**Quick start**
1. Read this `SKILL.md` (philosophy, workflow, anti-patterns).
2. Load specs on demand: `<skill-dir>/references/tokens.md`, `components.md`, `icons.md`, `assets.md`.
3. Declare fonts (Inter, Playfair Display, Roboto Mono), ask light/dark, then implement with `--pt-*` tokens.

**Example prompts**
- 「用 oi-nameslink-ui 做 Nameslink 首页」
- 「按 Nameslink tokens 改 pricing 卡片」
- 「Nameslink 深色模式 hero + glass search」

**Do not use for:** generic UI without explicit Nameslink request; multi-style libraries → `oi-awesome-ui` / `oi-taste-ui`; ffmpeg / video (`widget/*`).

## When to use

- User wants **Nameslink** brand UI (domain/marketplace product, editorial floors, flat plan cards)
- Landing pages, marketing, or app chrome that must match Nameslink tokens and components
- Need icon kit, logo rules, photography slots, and CTA inversion patterns

**Do not use** unless the user names Nameslink or this skill.

---

## 1. Design philosophy

- **Simple, flat, quiet.** 简洁平白：中性色阶 + 留白为主；弱描边、淡阴影（见上方核心约束）。
- **Flat minimalism.** Surfaces differ by neutral steps and whitespace — not thick borders, not heavy shadows.
- **Purple is intentional.** Accent `primary-550` (`#6940FF`) for links, focus, dark-mode CTA; light primary CTA stays near-black with purple hover.
- **Typography carries hierarchy.** Inter for UI; **Playfair Display** only for floor titles and plan pricing; Roboto Mono for labels/code.
- **Gradients are scarce.** Logo nib, one hero highlight word, search placeholder, AI Tools nav link — never on buttons or page backgrounds.
- **Both modes are first-class.** Ask light or dark; neutral ramp inverts roles in dark mode.

**Fonts (declare before coding):**

```html
<link rel="stylesheet" href="https://acd-assets.alicdn.com/acd_work/web-fonts/inter/inter.css" />
<link rel="stylesheet" href="https://acd-assets.alicdn.com/acd_work/web-fonts/playfair-display/playfair-display.css" />
```

Roboto Mono: see `references/tokens.md` §2.

---

## 2. Craft rules

### 2.1 Token namespace

Copy `--pt-*` values verbatim from `references/tokens.md`. Do not invent parallel semantic names.

### 2.2 Signature patterns

| Pattern | Rule |
|---------|------|
| Primary CTA | Pill, `cta-fill` → hover `primary-650`; light = black fill, dark = `primary-550` fill |
| Secondary CTA | Soft `primary-150` fill; no outline |
| Tertiary | Transparent + 1px `line-100` only |
| Hero | One JPG per screen (`light_hero_*` or `dark_hero_*`), radius 20px, flat `neutral-50` shell |
| Service cards | Flat `neutral-50`, 10px radius, 30px outlined icon, solid action chip |
| Glass search | 18px radius; gradient on placeholder/rim token only — no shadow stack |
| Logo | Wordmark `currentColor`; nib uses `--pt-gradient-1` only |

### 2.3 Layout

- Grid base **4px**; desktop gutters **70px**, ≤1024px **20px**
- Max width `min(100vw - 140px, 1920px)`
- Section rhythm: wide vertical gaps (80–280px), not boxed sections

### 2.4 Icons & assets (CDN)

All brand assets live on CDN — **not** in `<skill-dir>`. See `references/assets.md`.

| Asset | Source |
|-------|--------|
| Guideline | `…/nameslink/Guideline.html` |
| Icons (67) | `…/nameslink/Icons.json` → `Icons/*.svg` |
| Images | `…/nameslink/Images.json` → absolute JPG URLs |
| Logo | Inline in Guideline (gradient nib) |

**Mandatory:** resolve every icon and JPG from `Icons.json` / `Images.json` — no substitutes. One icon system per surface (CDN SVG from manifest **or** production iconfont `5164327` — never mix in one control). See `references/icons.md`.

---

## 3. Anti-patterns

- No stock photos, placeholder images, or icons outside `Images.json` / `Icons.json`
- No heavy or decorative box-shadow; no multi-layer shadow stacks (淡阴影 token only when unavoidable)
- No gradient fills on CTAs or page backgrounds
- No Playfair on body copy or nav
- No thick borders as default separation
- No bounce/stagger/parallax; color/opacity transitions at `0.25s` only
- No emoji as icons; use outlined SVG kit
- No flattening logo nib to solid purple

---

## 4. Workflow

1. **Declare fonts** — Inter, Playfair, Roboto Mono
2. **Ask mode** — light or dark (`data-prefers-color`)
3. **Load tokens** — `references/tokens.md`
4. **Compose** — `references/components.md` for buttons, cards, search, nav, plans
5. **Manifests** — fetch `Icons.json` + `Images.json`; bind all icons/photos to manifest `href` / URLs (required)
6. **Guideline** — open `Guideline.html` for visual QA on unfamiliar sections
7. **Review** — checklist below

---

## 5. Reference files

| File | Path |
|------|------|
| Tokens | `<skill-dir>/references/tokens.md` |
| Components | `<skill-dir>/references/components.md` |
| Icons | `<skill-dir>/references/icons.md` |
| CDN assets | `<skill-dir>/references/assets.md` |

---

## 6. Review checklist

- [ ] `--pt-*` tokens used; CTA inversion matches mode
- [ ] Flat cards — no shadow; borders only on tertiary/outline cases
- [ ] ≤1 gradient text treatment per screen (plus logo nib)
- [ ] Playfair limited to floors + plan price
- [ ] Hero/cards use JPG URLs from `Images.json` only (one hero per page)
- [ ] Icons from `Icons.json` `href` only; `currentColor`, outlined, single kit per control
- [ ] 简洁平白：弱描边、无重阴影、无渐变铺底
- [ ] `prefers-reduced-motion` respected
