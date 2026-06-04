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

Reference specs: `references/` (`tokens.md`, `components.md`, `layouts.md`, `icons.md`, `assets.md`). Brand kit on CDN — see `assets.md`.

---

## 核心约束（Agent 必守）

### ★ 头号铁律 — 大标题永远不要压在视觉元素上

**Playfair heading + subtitle are their own clean paragraph on canvas (`--pt-color-neutral-100`). The poster/photo/gradient lives in a SEPARATE rounded card below or beside. Two paragraphs, never one box.**

- ❌ Wrong: `<div class="hero-card" style="background-image: poster.jpg"><h1>Playfair 64</h1></div>` — heading sitting over the poster
- ✅ Right: `<HomeHeroHead>` (h1 + typewriter) on `bg-neutral-100`, **then** a separate `<HeroCard className="bg-neutral-50 rounded-[20px]">` below holding the absolute poster + trust strip + glass search
- The same rule applies to every `home-section-title` (Playfair 40/54) — title sits on the floor's bg plane, cards/photos live in a row beneath
- No `text-shadow`, no dark overlay "for legibility" — if a heading needs help reading, it's in the wrong place
- Upper bound for text on imagery: **title-sm 20 px** (dock prompts, trust strip emphasis). Anything ≥36 px belongs on canvas
- Imagery = photos, videos, flower/abstract/liquid renders, animated gradients. Stepped neutrals (`neutral-100`, `primary-50`, `gradient-card-bg`) are NOT imagery — headings on those are fine

Full rule + DO/DON'T diagrams: `references/layouts.md` §2.

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
2. Load specs on demand: `<skill-dir>/references/tokens.md`, `components.md`, `layouts.md`, `icons.md`, `assets.md`.
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

Page-level composition lives in `references/layouts.md`. Highlights:

- **Three container layers** (§1): outer `.layout-max-wide` (50-px gutter desktop, framed visuals) → inner `.layout-max-inner` (default for headings/grids/copy) → reader cap 768 px (long-form). Mobile gutters drop to 20 px.
- **Heading-on-canvas rule (★ §2)** — Playfair H1 + subtitle live as their own clean paragraph on `neutral-100`; the rounded hero card with the poster lives BELOW with ≥32 px whitespace between. Never overlay big headings on imagery.
- **Floor vertical rhythm:** `mt-20 / [120] / [140] / [170] / [280]`; tablet collapses to `mt-[70px]` / `[100px]`.
- **Section title pattern (§4.1):** Playfair 40/54, `mb-15` (10 mobile).
- **Card system (§5):** **borderless by default** — `bg-neutral-50 + rounded-[10/20/28]` with no border, no shadow unless interactive. Borders appear only on faq + why-choose list rules, mobile profile chip, tag outline variants, tertiary CTA.
- **CTA inversion:** light primary = near-black at rest → purple hover; dark primary = purple → deeper purple.
- **Breakpoint:** 1024 px; quick-nav uses container queries (only place).

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

1. **Declare fonts** — Inter, Playfair (Roboto Mono not used in this codebase)
2. **Ask mode** — light or dark (`data-prefers-color`)
3. **Load tokens** — `references/tokens.md` (includes Dark/Light mode section)
4. **Pick layout** — `references/layouts.md`: container layer (§1) → hero arrangement (§2 — heading-on-canvas!) → floor (§4) → section header pattern (§4.3) → card archetype (§5)
5. **Compose components** — `references/components.md` for buttons, cards, search, nav, plans
6. **Manifests** — fetch `Icons.json` + `Images.json`; bind all icons/photos to manifest `href` / URLs (required); pick per-mode hero (`light_hero_*` / `dark_hero_*`)
7. **Guideline** — open `Guideline.html` for visual QA on unfamiliar sections
8. **Review** — checklist below + `layouts.md` §14

---

## 5. Reference files

| File | Path | Scope |
|------|------|-------|
| Tokens | `<skill-dir>/references/tokens.md` | Color, type, radius, motion, layout tokens + Dark/Light mode adaptation |
| Components | `<skill-dir>/references/components.md` | Buttons, cards, glass-search, nav, plans, tags |
| Layouts | `<skill-dir>/references/layouts.md` | Container layers, ★ heading-on-canvas rule, hero, floors, card archetypes, sub-blocks, CTAs |
| Icons | `<skill-dir>/references/icons.md` | CDN SVG + iconfont rules |
| CDN assets | `<skill-dir>/references/assets.md` | Image / icon manifest URLs |

---

## 6. Review checklist

- [ ] **★ Heading on canvas, never on imagery** — title paragraph + visual paragraph are two separate boxes (`layouts.md` §2)
- [ ] `--pt-*` tokens used; CTA inversion matches mode (light black→purple, dark purple→deeper purple)
- [ ] Both light + dark verified — `data-prefers-color` set; per-mode hero JPG (`light_hero_*` / `dark_hero_*`)
- [ ] Cards are borderless by default (`bg-neutral-50` + `rounded-[10/20/28]`); borders only on the listed list-rule cases (`layouts.md` §5.2)
- [ ] ≤1 gradient text treatment per visible floor (plus logo nib)
- [ ] Playfair scope: hero h1, section titles, plan/dock price, FAQ Q-label — never on body, cards, or nav
- [ ] Hero/cards use JPG URLs from `Images.json` only (one hero per page)
- [ ] Icons from `Icons.json` `href` only; `currentColor`, outlined, single kit per control
- [ ] 简洁平白：弱描边、无重阴影、无渐变铺底
- [ ] Page passes the layout checklist in `layouts.md` §14
- [ ] `prefers-reduced-motion` respected
