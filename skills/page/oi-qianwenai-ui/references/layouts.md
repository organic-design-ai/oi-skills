# 千问云 — Page Layouts

Page-level composition. Tokens: `tokens.md` (`--pt-cn-*`). Components: `components.md`. Icons/photos: manifest (`icons.md`, `assets.md`).

**Reuse existing tokens. Do not invent new ones.** Spacing is written as literal px on a 2-px rhythm; pick from `{4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 44, 48, 56, 64, 72, 96, 122}`.

---

## 1. Page shell & container scope

### 1.1 The page nests in three layers

```
┌──────────────────────────────────────────────────────────────────┐
│  viewport (100vw)                                                │
│                                                                  │
│   ┌─ .layout-max-wide ─ outer ─────────────────────────────┐    │   ← gutter ≈ 70 px
│   │   max-width: calc(--pt-cn-layout-max-width + 72px)        │    │
│   │   padding: 0 70px                                      │    │
│   │                                                        │    │
│   │   ┌─ .layout-max-inner ─ inner ─────────────────┐     │    │
│   │   │   max-width: var(--pt-cn-layout-max-inner)     │     │    │   ← gutter ≈ 140 px from viewport
│   │   │   (wrap padding: 8px 36px 0)                │     │    │
│   │   │                                             │     │    │
│   │   │   ┌─ reader ─ var(--pt-cn-layout-max-read-box)  │     │    │
│   │   │   │   640 px cap, centered                  │     │    │
│   │   │   └─────────────────────────────────────────┘     │    │
│   │   └─────────────────────────────────────────────┘     │    │
│   └────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

Three width tokens, three layers — never bypass:

| Token | Value | Class | What sits here |
|-------|-------|-------|----------------|
| `--pt-cn-layout-max-width` | `min(100vw - 140px, 1920px)` | `.layout-max-wide` (outer) | Full-bleed framed visuals: hero image/video panel, era CTA, bulletin, marketplace carousel |
| `--pt-cn-layout-max-inner` | `min(100vw - 280px, calc(1920px - 140px))` | `.layout-max-inner-wrap > .layout-max-inner` (inner) | **Default for everything else**: headings, section heads, grids, copy, tabs, filters |
| `--pt-cn-layout-max-read-box` | 640 px | (utility — `width: min(100%, var(--pt-cn-layout-max-read-box))`) | Long-form prose: legal, docs body, skills-detail body, models-detail body, hero subtitle |

### 1.2 Decision rule (must follow)

- **Outer (`.layout-max-wide`)** — only when the section's visual content is itself a framed media panel (video, photo, carousel, big rounded surface) that should reach near the viewport edges. Outer is wider — 140 px viewport gutter — so visuals breathe.
- **Inner (`.layout-max-inner`)** — for everything else. **Headings, subtitles, section heads, grids, paragraphs, filter rails, cards, accordions, FAQ, tables, forms.** Inner is narrower (280 px viewport gutter) — text gets more whitespace and is easier to scan.
- **Reader** — nest *inside* inner. Long-form prose (>3 paragraphs), legal/docs/skills-detail body. Cap at 640 px and center.

**A hero typically uses both:** the H1/subtitle stack lives in **inner**, then the image/video panel below lives in **outer**. Don't put the giant heading in the outer wrap — see §2.1.

### 1.3 Shell skeleton

```jsx
<div className="page-shell page-<name>">
  <Nav />                                {/* sticky, 84 px desktop / 62 px mobile */}
  <div className="page">                 {/* min-height:100vh; bg: --pt-cn-color-neutral-50; pb: 48px */}

    {/* Inner: heading stack */}
    <div className="layout-max-inner-wrap">
      <div className="layout-max-inner">
        <header className="hero-head">
          <h1>…</h1>
          <p className="hero-sub">…</p>
          <div className="hero-cta-row">…</div>
        </header>
      </div>
    </div>

    {/* Outer: framed visual */}
    <div className="layout-max-wide">
      <div className="hero-panel">…video / image…</div>
    </div>

    {/* Inner: subsequent sections */}
    <div className="layout-max-inner-wrap"><div className="layout-max-inner">
      <section>…</section>
      <section>…</section>
    </div></div>

  </div>
  <footer className="page-footer">…</footer>
</div>
```

### 1.4 Sticky offsets

- Nav var: `--pt-cn-nav-backdrop-offset: 84px` desktop · `62px` ≤1024
- Sticky filter / TOC rails: `top: calc(var(--pt-cn-nav-backdrop-offset) + 12px)`
- Read-section sticky headings: `top: calc(var(--pt-cn-nav-backdrop-offset) + 8px)`
- Mobile sticky bars (search dropdown, compare bar): `top: calc(var(--pt-cn-nav-backdrop-offset) + 8px)`

### 1.5 Section vertical rhythm (between floors)

Between top-level "floors" (sibling sections of the page):

- `margin-top: 96px` (compact) · `122px` (default) · `138px` (loose, between major chapters)

Inside a floor (between its head and its grid/body):

- `margin-bottom: 48px / 60px / 64px` on the head

Mobile (≤1024 px): collapse to `64 px` between floors, `32 px` head→body.

### 1.6 Marketing flat contract  ★

Guideline 长页（首页、Token Plan、Hackathon）共享 **平面** 体系。所有 §4 营销楼层默认遵守（数据页 §17 除外）。

| 规则 | 规范 |
|------|------|
| **阴影** | 营销卡、楼层、logo、FAQ、arena 视觉：**默认 `box-shadow: none`** |
| **分层** | 仅 `neutral-50` 画布 ↔ `neutral-100` 色带 ↔ `gradient-card-bg` 面板（§4.1） |
| **描边** | 价卡、logo 矩阵 A、outline 按钮用 `line-100`；panel-as-card **无** 外框（§11.6） |
| **Hover** | 营销价卡 **无** 上浮；logo 矩阵仅描边加深 |
| **CTA** | Hero/尾部：**L1 primary + L3 outline**（§2.7）；价卡内 featured 用 primary |
| **渐变字** | 每屏 ≤1 词；千问云优先 **`gradient-1/2/3/8/9`（蓝绿青）** — 见 `tokens.md` |
| **嵌套** | 价卡/FAQ/面板列表内 **禁止** 灰底嵌套子卡 |

---

## 2. Heading vs imagery — the cleanliness rule  **★ most important rule ★**

> **Big headings sit on white. Imagery sits in its own panel. Title + subtitle are their own paragraph block, with breathing room above the visual.**
>
> Violating this is the single biggest way to make the page look wrong. This rule overrides almost every other consideration.

### 2.1 ❌ WRONG vs ✅ RIGHT — burn this in

```
❌ WRONG — heading laid over a flower/gradient/photo, fighting the visual
┌─────────────────────────────────────────────────────────────────┐
│   ╔═══════════════════════════════════════════════════════╗    │
│   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║    │
│   ║░░░░░░░ purple/pink model poster / abstract / video ░░░░░░░░║    │
│   ║░░░░░                                          ░░░░░░░║    │
│   ║░░░░░       AI驱动的短剧·漫剧创作工坊         ░░░░░░░║   ← 60+ px heading
│   ║░░░░░       ← 60+ px Inter Bold              ░░░░░░░░║     PHYSICALLY ON
│   ║░░░░░                                          ░░░░░░░║     the gradient/image.
│   ║░░░░░       从剧本到成片… subtitle paragraph  ░░░░░░░║     This looks BAD.
│   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║    │
│   ╚═══════════════════════════════════════════════════════╝    │
└─────────────────────────────────────────────────────────────────┘

✅ RIGHT — heading + subtitle on clean white, image is a separate panel
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │   ← whitespace
│   Ship the next                                                 │   ← H1 on
│   ────────────────────                                          │     neutral-50
│   AI-Native Cloud with models, tools, apps, ready out of box.   │   ← sub paragraph
│                                                                 │     on neutral-50
│   [ Try now ]  [ Get API keys ]                                 │   ← CTAs on canvas
│                                                                 │   ← whitespace
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ 1,000,000+   Scaling     99.9%       Ultra Low          │  │
│   │ Model Users  In Seconds  Uptime      Latency            │  │   ← image panel
│   │                                                         │  │     BELOW.
│   │       ░░░░ purple flower / gradient ░░░░               │  │     Heading is
│   │       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                   │  │     NOT in here.
│   └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

The Token Plan page does the same: "千问云 Token Plan" sits centered on white at top, the lavender card with screenshots starts BELOW it with clear whitespace. The image never reaches up to touch the heading.

### 2.2 Anti-patterns — never do these

- ❌ H1 / H2 (≥36 px) physically overlapping a photo, video, abstract gradient, flower, or any visual asset
- ❌ Hero panel that contains both the giant heading AND the imagery in the same rectangle
- ❌ Adding `text-shadow`, blur layer, or dark overlay to "make the heading readable on the photo" — if you need that, the heading is in the wrong place
- ❌ A heading positioned absolute inside a `.hero-panel` that has `background-image`
- ❌ Centering an H1 on top of `--pt-cn-gradient-card-bg` so the gradient ladders behind the type
- ❌ "Filling" empty whitespace above an image by sliding the heading down into it

### 2.3 The canonical arrangement

```
┌── .layout-max-inner ─────────────────────────────────────┐    ↑ on --pt-cn-color-neutral-50
│                                                          │    │
│   eyebrow (optional, mono caption-sm, neutral-450)       │    │   PARAGRAPH 1
│   H1   (60 – 96 px, font-bold, neutral-950)              │    │   text only, on canvas
│        with at most ONE gradient word                    │    │   margin-bottom: 32–48 px
│   subtitle  (body-lg, neutral-650, max-width 620–768)    │    │
│   [ L1 primary ] [ L3 outline ]   ← home: §2.7           │    │
│                                                          │    │
└──────────────────────────────────────────────────────────┘    ↓
                                                                    ← whitespace mt 48–64 px
┌── .layout-max-wide ─────────────────────────────────────────┐ ↑ separate panel
│  ┌────────────────────────────────────────────────────┐    │ │
│  │  ░░ image / video / flower / gradient ░░           │    │ │   PARAGRAPH 2
│  │  border-radius: var(--pt-cn-radius-md or lg)          │    │ │   visual only
│  │  object-fit: cover                                 │    │ │   in its own card
│  │  optional small overlay (metric chips, see §8.1)   │    │ │
│  └────────────────────────────────────────────────────┘    │ │
└─────────────────────────────────────────────────────────────┘ ↓
```

Two **separate paragraphs**, in this order:

1. **Title paragraph** — eyebrow + H1 + subtitle + CTAs. Lives in `.layout-max-inner`. Background: `--pt-cn-color-neutral-50` (canvas). Nothing visual, just type.
2. **Visual paragraph** — image / video panel. Lives in `.layout-max-wide` (or stays in inner). Its own rounded card. Plenty of whitespace above (`margin-top: 48–64 px`) separating it from the title paragraph.

This is what makes pages like 千问云 "Ship the next" and Cohere's Security/Deployment/Customization (line icons + headline on clean white, hero photo as a separate band below) feel calm — title and visual are **never in the same box**.

### 2.4 Hard rules

- **Heading (≥36 px) sits on `--pt-cn-color-neutral-50`** (canvas) or `--pt-cn-color-neutral-100` (tinted floor — also neutral, no imagery). Not on any photo, video, gradient, or model poster.
- **Subtitle paragraph** sits with the heading, on the same canvas, never on imagery.
- **Image / video lives in its own card** with `border-radius: var(--pt-cn-radius-md)` or `lg`. The image's top edge is **at least 32 px** below the bottom of the title paragraph.
- **CTAs live with the heading**, not on imagery.
- **Permitted overlays on the image card** — small and quiet only:
  - 4-up metric chips (title-lg `28 px` strong + body-md small caption + colored dot, see §8.1)
  - A small caption-md mono label in a corner
  - A subtle gradient wash applied to the image itself (not behind a heading) for tonal balance
- **Upper bound for text on imagery: title-lg (28 px).** Anything bigger must move to the title paragraph above.
- **No text-shadow, no dark overlay, no blur backdrop "for legibility."** If the heading needs help reading, it's in the wrong place — move it up to the canvas.

### 2.5 The one exception: era / closing CTA hero (variant F)

The final closing-CTA pattern (`era-hero`) is the only hero where a heading sits over imagery. The rule survives because:

- The video is **explicitly designed** as a quiet, low-contrast backdrop (the visual was art-directed FOR this purpose).
- The h2 is **moderate** (72 px), not the giant marketing hero (96+ px).
- Content is **centered**, the panel is **790 px** tall (§4.9；旧 CSS 可能为 780 px) — extreme whitespace inside.
- A **glass / blurred backdrop** sits behind the CTA pill (not the heading) for the form input only.
- This is a closing footer beat — not the page-leading hero.

If you're not building this exact closing-CTA pattern with these constraints, **stack vertically — title paragraph above, visual paragraph below.**

### 2.6 Where headings ARE allowed on a stepped surface

`neutral-100` (tinted floor) is fine. `--pt-cn-gradient-card-bg` (almost-flat 135° wash from `neutral-150` → `neutral-50`) is fine for the two-column panel head (§5 pattern C). These are *quiet neutral bg steps* — they read as canvas, not imagery.

Imagery means: photographs, videos, model poster / abstract / liquid renders, animated gradients, glass blur over a photo. Stepped neutrals are NOT imagery.

### 2.7 Home page hero — title stack  *(首页 canonical)*

The marketing **homepage** (and any page that opens with the same two-paragraph beat — e.g. Hackathon landing, Token Plan intro) uses one fixed title stack in **inner**, then one **visual panel** in **outer**. Reference: Guideline home, Hackathon hero, Token Plan hero.

```
┌── .layout-max-inner — PARAGRAPH 1 (canvas only) ─────────────┐
│                    margin-top: 48–64 px                       │
│                                                               │
│              H1  centered  2xl–3xl  one gradient word         │
│              subtitle  body-lg  neutral-650  max read-box     │
│              [ Level 1 primary ]  [ Level 3 outline ]           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
                         ↕  48–64 px  (字不压视觉 — never less)
┌── .layout-max-wide — PARAGRAPH 2 (visual only) ──────────────┐
│  ┌─ .hero-visual  radius-lg  overflow hidden ─────────────┐  │
│  │  Mode A: hero media 450–480 px  OR                      │  │
│  │  Mode B: info showcase 420 px  (accordion + preview)    │  │
│  └─────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────┘
```

#### Title stack anatomy

```scss
.hero-head {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  text-align: center;
  margin-top: 48px;                                       // 64 px on airy home
  margin-bottom: 0;                                       // gap to visual lives on .hero-visual

  h1 {
    font-size: var(--pt-cn-heading-font-size-2xl);        // 72 — or clamp(72px, 8vw, 86px) CN
    line-height: var(--pt-cn-heading-line-height-2xl);
    font-family: var(--pt-cn-font-bold);
    letter-spacing: var(--pt-cn-letter-spacing-tight);
    color: var(--pt-cn-color-neutral-950);
    margin: 0;
    max-width: min(100%, 920px);
  }

  .hero-sub {
    margin: 16px auto 0;
    max-width: var(--pt-cn-layout-max-read-box);          // 640 px
    font-size: var(--pt-cn-body-font-size-lg);
    line-height: var(--pt-cn-body-line-height-lg);
    color: var(--pt-cn-color-neutral-650);
  }

  .hero-cta-row {
    display: inline-flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-top: 36px;
  }
}
```

- **H1 is always center-aligned** on `--pt-cn-color-neutral-50`. At most **one** gradient-clipped `<span>` inside the h1.
- **Subtitle** sits with the h1 on canvas — never inside `.hero-visual`.
- **Eyebrow** (optional): mono `caption-sm`, uppercase, `neutral-450`, above h1.

#### CTA pairing — Level 1 + Level 3 only  *(homepage hero)*

Home hero CTAs use exactly **two** buttons in this order — not `btn--secondary` (purple soft fill):

| Slot | Component | Role |
|------|-----------|------|
| **Level 1** | `btn--primary` | Black pill (`cta-fill` → hover `primary-550`); leading action |
| **Level 3** | `btn--outline` | Transparent + `1px line-200`; quiet secondary path |

```
✅ RIGHT — Hackathon / home hero
[ 立即申请 ]  [ 查看套餐 ]
     btn--primary    btn--outline

❌ WRONG — primary + secondary soft-fill on home hero
[ 立即体验 ]  [ 获取 API Key ]     ← secondary 紫底与 L1 争抢注意力

❌ WRONG — three buttons
[ Primary ] [ Outline ] [ Text link ]   ← title stack 最多两个 CTA
```

- Icon on Level 1 only: `arrow-up-right-outlined` trailing (千问云主 CTA 规范).
- Card / pricing / floor bodies may still use `primary + outline` or `primary + secondary` — **L1+L3 lock applies to the homepage title paragraph** and campaign openers that copy it.

#### Spacing — 字不压视觉

| Gap | Value | Rule |
|-----|------:|------|
| Nav → title stack | `48–64 px` | `margin-top` on `.hero-head` |
| H1 → subtitle | `16 px` | stack `gap` or sub `margin-top` |
| Subtitle → CTA row | `36 px` | `.hero-cta-row { margin-top: 36px }` |
| **CTA row → visual panel** | **`48–64 px`** | `margin-top` on `.hero-visual` — **minimum 48 px** |
| Visual → next floor | `96–122 px` | §1.5 |

### 2.8 Hero visual panel — shared chrome & two modes

`.hero-visual` is the **single large rounded block** below the title stack. It always lives in `.layout-max-wide`. Pick **one mode** per page.

#### Shared shell (both modes)

```scss
.hero-visual {
  margin-top: 48px;                                       // 64 px when title block is short
  width: 100%;
  border-radius: var(--pt-cn-radius-lg);                  // 36 px
  overflow: hidden;
  position: relative;
  isolation: isolate;
}
```

