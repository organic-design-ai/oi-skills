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

### 配图与图标：只从 manifest 抽取（Lucide 仅作回退）

**禁止** 使用 stock 图、占位图、自造 CDN、emoji 或随意 SVG。配图无回退方案 — 必须来自 `Images.json`。

| 类型 | 做法 |
|------|------|
| **配图** | 先 fetch `Images.json`（见 `assets.md`），从返回的 **绝对 URL** 中选文件名（如 `light_hero_2.jpg`）；`<img src>` 必须用 manifest 中的 URL |
| **图标** | 先 fetch `Icons.json`，按 `id` / `component` 匹配场景，`<use href>` 或 `<img src>` 必须用条目里的 **`href`**（CDN 绝对路径） |
| **图标回退** | 仅当 `Icons.json` 中确实**没有**所需图标时，可使用开源 [Lucide](https://lucide.dev) line icons（CDN `https://unpkg.com/lucide-static@latest/icons/{name}.svg` 或 React 包）。仍须 `currentColor`、outlined、`stroke-width:1.5`，与 manifest SVG 同一视觉权重；同一个控件内**不可混用** Lucide 与 manifest |

实现前若未读 manifest，先 fetch 再写 markup。详见 `references/assets.md`、`references/icons.md`。

### 卡内不嵌灰底小卡

**禁止** 在已经是 `bg-neutral-50` 卡片内再嵌一层 `bg-neutral-150` / `neutral-100` 灰底小卡（包括 recommended-models 列表项、cost summary 行、benefit/spec 子区域等）。

- ❌ 错误：外层 `bg-neutral-50 rounded-[20px]` 卡内套若干 `bg-neutral-150 rounded-[12px]` 灰底盒子，制造"卡中卡"
- ✅ 正确：内嵌信息直接放在干净的卡面上，靠 `border-b border-line1` 分隔行、靠字号/字重/留白分层；需要标签感时用 pill chip 而非整块灰底
- 仅当该子项**本身就是一个独立可点击实体**（如 mode pill rack 的轨道、search 内的功能按钮）才允许浅灰底；信息展示一律保持卡内空白干净

参见 `references/layouts.md` §5.6。

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-nameslink-ui` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-nameslink-ui`), then ask what they want to accomplish.

**Triggers:** `oi-nameslink-ui`, `nameslink-ui`, Nameslink style, Nameslink design, Nameslink 风格 / 设计系统.

**Quick start**
1. Read this `SKILL.md` (philosophy, workflow, anti-patterns).
2. Load specs on demand: `<skill-dir>/references/tokens.md`, `components.md`, `layouts.md`, `icons.md`, `assets.md`.
3. Inject the `@font-face` block below (Inter + Playfair Display). **Default to light theme tokens** unless the user explicitly asks for dark. Implement with `--pt-*` tokens.

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
- **Light is default; dark is supported.** Use light tokens (`data-prefers-color='light'`) unless the user explicitly requests dark. The neutral ramp inverts roles in dark mode.
- **Playfair H1 is upright, never italic.** Default `font-style: normal` on all hero / section headings. Italic is reserved for in-line emphasis spans only.

**Fonts (inject before coding):**

Embed the following `@font-face` block in the page's `<style>` (or top of the global CSS). Do **not** swap in Google Fonts, system fallbacks, or alternate URLs.

```css
@font-face {
    font-family: 'Inter';
    src: url('https://acd-assets.alicdn.com/acd_work/web-fonts/inter/Inter-Variable.ttf') format('truetype');
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
}

@font-face {
    font-family: 'Playfair Display';
    src: url('https://acd-assets.alicdn.com/acd_work/web-fonts/playfair-display/PlayfairDisplay-VariableFont_wght.ttf')
        format('truetype');
    font-style: normal;
    font-weight: 400 900;
    font-display: swap;
}
```

Then set `--pt-font-regular: 'Inter', sans-serif` and `--pt-font-playfair: 'Playfair Display', serif`. Roboto Mono: see `references/tokens.md` §2.

**Reset (inject right after the `@font-face` block):**

Browser defaults italicize `<em>`, `<i>`, `<cite>`, `<dfn>`, `<var>`, `<address>` — that creates accidental italics inside body copy, captions, blockquotes, and AI-generated prose. Inject this minimal reset so emphasis becomes a deliberate utility class instead of a default. Reference: `/Users/duhaihang/Ali/Gitwork/organic/src/css/reset.scss` (canonical Meyer-style reset used by the source codebase — copy it wholesale when the page is more than a single landing block).