- **No border, no shadow** on the shell.
- Heading / subtitle / CTAs stay **outside** (§2.7).
- Mobile: keep `radius-lg`.

#### Mode A — Hero media  *(`.hero-visual--media`)*

Reference: campaign / home — `qwen-model-*` poster with optional metric strip.

```
┌─ .hero-visual--media  h: 450–480 ─────────────────────────────┐
│  ┌─ optional metric row (4-up, §8.1) ─────────────────────┐  │
│  │  ● 10B+ TPM    ● Scaling    ● Optimal    ● Ultra-Low   │  │
│  └────────────────────────────────────────────────────────┘  │
│  ░░░░░░░░░░  qwen-model-* / video  object-fit: cover ░░░░░░░  │
└───────────────────────────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Height | **`450 px`** (minimal) · **`460 px`** (default) · **`480 px`** (4-up metrics) — max 480 on home |
| Media | One `qwen-model-*` from `Images.json` **or** cover video |
| Overlay | Optional 4-up metrics (§8.1); text ≤ title-lg (28 px) |

```scss
.hero-visual--media {
  height: 460px;
}
.hero-visual--media__media {
  position: absolute;
  inset: 0;
  object-fit: cover;
}
```

Mobile: `min(420px, 56vw)`; metrics 2×2.

#### Mode B — Info showcase  *(`.hero-visual--showcase`)*

Reference: **Token Plan** — accordion left, product preview right.

| Property | Value |
|----------|-------|
| Height | **`420 px` locked** |
| Background | `var(--pt-cn-gradient-card-bg)` |
| Padding | `60px 44px` desktop · `32px 20px` mobile |
| Grid | `1fr 1fr; gap: 64px` |
| Left | Accordion (§8.6): icon + title + `+` collapsed; body-sm when open |
| Right | `.hero-visual-preview` — `.is-active` cross-fade |

```scss
.hero-visual--showcase {
  height: 420px;
  background: var(--pt-cn-gradient-card-bg);
  padding: 60px 44px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
}
```

Mobile: accordion + preview stack; `min-height: 420px`.

#### Mode picker

| Page intent | Mode | Height |
|-------------|------|--------|
| Home, campaign — one strong model poster | **A — media** | 450–480 px |
| Token Plan, feature walkthrough | **B — showcase** | 420 px |
| Tagline + code panel | §3 variant **A** | — |

---

## 3. Hero variants

Pick exactly one per page. Never stack two heroes. All variants follow §2 — title on canvas, imagery framed below or beside.

### A. Split tagline hero  *(home tagline)*

Two-column inside `.layout-max-inner`.

- Grid: `minmax(0,1fr) minmax(320px, 392px)` · `gap: 44px` · `margin-top: 64px`
- Left: H1 `--pt-cn-heading-font-size-xl` (64/68), letter-spacing tight, **one** `<span>` gradient-clipped. Sub `--pt-cn-body-font-size-lg`, `max-width: 680px`. CTA row `inline-flex; gap: 10px; margin-top: 36px`.
- Right: bordered command/code panel — `border: 1px solid var(--pt-cn-color-line-100); border-radius: var(--pt-cn-radius-md)`. Both columns on canvas — no imagery in this hero.
- Mobile: 1 column; right panel drops below.

### B. Stacked center hero  *(home, campaign, Token Plan opener)*

**Canonical homepage layout — full spec in §2.7–§2.8.** Two-piece: centered title stack in inner → `.hero-visual` in outer.

```
.layout-max-inner-wrap
  .layout-max-inner
    .hero-head
      h1          (centered, 2xl–3xl, on neutral-50, ≤1 gradient word)
      .hero-sub   (centered, max-width: var(--pt-cn-layout-max-read-box))
      .hero-cta-row
        btn--primary          ← Level 1
        btn--outline          ← Level 3
.layout-max-wide
  .hero-visual
    .hero-visual--media      Mode A: 450–480 px, qwen-model-* / video
    — or —
    .hero-visual--showcase    Mode B: 420 px, accordion + preview
```

- **Title stack:** §2.7 — centered h1, subtitle, **Level 1 + Level 3** CTAs; L1 icon `arrow-up-right-outlined`.
- **Visual panel:** §2.8 — `radius-lg`; **48–64 px** below CTAs (字不压视觉).
- **Mode A:** `450–480 px` (default `460`); **Mode B:** `420 px` locked.
- H1: `2xl` (72) or `clamp(72px, 8vw, 86px)` CN; sub `--pt-cn-color-neutral-650`.

### C. Centered intro hero  *(skills-detail, docs-adjacent)*

`.intro-header { display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center }`

- H1: `--pt-cn-heading-font-size-lg` (60), letter-spacing tight, on canvas.
- `.heading-desc`: body-lg, color `--pt-cn-color-neutral-750`, `max-width: 560–620 px`.
- **Token Plan / coding-plan openers** → **variant B + §2.8 Mode B** (`.hero-visual--showcase` 420 px).

### D. Compact left-aligned hero  *(models, models/detail, models/compare, docs)*

Heading row inside `.layout-max-inner`.

- `display: flex; align-items: flex-end; justify-content: space-between; gap: 24px; margin-bottom: 50px`
- H1: `--pt-cn-heading-font-size-md` (44) or `--pt-cn-heading-font-size-sm` (36) for sub-pages
- Right side: actions (filter button, share, theme toggle, breadcrumb)
- Subtitle: body-md, color `--pt-cn-color-neutral-800`, `margin: 12px 0 48px`

### E. Docs panel hero

Tinted inset panel, not full-bleed.

- `.docs-content-panel`: `background: var(--pt-cn-color-neutral-100); border-radius: var(--pt-cn-radius-lg); padding: 40px 48px`
- Inside: `grid-template-areas: 'heading actions'; grid-template-columns: minmax(0,1fr) auto`
- Breadcrumb row above (`max-width: var(--pt-cn-layout-max-read-box)`)

### F. Era / closing CTA hero  *(closing block — §4.9)*

§2.3 例外。完整规范见 **§4.9 尾部大视觉**。

- **高版** `790px`（`.tail-visual--tall` / legacy `.era-hero-shell` ~780 px）
- **紧凑** `370px`（`.tail-visual--compact`）
- `radius-lg`；居中 h2 + **L1 primary + L3 outline**；可选 §8.25 kicker 内链

### G. Marketplace carousel hero  *(models)*

Heading inside inner, carousel breaks out to viewport right edge.

- Heading row: `display: flex; align-items: flex-end; justify-content: space-between; margin-bottom: 50px`
- Carousel track: `padding-left: max(20px, calc((100vw - var(--pt-cn-layout-max-width)) / 2))` so cards align to inner gutter but overflow right
- Cards: 588×244, gap 24, `border-radius: var(--pt-cn-radius-md)`

### H. Reader-column hero  *(legal, docs body, skills-detail body)*

Long-form prose. See §6.

### I. Asymmetric skill hero  *(organic skills, ref pattern)*

Two-column grid `1fr 6fr; gap: 120px` inside inner. Left = small meta caption (mono, body-sm). Right = giant H1 (--pt-cn-heading-font-size-xl, 64 px) with optional gradient segment + inline install command box. Used for "documentation-leading" pages where a single artifact (skill, model, doc) is the subject.

---

## 4. Floor (section) taxonomy

A "floor" is one top-level section of the page. Floors stack vertically with §1.5 rhythm. 营销页遵守 **§1.6 平面契约**。

### 4.0 Canonical marketing page stacks  ★

Guideline 参考页的楼层编排 — 选一条 recipe，勿乱序。楼层间交替 §4.1 背景。

**首页：** §2.7–§2.8 hero A → 模型/特性 → §4.7 次级 → §4.11 证言（可选）→ §4.8 B logo 条 → §4.9 大尾部 790px → §4.10 footer

**Token Plan：** §2.7 B + §2.8 **Mode B**（手风琴在 hero 420px 内，**非** §4.13）→ §4.4 四卡价 → §4.8 A 工具矩阵 → §4.12 FAQ 外壳 B → §4.10 footer（常无尾部大视觉）

**Hackathon：** hero → §4.4 三卡奖 → §4.13 arena **或** §4.6 步骤 → §4.8 B 伙伴 → §4.9 紧凑 370px → footer

**§4.13 vs §2.8 Mode B：** Token Plan 折叠在 **hero 视觉盒**；Choose Your Arena 是 **页中** §4.13。同页勿重复。

### 4.1 Floor backgrounds (the alternation rule)

Only three planes — alternate them; **never put two floors of the same tint adjacent**:

| Plane | Color | When to use |
|-------|-------|-------------|
| Canvas | `--pt-cn-color-neutral-50` | Default floor |
| Tinted | `--pt-cn-color-neutral-100` | Every 2nd or 3rd floor for visual rhythm; data-dense floors that need contrast from canvas |
| Card-wash | `--pt-cn-gradient-card-bg` (`135deg, neutral-150 → neutral-50`) | A floor that *is* a single panel (e.g. AI-powered-product, FAQ panel, intro showcase) — wrap the whole floor in one rounded box |

**Do not use shadow or border to separate floors** — that's what the bg step is for. Floors transition by background change + whitespace only.

### 4.2 Floor anatomy

```
┌── floor (full viewport width) ─────────────────────────────┐
│  bg: neutral-50 | neutral-100 | gradient-card panel       │
│  margin-top: 96 / 122 / 138 from previous floor           │
│                                                            │
│  .layout-max-inner-wrap                                    │
│    .layout-max-inner                                       │
│      ┌── floor-head (one of A/B/C, see §5) ──┐            │
│      │   eyebrow? · h2 · sub                  │            │
│      │   margin-bottom: 48 / 60               │            │
│      └────────────────────────────────────────┘            │
│      ┌── floor-body ──────────────────────────┐            │
│      │   grid | accordion | cards | list      │            │
│      └────────────────────────────────────────┘            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 4.3 Floor sizing patterns

- **Standard floor:** height = content + breathing room. Don't fix heights; let content dictate.
- **Hero floor (home variant B):** title stack + visual **450–480 px** (Mode A) or **420 px** (Mode B); §2.7–§2.8.
- **Hero floor (era / tail):** **790 px** 或 **370 px** compact（§4.9 / §3 F）。
- **Bulletin floor:** `--pt-cn-bulletin-height: 306px` (24-px padding mobile, 70-px desktop) — pinned strip for announcements.
- **Stacking scroll floor:** `height: 180vh` with `position: sticky` interior — for scroll-choreographed reveals (rare; e.g. featured model stack on home).
- **Closing CTA / tail visual:** **790 px** 大视觉或 **370 px** 紧凑版（§4.9）；legacy `.era-hero-shell` ≈780 px。
- **Card row floor:** content-driven height; 3-up or 4-up equal cards (§4.4).
- **Media duo floor:** 2-up borderless visual cards (§4.5) — agent builder; text-link CTAs.
- **Simple card floor:** 3-up `line-100` skill/step cards (§4.6) — tag, price-text, metrics.
- **Secondary showcase:** tabs + text-only cards (§4.7) — bottom hairline only.
- **Logo floor:** §4.8 — **A** 描边矩阵 **或** **B** 无边透明 Logo 条。
- **Tail visual CTA:** 790 / 370 px 尾部大视觉（§4.9）— 居中文案 + 双按钮，紧贴 Footer。
- **Site footer:** 35 / 65 不均分 + 底栏版权（§4.10）。
- **Carousel toggle:** 100vw 卡片轨道 + ‹ › 切换（§4.11）— `line-100` 或 `neutral-100` 底，无阴影。
- **FAQ：** 双栏手风琴（§4.12）— inner `neutral-50` **或** 宽屏 `neutral-100` 大圆角面板；`+` 互斥单开。
- **信息折叠 + 视觉联动：** 左折叠列表驱动右预览（§4.13）— 如 Choose Your Arena。

### 4.4 Card row floor — pricing / plan / prize comparison  ★

The most common **mid-page floor** after the hero: centered floor-head (Pattern A, §5) + a horizontal row of **3 or 4** equal comparison cards. Reference: Hackathon **Prizes and rewards $65,000+** (3-up), Token Plan **Limited Offer** (4-up + Enterprise/Personal toggle).

```
┌── floor — canvas neutral-50 ─────────────────────────────────────────┐
│              h2  centered  one gradient word optional                 │
│              subtitle  body-lg  neutral-750                          │
│              [ Enterprise | Personal ]  ← optional pill toggle       │
│                                                                      │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────────┐ │
│   │ line-100    │  │ gradient rim│  │ line-100    │  │ line-100 │ │
│   │ neutral-50  │  │ .featured   │  │ neutral-50  │  │          │ │
│   │ name·price  │  │ name·price  │  │ name·price  │  │          │ │
│   │ [secondary] │  │ [ primary ] │  │ [secondary] │  │          │ │
│   │ ─────────── │  │ ─────────── │  │ ─────────── │  │          │ │
│   │ icon+features│  │ icon+features│  │ icon+features│  │          │ │
│   └─────────────┘  └─────────────┘  └─────────────┘  └──────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

#### When to use 3-up vs 4-up

| Count | Use when | Reference |
|-------|----------|-----------|
| **3-up** | Wider cards, simpler choice | Prizes $65,000+, 3 tiers |
| **4-up** | Dense SKU / credit grid | Token Plan monthly tiers |

Pick **one** count per row. All siblings share **R9** (§11.2).

#### Floor shell

```jsx
<section className="floor floor--card-row">
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <header className="floor-head">…Pattern A…</header>
      <div className="card-row-toggle" role="tablist">…§8.4 optional…</div>
      <div className="card-row-grid card-row-grid--3">   {/* or --4 */}
        <article className="card-row-item is-featured">…</article>
        …
      </div>
    </div>
  </div>
</section>
```

- Floor bg: **canvas** (`--pt-cn-color-neutral-50`). No outer bordered wrap.
- Head → grid: `margin-bottom: 48px`; toggle `margin-bottom: 40px` when present.

#### Grid

```scss
.card-row-grid {
  display: grid;
  align-items: stretch;
  gap: 24px;
}
.card-row-grid--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.card-row-grid--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
```

≤1024 px: `1fr`, gap **18**.

#### Card chrome — no shadow, hairline or gradient rim only

| State | Border | Fill | Radius | Padding | Shadow |
|-------|--------|------|--------|---------|--------|
| Default | `1px solid var(--pt-cn-color-line-100)` | `--pt-cn-color-neutral-50` | `--pt-cn-radius-sm` (18) | 32 | **none** |
| Featured `.is-featured` | Gradient rim (§11.1 C) | same `neutral-50` | inherit | 32 | **none** |

- **No hover lift** on card-row items.
- Interior **solid `neutral-50`** — no inset grey feature blocks.
- **≤1** `.is-featured` per row; rim `--pt-cn-gradient-2` or `--pt-cn-gradient-1`.

#### Internal anatomy — R9 three zones

**ZONE A** — name (`semibold` `body-lg`) + optional `Hot` pill; price `title-lg` bold + `body-sm` period; meta `body-sm` `neutral-650`.

**ZONE B** — full-width pill; `btn--secondary` default · `btn--primary` on featured only.

**ZONE C** — `border-top 1px line-100`; §8.16 icon rows; nested bullets `body-sm` `neutral-650` with 3 px primary dot — icons: `check-mark-outlined`, `notification-outlined`, `sparkle-outlined`.

#### Featured vs default

| Element | Default | `.is-featured` |
|---------|---------|----------------|
| Border | `line-100` | Gradient rim |
| CTA | `btn--secondary` | `btn--primary` |

#### Anti-patterns

❌ shadow / hover lift · grey feature sub-cards · panel-as-card outer wrap · mixed 3+4 columns · two featured cards · `btn--outline` as row CTA

#### Checklist

- [ ] Pattern A head; optional §8.4 toggle
- [ ] 3-up or 4-up §7 grid; stretch; gap 24
- [ ] `neutral-50`, `radius-sm`, pad 32, shadow none
- [ ] R9 + §8.16; CTA secondary / featured primary

### 4.5 Media duo floor — visual 2-up, borderless cards  ★

**视觉配图横排：** 1 行 **2 列**，无描边、无阴影；上大圆角配图帧，下左对齐文案 + **文字链 CTA**。参考：**Become an agent builder**（Agent builder · Agents SDK）。

```
┌── canvas neutral-50 ────────────────────────────────────────────────┐
│        h2 居中  "Become an **agent builder**"（复合标题可 ≤2 渐变词）   │
│        subtitle  body-lg  neutral-750  居中                          │
│  ┌─ media-duo-item 无边框 ─────────────┐  ┌─ media-duo-item ──────┐ │
│  │ ┌─ media-duo-visual radius-md ────┐ │  │ ┌─ visual ──────────┐ │ │
│  │ │ 配图/视频  cover  左上 20px 图标 │ │  │ │  …                │ │ │
│  │ └──────────────────────────────────┘ │  │ └───────────────────┘ │ │
│  │ 标题 title-md 左对齐                  │  │  Agents SDK           │ │
│  │ 描述 body-md 2行 clamp neutral-650   │  │  …                    │ │
│  │ 立即开始 ↗  文字链 CTA               │  │  查看文档 ↗ 紫色      │ │
│  └──────────────────────────────────────┘  └───────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

**与 §4.4 区别：** §4.4 是带 `line-100`/渐变 rim 的价目卡 + 全宽 pill 按钮；§4.5 **整卡无描边**，靠配图圆角与留白分区，CTA 为 **文字链**。

#### 用法

- 产品能力双列（Builder + SDK、双工作流、双集成）
- 非定价 SKU（定价用 §4.4）

#### 网格

```scss
.media-duo-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
  align-items: start;                                    // 非等高拉伸
}
```

≤1024 px：`1fr` 纵排，gap 18。

#### 卡片外壳 — 无描边、无阴影

```scss
.media-duo-item {
  display: flex;
  flex-direction: column;
  background: transparent;
  border: 0;
  box-shadow: none;
  padding: 0;
}
```

#### 三区（R10）

**ZONE 1 `.media-duo-visual`** — `radius-md` (24)，`aspect-ratio: 16/10` 或 h **248–280**，`object-fit: cover`，**无边框无阴影**；左上 **20×20** 白色/浅色图标；可选 pathway 装饰标签 ≤ `caption-sm` mono。

**ZONE 2 `.media-duo-body`** — `margin-top: 20–24`；**左对齐**，与配图左缘对齐：
- `.media-duo-title`: `title-md` semibold `neutral-950`
- `.media-duo-desc`: `body-md` `neutral-650`，**2 行 clamp**，`margin-top: 12`

**ZONE 3 `.media-duo-link`** — 非 pill；`inline-flex` + `arrow-up-right-outlined` 14px；`margin-top: 16–20`；默认 `neutral-950` → hover `primary-550`；第二卡可用 `.is-accent` 紫色静息。

#### 反模式

❌ 给 item/visual 加 `line-100` 或阴影 · 配图下用 `btn--primary/secondary` 全宽按钮 · 文案居中 · 标题压在照片上 · 灰底包裹文案区 · 同行第 3 列

#### Checklist

- [ ] Pattern A 头；2 列 gap 18，`align-items: start`
- [ ] item/visual：**border 0, shadow none**；visual `radius-md`
- [ ] 文案左对齐；CTA 文字链 + `arrow-up-right-outlined`

### 4.6 Simple card floor — skill / step / model showcase  ★

**简洁卡片楼层：** `line-100`、**无阴影**、`neutral-50` 纯色内底；`step-tag` · `price-text` · `modality-chip` · metrics 纵向组合。参考：**Ready to Grow Together**（步骤 3 卡 + 楼层 CTA）、**Qwen 模型推荐行**。

#### 变体

| 变体 | 钩子 | 列数 | 圆角 | 内边距 | 卡内 CTA | 楼层 CTA |
|------|------|------|------|--------|----------|----------|
| **A 步骤流** | `.floor--step-cards` | 3-up | `radius-md` | 32 | 无 | 居中 `btn--primary` |
| **B 技能/模型** | `.floor--skill-cards` | 3-up | `radius-sm` | 24 | 可选文字链 | 无 |

共用：`1px line-100`、`shadow: none`、**无 hover 上浮**（营销页）。

#### 网格

```scss
.simple-card-grid {
  display: grid;
  gap: 24px;
  align-items: stretch;
}
.simple-card-grid--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.simple-card-grid--3.is-asymmetric {
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 1fr) minmax(0, 1fr);
}
```

≤1024 px：`1fr`，gap 18。

#### 卡片外壳

```scss
.simple-card {
  background: var(--pt-cn-color-neutral-50);
  border: var(--pt-cn-line-size-normal) solid var(--pt-cn-color-line-100);
  border-radius: var(--pt-cn-radius-sm);
  padding: 24px;
  box-shadow: none;
  &:hover { box-shadow: none; transform: none; }
}
.simple-card--step {
  border-radius: var(--pt-cn-radius-md);
  padding: 32px;
}
```

无渐变 rim（留给 §4.4）。Hot 用 `tag-hot` pill，不用渐变描边。

#### A — 步骤卡（R12）

1. `.step-tag` §8.17  
2. `.simple-card-title` `title-md` semibold，`mt 16`  
3. `.simple-card-desc` `body-md` `neutral-650`，`mt 12`  
4. 楼层下居中 `.simple-card-floor-cta` → `btn--primary`

#### B — 技能/模型卡（R11）

1. 名称 `body-lg` semibold + 可选 `tag-hot`  
2. 描述 `body-sm` 2 行 clamp  
3. `.simple-card-chips` §8.19  
4. `.simple-card-price` §8.18  
5. `border-top line-100`  
6. 2 列 metrics：`title-sm` + `body-sm` label  

控制台 marketplace 的 hover-reveal（§17.7）不用于营销 skill 楼层。

#### 反模式

❌ 阴影/hover 上浮 · §4.4 渐变 rim · 步骤卡内 Subscribe · 价目区灰底盒子 · 外层 panel-as-card · A/B 混排

#### Checklist

- [ ] A 或 B 二选一；`line-100` + shadow none  
- [ ] A：`step-tag` + 楼层 `btn--primary`  
- [ ] B：R11 + §8.18 price-text + §8.19 chips

### 4.7 Secondary showcase floor — text-only cards  ★

**次级信息楼层**，衬托主楼层。共享 `.text-card`：**无 bg/描边/阴影**，**仅** `border-bottom: 1px line-100`。

| 变体 | 参考 | 标题 | 筛选 | 底栏 |
|------|------|------|------|------|
| **A 带 tabs** | Model serving **industries** | Pattern B，一词渐变 | §8.20 tabs | 可选 `btn--outline` |
| **B 无 tabs** | **AI and Cloud** / Solutions For All Your Needs | 双行左对齐 §4.7 | 无 | §8.22 圆钮分页 ‹ › |

```
A: h2 → tabs → text-card×4 → [Browse all]
B: 渐变行1 + 黑字行2 → text-card×4 (R13b) → ( ‹ › ) pager
```

#### 共享网格与外壳

```scss
.text-card-grid { display: grid; gap: 24px 32px; align-items: start; }
.text-card-grid--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.text-card {
  padding: 0 0 24px; background: transparent; border: 0; box-shadow: none;
  border-bottom: 1px solid var(--pt-cn-color-line-100); border-radius: 0;
}
```

#### 变体 A

§8.20 tabs → **R13**（icon+名 / 描述 / 可选 chip / ↗）→ 可选 `btn--outline`。

#### 变体 B — 无 tabs

**双行左标题** `.floor-head--stacked-left`：

- 行 1：整行渐变字（如「AI and Cloud」）  
- 行 2：实心黑字（如「Solutions For All Your Needs」）  

**R13b 极简卡** `.text-card--minimal`：标题 → 描述 → ↗（无 icon 行、无 chip）。

**分页** §8.22 `.text-card-pager`：底部居中两枚 **40px 圆钮**，`line-100` 描边、透明底、无阴影；`chevron-left/right-outlined` 16px。与 `btn--outline` **二选一**。

#### 反模式

❌ 四边描边卡 · B 变体加 tabs · 同时 pager + outline 按钮 · 黑色 primary 底栏

#### Checklist

- [ ] 选 A **或** B  
- [ ] text-card 仅 bottom `line-100`  
- [ ] A：tabs + R13 · B：双行头 + R13b + pager

### 4.8 Logo floor — 矩阵描边 / 无边透明条  ★

信任/合作伙伴轻楼层。每页 **二选一**：

| 变体 | 参考 | 布局 | 外壳 |
|------|------|------|------|
| **A 描边矩阵** | Supported AI Tools | 4×N 网格；icon + 名称 | 仅 `line-100` |
| **B 无边透明条** | **Our Partners** | 1×N 横排 Logo | **无** 描边/底/阴影 |

共享：Pattern A 居中标题 + 副标题（A 可选 §8.23 链）。

---

#### 变体 A — 描边矩阵

```
副标题… [Learn More ↗]
┌─────────┐×4  gap 12  h 64
│[icon] Name│  line-100 · radius-xs · no shadow
└─────────┘
```

`repeat(4, 1fr)` · gap **12** · h **64**。≤1024：`2` 列。

```scss
.logo-matrix-tile {
  display: flex; align-items: center; gap: 12px;
  height: 64px; padding: 0 16px 0 20px;
  background: transparent;
  border: 1px solid var(--pt-cn-color-line-100);
  border-radius: var(--pt-cn-radius-xs);
  box-shadow: none;
  &:hover { border-color: var(--pt-cn-color-line-200); }
}
```

**R14** — icon 24 + 名 `body-sm` medium；等同 `.coding-plan-tools-item`。

---

#### 变体 B — 无边透明 Logo 条

参考：**Our Partners** — 副标题「Organizations supporting the hackathon community.」+ 横排彩色品牌标，**直接落在画布上**。

```
        Our Partners
  Organizations supporting…
        ↓ 48–64px
  [logo]  [logo]  [logo]  [logo]  [logo]  [logo]
  flex 居中 · 保留品牌色 · 共用垂直中线
```

```scss
.logo-strip {
  display: flex; flex-wrap: wrap;
  align-items: center; justify-content: center;
  gap: clamp(32px, 6vw, 64px) clamp(24px, 5vw, 56px);
}
.logo-strip-item {
  padding: 0; background: transparent;
  border: 0; box-shadow: none;
  &:hover { transform: none; border: 0; background: transparent; }
}
.logo-strip-item__logo {
  height: 40px; max-height: 48px; max-width: min(160px, 28vw);
  width: auto; object-fit: contain;
}
```

| 规则 | 值 |
|------|-----|
| 外壳 | **无** border / bg / shadow |
| Logo | 高 **40–48px**，宽自适应；**保留品牌色** |
| Hover | 链接可选 `opacity` 变化 only |
| 间距 | 标题 → 条 **48–64px**；logo 间 `clamp(32px, 6vw, 64px)` |

**R19** — 纯 Logo 项；**无** 下方文字名（有名称用变体 A）。

#### 反模式

❌ B 变体给 logo 加 line-100 方框 · A/B 混排 · 阴影/灰底条 · 强制等宽方格压扁 wordmark

#### Checklist

- [ ] 选 **A** 或 **B**（不同楼层可各用一种）
- [ ] **A：** 4 列 h64 R14 · **B：** `.logo-strip` R19 无边透明

### 4.9 Tail visual CTA floor — 尾部大视觉  ★

页末最后一个营销楼层，紧接 `.page-footer`。`.layout-max-wide` 内单块大圆角面板，**居中标题 + 副标题 + 行动按钮**叠在抽象渐变 / `qwen-model-*` / 轻视频上。参考：**Co-Build Future · AI-Powered Era**（790 px）· **Join the community**（370 px）。适用 §2.5 例外（文案可压视觉）。

```
.tail-visual  radius-lg  h 790 | 370
  可选 kicker + 紫色内链 §8.25
  h2 居中 ≤1 个渐变词/短语
  副标题 body-lg
  [ btn--primary ]  [ btn--outline ]
        ↓ 无额外色带间隔
.page-footer §4.10
```

| 高度 | 场景 | 参考 |
|------|------|------|
| `.tail-visual--tall` **790px** | 首页收尾、时代感 campaign | Co-Build Future；两行 h2；Get API Keys + Try now |
| `.tail-visual--compact` **370px** | 社区、Hackathon、项目招募 | Join the **community**；单行 h2 + 短副标题 |

```scss
.tail-visual {
  position: relative; width: 100%;
  border-radius: var(--pt-cn-radius-lg);
  overflow: hidden; box-shadow: none;
  &--tall    { height: 790px; min-height: 790px; }
  &--compact { height: 370px; min-height: 370px; }
}
.tail-visual__content {
  position: relative; z-index: 1;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; height: 100%;
  padding: 48px 32px; gap: 16px;
}
```

- **R15** 内容栈：可选 `.tail-visual-kicker`（§8.25）→ h2（高版 72 / 紧凑 44）→ 副标题 `max-width: var(--pt-cn-layout-max-read-box)` → `.tail-visual-cta-row`（**L1 primary + L3 outline**，同 §2.7）
- 上一楼层间距 **96–122 px**；面板下 **无** 额外 padding — Footer 紧贴
- **禁止** 面板外再叠 Pattern A 楼层头；**禁止** 阴影、`line-100` 外框、`btn--secondary` 作次按钮

#### Checklist

- [ ] 每页至多一块；高 **790** 或 **370**
- [ ] R15 居中栈；≤1 渐变短语
- [ ] Footer 紧贴其下

### 4.10 Site footer floor — 页脚不均分  ★

`.page-footer` 为 `.page-shell` 最后节点。画布 `neutral-50`，无阴影、无卡片外壳。

```
35% 左侧                    65% 右侧
[X][GitHub][LinkedIn][Discord]   Products | Company | Resources
                                 各列：粗标题 + 链接列表
──────── line-100 ─────────────────────────────────────
© 2026 … 保留所有权利。              管理 Cookie
```

```scss
.page-footer-main {
  display: grid;
  grid-template-columns: minmax(0, 35fr) minmax(0, 65fr);
  gap: 48px 64px;
}
.page-footer-nav {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 32px 48px;
}
.page-footer-legal {
  margin-top: 48px; padding-top: 24px;
  border-top: 1px solid var(--pt-cn-color-line-100);
  display: flex; justify-content: space-between;
  font-size: var(--pt-cn-caption-font-size-sm);
  color: var(--pt-cn-color-neutral-550);
}
```

| 区域 | 规则 |
|------|------|
| **左侧 35%** `.page-footer-aside` | 横排社交 icon **20×20**，`neutral-950`，**无** 描边/底色/阴影（§8.24） |
| **右侧 65%** `.page-footer-nav` | **3 列**链接组（**R16**）：`body-sm` 粗标题 + 链接 `neutral-650` |
| **底栏** | 版权左对齐；「管理 Cookie」等右对齐 |

社交品牌标不在 manifest 时用 Tabler `brand-*`（20 px，`stroke: 1.5`）。≤1024：主栅格 `1fr`；链接 `2` 列；≤640：链接单列，底栏纵排。

#### 反模式

❌ 灰底 footer 色带 · 社交 icon 方框描边 · 50/50 均分 · footer 内 pill 主按钮

#### Checklist

- [ ] 35fr / 65fr；左社交 §8.24，右 R16 三列链
- [ ] 底栏 `line-100` 顶线；版权左、Cookie 右
- [ ] 有 §4.9 时紧贴其下

### 4.11 Interactive carousel toggle floor — 100vw 可切换横滑  ★

**可交互横滑楼层：** 标题在 **inner**；卡片轨道 **100vw 通栏** breakout。点击 **‹ ›**（§8.26）切换 — 无 autoplay/圆点/阴影。参考：**Judging Criteria**（左头 + 右上分页）· 证言横滑（居中头 + 底部分页）。

| 变体 | 参考 | 标题 | 分页位置 | 卡内 |
|------|------|------|----------|------|
| **A** | 证言 / quote 横滑 | Pattern A 居中 | 轨道下方居中 §8.26 | **R17** 证言卡 |
| **B** | Judging **Criteria** | 左对齐 + 副标题 | 标题行右上 §8.26 | **R18** 评分卡 |

#### 100vw 轨道

```scss
.carousel-floor-viewport {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  overflow: hidden;
}
.carousel-floor-track {
  display: flex; gap: 24px;
  padding-left: max(20px, calc((100vw - var(--pt-cn-layout-max-width)) / 2));
  padding-right: max(20px, calc((100vw - var(--pt-cn-layout-max-width)) / 2));
  transition: transform var(--pt-cn-motion-normal) ease;
}
```

首卡对齐 inner 左 gutter（同 §3G）；末卡右侧 **peek** 裁切。

#### `.carousel-card` 外壳（二选一，全轨统一）

```scss
.carousel-card {
  flex: 0 0 auto;
  border-radius: var(--pt-cn-radius-lg);
  padding: 32px;
  box-shadow: none;
  &--bordered {
    background: var(--pt-cn-color-neutral-50);
    border: 1px solid var(--pt-cn-color-line-100);
  }
  &--filled {
    background: var(--pt-cn-color-neutral-100);
    border: 0;
  }
}
```

卡宽：证言 `min(420px, 85vw)` · 评分 `min(380px, 80vw)`。

#### 变体 A / B

- **A：** 居中 h2（一词渐变）→ 轨道 R17（引号 icon · 正文 3–4 行 · 头像+姓名+职位）→ 底部分页
- **B：** `.carousel-floor-head-row`（`flex-end space-between`）左 head + 右 `.carousel-pager--head-inline` → 轨道 R18（大号 **30%** · 标题 · 圆点列表）

#### 反模式

❌ 阴影/上浮 · 同轨混用 bordered+filled · autoplay · 圆点指示器 · 与 §4.7 text-card 混排

#### Checklist

- [ ] 选 A 或 B；标题在 inner，轨道 100vw
- [ ] 全卡 `--bordered` 或 `--filled`；§8.26 ‹ ›
- [ ] R17 或 R18 内构

### 4.12 FAQ floor — 双栏手风琴  ★

左栏标题留白 + 右栏 **`+` 折叠列表**（§8.27：**默认第一项展开**，**始终仅一项打开**，互斥）。参考：**Frequently asked questions** + Learn More ↗。

| 外壳 | 背景 | 宽度容器 |
|------|------|----------|
| **A inner** | 楼层 `neutral-50`，无外包面板 | `.layout-max-inner` |
| **B 宽面板** | `.faq-panel` `neutral-100` `radius-lg` | `.layout-max-wide` |

```
左 ~38%                    右 ~62%
Frequently                 Q1  +
asked questions (渐变)     ─────
Learn More ↗               Q2  +  ← 展开时显示答案
                           Q3  +
```

```scss
.faq-layout {
  display: grid;
  grid-template-columns: minmax(200px, 38%) minmax(0, 1fr);
  gap: clamp(48px, 10vw, 120px);
}
.faq-panel {
  background: var(--pt-cn-color-neutral-100);
  border-radius: var(--pt-cn-radius-lg);
  padding: 60px 44px;
  box-shadow: none; border: 0;
}
```

#### `.faq-item`（R20）