```css
*, *::before, *::after { box-sizing: border-box; }
html, body, h1, h2, h3, h4, h5, h6, p, ul, ol, li, figure, blockquote, dl, dd {
    margin: 0;
    padding: 0;
}
ul, ol { list-style: none; }
a { color: inherit; text-decoration: none; }
button { background: none; border: 0; padding: 0; font: inherit; color: inherit; cursor: pointer; }
img, svg, video { display: block; max-width: 100%; }
input, textarea, select { font: inherit; color: inherit; }

/* No accidental italics — render upright by default; italicize only via an explicit utility. */
em, i, cite, dfn, var, address { font-style: normal; }
```

If you need real emphasis, mark it with a deliberate class (e.g. `<em class="is-italic">`) and style it explicitly — never rely on the user-agent default.

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

- No stock photos, placeholder images, or icons outside `Images.json` / `Icons.json` (Lucide allowed **only** as last-resort fallback when manifest lacks the glyph)
- No italic Playfair H1 / section title; default `font-style: normal` for all ≥36 px headings
- No accidental italics anywhere — reset block must include `em, i, cite, dfn, var, address { font-style: normal }`; italic only via an explicit utility class
- No grey-bg (`neutral-150` / `neutral-100`) inset cards stacked inside an already-card surface — keep card interiors clean, separate rows by `border-b border-line1` instead
- No heavy or decorative box-shadow; no multi-layer shadow stacks (淡阴影 token only when unavoidable)
- No gradient fills on CTAs or page backgrounds
- No Playfair on body copy or nav
- No thick borders as default separation
- No bounce/stagger/parallax; color/opacity transitions at `0.25s` only
- No emoji as icons; use outlined SVG kit
- No flattening logo nib to solid purple

---

## 4. Workflow

1. **Inject fonts** — paste the `@font-face` block above into the page CSS (Inter + Playfair Display; Roboto Mono not used in this codebase)
2. **Pick mode** — **default light** (`data-prefers-color='light'`); only switch to dark if the user explicitly asks
3. **Load tokens** — `references/tokens.md` (includes Dark/Light mode section)
4. **Pick layout** — `references/layouts.md`: container layer (§1) → hero arrangement (§2 — heading-on-canvas!) → floor (§4) → section header pattern (§4.3) → card archetype (§5)
5. **Compose components** — `references/components.md` for buttons, cards, search, nav, plans
6. **Manifests** — fetch `Icons.json` + `Images.json`; bind all icons/photos to manifest `href` / URLs (required); pick per-mode hero (`light_hero_*` / `dark_hero_*`); only use Lucide line icons as a **last-resort** fallback when the manifest lacks the glyph (see §核心约束)
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

- [ ] `@font-face` block for Inter + Playfair Display injected verbatim (acd-assets URLs)
- [ ] Reset block injected right after `@font-face` — includes `em, i, cite, dfn, var, address { font-style: normal }`, list/link/button resets, `box-sizing: border-box`
- [ ] **Light theme is the default** unless dark was explicitly requested; `data-prefers-color='light'` set on `<html>`
- [ ] Playfair H1 / section titles are upright (`font-style: normal`) — no italic by default
- [ ] **★ Heading on canvas, never on imagery** — title paragraph + visual paragraph are two separate boxes (`layouts.md` §2)
- [ ] No grey (`neutral-150` / `100`) inset sub-cards inside an already-card surface — info rows sit on clean card, divided by `border-b border-line1`
- [ ] `--pt-*` tokens used; CTA inversion matches mode (light black→purple, dark purple→deeper purple)
- [ ] If dark requested: both light + dark verified — `data-prefers-color` set; per-mode hero JPG (`light_hero_*` / `dark_hero_*`)
- [ ] Cards are borderless by default (`bg-neutral-50` + `rounded-[10/20/28]`); borders only on the listed list-rule cases (`layouts.md` §5.2)
- [ ] ≤1 gradient text treatment per visible floor (plus logo nib)
- [ ] Playfair scope: hero h1, section titles, plan/dock price, FAQ Q-label — never on body, cards, or nav
- [ ] Hero/cards use JPG URLs from `Images.json` only (one hero per page)
- [ ] Icons from `Icons.json` `href` only; Lucide allowed **only** as fallback when manifest lacks the glyph; `currentColor`, outlined, single kit per control
- [ ] 简洁平白：弱描边、无重阴影、无渐变铺底
- [ ] Page passes the layout checklist in `layouts.md` §14
- [ ] `prefers-reduced-motion` respected