- 行间仅 `border-bottom: line-100`；**无** 行级阴影/灰底卡
- 触发器：左 **问题** `body-md` semibold · 右 **`+`** `primary-550`；展开时 `+` **隐藏**
- 答案：`body-sm` `neutral-650`；`grid-template-rows: 0fr→1fr` 动画（§8.6）

#### §8.27 交互契约

| 规则 | 行为 |
|------|------|
| 初始 | **第一项** `.is-open` |
| 互斥 | 同时 **仅一项** 展开 |
| 点击已开项 | **不收起** — 须切换到另一题 |
| 键盘 | Enter/Space 切换 |

#### Checklist

- [ ] 外壳 A **或** B  
- [ ] `.faq-layout` 38/62；左 `.faq-head` + 右 `.faq-accordion`  
- [ ] §8.27 单开 + 默认首项；R20

### 4.13 Accordion + visual sync floor — 信息折叠 + 视觉联动  ★

居中标题 → **左 `+` 折叠列表** + **右大视觉**（随选中项 cross-fade）。参考：**Choose Your Arena** — MemoryAgent · EdgeAgent · AI Showrunner。

```
Choose Your Arena（居中）
左 ~42% 折叠列表          右 ~58% radius-lg 视觉
MemoryAgent            +    ┌─────────────────┐
──────────────────            │  cover media    │
AI Showrunner (open)          │  is-active      │
  描述 body-sm…               └─────────────────┘
```

| 对比 | §2.8 hero Mode B | §4.12 FAQ | **§4.13** |
|------|------------------|-----------|-----------|
| 位置 | `.hero-visual` 420px | 左标题+右问答 | 居中标题+左右分栏 |
| 右侧 | 同盒预览 | 无视觉 | **独立大视觉** |

```scss
.arena-sync-layout {
  display: grid;
  grid-template-columns: minmax(0, 42%) minmax(0, 1fr);
  gap: clamp(40px, 6vw, 64px);
}
.arena-sync-visual {
  position: relative;
  min-height: 400px;
  border-radius: var(--pt-cn-radius-lg);
  overflow: hidden;
  background: var(--pt-cn-color-neutral-100);
  box-shadow: none;
}
.arena-sync-visual-panel {
  position: absolute; inset: 0; opacity: 0;
  transition: opacity var(--pt-cn-motion-normal) ease;
  &.is-active { opacity: 1; }
}
```

- **R21** 左栏：与 R20 类似 — `line-100` 分割、标题 + `+`、`body-sm` 描述；`data-arena-panel="n"`
- **§8.28**：互斥单开（同 §8.27）+ 同步 `.arena-sync-visual-panel[data-panel="n"].is-active`
- 容器：**`.layout-max-inner`**；首项与首面板默认展开
- 移动：手风琴在上，视觉在下 `min-height 280–320px`

#### Checklist

- [ ] Pattern A 居中标题 + `.arena-sync-layout` 42/58  
- [ ] §8.28 折叠与视觉联动；R21  
- [ ] 视觉 `radius-lg`、无阴影；非 §2.8 hero 内嵌

---

## 5. Floor-head patterns (section headers)

Three patterns. Choose by section role; don't blend.

### Pattern A — Centered head  *(most floors)*

```scss
.<floor>-head {
  display: flex; flex-direction: column;
  align-items: center; gap: 16px;
  text-align: center;
  margin-bottom: 48px;

  .eyebrow {                                             // optional kicker
    font-family: var(--pt-cn-font-mono);
    font-size: var(--pt-cn-caption-font-size-sm);           // 12
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--pt-cn-color-neutral-600);
  }
  h2 {
    font-size: var(--pt-cn-heading-font-size-md);           // 44
    line-height: var(--pt-cn-heading-line-height-md);
    font-family: var(--pt-cn-font-bold);
    letter-spacing: var(--pt-cn-letter-spacing-tight);
    color: var(--pt-cn-color-neutral-950);
    margin: 0;
  }
  .heading-desc {                                        // subtitle
    margin: 0;
    color: var(--pt-cn-color-neutral-750);
    font-size: var(--pt-cn-body-font-size-lg);
    line-height: var(--pt-cn-body-line-height-lg);
    max-width: 620px;                                    // ← see §9.4 width caps
  }
}
```

One `<span>` inside `h2` may clip a gradient (`--pt-cn-gradient-1…8`). Max one gradient word per screen.

### Pattern B — Left-aligned head  *(analyst, reliability, industry blocks, models hero D)*

Same typography; flex-start alignment. Right side carries a one-line description, link list, or CTA.

```scss
.<floor>-head {
  display: flex; justify-content: space-between; align-items: flex-end;
  gap: 48px;
  margin-bottom: 52px;

  h2 { max-width: 760px; }                               // wrap point
  .head-meta {                                           // right slot
    flex: 0 0 auto;
    font-size: var(--pt-cn-body-font-size-md);
    color: var(--pt-cn-color-neutral-650);
  }
}
```

### Pattern C — Two-column panel head  *(faq, ai-powered-product)*

左标题 + 右内容双栏。营销 FAQ 完整规范见 **§4.12**（外壳 A/B、§8.27 互斥单开）。下文为 legacy 渐变 wash 面板配方。

```scss
.<floor>-panel {
  background: var(--pt-cn-gradient-card-bg);
  border-radius: var(--pt-cn-radius-md);
  padding: 60px 44px;
  display: grid;
  grid-template-columns: minmax(240px, 320px) minmax(0, 1fr);
  gap: 64px;                                             // or 154 px for very airy faq
}
.<floor>-panel h2 { font-size: var(--pt-cn-heading-font-size-sm); }   // 36
```

Mobile: collapse to 1 column; padding → `32 20`; gap → 32.

### Pattern D — Asymmetric "skill" head  *(organic skills page; ref pattern)*

Grid `1fr 6fr; gap: 120px` inside inner. Left column = mono meta label. Right column = h1 + inline install/command block.

---

## 6. Reader column  *(legal, docs body, skills-detail body)*

Centered narrow column for long-form text. **Width = `min(100%, var(--pt-cn-layout-max-read-box))` = 640 px.**

```scss
.legal-main-wrap     { padding-top: 108px; }             // 36 ≤640 px
.legal-main          { width: min(100%, var(--pt-cn-layout-max-read-box));
                       margin: 0 auto 160px; }
.legal-page-title    { font-size: var(--pt-cn-heading-font-size-sm);  // 36
                       font-family: var(--pt-cn-font-bold);
                       margin: 48px 0 32px; }
.legal-subtitle      { font-size: var(--pt-cn-title-font-size-md);    // 24
                       font-family: var(--pt-cn-font-semibold);
                       margin-top: 48px; }
.legal-subsubtitle   { font-size: var(--pt-cn-title-font-size-sm);    // 20
                       font-family: var(--pt-cn-font-semibold);
                       margin-top: 28px; }
.legal-paragraph     { font-size: var(--pt-cn-body-font-size-md);
                       line-height: var(--pt-cn-body-line-height-md);
                       color: var(--pt-cn-color-neutral-650);
                       margin-top: 16px; }
.legal-list li::before { width: 3px; height: 3px;
                         background: var(--pt-cn-color-primary-550); }
.legal-note          { background: var(--pt-cn-color-neutral-150);
                       border-radius: var(--pt-cn-radius-xs);
                       padding: 16px; }
```

No side TOC. Tables use `border-bottom: var(--pt-cn-line-size-normal) solid var(--pt-cn-color-line-200)` on header rows. Code blocks `background: var(--pt-cn-color-neutral-100); border-radius: var(--pt-cn-radius-xs); padding: 16px`.

---

## 7. Grid systems

All grids snap to a small set of column×gap combinations. Pull from one row of the table; don't invent.

| Block | Columns | Gap (px) | Notes |
|-------|---------|---------:|-------|
| Featured model stack | 1 (stacking-card) | 14 | Inside the card: 2-col flex, main `flex: 0 0 45%` |
| **Media duo / agent-builder** | `repeat(2, minmax(0,1fr))` | 18 | Borderless; `align-items: start`; §4.5 |
| Industry / quick cards | `repeat(4, minmax(0,1fr))` | 36 | Mobile → 1fr; gap 18 |
| Analyst (asymmetric 2/1/1) | `2fr 1fr 1fr` | 24 | Mobile → 1fr; gap 16 |
| Reliability 2×2 | `repeat(2, minmax(0,1fr))` | col 114 / row 64 | Each item itself `100px 1fr; gap 48` |
| **Partner logo strip** (无边) | flex center 或 `repeat(6–8, 1fr)` | `clamp(32px, 6vw, 64px)` | §4.8 **变体 B** |
| Customer logo strip (legacy) | `repeat(7, minmax(0,1fr))` | `6vw` | 优先 §4.8 B flex |
| Pricing offer (centered 2-up) | `repeat(2, clamp(320px, 30vw, 400px))` | 24 | `justify-content: center` |
| **Card row 3-up** (pricing / prize) | `repeat(3, minmax(0, 1fr))` | 24 | Equal stretch; §4.4; no shadow |
| **Card row 4-up** (token / credit plans) | `repeat(4, minmax(0, 1fr))` | 24 | + optional §8.4 toggle; §4.4 |
| **Simple card 3-up** (step / skill) | `repeat(3, minmax(0, 1fr))` | 24 | `line-100`, no shadow; §4.6 |
| **Simple card 2-up** (step pair) | `repeat(2, minmax(0, 1fr))` | 24 | §4.6 variant A |
| **Text-card 4-up** (secondary) | `repeat(4, minmax(0, 1fr))` | 24 / 32 | Bottom line-100 only; §4.7 |
| **Text-card 3-up** (secondary) | `repeat(3, minmax(0, 1fr))` | 24 / 32 | §4.7 |
| **Logo matrix** | `repeat(4, minmax(0,1fr))` | 12 | §4.8 **变体 A** |
| Tools / logo tiles | `repeat(4, minmax(0,1fr))` | 12 | `.coding-plan-tools-item` = §4.8 A |
| **Site footer nav** | `repeat(3, minmax(0, 1fr))` in 65% col | 32 / 48 | §4.10 R16 |
| **Site footer main** | `35fr 65fr` | 48 / 64 | §4.10 |
| **Carousel toggle track** | flex 横滑；卡宽 380–420 | 24 | 100vw breakout · §4.11 |
| **FAQ 双栏** | `38% 1fr` `.faq-layout` | 48–120 | §4.12 |
| **Arena sync** | `42% 1fr` `.arena-sync-layout` | 40–64 | §4.13 |
| Models marketplace | `repeat(auto-fill, minmax(260px, 1fr))` | 24 | Card 340-px tall, `--pt-cn-radius-sm` |
| Models compare | `repeat(3, minmax(0,1fr))` | 24 | Mobile → 1fr |
| Models detail io / context | `repeat(2, minmax(0,1fr))` | 12 | ≤1280 → 1fr |
| Customer stories 2×2 | `repeat(2, minmax(0,1fr))` | 24 | Full-bleed image cards |
| Docs cards | `repeat(2, minmax(0,1fr))` | 16 | Mobile → 1fr |
| Hero metric overlay | `repeat(4, minmax(0,1fr))` | `clamp(16px, 3vw, 40px)` | Inside hero panel; small text only |
| Hero image grid (showcase) | `repeat(3, …)` × 2 rows | 16 | `16:10` aspect |

**Universal mobile rule** (≤1024 px): collapse to `1fr` unless density is essential. Gaps step down one bucket: 36 → 18, 24 → 18, 18 → 14, 14 → 12.

---

## 8. Sub-block vocabulary

The repeating small pieces that compose floors. Use this vocabulary inside cards/heroes; don't reinvent.

### 8.1 Hero metric chip (the only "text over imagery" permitted)

```
display: grid;
grid-template-columns: 12px 1fr;
column-gap: 12px; row-gap: 2px;
```

- Dot 6×6 px, `border-radius: 999px`, color from `--pt-cn-color-accent-{mint|orchid|electric-blue|rose|emerald|apricot|sky}`
- `strong`: `--pt-cn-title-font-size-lg` (28), `--pt-cn-font-semibold`
- `small`: `--pt-cn-body-font-size-md`, color `--pt-cn-color-neutral-550`
- Symbols (`+`, `<`, `%`) render as sibling `<span>`

Used in: home hero overlay (4-up), signup brand panel.

### 8.2 Chip / tag pill

```
display: inline-flex; align-items: center;
padding: 8px 12px;
border-radius: var(--pt-cn-radius-full);
font-size: var(--pt-cn-body-font-size-sm);
background: var(--pt-cn-color-neutral-150);
color: var(--pt-cn-color-neutral-700);
```

Active: `background: var(--pt-cn-color-primary-50); color: var(--pt-cn-color-primary-550)`. No border on filled; outline variant uses `--pt-cn-color-line-200`.

### 8.3 Pill tab (with leading dot when active)

Same pill shape. Active tab gets a 6-px primary dot rendered as `::before { margin-right: 6px }`.

次级楼层 flat tabs → **§8.20**（5px 圆点 + `neutral-150` active）。

### 8.4 Pill segmented control

```
height: 36–40px;
padding: 4–6px;
border-radius: var(--pt-cn-radius-full);
background: var(--pt-cn-color-neutral-150);
display: inline-flex; gap: 4px;
```

Selected child: `background: var(--pt-cn-color-neutral-50); box-shadow: var(--pt-cn-shadow-light); border-radius: var(--pt-cn-radius-full)`.

### 8.5 Underline sub-nav

```
display: inline-flex; gap: 32px;
border-bottom: var(--pt-cn-line-size-thin) solid var(--pt-cn-color-line-100);
```

Active tab: `position: relative; &::after { content:''; position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: var(--pt-cn-color-primary-550) }`.

### 8.6 Accordion item

```
.content {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition: grid-template-rows var(--pt-cn-motion-fast) ease-in-out,
              opacity var(--pt-cn-motion-fast) ease-in-out;
}
.is-open .content { grid-template-rows: 1fr; opacity: 1; }
```

Item divider: `border-bottom: var(--pt-cn-line-size-normal) solid var(--pt-cn-color-line-200)`; padding `40px 0`. Plus-icon button hidden in expanded state.

### 8.7 Inline command / code box

```
padding: 16px;
border-radius: var(--pt-cn-radius-xs);
background: var(--pt-cn-color-neutral-100);
min-height: 44px;
gap: 8px;
font-family: var(--pt-cn-font-mono);
font-size: var(--pt-cn-body-font-size-sm);
```

Trailing copy button: `flex: 0 0 auto`, icon-only (`copy-outlined`).

### 8.8 Inline notice

```
margin-top: 24px;
padding: 16px;
border-radius: var(--pt-cn-radius-xs);
background: var(--pt-cn-color-supporting-{blue|orange|green|red}-bg);
display: flex; gap: 12px;
```

Icon at start (12 px), text fills rest.

### 8.9 Section divider line

`border-bottom: var(--pt-cn-line-size-normal) solid var(--pt-cn-color-line-200)`. Use for accordion items and intra-card metric rows — **never as floor boundaries** (use whitespace + bg step instead).

### 8.10 Sticky compare bar (overlay)

```
position: fixed; left: 50%; bottom: 24px;
transform: translateX(-50%);
padding: 24px 32px;
border-radius: var(--pt-cn-radius-md);
background: var(--pt-cn-color-neutral-50);
box-shadow: var(--pt-cn-shadow-light);
backdrop-filter: blur(10px);
z-index: 1000;
```

### 8.11 Search input — pill with gradient focus ring

Nav-style.

```
height: 48px;
padding: 0 16px 0 14px;
border: 1px solid var(--pt-cn-color-line-200);
border-radius: var(--pt-cn-radius-full);
background: var(--pt-cn-color-neutral-50);
font-size: var(--pt-cn-body-font-size-sm);
```

Focus: `border-color: transparent`, plus a 1-px gradient ring drawn with `::before { background: var(--pt-cn-gradient-4); -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); mask-composite: exclude }`. Width default 228 px, expand-on-focus to 490 px.

Leading icon: `search-outlined`. Trailing: `command-outlined` (⌘K), small mono caption-md.

### 8.12 Dropdown / collapsible group

```
.dropdown {
  border-radius: var(--pt-cn-radius-sm);
  background: var(--pt-cn-color-neutral-50);
}
.dropdown-trigger {
  width: 100%; min-height: 48px;
  padding: 0 16px;
  display: flex; align-items: center; justify-content: space-between;
  color: var(--pt-cn-color-neutral-850);
  font-size: var(--pt-cn-body-font-size-sm);
  font-family: var(--pt-cn-font-semibold);
  background: transparent; border: 0;
}
.dropdown-trigger svg { width: 16px; transition: transform var(--pt-cn-motion-fast) ease; }
.dropdown.is-open .dropdown-trigger svg { transform: rotate(90deg); }     // or 180° for chevron-down
.dropdown-content {
  padding: 0 14px 14px;
  color: var(--pt-cn-color-neutral-750);
  font-size: var(--pt-cn-body-font-size-sm);
  line-height: var(--pt-cn-body-line-height-sm);
}
```

Use for: docs sidebar groups, filter groups, mobile-collapsed sections.

### 8.13 Floating search dropdown panel

```
position: absolute;                                      // anchored under nav search
margin-top: calc(var(--pt-cn-nav-backdrop-offset) + 20px);
max-height: min(560px, calc(100vh - var(--pt-cn-nav-backdrop-offset) - 32px));
padding: 12px;
border-radius: var(--pt-cn-radius-md);
background: var(--pt-cn-color-neutral-50);
box-shadow: var(--pt-cn-shadow-light);
overflow: auto;
```

Result items: 48-px-tall rows, padding `8px 12px`, hover bg `--pt-cn-color-neutral-100`, `border-radius: var(--pt-cn-radius-xs)`.

### 8.14 Breadcrumb row

```
display: inline-flex; align-items: center; gap: 8px;
font-size: var(--pt-cn-body-font-size-sm);
color: var(--pt-cn-color-neutral-650);
```

Separator: `chevron-right-outlined` 12 px, color `--pt-cn-color-neutral-450`. Last segment color `--pt-cn-color-neutral-950`.

### 8.15 Stat / kv row inside cards

```
display: grid;
grid-template-columns: minmax(0, auto) 1fr;
column-gap: 8px;
font-size: var(--pt-cn-body-font-size-sm);
```

Key (left): color `--pt-cn-color-neutral-650`. Value (right): color `--pt-cn-color-neutral-950`, mono if numeric.

### 8.16 Icon + text feature row  *(inside card-row ZONE C)*

Typography carries hierarchy — **no grey boxes.**

```
display: grid;
grid-template-columns: 16px 1fr;
column-gap: 12px;
align-items: start;
```

```scss
.card-feature-row {
  display: grid;
  grid-template-columns: 16px minmax(0, 1fr);
  column-gap: 12px;
  align-items: start;
  margin-bottom: 14px;

  .card-feature-icon {
    width: 16px; height: 16px; margin-top: 2px;
    color: var(--pt-cn-color-neutral-750);
  }
  .card-feature-text {
    font-size: var(--pt-cn-body-font-size-md);
    font-family: var(--pt-cn-font-semibold);
    color: var(--pt-cn-color-neutral-950);
  }
  .card-feature-sub {
    margin-top: 4px;
    font-size: var(--pt-cn-body-font-size-sm);
    color: var(--pt-cn-color-neutral-650);
    font-family: var(--pt-cn-font-regular);
  }
}
```

Nested list: `padding-left: 14px`; 3 px `primary-550` dot `::before`; `body-sm` `neutral-650`.

Icons: `check-mark-outlined`, `notification-outlined`, `sparkle-outlined` (manifest). Used in §4.4 ZONE C, `components.md` §07.

### 8.17 Step tag pill  *(§4.6 A)*

```scss
.step-tag {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 12px;
  border-radius: var(--pt-cn-radius-full);
  background: var(--pt-cn-color-primary-50);
  font-size: var(--pt-cn-body-font-size-sm);
  font-family: var(--pt-cn-font-medium);
  color: var(--pt-cn-color-neutral-800);
  &::before {
    content: ''; width: 6px; height: 6px; border-radius: 999px;
    background: var(--pt-cn-color-primary-550);
  }
}
```

### 8.18 Price-text row  *(§4.6 B)*

```scss
.simple-card-price {
  display: flex; flex-wrap: wrap; gap: 8px 16px; margin-top: 12px;
  font-size: var(--pt-cn-body-font-size-sm);
  font-family: var(--pt-cn-font-mono);
  color: var(--pt-cn-color-neutral-650);
}
```

无灰底包裹。与 `ui-price-text` 语义一致。

### 8.19 Modality chip

```scss
.modality-chip {
  padding: 6px 10px; border-radius: var(--pt-cn-radius-full);
  border: 1px solid var(--pt-cn-color-primary-150);
  background: transparent;
  font-size: var(--pt-cn-body-font-size-sm);
  color: var(--pt-cn-color-primary-550);
}
.simple-card-chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
```

单行展示，超出 `+N`。

### 8.20 Secondary tabs  *(§4.7)*

`.secondary-tabs` / `.secondary-tab` — inactive 透明；active `neutral-150` + **5px** `primary-550` 圆点。无轨道、无阴影。详见 §4.7。

### 8.21 Text-card link affordance

`.text-card-link` + `arrow-up-right-outlined` 14px；`margin-top: auto`；hover `primary-550`。整卡可包 `<a class="text-card">`。

### 8.22 Text-card carousel pager  *(§4.7 变体 B)*

```scss
.text-card-pager {
  display: flex; justify-content: center; gap: 12px; margin-top: 48px;
}
.text-card-pager-btn {
  width: 40px; height: 40px; border-radius: var(--pt-cn-radius-full);
  border: 1px solid var(--pt-cn-color-line-100);
  background: transparent; box-shadow: none;
  color: var(--pt-cn-color-neutral-550);
  &:disabled { opacity: 0.4; }
}
```

`chevron-left-outlined` / `chevron-right-outlined` 16px。

### 8.23 Floor-head subtitle inline link  *(§4.8)*

`.floor-head-link-desc` 居中 `body-lg` `neutral-750` + `.floor-head-inline-link` `primary-550` + `arrow-up-right-outlined` 12px。

### 8.24 Site footer social row  *(§4.10)*

`.page-footer-social` — icon **20×20**，`neutral-950`，gap **16–20**，无描边/底/阴影。Tabler `brand-x` / `brand-github` / `brand-linkedin` / `brand-discord`。

### 8.25 Tail-visual kicker  *(§4.9)*

`.tail-visual-kicker` — `body-md` `neutral-750`；紫色行动复用 `.floor-head-inline-link`（§8.23），非 pill。

### 8.26 Carousel toggle pager  *(§4.11)*

`.carousel-pager` + `.carousel-pager-btn` — 40px 圆钮，`line-100` 描边、无阴影。`chevron-left/right-outlined` 16px。

| 位置 | 类名 |
|------|------|
| 轨道下方居中 | `.carousel-pager--centered`（变体 A） |
| 标题行右上 | `.carousel-pager--head-inline`（变体 B） |

**Next** 强调态：`.carousel-pager-btn--next` — `neutral-950` 实心底 + 浅色 icon（有更多页时）。禁用态 `opacity: 0.4`。无圆点轨道。

### 8.27 FAQ accordion — 互斥单开  *(§4.12)*

`.faq-accordion` / `.faq-item`：**首项默认展开**；点击它项时关闭其余；**不允许全部收起**；`+` 展开后隐藏（非旋转 ×）。与 §2.8 hero、**§4.13** `.arena-sync-*` 区分。

### 8.28 Arena sync — 折叠 + 视觉联动  *(§4.13)*

在 §8.27 基础上：`data-arena-panel="n"` ↔ `.arena-sync-visual-panel[data-panel="n"]`；切换项时 cross-fade 右栏；`aria-live="polite"`。

---

## 9. Typography arrangement

### 9.1 Heading scale (where each size lives)

| Token | px | Role |
|-------|---:|------|
| `--pt-cn-heading-font-size-3xl` | 96 | Ultra-marketing hero (rare; e.g. organic home `clamp(72, 10vw, 168)`) |
| `--pt-cn-heading-font-size-2xl` | 72 | Marketing hero h1 (variant B), closing CTA h2 |
| `--pt-cn-heading-font-size-xl`  | 64 | Tagline split hero (variant A), asymmetric skill hero (variant I) |
| `--pt-cn-heading-font-size-lg`  | 60 | Centered intro hero (variant C) |
| `--pt-cn-heading-font-size-md`  | 44 | Section heads (pattern A/B), marketplace hero (variant D) |
| `--pt-cn-heading-font-size-sm`  | 36 | Legal page title, docs hero, sub-page h1, panel-head (pattern C) |
| `--pt-cn-title-font-size-lg`    | 28 | Card title, hero metric strong, sub-section title |
| `--pt-cn-title-font-size-md`    | 24 | Card title (compact), legal subtitle |
| `--pt-cn-title-font-size-sm`    | 20 | List item title, legal sub-subtitle |

All headings use `--pt-cn-font-bold` (or `--pt-cn-font-semibold` for titles) and `--pt-cn-letter-spacing-tight`. Line-height is locked to each size via `--pt-cn-{heading|title}-line-height-*` — don't override.

### 9.2 Body scale

| Token | px / lh | Role |
|-------|--------:|------|
| `--pt-cn-body-font-size-lg` | 18 / 24 | Hero subtitle, section subtitle, lead paragraph |
| `--pt-cn-body-font-size-md` | 16 / 22 | Body |
| `--pt-cn-body-font-size-sm` | 14 / 20 | Card meta, filter labels, chips, dropdown items |
| `--pt-cn-body-font-size-xs` | 13 / 18 | Caption mono, table cell, micro UI |
| `--pt-cn-caption-font-size-sm` | 12 / 16 | Eyebrow / uppercase mono kicker, breadcrumb separator label |

Body uses `--pt-cn-font-regular`; mono `--pt-cn-font-mono`. Body letter-spacing: `--pt-cn-letter-spacing-loose` (0.02em).

### 9.3 Type pairing by surface

| Surface | Title | Sub | Body |
|---------|-------|-----|------|
| Hero variant B | 2xl / 3xl | body-lg | — |
| Hero variant A/I | xl | body-lg | — |
| Hero variant C | lg | body-lg | — |
| Hero variant D/G | md | body-md | — |
| Section head A/B | md | body-lg | — |
| Section head C | sm | body-md | — |
| Card | title-lg or title-md | — | body-sm |
| Legal page | sm | title-md | body-md |
| Eyebrow / kicker | caption-sm mono uppercase | — | — |

### 9.4 Subtitle width caps

Subtitles never run wider than these — too-long lines kill rhythm.

| Subtitle context | Max width |
|------------------|-----------|
| Centered hero sub (B, C) | `var(--pt-cn-layout-max-read-box)` = 640 px |
| Centered floor-head A sub | 620 px (or 640 px for short copy) |
| Left-aligned floor-head B sub | 760 px |
| Hero variant A `tagline-desc` | 680 px |
| Card body copy | width of card (no explicit cap) |
| Legal paragraph | 640 px (inherited from reader column) |
| Asymmetric skill sub (I) | `min(620px, 100%)` |

Mobile: caps drop with the viewport; never set them in vw.

### 9.5 Gradient text rule

- **At most one gradient `<span>` per floor.**
- **At most one gradient `<span>` per visible viewport on the hero floor** (in practice: one gradient word in the h1).
- Use `--pt-cn-gradient-1` through `8`. Animation optional (`background-position` 6–12 s ease-in-out).
- Never on body copy. Never on buttons. Never on backgrounds.

---

## 10. Spacing rhythm

**No `--pt-cn-spacing-N` tokens in this kit.** Write px literals on the 2-px rhythm:

`4 · 6 · 8 · 10 · 12 · 14 · 16 · 18 · 20 · 24 · 28 · 32 · 36 · 40 · 44 · 48 · 56 · 64 · 72 · 96 · 122 · 138`

| Bucket | Used for |
|--------|----------|
| 4–8 | Chip gap, kv row column-gap, mono caption baseline trim |
| 10–14 | Card inner row gap, button content gap, command-box gap |
| 16–18 | Default content gap (section heading stack), grid card gap (dense) |
| 20–24 | Default grid gap, card padding (mid), filter row padding |
| 28–32 | Card padding (standard), reader paragraph margin |
| 36–48 | Floor head margin-bottom, panel padding, section-internal margin |
| 60–64 | Panel padding (gradient-card), head→grid margin (loose) |
| 72–96 | Top-of-floor margin (compact / default) |
| 122–138 | Top-of-floor margin (default / loose, between major chapters) |

**Outer page gutter is fixed** at `36 px` desktop / `20 px` mobile by `.layout-max-wide` and `.layout-max-inner-wrap`. Don't add additional outer padding on sections.

---

## 11. Card system

Cards are the central composition unit. **There are two equally first-class flavors: bordered cards (hairline `--pt-cn-color-line-100`) and borderless cards (separated by bg-step alone).** Pick by context — borderless when the card sits on a stepped surface (e.g. `neutral-50` card on `neutral-100` panel, or `gradient-card-bg` panel hosting nested rows); bordered when the card sits on the page canvas with no surrounding panel.

### 11.1 The card archetype table

All values are token-real (quoted from `qianwenai-v1/src`).

#### A — Standard bordered cards (canvas + hairline)

| Card | Bg | Border | Radius | Padding | Used |
|------|----|--------|--------|---------|------|
| Marketplace card (`.models-card`) | `--pt-cn-color-neutral-50` | `1px --pt-cn-color-line-100` | `--pt-cn-radius-sm` | 24 | `models` grid; fixed `height: 340` |
| Pricing offer (`.coding-plan-offer-card`) | `--pt-cn-color-neutral-50` | `1px --pt-cn-color-line-100` | `--pt-cn-radius-sm` | 32 | coding-plan pricing |
| Compare card (`.models-compare-card`) | `--pt-cn-color-neutral-50` | `1px --pt-cn-color-line-100` | `--pt-cn-radius-sm` | `36 24` | models/compare |
| Code-snippet (`.code-snippet`) | wrap `--pt-cn-color-neutral-50` | `1px --pt-cn-color-line-100` | `--pt-cn-radius-xs` | wrap 12; tabs h42; body 16 | docs, models-detail, skills |
| Try-it section (`.docs-tryit-section`) | `--pt-cn-color-neutral-50` | `1px --pt-cn-color-line-100` | `--pt-cn-radius-sm` | 14 | docs try-it drawer |
| Half-pixel data card (`.models-detail-tool-item`, `.models-detail-context-card`) | `--pt-cn-color-neutral-50` | `0.5px --pt-cn-color-line-100` (half-pixel hairline) | `--pt-cn-radius-sm` / `xs` | 16 / 24 | models-detail high-density rows |
| Tagline command panel (`.tagline-skills`) | inherits canvas | `1px --pt-cn-color-line-100` | `--pt-cn-radius-md` | 0 (children pad 16) | home tagline right column |
| Logo tile (`.coding-plan-tools-item`) | inherits | `1px --pt-cn-color-line-100` | `--pt-cn-radius-xs` | `0 8 0 24`, h64 | coding-plan tools 4-up |

**Hover:** `box-shadow: var(--pt-cn-shadow-light); transform: translateY(-4px)` — that's the entire move. Border stays.

#### B — Borderless cards (bg-step separation) — equally common

The kit uses borderless cards aggressively. **Whenever a card sits on a panel that is already one neutral step darker than canvas, drop the border.**

| Card | Bg | Radius | Padding | Used | Why borderless |
|------|----|--------|---------|------|----------------|
| `.afm-card` | `--pt-cn-color-neutral-150` | `--pt-cn-radius-md` | 28 | home AFM | Sits on canvas; step up to 150 carries it |
| `.afm-card-full` | `--pt-cn-gradient-card-bg` | `--pt-cn-radius-md` | 36 | home AFM hero / stacking | Gradient wash separates it |
| `.analyst-card` | `--pt-cn-color-neutral-100` + themed bg-image | `--pt-cn-radius-xs` | `32 24` | home analyst grid | Image inset; chrome would compete |
| `.afm-industry-card` | inherits | (only `border-bottom 1px --pt-cn-color-line-200`) | `4 4 20` | home industry 4-up | Bottom hairline only — reads as list row, not card |
| `.docs-content-panel` | `--pt-cn-color-neutral-100` | `--pt-cn-radius-lg` | `40 48` | docs page shell | The outer "panel hero" itself |
| `.docs-card` | `--pt-cn-color-neutral-50` | `--pt-cn-radius-sm` | 16 | docs `.docs-cards` 2-up | Sits on `neutral-100` parent panel |
| `.docs-minicard` | `--pt-cn-color-neutral-50` | `--pt-cn-radius-sm` | 16 | docs mini-cards grid | Same — parented by stepped panel |
| `.docs-next` | `--pt-cn-color-neutral-50` | `--pt-cn-radius-md` | 12 | docs page-bottom nav | Inner tile (`neutral-100, radius-xs, 12 20`) provides depth |
| `.docs-timeline-content` | `--pt-cn-color-neutral-50` | `--pt-cn-radius-sm` | `16 20` | docs timeline | Paired with dotted rail + glowing dot |
| `.signup-brand-panel` | `--pt-cn-color-neutral-100` + video | `--pt-cn-radius-lg` | 32 | signup left | Full-bleed video carries it |
| `.coding-plan-intro-showcase` | `--pt-cn-gradient-card-bg` | `--pt-cn-radius-md` | `60 44` | coding-plan intro | Big floor-as-panel |
| `.coding-plan-faq-panel` | `--pt-cn-gradient-card-bg` | `--pt-cn-radius-md` | `60 44` | coding-plan faq | Same |
| `.prod-shell` | `--pt-cn-gradient-card-bg` | `--pt-cn-radius-md` | `60 44 36` | home AI-powered product | Same |
| `.bulletin-section` | `--pt-cn-color-neutral-100` + themed bg | `--pt-cn-radius-md` | `var(--pt-cn-bulletin-padding)` | home bulletin | Banner card |
| `.models-detail-context-card-thinking` | `--pt-cn-color-neutral-100` | `--pt-cn-radius-xs` | 24 | models-detail | Borderless variant of the default context card |
| `.models-detail-side-highlight` | `--pt-cn-color-neutral-100` | `--pt-cn-radius-sm` | 16 | models-detail right rail | Carries progress meter + CTA |
| `.skills-detail-note` | `--pt-cn-color-neutral-100` | `--pt-cn-radius-xs` | `16 24` | skills detail | Inline tip card |
| `.docs-notice` | `--pt-cn-color-supporting-{green,blue,orange,red}` | `--pt-cn-radius-xs` | 16 | docs callouts | Colored bg already separates |
| `.legal-note` | `--pt-cn-color-neutral-150` | `--pt-cn-radius-xs` | 12 | legal pages | Inline aside |

**Rule of thumb:** if the surface behind the card already differs from canvas by one step, **the card has no border**. If both surfaces are canvas, **add the hairline**.

#### C — Featured / accent cards (gradient rim, animated border)

The kit reuses **one** gradient-rim recipe everywhere. Don't invent variants.

```scss
.card.is-featured {                                        // or .is-compared
  position: relative;
  isolation: isolate;
  border-color: transparent;                               // remove the hairline
}
.card.is-featured::before {
  content: '';
  position: absolute;
  inset: calc(-1 * var(--pt-cn-line-size-normal));
  padding: var(--pt-cn-line-size-normal);
  border-radius: inherit;
  background: var(--pt-cn-gradient-2);                        // or 4 / 7 by site role
  background-size: 140% 140%;
  -webkit-mask:
    linear-gradient(#000 0 0) content-box,
    linear-gradient(#000 0 0);
  mask-composite: exclude;
  animation: card-rim-flow 8s cubic-bezier(0.3, 0.08, 0.18, 1) infinite;
  pointer-events: none;
}
```

| Use | Gradient | Duration |
|-----|----------|---------:|
| Compared / selected card (`.models-card.is-compared`) | `--pt-cn-gradient-2` | 8 s |
| Featured pricing tier (`.coding-plan-offer-card.is-featured`) | `--pt-cn-gradient-2` | 8 s |
| Focused search input (`.models-market-search:focus-within`, `.nav-search:focus-within`) | `--pt-cn-gradient-4` | 3 s |
| Era CTA email input (`.era-hero-email`) | `--pt-cn-gradient-1` | 19.6 s |
| Solid hot tag (`.tag-normal.tag-hot`) | `--pt-cn-gradient-6` fill (not rim) | n/a |

**Stagger animations on tag clouds** with `:nth-child(3n / 4n / 5n)` delays — keeps the page from pulsing in lockstep.

Featured cards **never** get a shadow; the rim does the work.

#### D — Media-first cards (full-bleed image/video + content panel)

| Card | Recipe |
|------|--------|
| `.customers-say-card` 670×424 | `border-radius: --pt-cn-radius-md; background: cover image; ::before linear-gradient(0deg, rgba(7,8,14,0.1) → transparent) for legibility; .customers-say-overlay absolute top:12 right:12 w:44% min:337 — a borderless nested card on neutral-50, radius-sm, padding 30 20 24 20, holding quote (h36 bold) + p (body-sm neutral-750) + signature + logo bottom-right` |
| `.models-hero-card` 588×244 | `border-radius: --pt-cn-radius-xs (mobile: 18); padding 12 outer; .models-hero-card-main is a 270×220 right-anchored borderless panel on neutral-50 holding logo (24×24) + title-sm + 2-line clamp + tag row` |
| `.skills-detail-hero` | `border-radius: --pt-cn-radius-lg; bg: neutral-100 + cover image; padding 24; centered glass command box inside (see G)` |
| `.era-hero-shell` / `.tail-visual--tall` 790h | `radius-lg · absolute media · R15 居中栈 · §4.9` |
| `.tail-visual--compact` 370h | `同上 · h2 44 · 社区/Hackathon 收尾 · §4.9` |
| `.media-duo-visual` / marketing agent-builder | `radius-md; **no border**; **no shadow**; 16:10 or h 248–280; icon 20×20 top-left; §4.5` |
| `.agent-builder-visual` (§08 gallery only) | `radius-xs; 1px line-100; h248` — marketing floors use §4.5 borderless |

**Pattern:** floor-head 在网格上方；卡片标题在配图**下方**，不压在照片上 (§2)。

#### E — Compact tiles (logo tiles, mini-cards, chips-as-cards)

| Tile | Recipe |
|------|--------|
| `.afm-card-half` / `.afm-card-quarter` | `bg: transparent; border: 1px line-100; radius-xs; padding 28; height 294px desktop`; title-row mb12 + desc + metric col-stack + arrow at bottom |
| `.afm-industry-card` | borderless (bottom hairline only) — see B |
| `.coding-plan-tools-item` | bordered, see A |
| `.models-detail-io-card` | `border: 0.5px line-100; radius-xs; padding 24; min-height: calc(48 * 3.3)` — heading `body-sm neutral-550 mb8` + centered chip rail (chips: `bg supporting-purple, fg primary-550, radius-full, padding 8 12`) |
| `.docs-search-result` | borderless; `padding 10; radius-xs; :hover bg neutral-100`; title row (icon 14×14 + label + meta tag) → desc indented to align under title icon (`padding-left: 14 + 6`) |

#### F — Composite cards (scroll-driven, asymmetric grids)

| Composite | Behavior |
|-----------|----------|
| **Stacking model cards** (`.afm-full-stack-section`) | `height: 180vh` container; `.afm-full-stack-sticky position: sticky; top: 120`; stack cards `position: absolute; inset: 0; transform-origin: center top; will-change: transform`. Scroll drives 3D stack via custom props (`--stack-scale`, `--stack-y`, `--stack-shadow-opacity` 0–0.08). Mobile: degrades to a normal vertical grid. |
| **Horizontal scroll-jacked carousel** (`.customers-say-track`) | `.customers-say-sticky position: sticky; top: 150`; inline-flex track translated via JS. Mobile: becomes native `overflow-x: auto; scroll-snap-type: x mandatory`. |
| **Synced preview pair** (`.hero-visual--showcase` / `.coding-plan-intro-showcase`) | 2-col `1fr 1fr; gap: 64`; accordion + `.hero-visual-preview-panel.is-active` fade. Locked **`height: 420`**. |
| **Coupled left fixed + right expandable** (`.prod-shell`) | 2-col `1fr 1.35fr; gap: 36`. Left = title + pill. Right = `.prod-group` list whose expand-state reveals a `.prod-app-list` 2-col sub-grid. |
| **3-col sticky reading** (`.models-detail-layout`) | `grid-template-columns: 240 1fr 240; gap: 48`; both rails `position: sticky; top: calc(84 + 36)`; anchor highlights as you scroll. |

Composite cards inherit the underlying card chrome rules — they wrap A/B archetypes, they don't replace them.

#### G — Form / input "cards" (single inputs styled as cards)

| Element | Recipe |
|---------|--------|
| `.signup-input` (pill) | `bg: transparent; border: 1px line-300; radius-full; padding: 0 20; height: 48; focus → border neutral-800; error → func-danger` |
| `.signup-code-input` | `border: 1px line-300; radius-xs; 48×48; grid repeat(6, 1fr); focus → primary-550; error → func-danger; error-dismiss keyframe` |
| `.signup-checkbox-wrap` | `border: 1px line-300; radius-sm; padding 16` — card wraps the checkbox |
| `.signup-provider-btn` | `border: 1px line-300; radius-full; height 48` — provider tile is a pill |
| `.skills-detail-command-box` | **glass tile**: `bg: color-mix(in srgb, --pt-cn-color-neutral-100 82%, transparent); backdrop-filter: blur(12px); radius-xs; padding 16; height 52; box-shadow: --pt-cn-shadow-light` |
| `.tagline-skills-command-wrap` | **stepped tile**: `bg: --pt-cn-color-neutral-100; radius-xs; padding 16; min-height: 44`; mono prompt + command + copy button |
| `.signup-back-btn` | circular tile `bg neutral-150; radius-full; 30×30` |

#### H — Overlay panels (popovers, FABs, sticky bars, sheets)

| Panel | Recipe |
|-------|--------|
| Sort/model/language dropdown (`.models-market-sort-dropdown`, `.models-detail-model-dropdown`, etc.) | `bg neutral-50; radius-md; padding 12; box-shadow --pt-cn-shadow-light; flex-col gap 8`. **No border.** Items: pill `radius-full; padding 8 16`; selected `bg neutral-150`; hover `bg neutral-100`; right-side check 16×16. |
| Compare bar (`.models-compare-bar`) | **glass + normal shadow** — `bg --pt-cn-color-models-compare-bar-bg; backdrop-filter: blur(10px); radius-md; padding 24 32; box-shadow --pt-cn-shadow-normal; position: fixed; left: 50%; bottom: 24; transform: translateX(-50%); z-index: 1000`. Tags row max-content + actions ml40 (now-btn light + close 32×32 round). |
| Mobile filter sheet (`.models-market-sidebar.is-open`) | `bg neutral-50; padding 20 12 12; box-shadow --pt-cn-shadow-normal; position: fixed; full-vh below nav offset`. |
| Mobile FAB (`.models-market-sidebar-fab`) | `bg neutral-50; border: 1px line-100; radius-full; padding: 0 20; height: 40; box-shadow --pt-cn-shadow-normal; position: fixed; right: 20; bottom: 20`. Stacks (rises) when compare-bar is present. |
| Docs search dropdown (`.docs-search-dropdown`) | **glass via pseudo** — `::before { bg --pt-cn-color-neutral-50; backdrop-filter: blur(12px) }`; `radius-sm; padding 16; box-shadow --pt-cn-shadow-normal`. Holds pill input (with gradient focus rim — variant C) + tabs row + results grid. |
| Compare picker modal (`.models-compare-picker-modal`) | `bg neutral-50; radius-sm; box-shadow --pt-cn-shadow-normal; margin-top: calc(--pt-cn-nav-backdrop-offset + 20)`. |
| Compare select popup (`.models-compare-select-popup`) | `bg neutral-50; border: 1px line-100; radius-sm; padding 4; box-shadow --pt-cn-shadow-normal` — the rare *bordered* popover (it sits in dense data UI). |

### 11.2 Eight recurring internal recipes

Use these top-to-bottom recipes verbatim — they appear across many cards.

**R1. Card-with-divider-then-metrics**
```
head row (icon + add-btn) — gap 6
title (body-lg, font-semibold) — mt 16
version row (caption mono, copy btn) — mt 4
desc (body-sm, neutral-650, 2-line clamp) — mt 12
modalities row (chips, gap 8) — mt 14
spacer (mt: auto)
border-top 1px line-100 — pt 12
2-col metric grid: strong (title-sm) + label (body-sm neutral-650)
footer CTA row
```
Used by: `.models-card`, `.afm-card`, `.coding-plan-offer-card`.

**R2. Eyebrow-mono → title → desc**
```
eyebrow: mono caption-sm, neutral-450, uppercase 0.06em
title: h3/h4, semibold, body-lg — mt 8–16
desc: p, body-sm, neutral-650/750
```
Used by: `.analyst-card`, `.docs-timeline-content`, `.reliability-item-meta`.

**R3. 2-line clamp body**
```scss
.desc {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
}
```
Used in: `.afm-card-desc`, `.models-card-desc`, `.models-hero-card-main p`, `.docs-card p`.

**R4. Accordion row inside a borderless panel**
```
parent: --pt-cn-gradient-card-bg, radius-md, padding 60 44
item:   border-bottom 1px line-200; padding 16–40 0
head:   button — h3 semibold + chevron primary-550
body:   grid-template-rows: 0fr → 1fr (animated)
        p body-sm clamp on closed; full on open
```
Used by: `.coding-plan-feature-item`, `.prod-group`, `.coding-plan-faq-item`.

**R5. Chip rail body** *(cards whose body IS a wrap of chips)*
```
heading: body-sm neutral-550 mb 8
.chips: flex wrap, gap 8, justify-content center
.chip:  inline-flex, gap 8, bg supporting-purple, fg primary-550,
        radius-full, padding 8 12, icon 16×16
```
Used by: `.models-detail-io-card`, `.models-detail-context-card`.

**R6. KV row separated by half-pixel rule**
```
.row {
  display: flex; justify-content: space-between;
  align-items: center; gap: 8;
  padding: 8 0;
  border-bottom: 0.5px solid --pt-cn-color-line-200;
}
.row .key   { body-sm; color: --pt-cn-color-neutral-650; }
.row .value { body-sm; color: --pt-cn-color-neutral-950;
              font-family: --pt-cn-font-medium;
              text-align: right; }
```
Used by: `.models-detail-feature-item`, `.models-detail-pricing-item`, `.models-compare-kv`.

**R7. Glass + light-shadow tile**
```
background: color-mix(in srgb, --pt-cn-color-neutral-100 ~82%, transparent);
backdrop-filter: blur(10–12px);
border-radius: --pt-cn-radius-xs;
padding: 16;
box-shadow: --pt-cn-shadow-light;
```
Used by: `.skills-detail-command-box`, `.docs-search-dropdown`, `.models-compare-bar` (variant on top of dynamic bg).

**R8. Stepped command tile (no glass, no shadow)**
```
background: --pt-cn-color-neutral-100;
border-radius: --pt-cn-radius-xs;
padding: 16;
font-family: --pt-cn-font-mono;
font-size: body-sm;
```
Used by: `.tagline-skills-command-wrap`, `.docs-next-center`, `.skills-detail-code-block` inner.

**R9. Card-row tier interior** *(3-up / 4-up — §4.4)*
```
ZONE A: name + Hot? · price + period · meta (body-sm neutral-650)
ZONE B: full-width pill — btn--secondary | btn--primary (featured)
ZONE C: border-top line-100 · §8.16 icon rows · nested bullets
```
Chrome: `neutral-50` · `radius-sm` · pad 32 · `line-100` or gradient rim · **shadow: none**.

Used by: `.card-row-item`, `.coding-plan-offer-card`, `.tier`.

**R10. Media duo interior** *(2-up borderless — §4.5)*
```
item: border 0 · shadow none · pad 0
ZONE 1 visual: radius-md · 16:10 or h 248–280 · cover · 20px icon · NO border
ZONE 2 body: left-align · title-md · desc 2-line clamp · mt 20–24
ZONE 3 link: text + arrow-up-right-outlined · ink or .is-accent
```

**R11. Skill / model simple card** *(§4.6 B)*
```
head + tag-hot · desc clamp · chips §8.19 · price §8.18 · divider line-100 · 2-col metrics
```

**R12. Step simple card** *(§4.6 A)*
```
step-tag §8.17 · title · desc · floor btn--primary
```

**R13. Text-card variant A** *(§4.7)*
```
border-bottom line-100 only · icon+name · desc · chips? · arrow
```

**R13b. Text-card minimal variant B** *(§4.7 无 tabs)*
```
same chrome · name · desc · arrow · pager §8.22
```

**R14. Logo matrix tile** *(§4.8 A)*
```
line-100 · radius-xs · h 64 · transparent · icon 24 + name body-sm · hover border only
```

**R19. Borderless logo strip item** *(§4.8 B)*
```
无 chrome · logo h 40–48 · object-fit contain · 品牌色保留 · hover opacity only
```

**R20. FAQ accordion row** *(§4.12)*
```
line-100 底部分割 · 问题+右 + · 答案 body-sm · §8.27 单开
```

**R21. Arena sync accordion row** *(§4.13)*
```
同 R20 行级 chrome · data-arena-panel=n · §8.28 联动右栏视觉
```

**R15. Tail visual content stack** *(§4.9)*
```
layout-max-wide · radius-lg · h 790|370 · 居中：kicker? · h2 · 副标题 · L1+L3 按钮
```

**R16. Footer link column** *(§4.10)*
```
title body-sm semibold · list gap 12 · link body-sm neutral-650
```

**R17. Testimonial carousel card** *(§4.11 A)*
```
carousel-card · radius-lg · pad 32 · quote · body 3–4 行 · avatar+署名
```

**R18. Criteria carousel card** *(§4.11 B)*
```
metric title-lg · title body-lg · ul body-sm neutral-650
```

### 11.3 Ten "clean & flat" signals

The kit reads as clean and flat because of these specific techniques. Replicate all of them.

1. **No inset border + no shadow on most content cards.** Separation is bg-step, not chrome. The default move when a card sits on a stepped panel is to drop the border entirely.
2. **Hairlines use the smallest available line size** — `var(--pt-cn-line-size-normal)` (1 px), and in dense data UI, literal `0.5px` (`--models-detail-card-line`) or `0.75px` for KV dividers. Hairlines fade toward "almost not there."
3. **Border tokens stay desaturated.** Only `--pt-cn-color-line-100/200/300` — never `neutral-300+`. Boundaries never compete with text.
4. **Hover lift = single low-opacity shadow + small Y translate.** `--pt-cn-shadow-light` + `translateY(-4px)`. No depth stacks, no scale, no border-color flip.
5. **Featured states swap border for a mask-composite gradient rim**, keeping the same outer footprint. `border-color: transparent` + `::before { padding: 1px; mask-composite: xor; background: --pt-cn-gradient-2 }`.
6. **Dropdowns / popovers default to no border + `--pt-cn-shadow-light`.** Bordered popovers are reserved for dense data UI where a border helps anchor a long scrollable list.
7. **Internal dividers are top/bottom only, never box outlines.** `border-top --pt-cn-color-line-100` for the metrics rule; `border-bottom --pt-cn-color-line-200` for stacked accordion rows.
8. **Bg-step nesting instead of chrome-on-chrome.** Stepped panels (`neutral-100`) host `neutral-50` cards. `gradient-card-bg` floors host borderless content rows. Children never re-paint their border.
9. **Pill controls bg-shift for state, never outline.** Active = `neutral-150`; hover = `neutral-100`. `--pt-cn-shadow-light` only on segmented toggles in the *elevated active* role.
10. **Half-pixel hairlines for high-density data UI.** `0.5px` (model detail rows) and `0.75px` (compare grid dividers) push the rule visually toward "barely there," so the data reads as text-only.

### 11.4 Card decision tree

Use this short flow when composing a new card.

```
Q0. Is the card actually a panel-as-card hosting a list of repeated rows
    (recommended models, cost summary, plan benefits, FAQ list, bundle items)?
    └─ Yes → panel-as-card (§11.6). Borderless wash outer + typography + hairline rows.
              Skip Q1; do not give the panel a 1px outer hairline, do not nest grey sub-cards.

Q1. Does the card sit on the page canvas (neutral-50)?
    └─ Yes → bordered card (A). Hairline 1px line-100; bg neutral-50; radius sm/md by size.
    └─ No  → it sits on a stepped panel → borderless card (B). Bg neutral-50 or neutral-100; no border.

Q2. Is the card "selected" / "featured" / "in-focus"?
    └─ Yes → swap the hairline for the mask-composite gradient rim (C). Same footprint.

Q3. Does the card lead with imagery (photo / video / cover bg)?
    └─ Yes → media-first card (D). Heading stays OUTSIDE the card (above, in .layout-max-inner).
              The only on-image text is a nested borderless overlay panel.

Q4. Is the card actually a tile or chip-card (small, repeated, no body copy)?
    └─ Yes → compact tile (E). Either thin-border 1px line-100 + radius-xs, or borderless with
              a bottom hairline acting as a list divider.

Q5. Is the card scroll-driven, sticky, or coupled to a sibling?
    └─ Yes → composite (F). Wrap an A/B card; don't reinvent chrome.

Q6. Is the card a styled input?
    └─ Yes → form-card (G). Border line-300 (not line-100); pill or radius-xs by shape.

Q7. Is the card an overlay (dropdown, sheet, fab, sticky bar)?
    └─ Yes → overlay (H). Borderless + shadow-light for most; bordered + shadow-normal only
              when it anchors a long scrollable list.
```

### 11.5 Card padding & radius defaults (when in doubt)

| Density | Radius | Padding |
|---------|--------|---------|
| Small tile, mini-card | `--pt-cn-radius-xs` | 12 / 16 |
| Mid card (most marketplace / pricing) | `--pt-cn-radius-sm` | 24 / 28 / 32 |
| Standard content card | `--pt-cn-radius-md` | 28 / 32 |
| Panel-as-card (faq, intro, prod) | `--pt-cn-radius-md` | 60 44 (mobile 32 20) |
| Hero / signup / era panel | `--pt-cn-radius-lg` | 32 / 40 48 / 48 |

### 11.6 Panel-as-card: no outer stroke, no grey sub-card inside  ★

When a card's job is to **host multiple items as one block** (recommended models, cost summary, plan benefits, step intro with embedded list, FAQ list, prod-shell prod-group, customer bundle "what you get") it is a **panel-as-card** — and it must follow these two rules **together**:

1. **The outer panel is borderless.** Background is `--pt-cn-gradient-card-bg` (preferred) or one neutral step (`neutral-100`); `border: 0`; `box-shadow: none`. Visual separation from canvas comes from the bg-step alone. No 1px hairline `--pt-cn-color-line-100` wrapping the whole block.
2. **Interior items are not nested grey sub-cards.** Each item sits directly on the panel surface and uses **typography + a single hairline** to read as a row:
   - Title row: `font-semibold` + body-lg/title-md; neutral-950 ink
   - Caption / meta: mono caption-sm uppercase, `0.06em`, `neutral-450/600`
   - Body / description: body-sm, `neutral-650`
   - Numeric / price: `--pt-cn-font-mono`, `func-success` for prices, `neutral-650` for labels
   - Pill chip for tag (single small pill, `primary-50` or `neutral-150` fill) — never a whole grey block to host one piece of info
   - Divider between items: `border-bottom: 1px solid var(--pt-cn-color-line-100)` (standard) or `0.5px var(--pt-cn-color-line-200)` (dense data)
   - Spacing: `py 16–24` per row; section caption `mb 16–24`

```
❌ WRONG  — outer stroke + grey card-in-card
┌─ bg-neutral-50  border 1px line-100  radius-md ──────────────────┐
│  RECOMMENDED MODELS                                              │
│  ┌─ bg-neutral-150  radius-sm  padding 20 ─────────────────────┐ │
│  │  Qwen3.7-Max  [CORE]                  ¥12 / 1M tokens      │ │   ← grey
│  │  Flagship LLM with deep grasp of plot logic …              │ │     card-in-card
│  │  → Outline, episode scripts, dialogue lines                │ │
│  └─────────────────────────────────────────────────────────────┘ │
│  ┌─ bg-neutral-150  radius-sm  padding 20 ─────────────────────┐ │
│  │  Qwen3-Coder  [ASSIST]                Low cost             │ │
│  │  …                                                          │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘

❌ WRONG  — bundle with grey-bg cost summary inset
┌─ bg-neutral-50  border 1px line-100  radius-md ──────────────────┐
│  [♡ icon]                                                        │
│  Urban Sweet Romance                                             │
│  Light, sweet urban love stories …                               │
│  [ Qwen3.7-Max ] [ Wan 2.7 ] [ CosyVoice ] [ Wan 2.7 ]           │   ← model chips
│  ┌─ bg-neutral-100  radius-sm  padding 20 ─────────────────────┐ │   ← grey
│  │   EST. COST          ¥8–15 / ep                            │ │     inset
│  │   CYCLE              0.5–1 day / ep                        │ │     summary —
│  │   MODELS             4 core models                         │ │     anti-pattern
│  └─────────────────────────────────────────────────────────────┘ │
│  [ Activate bundle ]                                             │
└──────────────────────────────────────────────────────────────────┘

✅ RIGHT — borderless wash panel, typography + hairline rows
┌─ bg gradient-card-bg  radius-md  no border  no shadow ───────────┐
│  RECOMMENDED MODELS  (mono uppercase neutral-450, mb-24)         │
│                                                                  │
│  Qwen3.7-Max   [CORE chip]              ¥12 / 1M tokens          │
│  Flagship LLM with deep grasp of plot logic and character        │
│  arcs — drafts full-length, high-fidelity scripts.               │
│  → Outline, episode scripts, dialogue lines                      │
│  ───────────────────────────────  border-b 1px line-100          │
│  Qwen3-Coder   [ASSIST chip]            Low cost                 │
│  Code-tuned model that turns prose into structured output …      │
│  → Structured script JSON, relationship graphs                   │
└──────────────────────────────────────────────────────────────────┘

✅ RIGHT — bundle on canvas, summary rows as plain KV (typography only)
┌─ bg neutral-50  no border  radius-md  padding 32 ───────────────┐
│  [♡ icon — pill chip neutral-150, radius-md, 40×40]              │
│                                                                  │
│  Urban Sweet Romance        (Inter semibold 32, neutral-950)     │
│  Light, sweet urban love stories — optimized for short-video     │
│  platforms.                  (body-md neutral-650)               │
│                                                                  │
│  [Qwen3.7-Max · Script]  [Wan 2.7 · Visuals]  [CosyVoice · …]    │   ← pill chips
│  [Wan 2.7 · Video]                                               │     (single pill,
│                                                                  │      not a grey
│  EST. COST                              ¥8–15 / ep               │   ← block per
│  ─────────────────────────  border-b 1px line-100                │     item)
│  CYCLE                                  0.5–1 day / ep           │
│  ─────────────────────────  border-b 1px line-100                │
│  MODELS                                 4 core models            │
│                                                                  │
│  [♟ For solo creators & small studios]   (pill chip)             │
│                                                                  │
│  [ Activate bundle ]   (primary CTA, full-width)                 │
└──────────────────────────────────────────────────────────────────┘
```

**When this rule applies:**

- Recommended-list panels (recommended models, related products)
- Cost / spec summary blocks inside a card
- Plan-benefit lists inside a pricing card
- Step intro with embedded "推荐产品" or "you get" sub-list
- `prod-shell` `prod-group` (already borderless — keep it that way)
- Customer bundle cards listing models / quotas / inclusions
- FAQ list (Pattern C panel-head + accordion rows — already correct; don't regress)

**When this rule does NOT apply (bordered tile grids are OK):**

- Compact tile grids on canvas where each tile **is** the unit (Supported AI Tools logo tiles, `logo tile` 4-up, `models-card` marketplace grid). These follow §11.1 A with a single 1px `line-100` hairline; they are tiles, not panels-as-card.
- A single content card on canvas (one quote, one product) — §11.1 A bordered card is fine.
- Cards leading with imagery (`customers-say-card`, hero media panel) where the chrome lives outside the visible image.

**Decision shortcut:** if the block contains a list of ≥2 sub-items that read as rows of the same thing, it is a panel-as-card — outer borderless + interior hairline rows. If the block is one self-contained card, archetype A/B/C applies as before.

**Implementation checklist for panel-as-card:**

- [ ] Outer container: `background: var(--pt-cn-gradient-card-bg)` (or `neutral-100`); `border: 0`; `box-shadow: none`; `border-radius: var(--pt-cn-radius-md)`; padding `60 44` desktop / `32 20` mobile
- [ ] Section caption: mono caption-sm uppercase, `0.06em`, `neutral-450/600`, `margin-bottom: 24`
- [ ] Each row: `padding: 20 0` (or `24 0` airy); `border-bottom: 1px solid var(--pt-cn-color-line-100)` except the last row
- [ ] Tag chip in a row: a single pill (§8.2), not a filled background block
- [ ] Numeric / price: `--pt-cn-font-mono`; price in `--pt-cn-color-func-success`, labels in `neutral-650`
- [ ] No `box-shadow`, no inset `background`, no nested `border` inside the panel

---

## 12. Filter rail & sidebar  *(models, docs, models/detail)*

### 12.1 Sticky filter rail (models marketplace)

- Width: **240 px** (`calc(60px * 4)`)
- Gap to content: **48 px**
- Position: `sticky; top: calc(var(--pt-cn-nav-backdrop-offset) + 12px); max-height: calc(100vh - var(--pt-cn-nav-backdrop-offset) - 12px); overflow: auto; padding-bottom: 48px`
- Internal stack: `display: flex; flex-direction: column; gap: 32px`
- ≤1024 px: hide rail; replace with a floating FAB (`position: fixed; right: 20px; bottom: 20px; border-radius: var(--pt-cn-radius-full); box-shadow: var(--pt-cn-shadow-light)`)

### 12.2 Filter primitives

- **Collapsible group head** (see §8.12): full-width button `padding: 6px 12px 6px 4px; font: medium body-sm`; chevron rotates 180° on expand.
- **Tag-cloud options**: `display: flex; flex-wrap: wrap; gap: 8px; padding: 8px 4px` — pills as §8.2.
- **List variant**: 1-px vertical guide via `::before` at `left: 14px`, indent 32 px; active item gets a 4-px primary dot via `::after`.
- **Range filter**: track 2 px; thumb 8 px; dual-input; values row `display: flex; justify-content: space-between; margin-top: 4px; font-size: var(--pt-cn-body-font-size-sm); font-family: var(--pt-cn-font-mono)`.
- **Toggle row** (§8.4 segmented or `--pt-cn-color-neutral-150` track with 34×20 switch): `display: flex; justify-content: space-between; padding: 6px 4px`.

### 12.3 3-column shell  *(docs, models/detail)*

```
grid-template-columns: 240px minmax(0, 1fr) 240px;
gap: 32–48px;
align-items: start;
```

- Left rail: anchor list (§12.2 list variant)
- Center: `max-width: var(--pt-cn-layout-max-read-box); margin: 16px auto 0` — reader column
- Right rail: "on this page" TOC (same list variant)
- Code-side variant: flips to 2-col with internal `1fr 1fr` for prose/code split

---

## 13. Off-shell pages

Skip `.page-shell` entirely. Don't retrofit.

### Signup
- 2-col page grid: `minmax(420px,1fr) minmax(460px,1fr); gap: 4px; padding: 32px`
- Left = brand panel: `padding: 32px; border-radius: var(--pt-cn-radius-lg)`, absolutely-positioned `.brand-copy { position: absolute; inset: auto 32px 120px 32px }` over background video
- Right = form; pill inputs (`components.md` §08); verification code grid `repeat(6, minmax(0,1fr))` of 48×48 px tiles
- Mobile: 1 column; brand becomes top banner

### Error
- Fullscreen centered flex (`min-height: 100vh; align-items: center; justify-content: center`)
- Headline: `font-size: clamp(45px, 20vw, 160px)` with per-character variable-font interactivity (the only place this kit uses font-variation effects)
- Sub: body-md, color `--pt-cn-color-neutral-650`
- Two CTAs centered beneath

### Docs (3-col shell, see §12.3)
Uses `.docs-main-wrap` instead of `.page` body; sidebar + content + anchor bar all in one grid.

---

## 14. Responsive

- **Breakpoint:** **1024 px**. Above → "desktop"; ≤ collapses.
- **Outer gutters:** desktop 36 px (utility), mobile 20 px. Don't add intermediate steps.
- **Mobile defaults:**
  - Grids → `1fr` (unless density is essential)
  - Floor gap → 64 px between floors; 32 px head→body
  - Panel padding 60 44 → 32 20
  - Card padding stays the same
  - Hero font-size: drop to `clamp(48px, 12vw, 88px)` for variant B; `clamp(20px, 3.6vw, 26px)` for hero metric strong
- **Nav:** desktop 84 px, mobile 62 px → sticky offsets recompute via `--pt-cn-nav-backdrop-offset`.
- **Sidebars:** hide ≤1024 px; replace with floating FAB or top sheet.
- **Subtitle width caps don't change**; the viewport already constrains them.
- **Fluid:** `clamp(min, vw, max)` only on hero h1, hero metric strong, and the panel `height: 60vh`. Never raw `vw` on padding or body text.

---

## 15. Radius vocabulary (the working five)

| Token | px | Use |
|-------|---:|-----|
| `--pt-cn-radius-full` | 999 | Pills, chips, CTAs, FABs, dots, dropdowns trigger |
| `--pt-cn-radius-xs` | 12 | Inner panels, tool tiles, command boxes, notices, docs cards |
| `--pt-cn-radius-sm` | 18 | Mid cards (marketplace, compare, pricing offer), dropdown panel |
| `--pt-cn-radius-md` | 24 | Standard cards, hero frames, gradient panels, customer story outer |
| `--pt-cn-radius-lg` | 36 | Full-bleed heroes, signup brand panel, era CTA, docs panel hero |

Don't use the other tokens (`xl 42, 2xl 48, 2xs 8, 3xs 6, 4xs 2`) unless the Guideline calls for them.

---

## 16. Background steps & elevation

Use background, not borders/shadows, to separate planes.

| Plane | Color | When |
|-------|-------|------|
| Canvas | `--pt-cn-color-neutral-50` | `.page` body; default floor |
| Tinted floor | `--pt-cn-color-neutral-100` | Every 2nd / 3rd floor for visual rhythm; docs panel hero; bulletin |
| Subtle surface | `--pt-cn-color-neutral-150` | Pill segmented track, chips, disabled input, legal note, dropdown hover |
| Card wash | `--pt-cn-gradient-card-bg` (`135deg, neutral-150 → neutral-50`) | Floor wrapped in a single rounded panel (faq, intro showcase, ai-powered-product) — almost flat |

Borders only on: outline buttons, inputs, featured pricing rim, weak card hairline (`--pt-cn-color-line-100`). Default `shadow: none`. Use `--pt-cn-shadow-light` only for: pill segmented selected child, card hover lift, sticky compare bar, floating FAB, search dropdown panel.

---

## 17. Data-page interaction surfaces  *(models, models/detail, models/compare, docs)*

Data pages have a denser interaction layer than marketing pages. This section catalogs every interactive surface and the exact tokens. Quote these — don't invent.

### 17.1 The toolbar row

The models page toolbar is the canonical pattern for "sidebar header + content controls."

```
┌─────────────── .models-market-top-row ──────────────────────────────────────┐
│ grid-template-columns: var(--models-page-sidebar-width) 1fr                │
│ column-gap: var(--models-page-sidebar-gap)                                  │
│ align-items: center                                                         │
│ padding: 32px 0 12px                                                        │
│ background: --pt-cn-color-neutral-50                                          │
│                                                                             │
│  ┌─ sidebar slot ─┐  ┌─ top-right (flex, gap 6, flex-wrap) ──────────────┐ │
│  │ h2 title-lg    │  │ [reset-btn] [compare-btn] [search] [view-toggle] │ │
│  │ semibold       │  │ [sort-trigger]                                    │ │
│  └────────────────┘  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Universal control sizing** (locked, applies to every toolbar control):

```scss
.page-models {
  --models-market-control-height: 40px;
  --models-market-control-radius: var(--pt-cn-radius-full);
  --models-market-control-icon-size: 18px;
}
```

All toolbar buttons / inputs / dropdowns share `height: 40px` and `border-radius: --pt-cn-radius-full` — the toolbar reads as a single height across its row.

### 17.2 Search input (pill with gradient focus ring)

```scss
.search {
  display: inline-flex; align-items: center; gap: 6px;
  height: 40px;                                          // --models-market-control-height
  padding: 0 14px;
  border-radius: var(--pt-cn-radius-full);
  background: var(--pt-cn-color-neutral-50);
  border: var(--pt-cn-line-size-normal) solid var(--pt-cn-color-line-100);
  color: var(--pt-cn-color-neutral-550);
  position: relative;
  isolation: isolate;
}
.search input {
  width: calc(48px * 4.6);                               // 221 px default
  border: 0; background: transparent;
  font-size: var(--pt-cn-body-font-size-sm);
  color: var(--pt-cn-color-neutral-750);
}
.search input::placeholder {
  color: var(--pt-cn-color-neutral-400);
}
.search:focus-within { border-color: transparent; }      // hide hairline; reveal gradient rim
.search:focus-within::before {                           // gradient rim (mask-composite)
  opacity: 1;
  animation: search-border-flow 3s ease-in-out infinite;
}
```

Pseudo-rim:
```scss
.search::before {
  content: '';
  position: absolute; inset: -1px;
  padding: 1px; border-radius: inherit;
  background: var(--pt-cn-gradient-4);
  background-size: 140% 140%;
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity var(--pt-cn-motion-fast) ease;
  pointer-events: none;
}
```

Leading icon (`search-outlined`) 18 px; placeholder uses `--pt-cn-color-neutral-400`. Nav search uses the same recipe at `height: 48`, `width: 228 → 490` on focus.

### 17.3 Sort trigger + dropdown

**Trigger** — pill button, same 40-px height. Chevron rotates 90° → -90° on open.

```scss
.sort-trigger {
  width: 100%;
  min-width: calc(48px * 2.9);                           // ~139 px
  height: 40px;
  padding: 0 18px;
  border-radius: var(--pt-cn-radius-full);
  border: 1px solid var(--pt-cn-color-line-100);
  background: var(--pt-cn-color-neutral-50);
  color: var(--pt-cn-color-neutral-750);
  font: medium 14px / 20px var(--pt-cn-font-medium);
  display: inline-flex; align-items: center; justify-content: space-between;
  gap: 4px;
}
.sort-trigger svg { width: 16px; transform: rotate(90deg); transition: transform .25s ease; }
.sort-trigger.is-open svg { transform: rotate(-90deg); }
```

**Dropdown** — `position: absolute; top: calc(100% + 4px); left: 0; right: 0`. Borderless, light shadow.

```scss
.sort-dropdown {
  display: flex; flex-direction: column; gap: 8px;
  padding: 12px;
  border-radius: var(--pt-cn-radius-md);
  background: var(--pt-cn-color-neutral-50);
  box-shadow: var(--pt-cn-shadow-light);
  z-index: 8;
}
.sort-option {
  padding: 8px 16px;
  border-radius: var(--pt-cn-radius-full);
  background: transparent; border: 0;
  display: inline-flex; align-items: center; justify-content: space-between; gap: 8px;
  color: var(--pt-cn-color-neutral-950);
  font-size: var(--pt-cn-body-font-size-sm);
}
.sort-option:hover            { background: var(--pt-cn-color-neutral-100); }
.sort-option.is-selected      { background: var(--pt-cn-color-neutral-150); }
.sort-option-check svg        { width: 16px; height: 16px; }
```

Selected option: bg `neutral-150` + trailing check; hover: bg `neutral-100`. **No border on either trigger or dropdown when open** — only the trigger's resting hairline.

### 17.4 View toggle (grid ↔ list)

Segmented pill — the "elevated active" variant.

```scss
.view-toggle {
  height: 40px;
  padding: 6px;
  display: inline-flex; align-items: center; gap: 2px;
  border-radius: var(--pt-cn-radius-full);
  background: var(--pt-cn-color-neutral-150);                // track
}
.view-toggle button {
  width: 32px; height: 28px;
  padding: 6px 8px;
  border-radius: var(--pt-cn-radius-full);
  background: transparent;
  color: var(--pt-cn-color-neutral-550);
  display: inline-flex; align-items: center; justify-content: center;
}
.view-toggle button.is-active {
  background: var(--pt-cn-color-neutral-50);
  color: var(--pt-cn-color-neutral-950);
  box-shadow: var(--pt-cn-shadow-light);                    // only place a shadow lands
}
```

Reuse exactly. The "elevated thumb" inside a `neutral-150` track is the kit's only segmented-control recipe — don't sub in colored fills.

### 17.5 Pill action buttons (reset / compare / compact CTAs)

```scss
.action-btn {
  height: 40px;
  padding: 0 16px;
  border-radius: var(--pt-cn-radius-full);
  display: inline-flex; align-items: center; gap: 4px;
  font: medium 14px var(--pt-cn-font-medium);
}
.action-btn--reset {
  background: transparent;
  border: 1px solid var(--pt-cn-color-line-100);
  color: var(--pt-cn-color-neutral-750);
}
.action-btn--compare {                                    // soft-fill, no border
  background: var(--pt-cn-color-primary-50);
  color: var(--pt-cn-color-primary-550);
  border-color: transparent;
}
.action-btn--compare:hover,
.action-btn--compare.is-active {
  background: var(--pt-cn-color-primary-150);
}
```

The primary-50 soft-fill is the "secondary CTA" archetype — use it whenever you need an emphasized but not-black action.

### 17.6 Card grid vs list view

Same `.models-market-main`, two layouts.

**Grid view** (default)
```
display: grid;
grid-template-columns: repeat(auto-fill, minmax(var(--models-page-card-min-width), 1fr));
column-gap: 24;
row-gap: 28;
```
`--models-page-card-min-width: calc(26px * 10) = 260px` (or `--…-dense: 220px` when toggled). Card height locked at 340 px.

**List view** (toggle)
```scss
.list {
  display: grid;
  min-width: var(--models-market-list-min-width);        // 1060px (horizontal scroll below)
  grid-template-columns:
    minmax(220px, 2.5fr)
    minmax(180px, 2fr)
    minmax(96px, 1fr)
    minmax(96px, 1fr)
    minmax(88px, 0.8fr)
    calc(48px * 1.6);                                    // actions column ≈ 77 px
}
.list-head { height: 60px; }
.list-row  { height: 80px; }
```

Responsive collapses **hide nth columns** in 4 breakpoint brackets (not reflow to rows): drop the rarely-used columns first, keep name + key metric + actions visible.

### 17.7 Card hover-reveal actions  *(`.models-card`)*

On hover, the bottom metrics row fades and an absolutely-positioned action row floats in.

```scss
.card                  { position: relative; isolation: isolate; }
.card-metrics-grid     { transition: opacity var(--pt-cn-motion-fast) ease; }
.card-actions {
  position: absolute; left: 24; right: 24; bottom: 24;
  display: flex; gap: 8;
  opacity: 0;
  transition: opacity var(--pt-cn-motion-fast) ease;
}
.card:hover .card-metrics-grid { opacity: 0; }
.card:hover .card-actions      { opacity: 1; }
.card:hover                    {
  transform: translateY(-4px);
  box-shadow: var(--pt-cn-shadow-light);
}
```

Use this pattern whenever a card has secondary actions ("Add to compare", "View detail", "Copy id") that shouldn't compete with the primary metric display.

### 17.8 Sticky compare bar

Already in §8.10 / §11 H — repeating the key constants here for the data-page context:

```scss
.compare-bar {
  position: fixed; left: 50%; bottom: 24px;
  transform: translateX(-50%);
  height: 44px;                                          // calc(40 + 4) tag + padding
  padding: 24px 32px;
  border-radius: var(--pt-cn-radius-md);
  background: var(--pt-cn-color-models-compare-bar-bg);
  backdrop-filter: blur(10px);
  box-shadow: var(--pt-cn-shadow-normal);
  z-index: 1000;
  display: inline-flex; align-items: center;
}
.compare-bar-tags    { display: flex; gap: 6; flex-wrap: wrap; max-content; }
.compare-bar-tag     { height: 40; padding: 0 12; border-radius: --pt-cn-radius-lg; }
.compare-bar-actions { margin-left: 40; display: inline-flex; gap: 8; align-items: center; }
.compare-bar-now     { /* primary-fill CTA */ }
.compare-bar-close   { width: 32; height: 32; border-radius: 999; }
```

Mobile (≤1024 px): bar shrinks to `padding: 16 20`; tags wrap; mobile FABs above it `bottom: calc(24 + 44 + 12)`.

### 17.9 Mobile sidebar sheet + FAB stack

```scss
.sidebar.is-open {                                       // mobile sheet
  position: fixed; inset: var(--pt-cn-nav-backdrop-offset) 0 0 0;
  bg: var(--pt-cn-color-neutral-50);
  padding: 20 12 12;
  box-shadow: var(--pt-cn-shadow-normal);
  overflow: auto;
  z-index: 900;
}
.sidebar-fab,                                             // entry button
.sidebar-reset-fab {                                      // 2nd FAB above 1st
  position: fixed; right: 20; bottom: 20;
  height: 40; padding: 0 20;
  border-radius: var(--pt-cn-radius-full);
  background: var(--pt-cn-color-neutral-50);
  border: 1px solid var(--pt-cn-color-line-100);
  box-shadow: var(--pt-cn-shadow-normal);
  display: inline-flex; align-items: center; gap: 6;
  font: medium 14px var(--pt-cn-font-medium);
}
.sidebar-reset-fab    { bottom: calc(20 + 40 + 8); }     // stack rules
.compare-bar ~ .sidebar-fab { bottom: calc(20 + 44 + 12); }
```

The FAB stack always sits above the compare bar. When both are present, recalculate `bottom` so the topmost FAB clears the bar — never let them overlap.

### 17.10 Range filter

```
track 2 px, color --pt-cn-color-neutral-200
thumb 8 px square, color --pt-cn-color-primary-550, border-radius 999
dual <input type="range"> stacked at the same position
values row beneath: display:flex; justify-content:space-between; margin-top:4;
                    font: --pt-cn-font-mono / body-sm
```

### 17.11 Collapsible filter group (sidebar)

```scss
.group-head {
  width: 100%;
  padding: 6 12 6 4;
  font: medium body-sm var(--pt-cn-font-medium);
  color: var(--pt-cn-color-neutral-950);
  display: flex; align-items: center; justify-content: space-between;
  background: transparent; border: 0;
}
.group-head svg                       { width: 16; transition: transform .25s ease; }
.group.is-open .group-head svg        { transform: rotate(180deg); }
.group-content {
  display: grid; grid-template-rows: 0fr;
  transition: grid-template-rows .25s ease-in-out, opacity .25s ease-in-out;
  opacity: 0;
}
.group.is-open .group-content         { grid-template-rows: 1fr; opacity: 1; }
```

Tag-cloud body: `flex-wrap; gap: 8; padding: 8 4`. List-variant body: `flex-direction: column; padding-left: 32`, 1-px vertical guide via `::before` at `left: 14`, active item gets a 4-px primary dot via `::after`.

### 17.12 Models-detail sticky reading layout

```
grid-template-columns: 240 minmax(0, 1fr) 240;
gap: 48;
align-items: start;

left rail:  position: sticky; top: calc(84 + 36); list of anchors; active dot
center:     max-width: var(--pt-cn-layout-max-read-box); margin: 16 auto 0
right rail: position: sticky; top: calc(84 + 36); "on this page" TOC
```

Anchor item recipe — reuse across docs/detail:
```scss
.anchor {
  width: 100%; height: 32;
  padding: 6 12 6 32;
  display: flex; align-items: center;
  font-size: var(--pt-cn-body-font-size-sm);
  color: var(--pt-cn-color-neutral-650);
  position: relative;
}
.anchor::before {                                         // vertical guide
  content: ''; position: absolute;
  left: 14; top: 0; bottom: 0;
  width: 1px; background: var(--pt-cn-color-line-100);
}
.anchor.is-active                  { color: var(--pt-cn-color-neutral-950); }
.anchor.is-active::after {                                // active dot
  content: ''; position: absolute;
  left: 12; top: 50%; transform: translateY(-50%);
  width: 4; height: 4; border-radius: 999;
  background: var(--pt-cn-color-primary-550);
}
```

### 17.13 Pricing range segmented tab  *(models/detail)*

Two-level pill: outer `neutral-150` track h36; inner tabs h28 with `radius-full; padding: 6 8`. Active: bg `neutral-50` + `--pt-cn-shadow-light` (the elevated-thumb pattern).

### 17.14 Interaction-layer review checklist

When building a models-like data page:

- [ ] All toolbar controls share `height: 40` and `border-radius: --pt-cn-radius-full`
- [ ] Search has `--pt-cn-color-line-100` resting border that **disappears** on focus and is replaced by the gradient mask-composite rim (`--pt-cn-gradient-4`)
- [ ] Sort trigger chevron rotates 90° → -90° on open
- [ ] Sort dropdown is borderless + `--pt-cn-shadow-light`; options are pills with `neutral-150` selected / `neutral-100` hover
- [ ] View toggle uses the segmented `neutral-150` track + `neutral-50` elevated thumb pattern
- [ ] Soft-fill CTAs (e.g. "Compare") use `primary-50` → `primary-150` hover, **no border**
- [ ] Grid view = `auto-fill, minmax(260, 1fr); gap 24/28`; List view drops columns at breakpoints rather than reflowing
- [ ] Cards reveal secondary actions on hover by fading metrics row, **not** by replacing the card
- [ ] Compare bar is glass + `--pt-cn-shadow-normal`, fixed bottom 24, with FABs computing `bottom` so they clear the bar
- [ ] Sticky rails use `top: calc(var(--pt-cn-nav-backdrop-offset) + 36)` for reading anchors

---

## 18. Layout review checklist

- [ ] **Marketing flat (§1.6):** 营销楼层无阴影；色阶交替；无灰底嵌套
- [ ] **长页编排：** 符合 §4.0 recipe（首页 / Token Plan / Hackathon）
- [ ] Picked the right container layer (inner default; outer only for framed visuals; reader for prose)
- [ ] Hero is exactly one of A–I; ≤1 gradient word; heading sits on canvas (`neutral-50`/`100`), **never** over a photo or video (except §2.3 era exception)
- [ ] **Home opener (variant B):** centered h1; **L1 `btn--primary` + L3 `btn--outline`**; **48–64 px** before `.hero-visual` (§2.7)
- [ ] **`.hero-visual`:** one mode — **A** 450–480 px **or** **B** 420 px showcase (§2.8)
- [ ] **Card row floor (§4.4):** 3/4-up; no shadow; `line-100` or one gradient rim; R9 + §8.16
- [ ] **Media duo (§4.5):** 2-up borderless; visual `radius-md`; text-link CTA; no pill buttons
- [ ] **Simple card (§4.6):** `line-100` no shadow; A step+floor CTA or B R11+price-text+chips
- [ ] **Secondary showcase (§4.7):** A tabs+R13 or B stacked head+R13b+pager; bottom hairline only
- [ ] **Logo floor (§4.8):** A 矩阵 R14 **或** B `.logo-strip` R19 无边透明
- [ ] **Tail visual (§4.9):** 790 or 370 px; R15; L1+L3; footer flush
- [ ] **Site footer (§4.10):** 35/65; R16; §8.24 social; legal line-100 bar
- [ ] **Carousel toggle (§4.11):** 100vw track; bordered or filled; §8.26; R17 or R18
- [ ] **FAQ (§4.12):** shell A/B；38/62；§8.27 单开；R20
- [ ] **Arena sync (§4.13):** 42/58；§8.28；R21
- [ ] Floor backgrounds alternate canvas / tinted / card-wash — no two adjacent floors with the same tint
- [ ] Floor-head matches pattern A/B/C/D; subtitle respects §9.4 width caps
- [ ] Grid pulls a row from the §7 grid table — column count + gap + mobile collapse all match
- [ ] Sticky offsets use `calc(var(--pt-cn-nav-backdrop-offset) + N)`; sidebar 240, gap 48
- [ ] Reader column = `var(--pt-cn-layout-max-read-box)`; legal/docs body never exceeds it
- [ ] Card classified through the §11.4 decision tree (A bordered / B borderless / C featured-rim / …); padding + radius from §11.5; one of the eight internal recipes §11.2
- [ ] Bordered vs borderless choice respects the "stepped panel ⇒ no border" rule (§11.1 B)
- [ ] **Panel-as-card** (recommended/cost/plan/feature/FAQ list blocks) is borderless outer + typography + hairline rows — no 1px outer hairline, no grey-bg inset sub-cards (§11.6)
- [ ] All ten "clean & flat" signals (§11.3) present — bg-step over chrome, hairlines only, hover lift via single shadow + 4-px Y, etc.
- [ ] Radius is one of the five working tokens (§15)
- [ ] Spacing values land on the 2-px rhythm; no orphan numbers
- [ ] Search / dropdown / segmented control / accordion follow §8.11–8.13 and §17.2–17.5
- [ ] Data-page interaction layer (if applicable) passes the §17.14 sub-checklist
- [ ] Mobile collapse follows §14; no per-breakpoint exceptions
- [ ] Console / dashboard pages reuse §08 card roots or `ui-*` primitives — no one-off card chrome

---

## 19. Component preview gallery (Guideline §08)

Guideline §08 is a **masonry gallery** of 53 production cards plus shared `ui-*` primitives — same tokens and React runtime as the 千问云 console (`Scripts/ui.js`).

### 19.1 Shell

```
.page-shell.page-home
  Nav (Guideline sticky nav)
  .page
    main.preview-grid[data-surface="chat"][data-ui-style="qianwenai"]
      .preview-grid__canvas          ← column masonry host
        .preview-grid__item × N      ← absolutely positioned tiles
          <Card specimen />           ← each root from components.md §08.3
```

| Property | Value |
|----------|-------|
| Max width | `var(--pt-cn-layout-max-width)` |
| Top padding | `108px` (clears nav) |
| Column gap | `--gap: 32px` (`--pt-cn-spacing-16`) |
| Columns | `--columns: 4` desktop; step down at breakpoints |
| Item width | `(canvasWidth - gap × (cols-1)) / cols` |

Mobile: reduce `--columns` to 2 → 1; keep `--gap` at 24–32 px.

### 19.2 When to use this layout

- **Guideline §08 only** — component catalog / design QA
- **Console dashboards** — borrow individual card roots (`analytics-card`, `invoice`, `kitchen-island`, …) inside `.layout-max-inner`; do **not** wrap marketing heroes in `preview-grid`
- Marketing pages still use §1–§18 patterns; pull card *anatomy* from §08, not the masonry shell

### 19.3 Card tile anatomy (all §08 specimens)

```
┌─ ui-card (radius-sm, neutral-50, hairline rim) ─────────┐
│  HEADER: title (semibold) + optional description          │
│  BODY: chart | form | list | media                        │
│  FOOTER (optional): secondary + primary actions           │
└──────────────────────────────────────────────────────────┘
```

- Flat by default — specimen rim is a 1px `color-mix` hairline, not a drop shadow
- Header/body gap: `24px` (`--pt-cn-spacing-12`)
- Chart cards: fixed aspect or min-height `200–280px`; legend mono `caption-md`
- Forms inside cards: pill inputs per `components.md` §08.2

### 19.4 Pairing with models toolbar (§17)

When a page mixes §08 cards with a models index:

1. Page shell + compact hero D (`layouts.md` §3)
2. Sticky toolbar (`ui-models-filter-*`) — full width inner
3. Card grid **or** §08 analytics stack below — never duplicate filter chrome inside each card
