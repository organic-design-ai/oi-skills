# Qwen Cloud — Page Layouts

Page-level composition. Tokens: `tokens.md` (`--pt-*`). Components: `components.md`. Icons/photos: manifest (`icons.md`, `assets.md`).

**Reuse existing tokens. Do not invent new ones.** Spacing is written as literal px on a 2-px rhythm; pick from `{4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 44, 48, 56, 64, 72, 96, 122}`.

---

## 1. Page shell & container scope

### 1.1 The page nests in three layers

```
┌──────────────────────────────────────────────────────────────────┐
│  viewport (100vw)                                                │
│                                                                  │
│   ┌─ .layout-max-wide ─ outer ─────────────────────────────┐    │   ← gutter ≈ 36 px
│   │   max-width: calc(--pt-layout-max-width + 72px)        │    │
│   │   padding: 0 36px                                      │    │
│   │                                                        │    │
│   │   ┌─ .layout-max-inner ─ inner ─────────────────┐     │    │
│   │   │   max-width: var(--pt-layout-max-inner)     │     │    │   ← gutter ≈ 140 px from viewport
│   │   │   (wrap padding: 8px 36px 0)                │     │    │
│   │   │                                             │     │    │
│   │   │   ┌─ reader ─ var(--pt-layout-max-read-box)  │     │    │
│   │   │   │   768 px cap, centered                  │     │    │
│   │   │   └─────────────────────────────────────────┘     │    │
│   │   └─────────────────────────────────────────────┘     │    │
│   └────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

Three width tokens, three layers — never bypass:

| Token | Value | Class | What sits here |
|-------|-------|-------|----------------|
| `--pt-layout-max-width` | `min(100vw - 140px, 1920px)` | `.layout-max-wide` (outer) | Full-bleed framed visuals: hero image/video panel, era CTA, bulletin, marketplace carousel |
| `--pt-layout-max-inner` | `min(100vw - 280px, calc(1920px - 140px))` | `.layout-max-inner-wrap > .layout-max-inner` (inner) | **Default for everything else**: headings, section heads, grids, copy, tabs, filters |
| `--pt-layout-max-read-box` | 768 px | (utility — `width: min(100%, var(--pt-layout-max-read-box))`) | Long-form prose: legal, docs body, skills-detail body, models-detail body, hero subtitle |

### 1.2 Decision rule (must follow)

- **Outer (`.layout-max-wide`)** — only when the section's visual content is itself a framed media panel (video, photo, carousel, big rounded surface) that should reach near the viewport edges. Outer is wider — 140 px viewport gutter — so visuals breathe.
- **Inner (`.layout-max-inner`)** — for everything else. **Headings, subtitles, section heads, grids, paragraphs, filter rails, cards, accordions, FAQ, tables, forms.** Inner is narrower (280 px viewport gutter) — text gets more whitespace and is easier to scan.
- **Reader** — nest *inside* inner. Long-form prose (>3 paragraphs), legal/docs/skills-detail body. Cap at 768 px and center.

**A hero typically uses both:** the H1/subtitle stack lives in **inner**, then the image/video panel below lives in **outer**. Don't put the giant heading in the outer wrap — see §2.1.

### 1.3 Shell skeleton

```jsx
<div className="page-shell page-<name>">
  <Nav />                                {/* sticky, 84 px desktop / 62 px mobile */}
  <div className="page">                 {/* min-height:100vh; bg: --pt-color-neutral-50; pb: 48px */}

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

- Nav var: `--pt-nav-backdrop-offset: 84px` desktop · `62px` ≤1024
- Sticky filter / TOC rails: `top: calc(var(--pt-nav-backdrop-offset) + 12px)`
- Read-section sticky headings: `top: calc(var(--pt-nav-backdrop-offset) + 8px)`
- Mobile sticky bars (search dropdown, compare bar): `top: calc(var(--pt-nav-backdrop-offset) + 8px)`

### 1.5 Section vertical rhythm (between floors)

Between top-level "floors" (sibling sections of the page):

- `margin-top: 96px` (compact) · `122px` (default) · `138px` (loose, between major chapters)

Inside a floor (between its head and its grid/body):

- `margin-bottom: 48px / 60px / 64px` on the head

Mobile (≤1024 px): collapse to `64 px` between floors, `32 px` head→body.

### 1.6 Marketing flat contract  ★

Guideline long-scroll pages (Home, Token Plan, Hackathon) share one **planar** system. Apply to every §4 marketing floor unless §17 data-page rules explicitly override.

| Rule | Spec |
|------|------|
| **Shadow** | Marketing cards, floors, logo tiles, FAQ rows, arena sync visual: **`box-shadow: none`** default |
| **Separation** | Background steps only — `neutral-50` canvas ↔ `neutral-100` tinted ↔ `gradient-card-bg` panel (§4.1). **Never** stack two identical tints |
| **Borders** | `line-100` hairline on comparison cards, logo matrix A, outline buttons — **not** around panel-as-card blocks (§11.6) |
| **Hover** | Marketing comparison cards: **no** `translateY` lift. Logo matrix: border darken only. Data pages may lift per §11.3 |
| **CTAs** | Hero / tail openers: **Level 1 `btn--primary` + Level 3 `btn--outline`** only (§2.7). Inside pricing cards: `btn--secondary` default, one `btn--primary` on featured tier |
| **Gradient words** | ≤1 clipped phrase per viewport; buttons stay solid black or outline — **no** gradient fills on pills |
| **Nested chrome** | No grey inset sub-cards inside pricing, FAQ, or panel lists — typography + one hairline (§11.6) |
| **Imagery** | Title on canvas; photos in framed panels (§2). Tail visual is the §2.5 exception |

Qianwen AI: prefer `--pt-cn-gradient-1/2/3/8` for headline clips; Qwen Cloud intl: `--pt-gradient-1/2/3`. See each kit `tokens.md`.

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
│   ║░░░░░░░ purple/pink flower / abstract / video ░░░░░░░░║    │
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

The Token Plan page does the same: "Qwen Cloud Token Plan" sits centered on white at top, the lavender card with screenshots starts BELOW it with clear whitespace. The image never reaches up to touch the heading.

### 2.2 Anti-patterns — never do these

- ❌ H1 / H2 (≥36 px) physically overlapping a photo, video, abstract gradient, flower, or any visual asset
- ❌ Hero panel that contains both the giant heading AND the imagery in the same rectangle
- ❌ Adding `text-shadow`, blur layer, or dark overlay to "make the heading readable on the photo" — if you need that, the heading is in the wrong place
- ❌ A heading positioned absolute inside a `.hero-panel` that has `background-image`
- ❌ Centering an H1 on top of `--pt-gradient-card-bg` so the gradient ladders behind the type
- ❌ "Filling" empty whitespace above an image by sliding the heading down into it

### 2.3 The canonical arrangement

```
┌── .layout-max-inner ─────────────────────────────────────┐    ↑ on --pt-color-neutral-50
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
│  │  border-radius: var(--pt-radius-md or lg)          │    │ │   visual only
│  │  object-fit: cover                                 │    │ │   in its own card
│  │  optional small overlay (metric chips, see §8.1)   │    │ │
│  └────────────────────────────────────────────────────┘    │ │
└─────────────────────────────────────────────────────────────┘ ↓
```

Two **separate paragraphs**, in this order:

1. **Title paragraph** — eyebrow + H1 + subtitle + CTAs. Lives in `.layout-max-inner`. Background: `--pt-color-neutral-50` (canvas). Nothing visual, just type.
2. **Visual paragraph** — image / video panel. Lives in `.layout-max-wide` (or stays in inner). Its own rounded card. Plenty of whitespace above (`margin-top: 48–64 px`) separating it from the title paragraph.

This is what makes pages like Qwen Cloud "Ship the next" and Cohere's Security/Deployment/Customization (line icons + headline on clean white, hero photo as a separate band below) feel calm — title and visual are **never in the same box**.

### 2.4 Hard rules

- **Heading (≥36 px) sits on `--pt-color-neutral-50`** (canvas) or `--pt-color-neutral-100` (tinted floor — also neutral, no imagery). Not on any photo, video, gradient, or flower image.
- **Subtitle paragraph** sits with the heading, on the same canvas, never on imagery.
- **Image / video lives in its own card** with `border-radius: var(--pt-radius-md)` or `lg`. The image's top edge is **at least 32 px** below the bottom of the title paragraph.
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
- Content is **centered**, the panel is **790 px** tall (§4.9; legacy CSS may read 780 px) — extreme whitespace inside.
- A **glass / blurred backdrop** sits behind the CTA pill (not the heading) for the form input only.
- This is a closing footer beat — not the page-leading hero.

If you're not building this exact closing-CTA pattern with these constraints, **stack vertically — title paragraph above, visual paragraph below.**

### 2.6 Where headings ARE allowed on a stepped surface

`neutral-100` (tinted floor) is fine. `--pt-gradient-card-bg` (almost-flat 135° wash from `neutral-150` → `neutral-50`) is fine for the two-column panel head (§5 pattern C). These are *quiet neutral bg steps* — they read as canvas, not imagery.

Imagery means: photographs, videos, flower / abstract / liquid renders, animated gradients, glass blur over a photo. Stepped neutrals are NOT imagery.

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
    font-size: var(--pt-heading-font-size-2xl);           // 72 — or clamp(72px, 8vw, 96px)
    line-height: var(--pt-heading-line-height-2xl);
    font-family: var(--pt-font-bold);
    letter-spacing: var(--pt-letter-spacing-tight);
    color: var(--pt-color-neutral-950);
    margin: 0;
    max-width: min(100%, 920px);                          // soft wrap; still centered
  }

  .hero-sub {
    margin: 16px auto 0;
    max-width: var(--pt-layout-max-read-box);             // 768 px
    font-size: var(--pt-body-font-size-lg);
    line-height: var(--pt-body-line-height-lg);
    color: var(--pt-color-neutral-650);
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

- **H1 is always center-aligned** on `--pt-color-neutral-50`. At most **one** gradient-clipped `<span>` inside the h1.
- **Subtitle** sits with the h1 on canvas — never inside `.hero-visual`.
- **Eyebrow** (optional): mono `caption-sm`, uppercase, `neutral-450`, above h1; does not replace the subtitle.

#### CTA pairing — Level 1 + Level 3 only  *(homepage hero)*

Home hero CTAs use exactly **two** buttons in this order — not `btn--secondary` (purple soft fill):

| Slot | Component | Role |
|------|-----------|------|
| **Level 1** | `btn--primary` | Black pill (`cta-fill` → hover `primary-550`); leading action |
| **Level 3** | `btn--outline` | Transparent + `1px line-200`; quiet secondary path |

```
✅ RIGHT — Hackathon / home hero
[ Apply as a VC Partner ]  [ View credit tiers ]
     btn--primary               btn--outline

❌ WRONG — primary + secondary soft-fill on home hero
[ Try now ]  [ Get API keys ]        ← secondary purple fill competes with L1 on marketing openers
     primary      secondary

❌ WRONG — three buttons or text-only tertiary
[ Primary ] [ Outline ] [ Text link ]   ← max two CTAs on the title stack
```

- Icon on Level 1 only: `arrow-up-outlined` trailing.
- Level 3 has **no** icon unless the label is an external link (then optional `arrow-up-right-outlined` 14 px).
- Card / pricing / floor bodies may still use `primary + outline` or `primary + secondary` — the **L1+L3 lock applies to the homepage title paragraph** and any page that copies this opener (Token Plan, campaign landings).

#### Spacing — 字不压视觉

| Gap | Value | Rule |
|-----|------:|------|
| Nav → title stack | `48–64 px` | `margin-top` on `.hero-head` |
| H1 → subtitle | `16 px` | stack `gap` or sub `margin-top` |
| Subtitle → CTA row | `36 px` | `.hero-cta-row { margin-top: 36px }` |
| **CTA row → visual panel** | **`48–64 px`** | `margin-top` on `.hero-visual` — **minimum 48 px**; never pull the panel up with negative margin |
| Visual → next floor | `96–122 px` | §1.5 default floor rhythm |

The visual panel's top edge must **never** overlap or touch the title paragraph. Whitespace is intentional — do not "fill" it by enlarging the image or sliding type down.

### 2.8 Hero visual panel — shared chrome & two modes

`.hero-visual` is the **single large rounded block** below the title stack. It always lives in `.layout-max-wide`. Pick **one mode** per page.

#### Shared shell (both modes)

```scss
.hero-visual {
  margin-top: 48px;                                       // 64 px when title block is short
  width: 100%;
  border-radius: var(--pt-radius-lg);                     // 36 px — pronounced corners
  overflow: hidden;
  position: relative;
  isolation: isolate;
}
```

- **No border, no shadow** on the shell — the radius + content (or bg-step) carries separation.
- Heading / subtitle / CTAs stay **outside** this element (§2.7).
- Mobile (≤1024 px): keep `radius-lg`; reduce horizontal bleed via outer gutter only — do not shrink radius to `md`.

#### Mode A — Hero media  *(`.hero-visual--media`)*

Reference: **Global AI Hackathon** hero — floral / abstract full-bleed with optional metric strip.

```
┌─ .hero-visual--media  h: 450–480 ─────────────────────────────┐
│  ┌─ optional metric row (4-up, §8.1) ─────────────────────┐  │
│  │  ● 10B+ TPM    ● Scaling    ● Optimal    ● Ultra-Low   │  │
│  └────────────────────────────────────────────────────────┘  │
│  ░░░░░░░░░░  flower_* / video cover  object-fit: cover ░░░░░  │
└───────────────────────────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Height | **`450 px`** (minimal overlay) · **`460 px`** (default) · **`480 px`** (4-up metrics + airy padding) — pick one; do not exceed 480 on home |
| Media | One `flower_*` from `Images.json` **or** cover video; `object-fit: cover`; `width/height: 100%` |
| Background | Image/video only — not `gradient-card-bg` |
| Overlay | Optional **4-up metric chips** (§8.1) along top inside panel; `padding: 32–40px`; text ≤ title-lg (28 px) |
| Text on media | Metrics + caption-md mono only — **no h1/h2** |

```scss
.hero-visual--media {
  height: 460px;                                          // 450 | 480 per table above
}
.hero-visual--media__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.hero-visual--media__metrics {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: clamp(16px, 3vw, 40px);
  padding: 36px 40px 0;
}
```

Mobile: height `min(420px, 56vw)`; metrics → `repeat(2, 1fr)` 2×2 grid.

#### Mode B — Info showcase  *(`.hero-visual--showcase`)*

Reference: **Token Plan** — lavender wash panel; **left accordion drives right preview** (fold / expand per item). Mid-page **Choose Your Arena** variant (taller visual, centered head above split): **§4.13** — not inside `.hero-visual`.

```
┌─ .hero-visual--showcase  h: 420  bg: gradient-card-bg ────────┐
│  ┌─ accordion col ─────────┐  ┌─ preview col ────────────────┐ │
│  │  </> Multiple models  + │  │  ░░ product screenshot ░░  │ │
│  │  ─────────────────────  │  │  ░░ floating UI chrome ░░  │ │
│  │  ▣ Seamless toolchain   │  │                              │ │
│  │     expanded body copy    │  │                              │ │
│  │  ─────────────────────  │  │                              │ │
│  │  $ Higher quota       + │  │                              │ │
│  └──────────────────────────┘  └────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Height | **`420 px` locked** — do not use 380 / 540 on this mode |
| Background | `var(--pt-gradient-card-bg)` — quiet wash; reads as canvas step, not photograph (§2.6) |
| Padding | `60px 44px` desktop · `32px 20px` mobile |
| Grid | `grid-template-columns: 1fr 1fr; gap: 64px; align-items: stretch; height: 100%` |
| Left | Accordion list (§8.6, §11.2 R4): icon + title row + `+` when collapsed; expanded item shows body-sm, hides `+` |
| Right | `.hero-visual-preview` — stacked absolute panels; one `.is-active`; cross-fade `opacity` + `--pt-motion-fast` |
| Interaction | Click / keyboard activate accordion item → swap active preview panel (no autoplay carousel) |

```scss
.hero-visual--showcase {
  height: 420px;
  background: var(--pt-gradient-card-bg);
  padding: 60px 44px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
}
.hero-visual-preview {
  position: relative;
  min-height: 0;
}
.hero-visual-preview-panel {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity var(--pt-motion-fast) ease;
  pointer-events: none;
}
.hero-visual-preview-panel.is-active {
  opacity: 1;
  pointer-events: auto;
}
```

Mobile: single column — accordion full width; preview **below** active item (`height: auto`; min preview `240px`); outer shell `height: auto; min-height: 420px`.

#### Mode picker

| Page intent | Mode | Visual height |
|-------------|------|---------------|
| Home, campaign, Hackathon — one strong photograph | **A — media** | 450–480 px |
| Product explainers, Token Plan, feature walkthrough | **B — showcase** | 420 px |
| Tagline + code panel (no big visual) | §3 variant **A** — no `.hero-visual` | — |

Never stack Mode A and Mode B on the same page. Never put the title stack inside either mode.

---

## 3. Hero variants

Pick exactly one per page. Never stack two heroes. All variants follow §2 — title on canvas, imagery framed below or beside.

### A. Split tagline hero  *(home tagline)*

Two-column inside `.layout-max-inner`.

- Grid: `minmax(0,1fr) minmax(320px, 392px)` · `gap: 44px` · `margin-top: 64px`
- Left: H1 `--pt-heading-font-size-xl` (64/68), letter-spacing tight, **one** `<span>` gradient-clipped. Sub `--pt-body-font-size-lg`, `max-width: 680px`. CTA row `inline-flex; gap: 10px; margin-top: 36px`.
- Right: bordered command/code panel — `border: 1px solid var(--pt-color-line-100); border-radius: var(--pt-radius-md)`. Both columns on canvas — no imagery in this hero.
- Mobile: 1 column; right panel drops below.

### B. Stacked center hero  *(home, campaign, Token Plan opener)*

**Canonical homepage layout — full spec in §2.7–§2.8.** Two-piece: centered title stack in inner → `.hero-visual` in outer.

```
.layout-max-inner-wrap
  .layout-max-inner
    .hero-head
      h1          (centered, 2xl–3xl, on neutral-50, ≤1 gradient word)
      .hero-sub   (centered, max-width: var(--pt-layout-max-read-box))
      .hero-cta-row
        btn--primary          ← Level 1
        btn--outline          ← Level 3  (not btn--secondary)
.layout-max-wide
  .hero-visual
    .hero-visual--media      Mode A: 450–480 px, flower_* / video, optional metrics
    — or —
    .hero-visual--showcase    Mode B: 420 px, accordion + preview (Token Plan)
```

- **Title stack:** §2.7 — centered h1, subtitle, **Level 1 + Level 3** CTAs only.
- **Visual panel:** §2.8 — `border-radius: var(--pt-radius-lg)`; **48–64 px** below CTAs (字不压视觉).
- **Mode A height:** `450–480 px` (default `460`) — not the legacy `540–720` band; reserve taller panels for §3 variant F (era CTA) only.
- **Mode B height:** `420 px` locked; `gradient-card-bg` + synced accordion/preview.
- H1 size: `--pt-heading-font-size-2xl` (72) or `clamp(72px, 8vw, 96px)` on home; ultra-marketing `3xl` only when copy is very short.
- Sub color: `--pt-color-neutral-650`; CTA row `margin-top: 36px`.

### C. Centered intro hero  *(skills-detail, docs-adjacent)*

`.intro-header { display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center }`

- H1: `--pt-heading-font-size-lg` (60), letter-spacing tight, on canvas.
- `.heading-desc`: body-lg, color `--pt-color-neutral-750`, `max-width: 560–620 px`.
- **Token Plan / coding-plan openers** should use **variant B + §2.8 Mode B** (title stack + `.hero-visual--showcase` 420 px) — not a separate smaller intro panel.
- Legacy inline showcase: `gradient-card-bg` + `radius-md` + `padding: 60px 44px` only when variant B is not used.

### D. Compact left-aligned hero  *(models, models/detail, models/compare, docs)*

Heading row inside `.layout-max-inner`.

- `display: flex; align-items: flex-end; justify-content: space-between; gap: 24px; margin-bottom: 50px`
- H1: `--pt-heading-font-size-md` (44) or `--pt-heading-font-size-sm` (36) for sub-pages
- Right side: actions (filter button, share, theme toggle, breadcrumb)
- Subtitle: body-md, color `--pt-color-neutral-800`, `margin: 12px 0 48px`

### E. Docs panel hero

Tinted inset panel, not full-bleed.

- `.docs-content-panel`: `background: var(--pt-color-neutral-100); border-radius: var(--pt-radius-lg); padding: 40px 48px`
- Inside: `grid-template-areas: 'heading actions'; grid-template-columns: minmax(0,1fr) auto`
- Breadcrumb row above (`max-width: var(--pt-layout-max-read-box)`)

### F. Era / closing CTA hero  *(closing block — see §4.9)*

The only variant where text overlays imagery (§2.3 exception). Full spec: **§4.9 tail visual CTA**.

- **Tall:** `790px` (`.tail-visual--tall` / legacy `.era-hero-shell` ~780 px) in `.layout-max-wide`
- **Compact:** `370px` (`.tail-visual--compact`) for community / program closes
- `border-radius: var(--pt-radius-lg)`; centered h2 ≤72 px (tall) or ≤44 px (compact)
- Level 1 `btn--primary` + Level 3 `btn--outline`; optional kicker with §8.23 inline link
- Quiet gradient / flower / video backdrop — art-directed for legibility

### G. Marketplace carousel hero  *(models)*

Heading inside inner, carousel breaks out to viewport right edge.

- Heading row: `display: flex; align-items: flex-end; justify-content: space-between; margin-bottom: 50px`
- Carousel track: `padding-left: max(20px, calc((100vw - var(--pt-layout-max-width)) / 2))` so cards align to inner gutter but overflow right
- Cards: 588×244, gap 24, `border-radius: var(--pt-radius-md)`

### H. Reader-column hero  *(legal, docs body, skills-detail body)*

Long-form prose. See §6.

### I. Asymmetric skill hero  *(organic skills, ref pattern)*

Two-column grid `1fr 6fr; gap: 120px` inside inner. Left = small meta caption (mono, body-sm). Right = giant H1 (--pt-heading-font-size-xl, 64 px) with optional gradient segment + inline install command box. Used for "documentation-leading" pages where a single artifact (skill, model, doc) is the subject.

---

## 4. Floor (section) taxonomy

A "floor" is one top-level section of the page. Floors stack vertically with §1.5 rhythm. All marketing floors obey **§1.6 flat contract** (no shadow, bg-step separation).

### 4.0 Canonical marketing page stacks  ★

Reference scroll compositions from Guideline. Pick one recipe; **do not** invent floor order. Alternate §4.1 backgrounds between siblings.

#### Home — `Ship the next` (long marketing)

| # | Floor | § | Notes |
|---|-------|---|-------|
| 1 | Hero title + media | §2.7 B + §2.8 **Mode A** | Centered h1; flower / `qwen-model-*` 450–480 px |
| 2 | Featured models + tabs | model cards | `line-100` or borderless on stepped bg; no shadow |
| 3 | Industries / solutions | §4.7 **A** | Secondary text-cards; bottom hairline |
| 4 | Customer stories | §4.11 **A** | 100vw testimonial carousel; optional |
| 5 | Logo strip | §4.8 **B** | Borderless partner row |
| 6 | Tail visual | §4.9 **tall** 790 px | Co-Build Future pattern |
| 7 | Footer | §4.10 | Flush under tail |

#### Token Plan / Coding Plan

| # | Floor | § | Notes |
|---|-------|---|-------|
| 1 | Hero title + showcase | §2.7 B + §2.8 **Mode B** | Accordion **inside** `.hero-visual` 420 px — **not** §4.13 |
| 2 | Pricing / limited offer | §4.4 **4-up** | `line-100` cards; Enterprise/Personal toggle §8.4; one featured rim |
| 3 | Supported tools | §4.8 **A** | Logo matrix `line-100` tiles |
| 4 | FAQ | §4.12 shell **B** | `neutral-100` `radius-lg` in `layout-max-wide` |
| 5 | Footer | §4.10 | Often **no** §4.9 tail between FAQ and footer |

#### Hackathon / Campaign

| # | Floor | § | Notes |
|---|-------|---|-------|
| 1 | Hero | §2.7 B + §2.8 **Mode A** | Campaign photo + optional metrics |
| 2 | Prizes | §4.4 **3-up** | Equal cards; featured center optional |
| 3 | Arena / tracks | §4.13 **or** §4.6 A | Accordion+visual **or** step cards |
| 4 | Partners | §4.8 **B** | Our Partners strip |
| 5 | Community CTA | §4.9 **compact** 370 px | Join the community |
| 6 | Footer | §4.10 | |

**§4.13 vs §2.8 Mode B:** Token Plan accordion lives in the **hero visual box** (420 px). **Choose Your Arena** is a **mid-page** §4.13 floor (taller right visual, centered head above). Never duplicate both on one page.

### 4.1 Floor backgrounds (the alternation rule)

Only three planes — alternate them; **never put two floors of the same tint adjacent**:

| Plane | Color | When to use |
|-------|-------|-------------|
| Canvas | `--pt-color-neutral-50` | Default floor |
| Tinted | `--pt-color-neutral-100` | Every 2nd or 3rd floor for visual rhythm; data-dense floors that need contrast from canvas |
| Card-wash | `--pt-gradient-card-bg` (`135deg, neutral-150 → neutral-50`) | A floor that *is* a single panel (e.g. AI-powered-product, FAQ panel, intro showcase) — wrap the whole floor in one rounded box |

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
- **Hero floor (home variant B):** title stack (content-driven) + visual panel **450–480 px** (Mode A) or **420 px** (Mode B showcase); see §2.7–§2.8.
- **Hero floor (era / other):** up to **780 px** panel (§3 variant F only).
- **Bulletin floor:** `--pt-bulletin-height: 306px` (24-px padding mobile, 70-px desktop) — pinned strip for announcements.
- **Stacking scroll floor:** `height: 180vh` with `position: sticky` interior — for scroll-choreographed reveals (rare; e.g. featured model stack on home).
- **Closing CTA floor / tail visual:** **790 px** tall (§4.9) or **370 px** compact — §3 variant F; legacy `.era-hero-shell` ≈780 px.
- **Card row floor:** content-driven height; 3-up or 4-up equal cards (§4.4) — pricing, token plans, prize pools.
- **Media duo floor:** 2-up borderless visual cards (§4.5) — agent builder, capability pairs; text-link CTAs.
- **Simple card floor:** 3-up `line-100` skill/step cards (§4.6) — tag, price-text, metrics; no shadow.
- **Secondary showcase:** tabs + text-only cards (§4.7) — bottom hairline only; supports primary floors.
- **Logo matrix / strip:** §4.8 — **A** bordered 4×N tiles (`line-100`, icon + name) **or** **B** borderless partner logo row (no chrome).
- **Tail visual CTA:** 790 px or 370 px closing panel (§4.9) — centered copy + buttons on art-directed backdrop; immediately above footer.
- **Site footer:** 35 / 65 asymmetric link grid + legal bar (§4.10) — flush under tail visual.
- **Carousel toggle:** 100vw card track + ‹ › pager (§4.11) — `line-100` or `neutral-100` cards, no shadow.
- **FAQ:** two-column accordion (§4.12) — inner `neutral-50` **or** wide `neutral-100` panel; single-open `+` accordion.
- **Accordion + visual sync:** left fold list drives right preview (§4.13) — e.g. Choose Your Arena.

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
| **3-up** | Wider cards, simpler choice (prize tracks, 3 tiers) | Prizes $65,000+ |
| **4-up** | Dense SKU / credit grid | Token Plan monthly tiers |

Pick **one** count per row — never mix 3 and 4 in the same grid. All siblings share the same internal recipe (§11.2 **R9**).

#### Floor shell

```jsx
<section className="floor floor--card-row">
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <header className="floor-head">…Pattern A…</header>
      {/* optional — only when two card sets (Enterprise / Personal): */}
      <div className="card-row-toggle" role="tablist">…§8.4 segmented…</div>
      <div className="card-row-grid card-row-grid--3">   {/* or --4 */}
        <article className="card-row-item">…</article>
        <article className="card-row-item is-featured">…</article>
        …
      </div>
    </div>
  </div>
</section>
```

- Floor bg: **canvas** (`--pt-color-neutral-50`). Cards carry their own chrome — **do not** wrap the row in an extra bordered panel or `gradient-card-bg` shell.
- Head → grid: `margin-bottom: 48px`. When a toggle sits between head and grid: toggle `margin-bottom: 40px`, head `margin-bottom: 32px`.
- Toggle (optional): centered pill segmented control (§8.4); swaps visible card set — only **one** grid visible at a time.

#### Grid

Pull from §7 — do not invent column counts.

```scss
.card-row-grid {
  display: grid;
  align-items: stretch;                                  // equal-height cards
  gap: 24px;
}
.card-row-grid--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.card-row-grid--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
```

| Variant | Columns | Gap | Notes |
|---------|---------|----:|-------|
| 3-up | `repeat(3, minmax(0, 1fr))` | 24 | Prizes, 3-tier pricing |
| 4-up | `repeat(4, minmax(0, 1fr))` | 24 | Token / credit plans |

≤1024 px: collapse to `1fr`, gap **18**. Default is **vertical stack** — not a shrunken 4-column grid. Optional compare carousel: `overflow-x: auto; scroll-snap-type: x mandatory` with each card `min-width: min(100%, 320px); scroll-snap-align: start` only when product requires side-by-side on phone.

#### Card chrome — no shadow, hairline or gradient rim only

Card-row items are **flat comparison tiles** on canvas — archetype **A** (§11.1). **Not** panel-as-card (§11.6).

| State | Border | Fill | Radius | Padding | Shadow |
|-------|--------|------|--------|---------|--------|
| Default `.card-row-item` | `1px solid var(--pt-color-line-100)` | `--pt-color-neutral-50` | `--pt-radius-sm` (18) | 32 | **none** |
| Featured `.card-row-item.is-featured` | **Gradient rim** (§11.1 C) — hairline removed | same `neutral-50` | inherit | 32 | **none** |

```scss
.card-row-item {
  display: flex;
  flex-direction: column;
  background: var(--pt-color-neutral-50);
  border: var(--pt-line-size-normal) solid var(--pt-color-line-100);
  border-radius: var(--pt-radius-sm);
  padding: 32px;
  box-shadow: none;
}
.card-row-item.is-featured {
  position: relative;
  isolation: isolate;
  border-color: transparent;
}
/* gradient rim ::before — copy §11.1 C verbatim; --pt-gradient-2 default */
```

**Hard rules for this floor:**

- **No `box-shadow`** on default or featured cards.
- **No hover lift** (`translateY`, shadow on `:hover`) — these are not marketplace cards.
- Interior is **solid `neutral-50`** — no `gradient-card-bg`, no `neutral-100` inset blocks per feature.
- **At most one** `.is-featured` per visible row.
- Featured rim: `--pt-gradient-2` (token plans) or `--pt-gradient-1` (warm prize emphasis) — one gradient per row, not per card.

#### Internal anatomy — three zones (R9)

Every card in the row uses the **same vertical stack**. Top → bottom:

```
┌─ .card-row-item ────────────────────────────────────────────────┐
│  ZONE A — identity + price                                        │
│    plan name (semibold)                    [Hot] optional         │
│    $698  / month          ← price bold + period suffix sm/grey    │
│    120,000 credits/month  (+ info icon 14px)                      │
│    Renews at $5.60/month  ← meta, body-sm neutral-650             │
│                                                                   │
│  ZONE B — CTA                                                     │
│    [ Subscribe ]  full-width pill                                 │
│                                                                   │
│  ─── border-top 1px line-100 ───  ZONE C ───                      │
│    🔔 Includes credits for …        ← icon + text row §8.16       │
│    ✦ 3× usage of …                                                │
│    · qwen3.5-plus   ← nested bullets, body-sm neutral-650         │
└───────────────────────────────────────────────────────────────────┘
```

**ZONE A — header + price** (`flex-direction: column; gap: 8–12px`)

| Element | Typography | Color |
|---------|------------|-------|
| Plan name | `body-lg` or `title-md`, `--pt-font-semibold` | `neutral-950` |
| Hot badge | pill `tag-hot` — `--pt-gradient-6` fill or `primary-50` / `primary-550` | featured only |
| Price amount | `title-lg` (28) or mono `title-lg`, `--pt-font-bold` | `neutral-950` |
| Period suffix (`/ month`, `First month`) | `body-sm` inline after price | `neutral-550` |
| Credits / renewal meta | `body-sm` | `neutral-650` |
| Info hint icon | 14 px manifest icon, `neutral-450`, inline after meta | optional |

Name row: `display: flex; align-items: center; gap: 8px; flex-wrap: wrap`.

**ZONE B — CTA** (`margin-top: 20px`)

- Button: **full width**, pill (`--pt-radius-full`), height 40–48 px.
- Default siblings: `btn--secondary` (`primary-50` fill, `primary-550` text).
- Featured card only: `btn--primary` (black fill → purple hover).
- **No** `btn--outline` inside card rows.

**ZONE C — feature list** (`margin-top: 24px; padding-top: 20px; border-top: 1px solid var(--pt-color-line-100)`)

- Rows: §8.16 icon + text — left-aligned, `gap: 10–12px`, `margin-bottom: 12–16px` between rows.
- Primary feature line: `body-md` `--pt-font-semibold` `neutral-950`.
- Secondary / nested: `body-sm` `neutral-650`; nested model list uses `padding-left: 22px` (align under text, not icon) + `·` or 3 px primary dot — **not** a grey rounded sub-card.
- Icons: 16 px, `currentColor`, `neutral-750` — `notification-outlined`, `sparkle-outlined`, `check-outlined` (`icons.md`). One icon per row; no icon grids.

#### Featured vs default — one row, one hero tier

| Element | Default cards | `.is-featured` |
|---------|---------------|----------------|
| Border | `1px line-100` | Gradient rim only |
| CTA | `btn--secondary` | `btn--primary` |
| Badge | — | optional `Hot` |
| Shadow / hover | none | none |

#### Anti-patterns

```
❌ box-shadow or hover lift on card-row items
❌ gradient-card-bg fill inside the card
❌ grey neutral-100/150 rounded box per feature row (card-in-card)
❌ outer panel-as-card wrapping the whole 3/4 grid (§11.6)
❌ mixed 3+4 columns in one row
❌ two .is-featured cards
❌ btn--outline or tertiary text link as the row CTA
❌ chips rail + Hot badge + tier tag on the same card
```

#### Checklist (card row floor)

- [ ] Pattern A floor-head; optional §8.4 toggle for dual card sets
- [ ] Grid from §7 card-row 3-up or 4-up row — gap 24, stretch align
- [ ] Each `.card-row-item`: `neutral-50`, `radius-sm`, pad 32, **shadow: none**
- [ ] Default: `line-100` hairline; featured: gradient rim (§11.1 C), ≤1 per row
- [ ] R9 zones A → B → divider → C; features via §8.16 only
- [ ] CTA: secondary on siblings, primary on featured only

### 4.5 Media duo floor — visual 2-up, borderless cards  ★

**Visual-led feature row:** 1 row × **2 columns**, each column is a **borderless** card — large rounded **media frame** on top, left-aligned copy + text-link CTA below. Reference: **Become an agent builder** (Agent builder · Agents SDK).

```
┌── floor — canvas neutral-50 ──────────────────────────────────────────┐
│           h2  centered   "Become an **agent builder**" (≤2 grad words) │
│           subtitle  body-lg  neutral-750  centered  max 620px          │
│                                                                       │
│   ┌─ media-duo-item (no border, no shadow) ─┐  ┌─ media-duo-item ─┐ │
│   │ ┌──────────────────────────────────────┐ │  │ ┌────────────────┐ │ │
│   │ │ ░░ abstract / video  radius-md ░░░░ │ │  │ │ ░░ visual ░░░░ │ │ │
│   │ │ </> 20px white icon  top-left       │ │  │ │  icon  top-left │ │ │
│   │ └──────────────────────────────────────┘ │  │ └────────────────┘ │ │
│   │  Agent builder          ← title left    │  │  Agents SDK         │ │
│   │  Accelerate your workflow…  2-line clamp│  │  Build agents…      │ │
│   │  Get started ↗            text CTA      │  │  View docs ↗ purple │ │
│   └────────────────────────────────────────┘  └──────────────────────┘ │
└───────────────────────────────────────────────────────────────────────┘
```

**Contrast with §4.4:** card-row floors use **hairline / gradient-rim boxes** + pill Subscribe buttons. Media duo uses **no card chrome** — the photograph/video frame + typography + whitespace separate the units.

#### When to use

| Floor | Cards | CTA | Media |
|-------|-------|-----|-------|
| **§4.5 Media duo** | 2-up, **borderless** | Text link + arrow (`btn--text`) | Large `radius-md` visual on top |
| §4.4 Card row | 3/4-up, `line-100` or rim | Full-width pill `btn--secondary` / `primary` | None (typography-only body) |
| §11.1 model-feature 2-col | 2-up bordered optional | Pill in card footer | Optional inset, not hero visual |

Use media duo for **product capability pairs** (builder + SDK, two workflows, two integrations) — not for pricing SKUs.

#### Floor shell

```jsx
<section className="floor floor--media-duo">
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <header className="floor-head">…Pattern A…</header>
      <div className="media-duo-grid">
        <article className="media-duo-item">
          <div className="media-duo-visual">…</div>
          <div className="media-duo-body">
            <h3 className="media-duo-title">…</h3>
            <p className="media-duo-desc">…</p>
            <a className="media-duo-link" href="…">Get started <Icon /></a>
          </div>
        </article>
        …
      </div>
    </div>
  </div>
</section>
```

- Floor bg: **canvas** (`neutral-50`). No outer panel, no row wrapper border.
- Head → grid: `margin-bottom: 48–60px`.
- Section h2 may use **up to two** gradient-clipped words when the phrase is a compound title (e.g. "agent" + "builder") — still one gradient *span* per word max; exception only for this floor-head pattern.

#### Grid

```scss
.media-duo-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;                                             // §7 Agent-builder row
  align-items: start;                                    // cards are NOT equal-height stretch
}
```

| Property | Value |
|----------|-------|
| Columns | `repeat(2, minmax(0, 1fr))` |
| Gap | **18 px** desktop |
| Align | `start` — shorter copy does not stretch the sibling |

≤1024 px: `1fr` stack, gap **18**. Visual keeps full width; text block unchanged.

#### Card chrome — borderless, shadowless

```scss
.media-duo-item {
  display: flex;
  flex-direction: column;
  background: transparent;                               // canvas shows through
  border: 0;
  box-shadow: none;
  padding: 0;
  min-width: 0;
}
```

| Rule | Value |
|------|-------|
| Border | **none** on `.media-duo-item` and `.media-duo-body` |
| Shadow | **none** — including `:hover` |
| Background | transparent shell; only `.media-duo-visual` carries imagery |
| Hover | CTA color shift only (`neutral-950` → `primary-550`) — no card lift |

**Not** archetype A (bordered). **Not** panel-as-card (§11.6). Separation = **media frame radius + vertical rhythm**, not hairlines.

#### ZONE 1 — Visual frame (`.media-duo-visual`)

```
┌─ .media-duo-visual  radius-md  overflow hidden  NO border  NO shadow ─┐
│  <video|img>  object-fit: cover  absolute inset 0                        │
│  ┌ optional decorative layer (pathway dots, step labels) ─ NOT h1 text ┐│
│  │  mono caption-xs labels OK (e.g. "01 Input") — title-sm max           ││
│  └──────────────────────────────────────────────────────────────────────┘│
│  <icon> 20×20  white/currentColor  top: 16–20  left: 16–20             │
└──────────────────────────────────────────────────────────────────────────┘
```

```scss
.media-duo-visual {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10;                                 // or fixed height 248–280px
  min-height: 248px;
  border-radius: var(--pt-radius-md);                     // 24 — large rounded frame
  overflow: hidden;
  border: 0;
  box-shadow: none;
  background: var(--pt-color-neutral-100);                // placeholder while media loads
}
.media-duo-visual__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.media-duo-visual__icon {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 20px;
  height: 20px;
  color: #fff;                                            // on dark/abstract art
  filter: drop-shadow(0 1px 2px rgba(7, 8, 14, 0.12));    // legibility only on icon
  z-index: 1;
}
```

- Assets: manifest stills or looped video cover — `Images.json` product art, not stock.
- **No border** on the visual frame (differs from legacy `.agent-builder-visual` console specimen which may use `line-100` in §08 gallery only).
- Decorative pathway / step nodes: optional product art; labels ≤ `caption-sm` mono, `neutral-50` on dark art — never heading sizes.
- Do not place h2/h3 **over** the photograph (§2); title lives in ZONE 2 below the frame.

#### ZONE 2 — Copy block (`.media-duo-body`)

Left-aligned; **left edge flush with visual frame** (no extra inset padding on the column).

```scss
.media-duo-body {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  margin-top: 20px;                                       // 24px airy variant
  gap: 0;
  padding: 0;
  border: 0;
}

.media-duo-title {
  margin: 0;
  font-size: var(--pt-title-font-size-md);                // 24
  line-height: var(--pt-title-line-height-md);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
}

.media-duo-desc {
  margin: 12px 0 0;
  font-size: var(--pt-body-font-size-md);
  line-height: var(--pt-body-line-height-md);
  color: var(--pt-color-neutral-650);
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  max-width: 100%;
}
```

#### ZONE 3 — Text CTA (`.media-duo-link`)

**Not** a pill button — inline text link with trailing arrow. Left-aligned under description.

```scss
.media-duo-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 16px;                                       // 20px airy
  padding: 0;
  border: 0;
  background: transparent;
  font-size: var(--pt-body-font-size-md);
  font-family: var(--pt-font-medium);
  color: var(--pt-color-neutral-950);                     // default ink
  text-decoration: none;
  transition: color var(--pt-motion-fast) ease;

  &:hover { color: var(--pt-color-primary-550); }

  &.is-accent { color: var(--pt-color-primary-550); }      // second card may rest purple
  &.is-accent:hover { color: var(--pt-color-primary-700); }

  svg, .qc-icon { width: 14px; height: 14px; }
}
```

- Icon: `arrow-up-right-outlined` 14 px (Qwen Cloud) — same as `btn--text` trailing affordance.
- **One** link per card; no secondary outline button under the visual.
- At most one `.is-accent` (purple rest) link per row — sibling stays `neutral-950`.

#### Pairing rhythm (two siblings)

| Slot | Visual icon | CTA color |
|------|-------------|-----------|
| Column 1 | e.g. `code-outlined` / `terminal-outlined` | `neutral-950` → purple hover |
| Column 2 | e.g. `sparkle-outlined` / product icon | optional `.is-accent` purple rest |

Both columns share identical structure — only copy, art, and CTA color may differ.

#### Anti-patterns

```
❌ 1px line-100 around .media-duo-item or .media-duo-visual (§4.4 chrome on a media floor)
❌ box-shadow on visual frame or card hover lift
❌ full-width btn--primary / btn--secondary under the image (use §4.4 for that)
❌ centered text under the visual (breaks left-align rhythm with frame edge)
❌ h2/h3 positioned on top of the photograph
❌ grey neutral-100 box wrapping title + desc (typography + spacing only)
❌ 3rd column in the same row — use a separate floor or §4.4 3-up instead
```

#### Checklist (media duo floor)

- [ ] Pattern A floor-head; h2 may use ≤2 gradient words for compound titles
- [ ] `.media-duo-grid`: 2-col, gap 18, `align-items: start`
- [ ] `.media-duo-item`: **border 0, shadow none, padding 0**
- [ ] Visual: `radius-md`, 16:10 or h 248–280, cover media, 20 px corner icon
- [ ] Body: left-aligned; title `title-md`; desc 2-line clamp `neutral-650`
- [ ] CTA: `.media-duo-link` + `arrow-up-right-outlined` — not pill buttons

### 4.6 Simple card floor — skill / step / model showcase  ★

**简洁卡片楼层：** `line-100` 描边、**无阴影**、纯色 `neutral-50` 内里，靠 **tag · title · price-text · chips · metrics** 等小组件纵向叠放 — 不是 §4.4 的全宽 Subscribe，也不是 §4.5 的无框配图。参考：**Ready to Grow Together**（步骤 3 卡 + 楼层 CTA）、**Qwen 模型推荐行**（tag + 价目 + 底栏 metrics）。

```
┌── floor — canvas neutral-50 ──────────────────────────────────────────┐
│              h2  centered  gradient accent word(s)                     │
│              subtitle  body-lg  neutral-750                             │
│                                                                         │
│  Variant A — step flow (3-up, radius-md)                                │
│   ┌─ line-100 ─────────┐ ┌──────────────┐ ┌──────────────┐             │
│   │ [• Step 1]         │ │ [• Step 2]   │ │ [• Step 3]   │             │
│   │ Sign up            │ │ Add payment  │ │ Start build  │             │
│   │ desc…              │ │ desc…        │ │ desc…        │             │
│   └────────────────────┘ └──────────────┘ └──────────────┘             │
│                    [ Apply Now ]  ← single floor CTA, centered         │
│                                                                         │
│  Variant B — skill / model row (3-up, radius-sm, R11)                 │
│   ┌─ line-100 ─────────────────┐ ┌────────────┐ ┌────────────┐        │
│   │ Qwen3-Omni-Flash  [Hot]    │ │ Model B    │ │ Model C    │        │
│   │ desc 2-line clamp          │ │ …          │ │ …          │        │
│   │ [Reasoning] [Multi-mod]    │ │ chips…     │ │            │        │
│   │ Input $0.10/M  output $2…   │ │ price-text │ │            │        │
│   │ ───── line-100 ─────       │ │            │ │            │        │
│   │ 64K Context │ 87.8 MMLU   │ │ metrics    │ │            │        │
│   └────────────────────────────┘ └────────────┘ └────────────┘        │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Floor taxonomy — pick A or B

| Variant | Class hook | Cards | Radius | Pad | In-card CTA | Floor CTA |
|---------|------------|-------|--------|-----|-------------|-----------|
| **A — Step flow** | `.floor--step-cards` | 3-up (sometimes 2–4) | `radius-md` (24) | 32 | **none** | **one** centered `btn--primary` below grid |
| **B — Skill / model** | `.floor--skill-cards` | 3-up (marketplace row) | `radius-sm` (18) | 24 | optional text link only | none |

Both share: `1px line-100`, `neutral-50` fill, **`box-shadow: none`**, **no hover lift** on marketing floors.

**Not** §4.4 (pricing tiers w/ pill Subscribe + §8.16 icon lists + gradient rim). **Not** §4.5 (borderless media-on-top).

#### Shared floor shell

```jsx
<section className="floor floor--step-cards">   {/* or floor--skill-cards */}
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <header className="floor-head">…Pattern A…</header>
      <div className="simple-card-grid simple-card-grid--3">
        <article className="simple-card simple-card--step">…</article>   {/* A */}
        {/* or */}
        <article className="simple-card simple-card--skill">…</article>   {/* B */}
      </div>
      {/* Variant A only: */}
      <div className="simple-card-floor-cta">
        <a className="btn btn--primary" href="…">Apply Now</a>
      </div>
    </div>
  </div>
</section>
```

- Head → grid: `margin-bottom: 48px`.
- Variant A: floor CTA `margin-top: 48px`; `display: flex; justify-content: center`.
- Variant B: no floor CTA unless the page needs one secondary action — never duplicate per-card buttons.

#### Shared grid

```scss
.simple-card-grid {
  display: grid;
  gap: 24px;
  align-items: stretch;
}
.simple-card-grid--3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
.simple-card-grid--2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
/* optional: first model card slightly wider */
.simple-card-grid--3.is-asymmetric {
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 1fr) minmax(0, 1fr);
}
```

≤1024 px: `1fr` stack, gap **18**.

#### Shared card chrome

```scss
.simple-card {
  display: flex;
  flex-direction: column;
  background: var(--pt-color-neutral-50);
  border: var(--pt-line-size-normal) solid var(--pt-color-line-100);
  border-radius: var(--pt-radius-sm);                    // B: sm — override to md for A
  padding: 24px;                                         // B — override to 32 for A
  box-shadow: none;
  min-width: 0;

  &:hover {
    box-shadow: none;
    transform: none;
  }
}
.simple-card--step {
  border-radius: var(--pt-radius-md);
  padding: 32px;
}
```

| Rule | Value |
|------|-------|
| Border | **only** `1px line-100` — no gradient rim on simple cards |
| Shadow | **none** at rest and hover |
| Fill | `neutral-50` only — no `gradient-card-bg` inside |
| Featured | optional single `tag-hot` pill on a skill card — **not** a gradient border |

---

#### Variant A — Step flow (`.simple-card--step`)

Interior stack — **R12** (§11.2):

```
1. .step-tag          §8.17  pill + primary dot + "Step N"
2. .simple-card-title   title-md / body-lg semibold  mt 16
3. .simple-card-desc    body-md neutral-650  mt 12  (no clamp required; keep ≤3 lines)
```

```scss
.simple-card--step .step-tag { margin-bottom: 0; }
.simple-card--step .simple-card-title {
  margin: 16px 0 0;
  font-size: var(--pt-title-font-size-md);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
}
.simple-card--step .simple-card-desc {
  margin: 12px 0 0;
  font-size: var(--pt-body-font-size-md);
  line-height: var(--pt-body-line-height-md);
  color: var(--pt-color-neutral-650);
}
```

- All content **left-aligned** inside the card.
- **No** price-text, chips, metrics, or in-card buttons.
- **One** `btn--primary` centered under the full row (`simple-card-floor-cta`).

---

#### Variant B — Skill / model showcase (`.simple-card--skill`)

Marketing **models-card** anatomy without marketplace hover-reveal. Follow **R11** (§11.2) top → bottom:

```
1. .simple-card-head     title row: name (semibold body-lg) + optional tag-hot
2. .simple-card-desc     body-sm neutral-650 · 2-line clamp · mt 12
3. .simple-card-chips    flex wrap gap 8 · mt 14 — §8.19 modality chips
4. .simple-card-price     §8.18 price-text row(s) · mt 12–14
5. (flex spacer mt: auto on tall cards)
6. .simple-card-divider   border-top 1px line-100 · mt 16–20 · pt 12
7. .simple-card-metrics   2-col grid · §8.15 stat kv or title-sm + body-sm label
```

```scss
.simple-card-head {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}
.simple-card-name {
  font-size: var(--pt-body-font-size-lg);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
}
.simple-card-divider {
  margin-top: auto;
  padding-top: 12px;
  border-top: var(--pt-line-size-normal) solid var(--pt-color-line-100);
}
.simple-card-metrics {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px 24px;
  margin-top: 12px;
}
.simple-card-metric strong {
  display: block;
  font-size: var(--pt-title-font-size-sm);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
}
.simple-card-metric small {
  display: block;
  margin-top: 2px;
  font-size: var(--pt-body-font-size-sm);
  color: var(--pt-color-neutral-650);
}
```

- **Price-text** (§8.18): mono caption for token rates — sits **above** the divider, never in the metrics grid.
- **Chips** (§8.19): outline purple modality tags — max one wrap row before truncating.
- Optional `min-height: 340px` when cards must align with marketplace `.models-card` height — content still flows R11; use `margin-top: auto` before divider.
- Interactive marketplace pages (§17.7 hover-reveal) are **console** behavior — marketing skill floors stay static flat.

---

#### Component quick-reference

| Block | Section | Role |
|-------|---------|------|
| Step tag pill | §8.17 | `• Step 1` lavender/neutral pill + dot |
| Price-text | §8.18 | `Input $ 0.10/M tokens` mono grey |
| Modality chip | §8.19 | `Reasoning` outline purple pill |
| Hot badge | §8.2 / `tag-hot` | solid gradient-6 or primary-50 pill |
| Metrics pair | §8.15 / R11 | `64K` + `Context` stacked |

#### Anti-patterns

```
❌ box-shadow or hover lift on .simple-card (marketing)
❌ gradient rim .is-featured (reserve for §4.4 pricing)
❌ full-width Subscribe inside step cards (floor CTA only for variant A)
❌ §8.16 icon feature rows inside skill cards (use chips + price-text instead)
❌ grey inset boxes around price or metrics
❌ panel-as-card outer wrap around the grid (§11.6)
❌ mixing step-card and skill-card recipes in one row
```

#### Checklist (simple card floor)

- [ ] Variant A **or** B — not blended in one grid
- [ ] Every card: `line-100`, `neutral-50`, **shadow none**, no hover lift
- [ ] A: `radius-md` pad 32, step-tag + title + desc, floor `btn--primary` centered
- [ ] B: `radius-sm` pad 24, R11 stack ending in divider + 2-col metrics
- [ ] price-text above divider; chips single wrap row; ≤1 Hot tag per card

### 4.7 Secondary showcase floor — text-only cards  ★

**次级信息楼层：** 排版驱动、视觉权重低于 hero / §4.4–§4.6，用来**衬托**主信息。共享同一 **`.text-card`** chrome：无描边、无背景、无阴影，**仅** `border-bottom: 1px solid line-100`。两种变体：

| Variant | Reference | Head | Filter | Footer |
|---------|-----------|------|--------|--------|
| **A — tabbed** | Model serving diverse **industries** | Pattern B/A, one gradient word | §8.20 `.secondary-tabs` | optional `btn--outline` |
| **B — plain row** | **AI and Cloud** / Solutions For All Your Needs | **Two-line left stack** §4.7.2 | **none** | §8.22 **carousel pager** `< >` |

```
Variant A — with tabs
┌── floor ──────────────────────────────────────────────────────────────┐
│  h2  "Model serving diverse **industries**"                            │
│  [ • Education ]  Healthcare   Retail    ← secondary-tabs §8.20      │
│  ┌ text-card ×4 ── border-bottom line-100 only ─────────────────────┐ │
│  │ icon? + name · desc · chips? · ↗                                   │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│              [ Browse all models ]  optional outline                    │
└───────────────────────────────────────────────────────────────────────┘

Variant B — no tabs
┌── floor ──────────────────────────────────────────────────────────────┐
│  AI and Cloud              ← line 1 gradient clip                      │
│  Solutions For All Your Needs   ← line 2 solid black (stacked-left)  │
│                                                                        │
│  ┌ text-card ×4 ── same chrome ─────────────────────────────────────┐ │
│  │ Elastic Compute Service (ECS)                                       │ │
│  │ Host your website and scale…                                        │ │
│  │ ↗                                                                   │ │
│  │────────────────────────────────────────────────────────────────────│ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                    ( ○ ‹   › ○ )   ← text-card-pager §8.22 centered   │
└───────────────────────────────────────────────────────────────────────┘
```

#### Role — when to use

| Tier | Floors | Visual weight |
|------|--------|---------------|
| **Primary** | §2.7 hero, §4.4 pricing, §4.5 media duo, §4.6 simple cards | High — borders, imagery, pills, metrics |
| **Secondary** | **§4.7** (this) | Low — typography + one hairline; tabs filter content |

Place §4.7 **after** a primary chapter. Prefer **tinted** floor bg (`neutral-100`) when the previous floor was canvas — or stay on canvas when the prior floor was already stepped (§4.1 alternation). Never stack two equally loud bordered card rows back-to-back.

#### Floor shell — shared

```jsx
<section className="floor floor--secondary-showcase floor--secondary-showcase-a">
  {/* or floor--secondary-showcase-b for no-tabs */}
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      {/* head — see Variant A or B */}
      {/* optional: secondary-tabs (A only) */}
      <div className="text-card-grid text-card-grid--4">…</div>
      {/* A: secondary-floor-cta · B: text-card-pager */}
    </div>
  </div>
</section>
```

---

#### Variant A — tabbed row

```jsx
<header className="floor-head floor-head--left">…Pattern B…</header>
<div className="secondary-tabs" role="tablist">…§8.20…</div>
<div className="text-card-grid text-card-grid--4" role="tabpanel">…</div>
<div className="secondary-floor-cta">
  <a className="btn btn--outline" href="…">Browse all models</a>
</div>
```

- Head → tabs: `margin-bottom: 32px`. Tabs → grid: cards carry bottom hairline.
- Tabs swap panel content — one grid visible; no autoplay.
- Floor CTA: `margin-top: 48px`, centered `btn--outline`.

**Head:** Pattern B default; one gradient word in h2. Optional short subtitle.

#### Secondary tabs (§8.20) — Variant A only

Extremely flat — **not** §8.4 segmented track, **not** §8.5 underline nav.

| State | Background | Border | Shadow | Affordance |
|-------|------------|--------|--------|------------|
| Inactive | **transparent** | none | none | plain `body-sm`/`md`, `neutral-650` |
| Active `.is-active` | `neutral-150` pill | none | none | **5 px** `primary-550` dot `::before` + `neutral-950` label |

```scss
.secondary-tabs {
  display: inline-flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-bottom: 32px;
  padding: 0;
  border: 0;
  background: transparent;
  box-shadow: none;
}

.secondary-tab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  border: 0;
  border-radius: var(--pt-radius-full);
  background: transparent;
  box-shadow: none;
  font-size: var(--pt-body-font-size-sm);
  font-family: var(--pt-font-medium);
  color: var(--pt-color-neutral-650);
  cursor: pointer;
  transition: background var(--pt-motion-fast) ease, color var(--pt-motion-fast) ease;

  &:hover:not(.is-active) {
    color: var(--pt-color-neutral-950);
  }

  &.is-active {
    background: var(--pt-color-neutral-150);
    color: var(--pt-color-neutral-950);

    &::before {
      content: '';
      width: 5px;
      height: 5px;
      border-radius: 999px;
      background: var(--pt-color-primary-550);
      flex-shrink: 0;
    }
  }
}
```

- No outer rail, no `neutral-150` track wrapping all tabs.
- Dot is **5 px** (not §8.3's 6 px pill-tab variant).

---

#### Variant B — plain row (no tabs)

Reference: **AI and Cloud / Solutions For All Your Needs** — services catalog, ECS-style listings. **No** `.secondary-tabs`. Pagination via carousel pager when items exceed one viewport.

```jsx
<header className="floor-head floor-head--stacked-left">
  <h2>
    <span className="floor-head-line floor-head-line--gradient">AI and Cloud</span>
    <span className="floor-head-line">Solutions For All Your Needs</span>
  </h2>
</header>

<div className="text-card-grid text-card-grid--4">
  <a className="text-card text-card--minimal" href="…">
    <h3 className="text-card-name">Elastic Compute Service (ECS)</h3>
    <p className="text-card-desc">Host your website and scale enterprise workloads anywhere</p>
    <span className="text-card-link" aria-hidden="true"><Icon arrow-up-right-outlined /></span>
  </a>
  …
</div>

<div className="text-card-pager" aria-label="Slide pages">
  <button type="button" className="text-card-pager-btn" aria-label="Previous">…</button>
  <button type="button" className="text-card-pager-btn" aria-label="Next">…</button>
</div>
```

##### Two-line left head (`.floor-head--stacked-left`)

```scss
.floor-head--stacked-left {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  gap: 0;
  margin-bottom: 48px;

  h2 {
    margin: 0;
    font-size: var(--pt-heading-font-size-md);
    line-height: var(--pt-heading-line-height-md);
    font-family: var(--pt-font-bold);
    letter-spacing: var(--pt-letter-spacing-tight);
  }

  .floor-head-line {
    display: block;
  }

  .floor-head-line--gradient {
    background: var(--pt-gradient-4);                    // or brand gradient token
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    margin-bottom: 4px;
  }

  .floor-head-line:not(.floor-head-line--gradient) {
    color: var(--pt-color-neutral-950);
  }
}
```

- Line 1: full line gradient clip (e.g. "AI and Cloud") — counts as the floor's **one** gradient accent.
- Line 2: solid `neutral-950` on its own line — not a subtitle paragraph; same h2 block.
- No centered Pattern A on variant B.

##### R13b minimal interior (variant B cards)

Skip icon row and chips unless the product truly needs them — default is **title → desc → ↗** only:

```
.text-card--minimal
  .text-card-name   body-lg semibold (no .text-card-head / icon)
  .text-card-desc   body-sm 2–3 clamp  mt 12
  .text-card-link   mt auto  pt 16  arrow 14px
```

Same chrome: transparent, **only** `border-bottom line-100`.

##### Carousel pager (§8.22) — Variant B footer

Replace `btn--outline` when the list paginates horizontally.

- Centered below grid: `margin-top: 40–48px`.
- Two circular **ghost** buttons: `‹` `›` (`chevron-left-outlined` / `chevron-right-outlined` 16–18 px).
- `1px line-100` circle border, **no fill**, **no shadow** — matches text-card quiet chrome.
- Advances one "page" of 4 (or 3) cards; disabled state `opacity: 0.4`, `pointer-events: none`.
- Mobile: same pager or native horizontal scroll on `.text-card-grid` — pick one, not both.

---

#### Shared — text-card grid

```scss
.text-card-grid {
  display: grid;
  gap: 24px 32px;                                        // row gap separates hairlines
  align-items: start;
}
.text-card-grid--4 {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}
.text-card-grid--3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
```

| Count | Columns | Gap | Use |
|-------|---------|-----|-----|
| 4-up | `repeat(4, minmax(0, 1fr))` | 24 × 32 | Industry model strip (default) |
| 3-up | `repeat(3, minmax(0, 1fr))` | 24 × 32 | Shorter lists |

≤1024 px: `repeat(2, 1fr)`; ≤640 px: `1fr`. Hairlines stay per card.

#### Text-card chrome — borderless, bottom hairline only

```scss
.text-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-height: 100%;
  padding: 0 0 24px;
  background: transparent;
  border: 0;
  box-shadow: none;
  border-bottom: var(--pt-line-size-normal) solid var(--pt-color-line-100);
  border-radius: 0;

  &:hover {
    box-shadow: none;
    transform: none;
    background: transparent;
  }
}
```

- **No** fill, **no** side/top border, **no** radius, **no** shadow — the row reads as typography on the floor plane.
- **Only** `border-bottom: 1px line-100` separates units.
- **Not** §4.6 `.simple-card` (full box). **Not** §11.6 panel-as-card.

#### Text-card interior — R13 / R13b (§11.2)

**R13** (variant A — models / industries):

```
1. .text-card-head      icon 16px + name body-lg semibold
2. .text-card-desc      body-sm neutral-650 · 2–3 line clamp · mt 12
3. .text-card-chips     modality-chip row §8.19 · mt 14 (optional)
4. .text-card-link      margin-top: auto; pt 16 — arrow-up-right-outlined 14px
```

**R13b** (variant B — solutions / ECS catalog): name → desc → ↗ only — see Variant B above.

```scss
.text-card-head {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
}
.text-card-icon {
  width: 16px;
  height: 16px;
  color: var(--pt-color-neutral-950);
  flex-shrink: 0;
}
.text-card-name {
  font-size: var(--pt-body-font-size-lg);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
}
.text-card-desc {
  margin-top: 12px;
  font-size: var(--pt-body-font-size-sm);
  line-height: var(--pt-body-line-height-sm);
  color: var(--pt-color-neutral-650);
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}
.text-card-link {
  display: inline-flex;
  align-items: center;
  margin-top: auto;
  padding-top: 16px;
  color: var(--pt-color-neutral-750);
  svg { width: 14px; height: 14px; }
  &:hover { color: var(--pt-color-primary-550); }
}
```

- Opensource / status chips may use §8.19 or a green-outline variant (`func-success` border) — max one row.
- Bottom-left ↗ is an **icon affordance**, not a full text CTA row — card may be entirely clickable via `<a class="text-card">` wrapper.

#### Optional floor footer

| Variant | Footer |
|---------|--------|
| **A** | `btn--outline` centered — "Browse all models" |
| **B** | §8.22 `.text-card-pager` — circular chevron prev/next |

- **Not** `btn--primary` black fill on secondary floors.
- Omit footer when navigation is unnecessary (≤4 static items, variant B).

#### Anti-patterns

```
❌ box border or radius on .text-card (becomes §4.6)
❌ shadow or hover lift on text-cards
❌ §8.4 segmented track for secondary tabs
❌ active tab with primary-50 purple fill (too loud — use neutral-150 only)
❌ tabs on variant B when the reference is a plain solutions row (use pager instead)
❌ both pager and btn--outline on the same floor
❌ placing this floor directly under hero without a primary card floor in between
❌ 4-up bordered simple-cards in the same visual band as text-cards
```

#### Checklist (secondary showcase)

- [ ] Floor tier is secondary — follows a primary chapter
- [ ] Picked **variant A** (tabs) **or** **variant B** (no tabs) — not both
- [ ] Each `.text-card` **only** `border-bottom line-100`; no bg/border/shadow
- [ ] **A:** §8.20 tabs; R13; optional `btn--outline`
- [ ] **B:** `.floor-head--stacked-left` two-line head; R13b; §8.22 pager when paginated

### 4.8 Logo floor — matrix tiles or borderless strip  ★

Quiet **trust / partner** band — lighter than §4.6, no metrics, no in-tile CTAs. Two variants; pick **one** per floor:

| Variant | Reference | Layout | Chrome |
|---------|-----------|--------|--------|
| **A — bordered matrix** | **Supported AI Tools** | **4×N** grid; icon + name per tile | `line-100` hairline box only |
| **B — borderless strip** | **Our Partners** | **1×N** horizontal logo row | **none** — logos on canvas |

```
Variant A — matrix                         Variant B — borderless strip
┌─────────────────────────────────┐        ┌─────────────────────────────────┐
│     Supported AI Tools          │        │        Our Partners             │
│     subtitle [Learn More ↗]     │        │  Organizations supporting…      │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐    │        │                                 │
│  │□ Na│ │□ Na│ │□ Na│ │□ Na│    │        │  [logo] [logo] [logo] [logo] …  │
│  └────┘ └────┘ └────┘ └────┘    │        │  ← no border · no shadow · flex  │
└─────────────────────────────────┘        └─────────────────────────────────┘
```

Shared: **Pattern A** centered head + optional subtitle (§8.23 link on A only). Lives in `.layout-max-inner` on canvas `neutral-50`.

---

#### Variant A — bordered logo matrix

**Logo 矩阵：** **4×N** 极薄描边小卡，每格 **icon + 名称**。参考：Qwen Code · Cline · Claude Code · Cursor …

#### Floor shell (variant A)

```jsx
<section className="floor floor--logo-matrix floor--logo-a">
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <header className="floor-head">
        <h2>Supported AI Tools</h2>
        <p className="floor-head-link-desc">
          Coding Plan works with mainstream tools compatible with OpenAI / Anthropic protocols{' '}
          <a className="floor-head-inline-link" href="…">Learn More <Icon /></a>
        </p>
      </header>
      <div className="logo-matrix-grid">
        <a className="logo-matrix-tile" href="…">
          <img className="logo-matrix-tile__icon" src="…" alt="" />
          <span className="logo-matrix-tile__name">Qwen Code</span>
        </a>
        …
      </div>
    </div>
  </div>
</section>
```

- **Pattern A** centered head (default). Subtitle may include §8.23 inline link — not a floor CTA button.
- No tabs, no pager, no per-tile arrow (unlike §4.7).

#### Grid

```scss
.logo-matrix-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  align-items: stretch;
}
```

| Layout | Columns | Row gap / col gap | Tile height |
|--------|---------|-------------------|-------------|
| **4×2** (default) | `repeat(4, minmax(0, 1fr))` | **12 px** both | **64 px** fixed |
| **4×3+** | same | 12 px | 64 px |
| **3×N** (narrow) | `repeat(3, minmax(0, 1fr))` | 12 px | 64 px |

≤1024 px: `repeat(2, minmax(0, 1fr))`, gap **12**. ≤480 px: `1fr` stack optional — prefer 2-col down to 640.

Pull grid row from §7 **Tools / logo tiles** — do not invent gaps.

#### Tile chrome — line-100 only

```scss
.logo-matrix-tile {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 64px;
  height: 64px;
  padding: 0 16px 0 20px;                                // asymmetric ok: more left for icon
  background: transparent;                                 // canvas shows through — NOT neutral-100 fill
  border: var(--pt-line-size-normal) solid var(--pt-color-line-100);
  border-radius: var(--pt-radius-xs);                     // 12
  box-shadow: none;
  text-decoration: none;
  color: inherit;
  transition: border-color var(--pt-motion-fast) ease, color var(--pt-motion-fast) ease;

  &:hover {
    box-shadow: none;
    transform: none;
    border-color: var(--pt-color-line-200);
  }
}
```

| Rule | Value |
|------|-------|
| Border | `1px line-100` only — full box hairline |
| Background | **transparent** — no `neutral-50` fill inside tile (same plane as floor) |
| Shadow | **none** — including `:hover` |
| Radius | `--pt-radius-xs` (12) |
| Hover | border `line-200` only — **no** lift, **no** bg-step |

Archetype **A** compact tile (§11.1 E · `.coding-plan-tools-item`). **Not** panel-as-card (§11.6).

#### Tile interior — R14 (§11.2)

```
.logo-matrix-tile__icon   24×24 (or 28×28) · object-fit contain · flex-shrink 0
.logo-matrix-tile__name   body-sm or body-md · font-medium · neutral-950 · truncate 1 line
```

```scss
.logo-matrix-tile__icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
  object-fit: contain;
}
.logo-matrix-tile__name {
  font-size: var(--pt-body-font-size-sm);
  font-family: var(--pt-font-medium);
  color: var(--pt-color-neutral-950);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  min-width: 0;
}
```

- Icons: product logos from manifest / brand kit — square, not emoji.
- Whole tile is one tappable `<a>` when linked; static pages may use `<div class="logo-matrix-tile">`.
- **No** description, **no** chips, **no** trailing ↗ inside the tile.

#### Subtitle with inline link (§8.23)

Centered under h2 inside Pattern A — `floor-head-link-desc` + `floor-head-inline-link` (`primary-550`, `arrow-up-right-outlined` 12–14 px). See §8.23.

#### Anti-patterns

```
❌ box-shadow or hover translateY on logo-matrix-tile
❌ neutral-100/150 fill inside tiles (reads as nested grey card)
❌ gradient rim or Hot badge on a logo tile
❌ 2-line description inside the 64px tile
❌ mixing logo-matrix tiles with §4.7 text-cards in one grid
❌ panel-as-card wrapper around the whole matrix
```

#### Checklist (variant A — matrix)

- [ ] Pattern A head; optional §8.23 subtitle link
- [ ] `.logo-matrix-grid` 4-col (or 3-col), gap **12**, tile h **64**
- [ ] Each `.logo-matrix-tile`: `line-100`, **transparent** bg, `radius-xs`, **shadow none**
- [ ] R14: icon 24 + name body-sm medium; hover border only

---

#### Variant B — borderless logo strip

**无边透明 Logo 排列：** 居中标题 + 一行（或多行 wrap）**纯品牌 Logo**，直接落在楼层画布上 — **无** 卡片、**无** `line-100`、**无** 阴影、**无** 灰底。参考：**Our Partners** — "Organizations supporting the hackathon community." + 6 个彩色品牌标横排。

```
┌── floor — canvas neutral-50 ──────────────────────────────────────────┐
│                    Our Partners          ← Pattern A h2              │
│     Organizations supporting the hackathon community.  ← body-lg     │
│                         margin 48–64                                    │
│    [Python]   [■]   [IDSW]   [INNOVATION…]   [◇]   [◎]   ← flex row   │
│    logos only · brand colors · shared vertical center axis            │
└────────────────────────────────────────────────────────────────────────┘
```

Quiet **sponsor / partner** band — even lighter than variant A. Use when logos are self-explanatory and names are embedded in the mark.

##### Floor shell (variant B)

```jsx
<section className="floor floor--logo-strip floor--logo-b">
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <header className="floor-head">
        <h2>Our Partners</h2>
        <p className="heading-desc">Organizations supporting the hackathon community.</p>
      </header>
      <div className="logo-strip" role="list">
        <a className="logo-strip-item" href="…" role="listitem">
          <img className="logo-strip-item__logo" src="…" alt="Python" />
        </a>
        …
      </div>
    </div>
  </div>
</section>
```

- Subtitle: `heading-desc` only — **no** §8.23 inline link required (plain gray line).
- Head → strip: `margin-bottom: 48–64 px` on `.floor-head`.
- Static pages: `<div className="logo-strip-item">` without link.

##### Strip layout

```scss
.logo-strip {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: clamp(32px, 6vw, 64px) clamp(24px, 5vw, 56px);
  width: 100%;
}
```

| Layout | Rule |
|--------|------|
| **Desktop** | Single horizontal row when ≤8 logos fit; `justify-content: center` |
| **Wrap** | `flex-wrap: wrap` — 2–3 logos per row on tablet; centered rows |
| **Equal grid (optional)** | `display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: clamp(18px, 6vw, 48px)` when all marks are similar aspect — pull §7 **Partner logo strip** row |

≤1024 px: gap steps down (`clamp(24px, 5vw, 40px)`). ≤640 px: prefer 2–3 logos per row, still centered.

##### Item chrome — fully transparent (R19)

```scss
.logo-strip-item {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: 0 1 auto;
  padding: 0;
  background: transparent;
  border: 0;
  box-shadow: none;
  text-decoration: none;
  color: inherit;

  &:hover {
    box-shadow: none;
    transform: none;
    border: 0;
    background: transparent;
  }
}

.logo-strip-item__logo {
  display: block;
  height: 40px;                                          // 32–48 px band
  max-height: 48px;
  width: auto;
  max-width: min(160px, 28vw);
  object-fit: contain;
  object-position: center;
}
```

| Rule | Value |
|------|-------|
| Border / bg / shadow | **none** on item and image wrapper |
| Logo color | **preserve brand colors** — no forced monochrome unless partner kit requires |
| Height | Shared **vertical center** axis — `align-items: center` on strip |
| Hover (linked) | optional `opacity: 0.85 → 1` only — **no** scale, lift, or border |
| Alt text | Partner / product name for each `img` |

- Logos may be icon-only, wordmark, or combined — variable aspect ratios are expected.
- **No** tool name caption below the mark (that's variant A's job).
- **No** grayscale filter by default.

##### Anti-patterns (variant B)

```
❌ line-100 box or neutral-100 tile around a strip logo (use variant A instead)
❌ mixing variant A tiles and variant B strip items in one floor
❌ box-shadow, hover translateY, or grey inset plate behind the row
❌ forcing all logos to identical square cells (distorts wordmarks)
❌ dot pager / carousel on a static partner row (use §4.11 only when interaction is required)
```

##### Checklist (variant B — strip)

- [ ] Pattern A centered head + `heading-desc` (neutral-650/750)
- [ ] `.logo-strip` flex center; gap `clamp(32px, 6vw, 64px)`; head → strip **48–64 px**
- [ ] Each `.logo-strip-item`: **no** border/bg/shadow; R19 logo `height 40–48`
- [ ] Brand colors preserved; optional opacity-only hover on links

##### Floor-level checklist (§4.8)

- [ ] Picked variant **A** (matrix) **or** **B** (strip) — not both on one floor

### 4.9 Tail visual CTA floor — page closing band  ★

The **last marketing floor** before `.page-footer`. One wide rounded panel in `.layout-max-wide` with **centered headline + subtitle + CTA row** over an art-directed abstract gradient / flower image / quiet video. Reference: **Co-Build Future. AI-Powered Era.** (790 px) · **Join the community** (370 px).

This is the §2.5 / §3 variant **F** exception — copy may sit on imagery because the backdrop is low-contrast and the panel is tall enough for breathing room.

```
┌── .layout-max-wide ─────────────────────────────────────────────┐
│  .tail-visual  radius-lg  overflow hidden  h 790 | 370            │
│  ┌─ backdrop: flower_* / gradient wash / muted video ─────────┐ │
│  │              [optional kicker + purple inline link]           │ │
│  │              H2  centered  one gradient word/phrase           │ │
│  │              subtitle  body-lg  neutral-650  max read-box     │ │
│  │              [ btn--primary ]  [ btn--outline ]               │ │
│  └──────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────┘
        ↓ flush — no extra tinted band between visual and footer
┌── .page-footer (§4.10) ─────────────────────────────────────────┐
```

#### Height variants

| Class / height | When | Reference |
|----------------|------|-----------|
| `.tail-visual--tall` **790 px** | Homepage close, era campaigns, high-impact close | Co-Build Future · **AI-Powered** gradient phrase · Get API Keys + Try now |
| `.tail-visual--compact` **370 px** | Community, hackathon, program invites | Join the **community** · one-line subtitle · Apply Directly + Learn About… |

Pick **one** height per page. Do not stack two tail visuals.

#### Shell

```scss
.tail-visual {
  position: relative;
  width: 100%;
  border-radius: var(--pt-radius-lg);
  overflow: hidden;
  box-shadow: none;

  &--tall    { height: 790px; min-height: 790px; }
  &--compact { height: 370px; min-height: 370px; }

  &__media {
    position: absolute;
    inset: 0;
    object-fit: cover;
    z-index: 0;
  }

  &__content {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    height: 100%;
    padding: 48px 32px;
    gap: 16px;
  }
}
```

Legacy alias: `.era-hero-shell` — same rules; height may read **780 px** in older Guideline CSS — prefer **790 px** for new pages.

Backdrop assets: `flower_*` from `Images.json` or soft abstract video — never a busy photo that fights the headline.

#### Content stack (R15)

Centered column inside `.tail-visual__content`:

| Zone | Spec |
|------|------|
| **Kicker** (optional) | `.tail-visual-kicker` — `body-md`, `neutral-750`; one §8.23-style inline link (`primary-550`, `arrow-up-right-outlined` 12 px). E.g. "70+ Million AI tokens… **View now**" |
| **Headline** | `h2` — tall: `--pt-heading-font-size-2xl` (72); compact: `--pt-heading-font-size-md` (44). **One** gradient-clipped word or short phrase (`--pt-gradient-1…8`). Remainder solid `neutral-950` |
| **Subtitle** | `body-lg`, `neutral-650`–`750`, `max-width: min(100%, var(--pt-layout-max-read-box))`, 1–2 lines |
| **CTA row** | `.tail-visual-cta-row` — `inline-flex; gap: 10–12px; margin-top: 20–36px; flex-wrap: wrap; justify-content: center` |
| **Buttons** | **Level 1** `btn--primary` + **Level 3** `btn--outline` only — same pairing as §2.7 homepage hero |

Tall variant may use a **two-line** `h2` (line 1 + line 2) with gradient on the key phrase only. Compact variant is usually single-line `h2` + one subtitle block.

#### Rhythm with previous floor & footer

- **Above:** `margin-top: 96–122 px` from the last content floor (same §1.5 rhythm).
- **Below:** **no** extra floor padding — `.page-footer` starts immediately under the wide panel (canvas continues `neutral-50`).
- **No** separate Pattern A `floor-head` above the panel — the headline lives **inside** the visual.

#### Anti-patterns

```
❌ Title stack on canvas + separate small image below (that's §2.7 — not a tail visual)
❌ Shadow, gradient rim, or line-100 box around the outer tail panel
❌ btn--secondary as the only secondary action (use btn--outline)
❌ Per-tile CTAs, forms, or accordion inside the panel (email capture = legacy era variant only)
❌ h1 / 96 px type on the tail band — cap at 72 px (tall) or 44 px (compact)
```

#### Checklist (tail visual)

- [ ] One `.tail-visual` per page; height **790** or **370**
- [ ] `.layout-max-wide`; `radius-lg`; backdrop + centered R15 stack
- [ ] Level 1 primary + Level 3 outline; ≤1 gradient phrase in `h2`
- [ ] Footer flush below — no tinted spacer band

### 4.10 Site footer floor — asymmetric link grid  ★

Global **`.page-footer`** — last node in `.page-shell`, directly under §4.9 (or the last content floor when no tail visual). Reference: Products / Company / Resources columns + social row + copyright bar.

```
┌── .page-footer — canvas neutral-50, no shadow ────────────────────┐
│  .layout-max-inner-wrap > .layout-max-inner                        │
│                                                                    │
│  .page-footer-main          35%          │  65%                    │
│  ┌─────────────────────┐    │  ┌──────────────────────────────────┐│
│  │ [X] [GitHub] [in] [Discord] │  Products │ Company │ Resources ││
│  │  social / brand icons     │  link cols (3-up)                  ││
│  └─────────────────────┘    │  └──────────────────────────────────┘│
│                                                                    │
│  ───────────── line-100 ─────────────────────────────────────────  │
│  © 2026 … All rights reserved.          Manage Cookies             │
└────────────────────────────────────────────────────────────────────┘
```

#### Main grid — 35 / 65 split

```scss
.page-footer {
  background: var(--pt-color-neutral-50);
  box-shadow: none;
  padding: 48px 0 32px;
}

.page-footer-main {
  display: grid;
  grid-template-columns: minmax(0, 35fr) minmax(0, 65fr);
  gap: 48px 64px;
  align-items: start;
}
```

| Column | Width | Content |
|--------|-------|---------|
| **Aside** `.page-footer-aside` | **35%** | Horizontal **social** icon row (default) or brand mark / certification icons — flat, no boxes |
| **Links** `.page-footer-nav` | **65%** | **3-column** link groups (typical); may be 2–4 cols by IA |

Left aside is **not** a card — icons sit on canvas with no border, bg, or shadow.

#### Social row (§8.24)

```scss
.page-footer-social {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px 20px;
}

.page-footer-social-link {
  display: inline-flex;
  color: var(--pt-color-neutral-950);
  &:hover { color: var(--pt-color-neutral-650); }
  svg, .qc-icon { width: 20px; height: 20px; }
}
```

Default set: X (Twitter) · GitHub · LinkedIn · Discord. Brand glyphs are **not** in the 48-icon manifest — use **Tabler** `brand-*` outlined icons at 20 px, `stroke: 1.5`, one kit per footer (Tabler only in this row is OK).

#### Link columns (R16)

```scss
.page-footer-nav {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 32px 48px;
}

.page-footer-nav-title {
  margin: 0 0 16px;
  font-size: var(--pt-body-font-size-sm);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
}

.page-footer-nav-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.page-footer-nav-link {
  font-size: var(--pt-body-font-size-sm);
  color: var(--pt-color-neutral-650);
  text-decoration: none;
  &:hover { color: var(--pt-color-neutral-950); }
}
```

Typical groups: **Products** (Models, Pricing, Cloud services, Enterprise) · **Company** (About us, Contact, Privacy, Terms) · **Resources** (Documentation). Titles are short labels — not gradient marketing heads.

#### Legal bar

```scss
.page-footer-legal {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--pt-color-line-100);
  font-size: var(--pt-caption-font-size-sm);
  color: var(--pt-color-neutral-550);
}

.page-footer-legal-link {
  color: var(--pt-color-neutral-550);
  text-decoration: none;
  &:hover { color: var(--pt-color-neutral-750); }
}
```

Copyright **left**; utility links (**Manage Cookies**) **right** on desktop. No pill buttons in the legal row.

#### Mobile (≤1024 px)

```scss
.page-footer-main { grid-template-columns: 1fr; gap: 40px; }
.page-footer-nav  { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 32px 24px; }
```

≤640 px: link grid → `1fr` stack; legal bar → column, left-aligned, gap 12 px.

#### Anti-patterns

```
❌ Tinted neutral-100 footer band or card wrapper around the whole footer
❌ Boxed social icons (line-100 squares) — keep icons naked on canvas
❌ 50/50 split — aside must stay ~35%, links ~65%
❌ Primary pill CTAs in the footer — text links only
❌ Duplicate tail-visual headline repeated in footer
```

#### Checklist (site footer)

- [ ] `.page-footer` last in shell; canvas `neutral-50`; no shadow
- [ ] `.page-footer-main` **35fr / 65fr**; social left, **3-col** links right (R16)
- [ ] `.page-footer-legal` — `line-100` top rule; copyright left, cookies right
- [ ] Flush under §4.9 tail visual when present

### 4.11 Interactive carousel toggle floor — 100vw card track  ★

**可交互横滑楼层：** 标题区留在 **inner**；卡片轨道 ** breakout 到 100vw**，右侧裁切暗示还有更多。用户点击 **‹ ›**（§8.26）前后切换 — 无 autoplay、无 dot 轨道、无阴影。参考：**Judging Criteria**（左头 + 右上分页）· 证言横滑（居中头 + 底部分页）。

```
Variant A — centered head + bottom pager          Variant B — left head + inline pager
┌── inner: h2 + subtitle ─────────────┐          ┌── inner: head row ────────── [‹ ›] ┐
│         Customer **stories**         │          │ Judging **Criteria**  + subtitle   │
└──────────────────────────────────────┘          └────────────────────────────────────┘
┌── 100vw track — cards bleed right ────────────────────────────────────────────────┐
│  ┌ carousel-card ─┐  ┌ carousel-card ─┐  ┌ carousel-card ─┐▌                      │
│  │ line-100 or     │  │ neutral-100 fill│  │ …               │  peek               │
│  │ neutral-100     │  │ R17 or R18      │  │                 │                     │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                     │
└──────────────────────────────────────────────────────────────────────────────────────┘
              ( ‹   › )  centered §8.26
```

#### Role — vs §4.7 / §3G

| Floor | Cards | Track | Pager |
|-------|-------|-------|-------|
| **§4.11** (this) | Bordered or filled **boxed** cards, `radius-lg` | **100vw** breakout | §8.26 ‹ › |
| §4.7 secondary | Text-only, bottom hairline | Inner grid, static pages | §8.22 centered (variant B) |
| §3G hero carousel | Marketplace hero cards | Viewport-right bleed at **top** | Usually none |

Use §4.11 for testimonials, judging rubrics, feature spotlights — anywhere **card chrome** + horizontal peek matters.

#### Floor shell

```jsx
<section className="floor floor--carousel-toggle floor--carousel-a">
  {/* or floor--carousel-b */}
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      {/* Variant A: Pattern A head · Variant B: head row + carousel-pager--head-inline */}
    </div>
  </div>

  <div className="carousel-floor-viewport" aria-roledescription="carousel">
    <div className="carousel-floor-track" style={{ transform: `translateX(${offset}px)` }}>
      <article className="carousel-card carousel-card--bordered">…</article>
      …
    </div>
  </div>

  {/* Variant A only: */}
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <div className="carousel-pager carousel-pager--centered" aria-label="Slide pages">…§8.26…</div>
    </div>
  </div>
</section>
```

- **Head → track:** `margin-bottom: 48–60 px`.
- **Track → bottom pager (A):** `margin-top: 48 px`.
- Toggle advances **one card width + gap** per click (or one viewport page — pick one and stay consistent).
- `prefers-reduced-motion`: jump without transform animation.

#### 100vw breakout track

```scss
.carousel-floor-viewport {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  overflow: hidden;
}

.carousel-floor-track {
  display: flex;
  align-items: stretch;
  gap: 24px;
  padding-left: max(20px, calc((100vw - var(--pt-layout-max-width)) / 2));
  padding-right: max(20px, calc((100vw - var(--pt-layout-max-width)) / 2));
  will-change: transform;
  transition: transform var(--pt-motion-normal) ease;
}
```

First card aligns to **inner** left gutter (same math as §3G marketplace carousel). Last card may **peek** off the right edge — intentional scroll affordance.

| Card width | When |
|------------|------|
| `min(420px, 85vw)` | Testimonial / quote cards (R17) |
| `min(380px, 80vw)` | Criteria / rubric cards (R18) |
| `clamp(320px, 32vw, 400px)` | Dense 3-up peek on wide screens |

Mobile ≤1024: one card ~`min(100% - 40px, 360px)` per view; track still 100vw; native `scroll-snap` optional **or** keep §8.26 buttons — not both fighting the same axis.

#### Carousel card chrome — bordered or filled

Two equally valid surfaces — **shadow always none**:

```scss
.carousel-card {
  flex: 0 0 auto;
  border-radius: var(--pt-radius-lg);
  padding: 32px;
  box-shadow: none;

  &--bordered {
    background: var(--pt-color-neutral-50);
    border: 1px solid var(--pt-color-line-100);
  }

  &--filled {
    background: var(--pt-color-neutral-100);
    border: 0;
  }
}
```

Pick **one** chrome per floor (all cards match). On `neutral-100` floor bg, prefer `--bordered`; on canvas `neutral-50`, either works — filled reads as a quiet grey tile.

**Anti-patterns:** `box-shadow` · hover lift · gradient rim · mixing bordered + filled in one track · autoplay · dot indicators.

#### Variant A — centered head + bottom pager

Reference: testimonial / quote **carousel** (not §4.13 arena sync).

```jsx
<header className="floor-head">
  <h2>…one gradient word…</h2>
  <p className="heading-desc">…subtitle…</p>
</header>
```

- Pattern A centered head; one gradient word in `h2`.
- Track: **R17** testimonial cards (quote glyph · body copy · avatar row).
- Pager: `.carousel-pager--centered` below track — §8.26.

#### Variant B — left head + head-inline pager

Reference: **Judging Criteria**.

```jsx
<div className="carousel-floor-head-row">
  <header className="floor-head floor-head--left">
    <h2>Judging <span className="grad">Criteria</span></h2>
    <p className="heading-desc">How your project will be scored.</p>
  </header>
  <div className="carousel-pager carousel-pager--head-inline" aria-label="Slide pages">…</div>
</div>
```

```scss
.carousel-floor-head-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 24px 48px;
  margin-bottom: 48px;

  .floor-head { margin-bottom: 0; flex: 1 1 auto; }
}
```

- Pattern B / left stack head — **no** centered pager below (omit bottom `.carousel-pager--centered`).
- Track: **R18** criteria cards (metric % · title · bullet list).
- Pager sits **top-right**, vertically aligned with the title block baseline.

#### Interior recipes

**R17. Testimonial carousel card** *(§4.11 variant A)*
```
carousel-card bordered|filled · radius-lg · pad 32 · shadow none
quote icon 20×20 neutral-450 top-left
body: body-md neutral-750 · 3–4 lines
footer row: avatar 40 circle + name body-sm semibold + role caption neutral-650
```

**R18. Criteria carousel card** *(§4.11 variant B)*
```
carousel-card bordered|filled · radius-lg · pad 32
metric: title-lg bold neutral-950 (e.g. 30%)
title: body-lg semibold neutral-950
list: ul body-sm neutral-650 · disc markers · gap 8–10
```

#### Checklist (carousel toggle)

- [ ] Picked variant **A** (bottom pager) **or** **B** (head-inline pager)
- [ ] Head in **inner**; track **100vw** breakout; first card aligns to inner gutter
- [ ] All `.carousel-card` same chrome: `--bordered` **or** `--filled`; **no shadow**
- [ ] §8.26 prev/next; no autoplay / dots
- [ ] R17 (testimonial) **or** R18 (criteria) interior

### 4.12 FAQ floor — two-column accordion  ★

**FAQ 楼层：** 左栏标题 + 留白，右栏 **手风琴列表**（`+` 折叠，§8.27 **互斥单开**，**默认第一项展开**）。参考：**Frequently asked questions** + Learn More ↗。

两种外壳 — 每页选 **一种**：

| Shell | Background | Width container | When |
|-------|------------|-----------------|------|
| **A — inner canvas** | Floor stays `neutral-50`; no outer panel | `.layout-max-inner` | Minimal FAQ on white canvas (ref: plain two-col) |
| **B — wide panel** | `neutral-100` rounded panel inside outer | `.layout-max-wide` → `.faq-panel` | Prominent FAQ band before footer (ref: grey card) |

```
Shell A — inner neutral-50              Shell B — layout-max-wide panel
┌── .layout-max-inner ─────────────┐    ┌── .layout-max-wide ────────────────┐
│  Frequently          │ Q1  +     │    │ ┌ .faq-panel neutral-100 radius-lg ┐│
│  asked questions       │─────────│    │ │ Frequently    │ Q1  +            ││
│  [Learn More ↗]        │ Q2  +   │    │ │ asked quest…  │──────────────────││
│  ← left whitespace     │ answer… │    │ │ Learn More ↗  │ Q2  +  (open)    ││
│                        │ Q3  +   │    │ └──────────────────────────────────┘│
└────────────────────────┴─────────┘    └───────────────────────────────────────┘
     ~34–38% left              ~62–66% right accordion (content sits right-heavy)
```

Internal **`.faq-layout`** is identical in both shells — only the outer wrapper changes.

#### Floor shell

**Variant A — inner**

```jsx
<section className="floor floor--faq floor--faq-a">
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <div className="faq-layout">
        <header className="faq-head">…</header>
        <div className="faq-accordion" role="tablist">…</div>
      </div>
    </div>
  </div>
</section>
```

**Variant B — wide panel**

```jsx
<section className="floor floor--faq floor--faq-b">
  <div className="layout-max-wide">
    <div className="faq-panel">
      <div className="faq-layout">
        <header className="faq-head">…</header>
        <div className="faq-accordion" role="tablist">…</div>
      </div>
    </div>
  </div>
</section>
```

```scss
.faq-panel {
  background: var(--pt-color-neutral-100);
  border-radius: var(--pt-radius-lg);                   // 36 — large rounded band
  padding: 60px 44px;
  border: 0;
  box-shadow: none;
}

@media (max-width: 1024px) {
  .faq-panel { padding: 32px 20px; border-radius: var(--pt-radius-md); }
}
```

- Shell B panel: **no** `line-100` outer rim, **no** shadow — bg-step only (panel-as-card §11.6).
- Optional: `.faq-panel--wash` uses `--pt-gradient-card-bg` instead of flat `neutral-100` (legacy `.coding-plan-faq-panel`) — prefer flat `neutral-100` for new pages unless matching Token Plan.

#### Two-column layout — content right-heavy

```scss
.faq-layout {
  display: grid;
  grid-template-columns: minmax(200px, 38%) minmax(0, 1fr);
  gap: clamp(48px, 10vw, 120px);
  align-items: start;
}

@media (max-width: 1024px) {
  .faq-layout {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}
```

| Column | Role | Spec |
|--------|------|------|
| **Left** `.faq-head` | Title + optional link | Sticky optional `top: calc(var(--pt-nav-backdrop-offset) + 24px)` on long FAQ lists |
| **Right** `.faq-accordion` | Accordion stack | Full width of right column; items separated by `line-100` hairlines |

Left column carries **breathing room** — title must not crowd the accordion. On desktop the accordion column is visually **right-heavy** (~62–66% width). Do not center the accordion under the title on desktop.

#### Left head — Pattern C lite

```scss
.faq-head {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-right: clamp(16px, 4vw, 48px);               // extra air before accordion
}

.faq-head h2 {
  margin: 0;
  font-size: var(--pt-heading-font-size-md);            // 44 — or sm 36 in dense pages
  line-height: var(--pt-heading-line-height-md);
  font-family: var(--pt-font-bold);
  letter-spacing: var(--pt-letter-spacing-tight);
  color: var(--pt-color-neutral-950);
}

.faq-head .heading-desc,
.faq-head-link-desc {
  margin: 0;
  font-size: var(--pt-body-font-size-md);
  color: var(--pt-color-neutral-650);
  max-width: 280px;
}
```

- One `<span className="grad">` inside `h2` for gradient phrase (e.g. "**asked questions**" on line 2).
- Optional **Learn More ↗** below title: reuse `.floor-head-inline-link` (§8.23) — text link, not a pill.
- Title may wrap to **two lines** (line 1 solid + line 2 gradient) — do not force single-line.

#### Accordion — R20 + §8.27

```jsx
<div className="faq-accordion">
  <div className="faq-item is-open">
    <button type="button" className="faq-item__trigger" aria-expanded="true">
      <span className="faq-item__question">What is the Qwen Coding Plan?</span>
      <span className="faq-item__icon" aria-hidden="true">+</span>
    </button>
    <div className="faq-item__content">
      <div className="faq-item__content-inner">
        <p>…answer body-sm neutral-650…</p>
      </div>
    </div>
  </div>
  <div className="faq-item">…</div>
</div>
```

```scss
.faq-accordion {
  display: flex;
  flex-direction: column;
  width: 100%;
  border-top: 1px solid var(--pt-color-line-100);       // optional top cap
}

.faq-item {
  border-bottom: 1px solid var(--pt-color-line-100);
}

.faq-item__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 24px 0;
  background: transparent;
  border: 0;
  box-shadow: none;
  text-align: left;
  cursor: pointer;
  color: inherit;
}

.faq-item__question {
  flex: 1 1 auto;
  font-size: var(--pt-body-font-size-md);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
  line-height: var(--pt-body-line-height-md);
}

.faq-item__icon {
  flex: 0 0 auto;
  font-size: 20px;
  line-height: 1;
  font-weight: 300;
  color: var(--pt-color-primary-550);
  transition: opacity var(--pt-motion-fast) ease;
}

.faq-item.is-open .faq-item__icon {
  opacity: 0;
  pointer-events: none;
}

.faq-item__content {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition: grid-template-rows var(--pt-motion-fast) ease-in-out,
              opacity var(--pt-motion-fast) ease-in-out;
}

.faq-item.is-open .faq-item__content {
  grid-template-rows: 1fr;
  opacity: 1;
}

.faq-item__content-inner {
  overflow: hidden;
  padding-bottom: 24px;

  p {
    margin: 0;
    font-size: var(--pt-body-font-size-sm);
    line-height: var(--pt-body-line-height-sm);
    color: var(--pt-color-neutral-650);
    max-width: 56ch;
  }
}
```

**Interaction (§8.27):**

| Rule | Behavior |
|------|----------|
| **Default** | **First** `.faq-item` has `.is-open` on load |
| **Single-open** | **Exactly one** item open at all times — mutually exclusive |
| **On click** | Open clicked item; close all others; update `aria-expanded` |
| **No collapse-all** | Clicking the open item does **not** close it — switch to another question instead |
| **Icon** | `+` visible when collapsed; **hidden** (opacity 0) when `.is-open` — not a rotating `×` |
| **Keyboard** | `Enter` / `Space` on trigger; optional arrow keys between triggers |

Differs from §2.8 hero showcase accordion, **§4.13 arena sync** (visual column), and §8.6 generic accordion — FAQ uses **strict single-open** policy with **no** preview panel.

#### Anti-patterns

```
❌ Centered Pattern A head above a full-width accordion (loses left whitespace rhythm)
❌ Multiple items open simultaneously
❌ All items collapsed on load
❌ Shadow or line-100 box around each FAQ row (hairlines between rows only)
❌ Grey inset sub-cards for answers
❌ btn--primary in the accordion list
❌ Mixing shell A outer panel with shell B inner-only layout
```

#### Checklist (FAQ)

- [ ] Shell **A** (inner `neutral-50`) **or** **B** (`faq-panel` `neutral-100` `radius-lg` in `layout-max-wide`)
- [ ] `.faq-layout` **38% / 62%** grid; left `.faq-head` + right `.faq-accordion`
- [ ] §8.27: first item open; single-open only; `+` hides when open
- [ ] R20 row chrome; answers `body-sm` `neutral-650`

### 4.13 Accordion + visual sync floor — arena showcase  ★

**信息折叠 + 视觉联动楼层：** 居中大标题 → **左栏可点击 `+` 折叠列表** + **右栏大视觉面板**（随选中项切换）。参考：**Choose Your Arena** — MemoryAgent · EdgeAgent · **AI Showrunner**（展开描述 + 右侧剧场视觉）。

```
┌── .layout-max-inner — canvas neutral-50 ──────────────────────────────┐
│              Choose Your **Arena**          ← Pattern A centered h2      │
│              subtitle body-lg neutral-650                                │
│                         ↓ 48–60 px                                       │
│  ┌─ accordion ~42% ─────────────┐  ┌─ visual ~58% radius-lg ──────────┐ │
│  │ MemoryAgent               + │  │                                   │ │
│  │ ─────────────────────────── │  │   cover image / video             │ │
│  │ EdgeAgent                 + │  │   cross-fade per active item      │ │
│  │ ─────────────────────────── │  │                                   │ │
│  │ AI Showrunner  (open)       │  │                                   │ │
│  │   body-sm description…      │  │                                   │ │
│  └─────────────────────────────┘  └───────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────┘
```

Mid-page **feature / arena** band — not the homepage hero (§2.8 Mode B lives *inside* `.hero-visual` at 420 px). Not FAQ (§4.12 has title *in* left column, no visual).

#### vs related patterns

| | §2.8 hero Mode B | §4.12 FAQ | **§4.13** |
|--|------------------|-----------|-----------|
| Position | Under §2.7 title stack | Mid-page | Mid-page |
| Head | Above `.hero-visual` | Left column in grid | **Centered above** split |
| Shell | `.hero-visual--showcase` 420 px `gradient-card-bg` | `.faq-layout` 38/62 | `.arena-sync-layout` 42/58 in **inner** |
| Right column | Preview in same 420 box | Accordion answers | **Large visual** 400–520 px |
| Left column | Accordion | (title only) | Accordion + descriptions |

#### Floor shell

```jsx
<section className="floor floor--arena-sync">
  <div className="layout-max-inner-wrap">
    <div className="layout-max-inner">
      <header className="floor-head">
        <h2>Choose Your <span className="grad">Arena</span></h2>
        <p className="heading-desc">…subtitle…</p>
      </header>

      <div className="arena-sync-layout">
        <div className="arena-sync-accordion" role="tablist">
          <div className="arena-sync-item is-open" data-arena-panel="0">
            <button type="button" className="arena-sync-item__trigger" aria-expanded="true">
              <span className="arena-sync-item__title">MemoryAgent</span>
              <span className="arena-sync-item__icon" aria-hidden="true">+</span>
            </button>
            <div className="arena-sync-item__content">
              <div className="arena-sync-item__content-inner">
                <p>…body-sm neutral-650…</p>
              </div>
            </div>
          </div>
          …
        </div>

        <div className="arena-sync-visual" aria-live="polite">
          <div className="arena-sync-visual-panel is-active" data-panel="0">
            <img src="…" alt="" />
          </div>
          <div className="arena-sync-visual-panel" data-panel="1">…</div>
        </div>
      </div>
    </div>
  </div>
</section>
```

- Container: **`.layout-max-inner`** on canvas `neutral-50` (default).
- Head → body: `margin-bottom: 48–60 px` on `.floor-head`.
- **No** outer `line-100` card around the whole split — visual uses `radius-lg` only on the right panel.

#### Two-column grid

```scss
.arena-sync-layout {
  display: grid;
  grid-template-columns: minmax(0, 42%) minmax(0, 1fr);
  gap: clamp(40px, 6vw, 64px);
  align-items: start;
}

@media (max-width: 1024px) {
  .arena-sync-layout {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}
```

| Column | Width | Role |
|--------|-------|------|
| **Left** `.arena-sync-accordion` | **~42%** | Fold list — titles + expandable copy |
| **Right** `.arena-sync-visual` | **~58%** | Linked preview — one active panel |

Top of accordion aligns with top of visual panel on desktop (`align-items: start`).

#### Left accordion — R21

Same chrome language as §4.12 / §2.8 — hairline rows, `+` toggle, **no** per-row shadow or grey inset cards.

```scss
.arena-sync-item {
  border-bottom: 1px solid var(--pt-color-line-100);
}

.arena-sync-item__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 20px 0;
  background: transparent;
  border: 0;
  box-shadow: none;
  text-align: left;
  cursor: pointer;
}

.arena-sync-item__title {
  font-size: var(--pt-body-font-size-md);
  font-family: var(--pt-font-semibold);
  color: var(--pt-color-neutral-950);
}

.arena-sync-item__icon {
  flex: 0 0 auto;
  font-size: 20px;
  color: var(--pt-color-primary-550);
  transition: opacity var(--pt-motion-fast) ease;
}

.arena-sync-item.is-open .arena-sync-item__icon {
  opacity: 0;
  pointer-events: none;
}

.arena-sync-item__content {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition: grid-template-rows var(--pt-motion-fast) ease-in-out,
              opacity var(--pt-motion-fast) ease-in-out;
}

.arena-sync-item.is-open .arena-sync-item__content {
  grid-template-rows: 1fr;
  opacity: 1;
}

.arena-sync-item__content-inner {
  overflow: hidden;
  padding-bottom: 20px;

  p {
    margin: 0;
    font-size: var(--pt-body-font-size-sm);
    line-height: var(--pt-body-line-height-sm);
    color: var(--pt-color-neutral-650);
    max-width: 42ch;
  }
}
```

Optional leading icon in title row (16–20 px, `neutral-550`) — keep sparse; reference items are mostly text titles.

#### Right visual panel

```scss
.arena-sync-visual {
  position: relative;
  width: 100%;
  min-height: 400px;
  aspect-ratio: 16 / 10;                                  // optional lock; min-height wins on short viewports
  border-radius: var(--pt-radius-lg);
  overflow: hidden;
  background: var(--pt-color-neutral-100);
  box-shadow: none;
  border: 0;
}

.arena-sync-visual-panel {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity var(--pt-motion-normal) ease;
  pointer-events: none;

  &.is-active {
    opacity: 1;
    pointer-events: auto;
  }

  img, video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
}
```

| Property | Value |
|----------|-------|
| Height | **`min-height: 400px`** — up to **520 px** on wide screens; taller than §2.8 Mode B (420) |
| Radius | `--pt-radius-lg` (36) |
| Background | `neutral-100` placeholder until media loads |
| Shadow | **none** |
| Transition | Cross-fade opacity between panels — no slide carousel |

Use manifest images / product screenshots — not stock. Each panel maps 1:1 to an accordion item via `data-arena-panel` / `data-panel`.

#### Interaction — §8.28

| Rule | Behavior |
|------|----------|
| **Default** | First `.arena-sync-item` `.is-open`; first `.arena-sync-visual-panel` `.is-active` |
| **Single-open** | One accordion row expanded at a time |
| **On click** | Expand clicked row; collapse siblings; swap `.is-active` on matching visual panel |
| **Visual sync** | `data-arena-panel="n"` on item ↔ `data-panel="n"` on visual panel |
| **Icon** | `+` when collapsed; hidden when open — same as §4.12 |
| **No autoplay** | User-driven only |

Clicking the already-open item: **keep open** (same as §8.27) — user switches via another row.

#### Mobile (≤1024 px)

1. Accordion full width first.
2. `.arena-sync-visual` **below** the list — `min-height: 280–320px`; `aspect-ratio` may drop.
3. Optional: pin preview directly under the active item (same as §2.8 mobile) — pick one pattern per page.

#### Anti-patterns

```
❌ Nesting this inside `.hero-visual` (that's §2.8 Mode B — use one or the other on a page)
❌ FAQ left-title layout (§4.12) with a visual bolted on — use §4.13 shell instead
❌ Carousel ‹ › pager on the visual column
❌ Shadow or line-100 frame around the whole two-column block
❌ Multiple visual panels visible at once
❌ Autoplay rotation through arenas
```

#### Checklist (arena sync)

- [ ] Pattern A centered head above `.arena-sync-layout` in **inner**
- [ ] **42 / 58** split; R21 accordion left; `radius-lg` visual right
- [ ] §8.28: first item + panel active; single-open; `data-panel` sync
- [ ] Visual `min-height 400+`; cross-fade; no shadow

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
    font-family: var(--pt-font-mono);
    font-size: var(--pt-caption-font-size-sm);           // 12
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--pt-color-neutral-600);
  }
  h2 {
    font-size: var(--pt-heading-font-size-md);           // 44
    line-height: var(--pt-heading-line-height-md);
    font-family: var(--pt-font-bold);
    letter-spacing: var(--pt-letter-spacing-tight);
    color: var(--pt-color-neutral-950);
    margin: 0;
  }
  .heading-desc {                                        // subtitle
    margin: 0;
    color: var(--pt-color-neutral-750);
    font-size: var(--pt-body-font-size-lg);
    line-height: var(--pt-body-line-height-lg);
    max-width: 620px;                                    // ← see §9.4 width caps
  }
}
```

One `<span>` inside `h2` may clip a gradient (`--pt-gradient-1…8`). Max one gradient word per screen.

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
    font-size: var(--pt-body-font-size-md);
    color: var(--pt-color-neutral-650);
  }
}
```

### Pattern C — Two-column panel head  *(faq, ai-powered-product)*

Heading owns left column, content (accordion / cards) owns right. **Marketing FAQ floors:** full spec **§4.12** (shell A/B, `.faq-layout`, §8.27 accordion). Pattern C below is the legacy **gradient wash** panel recipe — §4.12 shell B prefers flat `neutral-100` + `radius-lg`.

```scss
.<floor>-panel {
  background: var(--pt-gradient-card-bg);
  border-radius: var(--pt-radius-md);
  padding: 60px 44px;
  display: grid;
  grid-template-columns: minmax(240px, 320px) minmax(0, 1fr);
  gap: 64px;                                             // or 154 px for very airy faq
}
.<floor>-panel h2 { font-size: var(--pt-heading-font-size-sm); }   // 36
```

Mobile: collapse to 1 column; padding → `32 20`; gap → 32.

### Pattern D — Asymmetric "skill" head  *(organic skills page; ref pattern)*

Grid `1fr 6fr; gap: 120px` inside inner. Left column = mono meta label. Right column = h1 + inline install/command block.

---

## 6. Reader column  *(legal, docs body, skills-detail body)*

Centered narrow column for long-form text. **Width = `min(100%, var(--pt-layout-max-read-box))` = 768 px.**

```scss
.legal-main-wrap     { padding-top: 108px; }             // 36 ≤640 px
.legal-main          { width: min(100%, var(--pt-layout-max-read-box));
                       margin: 0 auto 160px; }
.legal-page-title    { font-size: var(--pt-heading-font-size-sm);  // 36
                       font-family: var(--pt-font-bold);
                       margin: 48px 0 32px; }
.legal-subtitle      { font-size: var(--pt-title-font-size-md);    // 24
                       font-family: var(--pt-font-semibold);
                       margin-top: 48px; }
.legal-subsubtitle   { font-size: var(--pt-title-font-size-sm);    // 20
                       font-family: var(--pt-font-semibold);
                       margin-top: 28px; }
.legal-paragraph     { font-size: var(--pt-body-font-size-md);
                       line-height: var(--pt-body-line-height-md);
                       color: var(--pt-color-neutral-650);
                       margin-top: 16px; }
.legal-list li::before { width: 3px; height: 3px;
                         background: var(--pt-color-primary-550); }
.legal-note          { background: var(--pt-color-neutral-150);
                       border-radius: var(--pt-radius-xs);
                       padding: 16px; }
```

No side TOC. Tables use `border-bottom: var(--pt-line-size-normal) solid var(--pt-color-line-200)` on header rows. Code blocks `background: var(--pt-color-neutral-100); border-radius: var(--pt-radius-xs); padding: 16px`.

---

## 7. Grid systems

All grids snap to a small set of column×gap combinations. Pull from one row of the table; don't invent.

| Block | Columns | Gap (px) | Notes |
|-------|---------|---------:|-------|
| Featured model stack | 1 (stacking-card) | 14 | Inside the card: 2-col flex, main `flex: 0 0 45%` |
| **Media duo / agent-builder** | `repeat(2, minmax(0,1fr))` | 18 | Borderless visual cards; `align-items: start`; §4.5 |
| Industry / quick cards | `repeat(4, minmax(0,1fr))` | 36 | Mobile → 1fr; gap 18 |
| Analyst (asymmetric 2/1/1) | `2fr 1fr 1fr` | 24 | Mobile → 1fr; gap 16 |
| Reliability 2×2 | `repeat(2, minmax(0,1fr))` | col 114 / row 64 | Each item itself `100px 1fr; gap 48` |
| **Partner logo strip** (borderless) | flex center **or** `repeat(6–8, minmax(0,1fr))` | `clamp(32px, 6vw, 64px)` | §4.8 variant B; mobile wrap 2–3/row |
| Customer logo strip (legacy grid) | `repeat(7, minmax(0,1fr))` | `6vw` | Prefer §4.8 B flex; mobile → `repeat(3, …); gap 18` |
| Pricing offer (centered 2-up) | `repeat(2, clamp(320px, 30vw, 400px))` | 24 | `justify-content: center` |
| **Card row 3-up** (pricing / prize) | `repeat(3, minmax(0, 1fr))` | 24 | Equal stretch; §4.4; no shadow |
| **Card row 4-up** (token / credit plans) | `repeat(4, minmax(0, 1fr))` | 24 | + optional §8.4 toggle; §4.4 |
| **Simple card 3-up** (step / skill) | `repeat(3, minmax(0, 1fr))` | 24 | `line-100`, no shadow; §4.6; optional `1.12fr 1fr 1fr` |
| **Simple card 2-up** (step pair) | `repeat(2, minmax(0, 1fr))` | 24 | §4.6 variant A |
| **Text-card 4-up** (secondary showcase) | `repeat(4, minmax(0, 1fr))` | 24 / 32 | Bottom `line-100` only; §4.7 |
| **Text-card 3-up** (secondary showcase) | `repeat(3, minmax(0, 1fr))` | 24 / 32 | §4.7 |
| **Logo matrix** (tools / partners) | `repeat(4, minmax(0,1fr))` | 12 | h 64 · `line-100` · §4.8 **variant A** |
| Tools / logo tiles (legacy class) | `repeat(4, minmax(0,1fr))` | 12 | `.coding-plan-tools-item` = §4.8 A |
| **Site footer nav** | `repeat(3, minmax(0, 1fr))` inside 65% column | 32 / 48 | §4.10 R16; mobile → 2 then 1 col |
| **Site footer main** | `35fr 65fr` | 48 / 64 | Aside social + link grid; §4.10 |
| **Carousel toggle track** | horizontal flex; card `380–420px` fixed | 24 | 100vw breakout; §4.11; peek right |
| **FAQ two-column** | `38% 1fr` inside `.faq-layout` | 48–120 | Left head + right accordion; §4.12 |
| **Arena sync** | `42% 1fr` `.arena-sync-layout` | 40–64 | Accordion + visual; §4.13 |
| Models marketplace | `repeat(auto-fill, minmax(260px, 1fr))` | 24 | Card 340-px tall, `--pt-radius-sm` |
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

- Dot 6×6 px, `border-radius: 999px`, color from `--pt-color-accent-{mint|orchid|electric-blue|rose|emerald|apricot|sky}`
- `strong`: `--pt-title-font-size-lg` (28), `--pt-font-semibold`
- `small`: `--pt-body-font-size-md`, color `--pt-color-neutral-550`
- Symbols (`+`, `<`, `%`) render as sibling `<span>`

Used in: home hero overlay (4-up), signup brand panel.

### 8.2 Chip / tag pill

```
display: inline-flex; align-items: center;
padding: 8px 12px;
border-radius: var(--pt-radius-full);
font-size: var(--pt-body-font-size-sm);
background: var(--pt-color-neutral-150);
color: var(--pt-color-neutral-700);
```

Active: `background: var(--pt-color-primary-50); color: var(--pt-color-primary-550)`. No border on filled; outline variant uses `--pt-color-line-200`.

### 8.3 Pill tab (with leading dot when active)

Same pill shape. Active tab gets a 6-px primary dot rendered as `::before { margin-right: 6px }`.

For **flat secondary-floor tabs** (inactive = no bg), use **§8.20** — 5 px dot, `neutral-150` active fill only.

### 8.4 Pill segmented control

```
height: 36–40px;
padding: 4–6px;
border-radius: var(--pt-radius-full);
background: var(--pt-color-neutral-150);
display: inline-flex; gap: 4px;
```

Selected child: `background: var(--pt-color-neutral-50); box-shadow: var(--pt-shadow-light); border-radius: var(--pt-radius-full)`.

### 8.5 Underline sub-nav

```
display: inline-flex; gap: 32px;
border-bottom: var(--pt-line-size-thin) solid var(--pt-color-line-100);
```

Active tab: `position: relative; &::after { content:''; position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: var(--pt-color-primary-550) }`.

### 8.6 Accordion item

```
.content {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition: grid-template-rows var(--pt-motion-fast) ease-in-out,
              opacity var(--pt-motion-fast) ease-in-out;
}
.is-open .content { grid-template-rows: 1fr; opacity: 1; }
```

Item divider: `border-bottom: var(--pt-line-size-normal) solid var(--pt-color-line-200)`; padding `40px 0`. Plus-icon button hidden in expanded state.

### 8.7 Inline command / code box

```
padding: 16px;
border-radius: var(--pt-radius-xs);
background: var(--pt-color-neutral-100);
min-height: 44px;
gap: 8px;
font-family: var(--pt-font-mono);
font-size: var(--pt-body-font-size-sm);
```

Trailing copy button: `flex: 0 0 auto`, icon-only (`copy-outlined`).

### 8.8 Inline notice

```
margin-top: 24px;
padding: 16px;
border-radius: var(--pt-radius-xs);
background: var(--pt-color-supporting-{blue|orange|green|red}-bg);
display: flex; gap: 12px;
```

Icon at start (12 px), text fills rest.

### 8.9 Section divider line

`border-bottom: var(--pt-line-size-normal) solid var(--pt-color-line-200)`. Use for accordion items and intra-card metric rows — **never as floor boundaries** (use whitespace + bg step instead).

### 8.10 Sticky compare bar (overlay)

```
position: fixed; left: 50%; bottom: 24px;
transform: translateX(-50%);
padding: 24px 32px;
border-radius: var(--pt-radius-md);
background: var(--pt-color-neutral-50);
box-shadow: var(--pt-shadow-light);
backdrop-filter: blur(10px);
z-index: 1000;
```

### 8.11 Search input — pill with gradient focus ring

Nav-style.

```
height: 48px;
padding: 0 16px 0 14px;
border: 1px solid var(--pt-color-line-200);
border-radius: var(--pt-radius-full);
background: var(--pt-color-neutral-50);
font-size: var(--pt-body-font-size-sm);
```

Focus: `border-color: transparent`, plus a 1-px gradient ring drawn with `::before { background: var(--pt-gradient-4); -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); mask-composite: exclude }`. Width default 228 px, expand-on-focus to 490 px.

Leading icon: `search-outlined`. Trailing: `command-outlined` (⌘K), small mono caption-md.

### 8.12 Dropdown / collapsible group

```
.dropdown {
  border-radius: var(--pt-radius-sm);
  background: var(--pt-color-neutral-50);
}
.dropdown-trigger {
  width: 100%; min-height: 48px;
  padding: 0 16px;
  display: flex; align-items: center; justify-content: space-between;
  color: var(--pt-color-neutral-850);
  font-size: var(--pt-body-font-size-sm);
  font-family: var(--pt-font-semibold);
  background: transparent; border: 0;
}
.dropdown-trigger svg { width: 16px; transition: transform var(--pt-motion-fast) ease; }
.dropdown.is-open .dropdown-trigger svg { transform: rotate(90deg); }     // or 180° for chevron-down
.dropdown-content {
  padding: 0 14px 14px;
  color: var(--pt-color-neutral-750);
  font-size: var(--pt-body-font-size-sm);
  line-height: var(--pt-body-line-height-sm);
}
```

Use for: docs sidebar groups, filter groups, mobile-collapsed sections.

### 8.13 Floating search dropdown panel

```
position: absolute;                                      // anchored under nav search
margin-top: calc(var(--pt-nav-backdrop-offset) + 20px);
max-height: min(560px, calc(100vh - var(--pt-nav-backdrop-offset) - 32px));
padding: 12px;
border-radius: var(--pt-radius-md);
background: var(--pt-color-neutral-50);
box-shadow: var(--pt-shadow-light);
overflow: auto;
```

Result items: 48-px-tall rows, padding `8px 12px`, hover bg `--pt-color-neutral-100`, `border-radius: var(--pt-radius-xs)`.

### 8.14 Breadcrumb row

```
display: inline-flex; align-items: center; gap: 8px;
font-size: var(--pt-body-font-size-sm);
color: var(--pt-color-neutral-650);
```

Separator: `chevron-right-outlined` 12 px, color `--pt-color-neutral-450`. Last segment color `--pt-color-neutral-950`.

### 8.15 Stat / kv row inside cards

```
display: grid;
grid-template-columns: minmax(0, auto) 1fr;
column-gap: 8px;
font-size: var(--pt-body-font-size-sm);
```

Key (left): color `--pt-color-neutral-650`. Value (right): color `--pt-color-neutral-950`, mono if numeric.

### 8.16 Icon + text feature row  *(inside card-row ZONE C, tier benefits)*

The clean icon + copy pattern for pricing / plan / prize cards. **Typography carries hierarchy — no grey boxes.**

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

  &:last-child { margin-bottom: 0; }

  .card-feature-icon {
    width: 16px;
    height: 16px;
    margin-top: 2px;                                     // optical align with body-md cap height
    color: var(--pt-color-neutral-750);
    flex-shrink: 0;
  }

  .card-feature-text {
    font-size: var(--pt-body-font-size-md);
    line-height: var(--pt-body-line-height-md);
    color: var(--pt-color-neutral-950);
    font-family: var(--pt-font-semibold);
  }

  .card-feature-sub {
    margin-top: 4px;
    font-size: var(--pt-body-font-size-sm);
    line-height: var(--pt-body-line-height-sm);
    color: var(--pt-color-neutral-650);
    font-family: var(--pt-font-regular);
    font-weight: 400;
  }
}
```

**Nested list** (model names, sub-bullets) — indent under text column, not icon:

```scss
.card-feature-nested {
  margin-top: 8px;
  padding-left: 0;
  list-style: none;

  li {
    position: relative;
    padding-left: 14px;
    font-size: var(--pt-body-font-size-sm);
    color: var(--pt-color-neutral-650);
    margin-bottom: 4px;

    &::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0.65em;
      width: 3px;
      height: 3px;
      border-radius: 999px;
      background: var(--pt-color-primary-550);
    }
  }
}
```

- One icon per row; icon from manifest (`check-outlined`, `notification-outlined`, `sparkle-outlined`).
- **No** background fill on rows; **no** `border` around individual features.
- Strong line + optional sub-line + optional nested list — max three levels, then truncate.

Used in: `.card-row-item` ZONE C (§4.4), `.coding-plan-offer-card` benefits, `.tier` feature list (`components.md` §07).

### 8.17 Step tag pill  *(§4.6 variant A)*

Leading-dot step label at top of step cards.

```scss
.step-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  border-radius: var(--pt-radius-full);
  background: var(--pt-color-primary-50);
  font-size: var(--pt-body-font-size-sm);
  font-family: var(--pt-font-medium);
  color: var(--pt-color-neutral-800);
  width: fit-content;

  &::before {
    content: '';
    width: 6px;
    height: 6px;
    border-radius: 999px;
    background: var(--pt-color-primary-550);
    flex-shrink: 0;
  }
}
```

Alt neutral: `background: var(--pt-color-neutral-150); color: var(--pt-color-neutral-700);` — dot stays `primary-550`.

### 8.18 Price-text row  *(§4.6 variant B, model cards)*

Token / rate lines above the card divider — mono, quiet, never in a grey box.

```scss
.simple-card-price {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 16px;
  margin-top: 12px;
  font-size: var(--pt-body-font-size-sm);
  font-family: var(--pt-font-mono);
  line-height: var(--pt-body-line-height-sm);
  color: var(--pt-color-neutral-650);
}
.simple-card-price__item {
  white-space: nowrap;
}
```

- Pattern: `Input $ 0.10/M tokens` · `output $ 2–3.60/M tokens` — side by side or stacked when narrow.
- Align with `ui-price-text` / `ui-unit-text` (`components.md` §08) on console; marketing uses this static row.
- **No** border, **no** `neutral-100` fill around the row.

### 8.19 Modality chip  *(skill card tag rail)*

Outline purple capability tags — distinct from §8.2 filled chips and from Hot badge.

```scss
.modality-chip {
  display: inline-flex;
  align-items: center;
  padding: 6px 10px;
  border-radius: var(--pt-radius-full);
  border: 1px solid var(--pt-color-primary-150);
  background: transparent;
  font-size: var(--pt-body-font-size-sm);
  color: var(--pt-color-primary-550);
}
.simple-card-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}
```

Max **one visual row** — if more modalities, show top 3–4 then `+N` caption-sm `neutral-550`.

### 8.20 Secondary tabs  *(§4.7 filter rail)*

Minimal tab switcher — no track, no underline bar. Full recipe in §4.7; class names `.secondary-tabs` · `.secondary-tab` · `.is-active`.

- Inactive: transparent, `neutral-650`, no border/shadow.
- Active: `neutral-150` pill + **5 px** `primary-550` dot before label.

### 8.21 Text-card link affordance  *(§4.7 bottom corner)*

```scss
.text-card-link {
  display: inline-flex;
  align-items: center;
  margin-top: auto;
  padding-top: 16px;
  color: var(--pt-color-neutral-750);
  transition: color var(--pt-motion-fast) ease;

  &:hover { color: var(--pt-color-primary-550); }

  svg, .qc-icon { width: 14px; height: 14px; }
}
```

Icon: `arrow-up-right-outlined`. Wrap entire `.text-card` in `<a>` when the whole tile is tappable.

### 8.22 Text-card carousel pager  *(§4.7 variant B)*

Centered prev/next for paginated text-card rows — circular ghost controls, no shadow.

```scss
.text-card-pager {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  margin-top: 48px;
}

.text-card-pager-btn {
  width: 40px;
  height: 40px;
  padding: 0;
  border-radius: var(--pt-radius-full);
  border: var(--pt-line-size-normal) solid var(--pt-color-line-100);
  background: transparent;
  box-shadow: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--pt-color-neutral-550);
  cursor: pointer;
  transition: color var(--pt-motion-fast) ease, border-color var(--pt-motion-fast) ease;

  svg { width: 16px; height: 16px; }

  &:hover:not(:disabled) {
    color: var(--pt-color-neutral-950);
    border-color: var(--pt-color-line-200);
  }

  &:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }
}
```

Icons: `chevron-left-outlined` · `chevron-right-outlined`. **No** fill, **no** `neutral-150` track — pairs with borderless text-cards.

### 8.23 Floor-head subtitle with inline link  *(§4.8 logo matrix)*

Centered lead + purple text link in one subtitle line — not a pill CTA.

```scss
.floor-head-link-desc {
  margin: 0;
  max-width: 620px;
  font-size: var(--pt-body-font-size-lg);
  line-height: var(--pt-body-line-height-lg);
  color: var(--pt-color-neutral-750);
  text-align: center;
}

.floor-head-inline-link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: var(--pt-color-primary-550);
  font-family: var(--pt-font-medium);
  text-decoration: none;

  &:hover { color: var(--pt-color-primary-700); }

  svg, .qc-icon { width: 12px; height: 12px; }
}
```

Icon: `arrow-up-right-outlined`. Keep on the same line as prose when possible.

### 8.24 Site footer social row  *(§4.10)*

Flat brand icons in `.page-footer-social` — **20×20 px**, `neutral-950`, gap **16–20 px**, no border/bg/shadow. Tabler `brand-x`, `brand-github`, `brand-linkedin`, `brand-discord` when not in manifest.

### 8.25 Tail-visual kicker line  *(§4.9)*

Optional single line above `h2` inside `.tail-visual__content`:

```scss
.tail-visual-kicker {
  margin: 0;
  font-size: var(--pt-body-font-size-md);
  color: var(--pt-color-neutral-750);
  max-width: min(100%, var(--pt-layout-max-read-box));
}
```

Reuse `.floor-head-inline-link` (§8.23) for the purple action — not a pill button.

### 8.26 Carousel toggle pager  *(§4.11)*

Circular **‹ ›** controls for 100vw card tracks. Distinct from §8.22 (text-card static grid) — supports **emphasis** on the forward control.

```scss
.carousel-pager {
  display: inline-flex;
  align-items: center;
  gap: 12px;

  &--centered {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-top: 48px;
  }

  &--head-inline {
    flex: 0 0 auto;
    align-self: flex-end;
    margin-bottom: 4px; // optically align with h2 baseline row
  }
}

.carousel-pager-btn {
  width: 40px;
  height: 40px;
  padding: 0;
  border-radius: var(--pt-radius-full);
  border: 1px solid var(--pt-color-line-100);
  background: transparent;
  box-shadow: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--pt-color-neutral-950);
  cursor: pointer;
  transition: background var(--pt-motion-fast) ease,
              border-color var(--pt-motion-fast) ease,
              color var(--pt-motion-fast) ease;

  svg, .qc-icon { width: 16px; height: 16px; }

  &:hover:not(:disabled) {
    border-color: var(--pt-color-line-200);
  }

  &:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }

  // Forward / "next" emphasis when more slides exist (Judging Criteria, Arena)
  &--next:not(:disabled),
  &.is-emphasis:not(:disabled) {
    background: var(--pt-color-neutral-950);
    border-color: var(--pt-color-neutral-950);
    color: var(--pt-color-neutral-50);

    &:hover {
      background: var(--pt-color-neutral-850);
      border-color: var(--pt-color-neutral-850);
    }
  }
}
```

Icons: `chevron-left-outlined` · `chevron-right-outlined`. **No** shadow · **no** `neutral-150` pill track · **no** dot pagination.

| Placement | Class | Pairs with |
|-----------|-------|------------|
| Below track | `.carousel-pager--centered` | §4.11 variant A |
| Head row right | `.carousel-pager--head-inline` | §4.11 variant B |

Wire `aria-label="Previous slide"` / `"Next slide"`; disable prev at start / next at end.

### 8.27 FAQ accordion — single-open policy  *(§4.12)*

Applies to `.faq-accordion` / `.faq-item` — **not** §2.8 hero preview accordion, **§4.13** `.arena-sync-accordion` (visual sync per §8.28), or docs sidebar groups.

| Rule | Implementation |
|------|----------------|
| Initial state | `faqItems[0].classList.add('is-open')`; `aria-expanded="true"` on first trigger only |
| Toggle | On trigger click: remove `.is-open` from **all** siblings; add to clicked item |
| Minimum one open | If click targets already-open item, **no-op** (keep it open) |
| Icon | `.faq-item__icon` = literal `+` or `plus-outlined` 16–20 px `primary-550`; hidden when `.is-open` |
| Dividers | `border-bottom: 1px line-100` per `.faq-item` — not a box around each row |
| Motion | `grid-template-rows: 0fr → 1fr` + opacity (§8.6); respect `prefers-reduced-motion` |

```js
// Behavioral contract (pseudocode)
function onFaqClick(clickedItem) {
  if (clickedItem.classList.contains('is-open')) return;
  accordion.querySelectorAll('.faq-item.is-open').forEach((el) => {
    el.classList.remove('is-open');
    el.querySelector('.faq-item__trigger')?.setAttribute('aria-expanded', 'false');
  });
  clickedItem.classList.add('is-open');
  clickedItem.querySelector('.faq-item__trigger')?.setAttribute('aria-expanded', 'true');
}
```

### 8.28 Arena sync — accordion + visual panel  *(§4.13)*

Applies to `.arena-sync-accordion` + `.arena-sync-visual` — extends §8.27 single-open rules with **preview sync**.

| Rule | Implementation |
|------|----------------|
| Pairing | `.arena-sync-item[data-arena-panel="n"]` ↔ `.arena-sync-visual-panel[data-panel="n"]` |
| Initial | Index `0` open on both sides |
| On select | Close all items; open clicked; remove `.is-active` from all panels; add to matched panel |
| Visual transition | Opacity cross-fade `--pt-motion-normal`; no horizontal slide |
| Already open | Same no-op as §8.27 |
| `aria-live` | `polite` on `.arena-sync-visual` when panel swaps |

```js
function onArenaSyncClick(clickedItem) {
  if (clickedItem.classList.contains('is-open')) return;
  const panelId = clickedItem.dataset.arenaPanel;
  accordion.querySelectorAll('.arena-sync-item.is-open').forEach((el) => {
    el.classList.remove('is-open');
    el.querySelector('.arena-sync-item__trigger')?.setAttribute('aria-expanded', 'false');
  });
  visual.querySelectorAll('.arena-sync-visual-panel.is-active').forEach((el) => {
    el.classList.remove('is-active');
  });
  clickedItem.classList.add('is-open');
  clickedItem.querySelector('.arena-sync-item__trigger')?.setAttribute('aria-expanded', 'true');
  visual.querySelector(`[data-panel="${panelId}"]`)?.classList.add('is-active');
}
```

Reuse §2.8 `.hero-visual-preview-panel` fade recipe when sharing CSS — class names may alias in implementation.

---

## 9. Typography arrangement

### 9.1 Heading scale (where each size lives)

| Token | px | Role |
|-------|---:|------|
| `--pt-heading-font-size-3xl` | 96 | Ultra-marketing hero (rare; e.g. organic home `clamp(72, 10vw, 168)`) |
| `--pt-heading-font-size-2xl` | 72 | Marketing hero h1 (variant B), closing CTA h2 |
| `--pt-heading-font-size-xl`  | 64 | Tagline split hero (variant A), asymmetric skill hero (variant I) |
| `--pt-heading-font-size-lg`  | 60 | Centered intro hero (variant C) |
| `--pt-heading-font-size-md`  | 44 | Section heads (pattern A/B), marketplace hero (variant D) |
| `--pt-heading-font-size-sm`  | 36 | Legal page title, docs hero, sub-page h1, panel-head (pattern C) |
| `--pt-title-font-size-lg`    | 28 | Card title, hero metric strong, sub-section title |
| `--pt-title-font-size-md`    | 24 | Card title (compact), legal subtitle |
| `--pt-title-font-size-sm`    | 20 | List item title, legal sub-subtitle |

All headings use `--pt-font-bold` (or `--pt-font-semibold` for titles) and `--pt-letter-spacing-tight`. Line-height is locked to each size via `--pt-{heading|title}-line-height-*` — don't override.

### 9.2 Body scale

| Token | px / lh | Role |
|-------|--------:|------|
| `--pt-body-font-size-lg` | 18 / 24 | Hero subtitle, section subtitle, lead paragraph |
| `--pt-body-font-size-md` | 16 / 22 | Body |
| `--pt-body-font-size-sm` | 14 / 20 | Card meta, filter labels, chips, dropdown items |
| `--pt-body-font-size-xs` | 13 / 18 | Caption mono, table cell, micro UI |
| `--pt-caption-font-size-sm` | 12 / 16 | Eyebrow / uppercase mono kicker, breadcrumb separator label |

Body uses `--pt-font-regular`; mono `--pt-font-mono`. Body letter-spacing: `--pt-letter-spacing-loose` (0.02em).

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
| Centered hero sub (B, C) | `var(--pt-layout-max-read-box)` = 768 px |
| Centered floor-head A sub | 620 px (or 768 px for short copy) |
| Left-aligned floor-head B sub | 760 px |
| Hero variant A `tagline-desc` | 680 px |
| Card body copy | width of card (no explicit cap) |
| Legal paragraph | 768 px (inherited from reader column) |
| Asymmetric skill sub (I) | `min(620px, 100%)` |

Mobile: caps drop with the viewport; never set them in vw.

### 9.5 Gradient text rule

- **At most one gradient `<span>` per floor.**
- **At most one gradient `<span>` per visible viewport on the hero floor** (in practice: one gradient word in the h1).
- Use `--pt-gradient-1` through `8`. Animation optional (`background-position` 6–12 s ease-in-out).
- Never on body copy. Never on buttons. Never on backgrounds.

---

## 10. Spacing rhythm

**No `--pt-spacing-N` tokens in this kit.** Write px literals on the 2-px rhythm:

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

Cards are the central composition unit. **There are two equally first-class flavors: bordered cards (hairline `--pt-color-line-100`) and borderless cards (separated by bg-step alone).** Pick by context — borderless when the card sits on a stepped surface (e.g. `neutral-50` card on `neutral-100` panel, or `gradient-card-bg` panel hosting nested rows); bordered when the card sits on the page canvas with no surrounding panel.

### 11.1 The card archetype table

All values are token-real (quoted from `qwencloud-v1/src`).

#### A — Standard bordered cards (canvas + hairline)

| Card | Bg | Border | Radius | Padding | Used |
|------|----|--------|--------|---------|------|
| Marketplace card (`.models-card`) | `--pt-color-neutral-50` | `1px --pt-color-line-100` | `--pt-radius-sm` | 24 | `models` grid; fixed `height: 340` |
| Pricing offer (`.coding-plan-offer-card`) | `--pt-color-neutral-50` | `1px --pt-color-line-100` | `--pt-radius-sm` | 32 | coding-plan pricing |
| Compare card (`.models-compare-card`) | `--pt-color-neutral-50` | `1px --pt-color-line-100` | `--pt-radius-sm` | `36 24` | models/compare |
| Code-snippet (`.code-snippet`) | wrap `--pt-color-neutral-50` | `1px --pt-color-line-100` | `--pt-radius-xs` | wrap 12; tabs h42; body 16 | docs, models-detail, skills |
| Try-it section (`.docs-tryit-section`) | `--pt-color-neutral-50` | `1px --pt-color-line-100` | `--pt-radius-sm` | 14 | docs try-it drawer |
| Half-pixel data card (`.models-detail-tool-item`, `.models-detail-context-card`) | `--pt-color-neutral-50` | `0.5px --pt-color-line-100` (half-pixel hairline) | `--pt-radius-sm` / `xs` | 16 / 24 | models-detail high-density rows |
| Tagline command panel (`.tagline-skills`) | inherits canvas | `1px --pt-color-line-100` | `--pt-radius-md` | 0 (children pad 16) | home tagline right column |
| Logo tile (`.coding-plan-tools-item`) | inherits | `1px --pt-color-line-100` | `--pt-radius-xs` | `0 8 0 24`, h64 | coding-plan tools 4-up |

**Hover:** `box-shadow: var(--pt-shadow-light); transform: translateY(-4px)` — that's the entire move. Border stays.

#### B — Borderless cards (bg-step separation) — equally common

The kit uses borderless cards aggressively. **Whenever a card sits on a panel that is already one neutral step darker than canvas, drop the border.**

| Card | Bg | Radius | Padding | Used | Why borderless |
|------|----|--------|---------|------|----------------|
| `.afm-card` | `--pt-color-neutral-150` | `--pt-radius-md` | 28 | home AFM | Sits on canvas; step up to 150 carries it |
| `.afm-card-full` | `--pt-gradient-card-bg` | `--pt-radius-md` | 36 | home AFM hero / stacking | Gradient wash separates it |
| `.analyst-card` | `--pt-color-neutral-100` + themed bg-image | `--pt-radius-xs` | `32 24` | home analyst grid | Image inset; chrome would compete |
| `.afm-industry-card` | inherits | (only `border-bottom 1px --pt-color-line-200`) | `4 4 20` | home industry 4-up | Bottom hairline only — reads as list row, not card |
| `.docs-content-panel` | `--pt-color-neutral-100` | `--pt-radius-lg` | `40 48` | docs page shell | The outer "panel hero" itself |
| `.docs-card` | `--pt-color-neutral-50` | `--pt-radius-sm` | 16 | docs `.docs-cards` 2-up | Sits on `neutral-100` parent panel |
| `.docs-minicard` | `--pt-color-neutral-50` | `--pt-radius-sm` | 16 | docs mini-cards grid | Same — parented by stepped panel |
| `.docs-next` | `--pt-color-neutral-50` | `--pt-radius-md` | 12 | docs page-bottom nav | Inner tile (`neutral-100, radius-xs, 12 20`) provides depth |
| `.docs-timeline-content` | `--pt-color-neutral-50` | `--pt-radius-sm` | `16 20` | docs timeline | Paired with dotted rail + glowing dot |
| `.signup-brand-panel` | `--pt-color-neutral-100` + video | `--pt-radius-lg` | 32 | signup left | Full-bleed video carries it |
| `.coding-plan-intro-showcase` | `--pt-gradient-card-bg` | `--pt-radius-md` | `60 44` | coding-plan intro | Big floor-as-panel |
| `.coding-plan-faq-panel` | `--pt-gradient-card-bg` | `--pt-radius-md` | `60 44` | coding-plan faq | Same |
| `.prod-shell` | `--pt-gradient-card-bg` | `--pt-radius-md` | `60 44 36` | home AI-powered product | Same |
| `.bulletin-section` | `--pt-color-neutral-100` + themed bg | `--pt-radius-md` | `var(--pt-bulletin-padding)` | home bulletin | Banner card |
| `.models-detail-context-card-thinking` | `--pt-color-neutral-100` | `--pt-radius-xs` | 24 | models-detail | Borderless variant of the default context card |
| `.models-detail-side-highlight` | `--pt-color-neutral-100` | `--pt-radius-sm` | 16 | models-detail right rail | Carries progress meter + CTA |
| `.skills-detail-note` | `--pt-color-neutral-100` | `--pt-radius-xs` | `16 24` | skills detail | Inline tip card |
| `.docs-notice` | `--pt-color-supporting-{green,blue,orange,red}` | `--pt-radius-xs` | 16 | docs callouts | Colored bg already separates |
| `.legal-note` | `--pt-color-neutral-150` | `--pt-radius-xs` | 12 | legal pages | Inline aside |

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
  inset: calc(-1 * var(--pt-line-size-normal));
  padding: var(--pt-line-size-normal);
  border-radius: inherit;
  background: var(--pt-gradient-2);                        // or 4 / 7 by site role
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
| Compared / selected card (`.models-card.is-compared`) | `--pt-gradient-2` | 8 s |
| Featured pricing tier (`.coding-plan-offer-card.is-featured`) | `--pt-gradient-2` | 8 s |
| Focused search input (`.models-market-search:focus-within`, `.nav-search:focus-within`) | `--pt-gradient-4` | 3 s |
| Era CTA email input (`.era-hero-email`) | `--pt-gradient-1` | 19.6 s |
| Solid hot tag (`.tag-normal.tag-hot`) | `--pt-gradient-6` fill (not rim) | n/a |

**Stagger animations on tag clouds** with `:nth-child(3n / 4n / 5n)` delays — keeps the page from pulsing in lockstep.

Featured cards **never** get a shadow; the rim does the work.

#### D — Media-first cards (full-bleed image/video + content panel)

| Card | Recipe |
|------|--------|
| `.customers-say-card` 670×424 | `border-radius: --pt-radius-md; background: cover image; ::before linear-gradient(0deg, rgba(7,8,14,0.1) → transparent) for legibility; .customers-say-overlay absolute top:12 right:12 w:44% min:337 — a borderless nested card on neutral-50, radius-sm, padding 30 20 24 20, holding quote (h36 bold) + p (body-sm neutral-750) + signature + logo bottom-right` |
| `.models-hero-card` 588×244 | `border-radius: --pt-radius-xs (mobile: 18); padding 12 outer; .models-hero-card-main is a 270×220 right-anchored borderless panel on neutral-50 holding logo (24×24) + title-sm + 2-line clamp + tag row` |
| `.skills-detail-hero` | `border-radius: --pt-radius-lg; bg: neutral-100 + cover image; padding 24; centered glass command box inside (see G)` |
| `.era-hero-shell` / `.tail-visual--tall` 790h | `border-radius: --pt-radius-lg; absolute media; centered R15 stack (h2 72 + L1/L3 CTAs); §4.9; legacy email-input variant optional` |
| `.tail-visual--compact` 370h | `same shell; h2 44; community / hackathon close; §4.9` |
| `.media-duo-visual` / marketing agent-builder | `radius-md (24); **no border**; **no shadow**; aspect 16:10 or h 248–280; cover video/img; icon 20×20 top-left; §4.5` |
| `.agent-builder-visual` (§08 gallery specimen only) | `radius-xs; 1px line-100; h248` — **do not** copy this chrome on marketing floors; use §4.5 borderless recipe |

**Pattern:** the section heading sits **outside** the media (floor-head above the grid, §2). Card titles sit **below** the visual frame, not on the photograph.

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
| **Synced preview pair** (`.hero-visual--showcase` / `.coding-plan-intro-showcase`) | 2-col `1fr 1fr; gap: 64`; left accordion controls right preview via absolute `.hero-visual-preview-panel` with `.is-active` fade. Locked **`height: 420`**. |
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
| `.skills-detail-command-box` | **glass tile**: `bg: color-mix(in srgb, --pt-color-neutral-100 82%, transparent); backdrop-filter: blur(12px); radius-xs; padding 16; height 52; box-shadow: --pt-shadow-light` |
| `.tagline-skills-command-wrap` | **stepped tile**: `bg: --pt-color-neutral-100; radius-xs; padding 16; min-height: 44`; mono prompt + command + copy button |
| `.signup-back-btn` | circular tile `bg neutral-150; radius-full; 30×30` |

#### H — Overlay panels (popovers, FABs, sticky bars, sheets)

| Panel | Recipe |
|-------|--------|
| Sort/model/language dropdown (`.models-market-sort-dropdown`, `.models-detail-model-dropdown`, etc.) | `bg neutral-50; radius-md; padding 12; box-shadow --pt-shadow-light; flex-col gap 8`. **No border.** Items: pill `radius-full; padding 8 16`; selected `bg neutral-150`; hover `bg neutral-100`; right-side check 16×16. |
| Compare bar (`.models-compare-bar`) | **glass + normal shadow** — `bg --pt-color-models-compare-bar-bg; backdrop-filter: blur(10px); radius-md; padding 24 32; box-shadow --pt-shadow-normal; position: fixed; left: 50%; bottom: 24; transform: translateX(-50%); z-index: 1000`. Tags row max-content + actions ml40 (now-btn light + close 32×32 round). |
| Mobile filter sheet (`.models-market-sidebar.is-open`) | `bg neutral-50; padding 20 12 12; box-shadow --pt-shadow-normal; position: fixed; full-vh below nav offset`. |
| Mobile FAB (`.models-market-sidebar-fab`) | `bg neutral-50; border: 1px line-100; radius-full; padding: 0 20; height: 40; box-shadow --pt-shadow-normal; position: fixed; right: 20; bottom: 20`. Stacks (rises) when compare-bar is present. |
| Docs search dropdown (`.docs-search-dropdown`) | **glass via pseudo** — `::before { bg --pt-color-neutral-50; backdrop-filter: blur(12px) }`; `radius-sm; padding 16; box-shadow --pt-shadow-normal`. Holds pill input (with gradient focus rim — variant C) + tabs row + results grid. |
| Compare picker modal (`.models-compare-picker-modal`) | `bg neutral-50; radius-sm; box-shadow --pt-shadow-normal; margin-top: calc(--pt-nav-backdrop-offset + 20)`. |
| Compare select popup (`.models-compare-select-popup`) | `bg neutral-50; border: 1px line-100; radius-sm; padding 4; box-shadow --pt-shadow-normal` — the rare *bordered* popover (it sits in dense data UI). |

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
parent: --pt-gradient-card-bg, radius-md, padding 60 44
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
  border-bottom: 0.5px solid --pt-color-line-200;
}
.row .key   { body-sm; color: --pt-color-neutral-650; }
.row .value { body-sm; color: --pt-color-neutral-950;
              font-family: --pt-font-medium;
              text-align: right; }
```
Used by: `.models-detail-feature-item`, `.models-detail-pricing-item`, `.models-compare-kv`.

**R7. Glass + light-shadow tile**
```
background: color-mix(in srgb, --pt-color-neutral-100 ~82%, transparent);
backdrop-filter: blur(10–12px);
border-radius: --pt-radius-xs;
padding: 16;
box-shadow: --pt-shadow-light;
```
Used by: `.skills-detail-command-box`, `.docs-search-dropdown`, `.models-compare-bar` (variant on top of dynamic bg).

**R8. Stepped command tile (no glass, no shadow)**
```
background: --pt-color-neutral-100;
border-radius: --pt-radius-xs;
padding: 16;
font-family: --pt-font-mono;
font-size: body-sm;
```
Used by: `.tagline-skills-command-wrap`, `.docs-next-center`, `.skills-detail-code-block` inner.

**R9. Card-row tier interior** *(3-up / 4-up pricing, prize, token plans — §4.4)*
```
ZONE A — gap 8–12
  name row: semibold body-lg/title-md + optional Hot pill
  price row: bold title-lg amount + body-sm period suffix (neutral-550)
  meta: body-sm neutral-650 (+ optional 14px info icon)
ZONE B — mt 20
  full-width pill CTA: btn--secondary (default) | btn--primary (featured only)
ZONE C — mt 24; pt 20; border-top 1px line-100
  repeat: §8.16 icon+text rows
  optional: .card-feature-nested bullet list under last row
```
Chrome: `neutral-50` fill · `radius-sm` · pad 32 · `line-100` OR gradient rim · **shadow: none** · **no hover lift**.

Used by: `.card-row-item`, `.coding-plan-offer-card`, `.tier` (`components.md` §07).

**R10. Media duo interior** *(2-up visual borderless — §4.5)*
```
.media-duo-item: border 0 · shadow none · pad 0 · bg transparent
ZONE 1 .media-duo-visual: radius-md · 16:10 or h 248–280 · cover media · 20px icon top-left · NO border
ZONE 2 .media-duo-body: mt 20–24 · left-align
  .media-duo-title: title-md semibold neutral-950
  .media-duo-desc: body-md neutral-650 · 2-line clamp · mt 12
ZONE 3 .media-duo-link: inline text + arrow-up-right-outlined 14px · mt 16–20 · ink or .is-accent purple
```
No pill CTA. No hairline around the column.

Used by: `.media-duo-item`, agent-builder floor, capability-pair promos.

**R11. Skill / model simple card** *(§4.6 variant B — marketing `.models-card` row)*
```
head: name body-lg semibold + optional tag-hot
desc: body-sm neutral-650 2-line clamp  mt 12
chips: modality-chip row  mt 14
price: .simple-card-price mono sm neutral-650  mt 12
divider: border-top line-100  mt auto|16  pt 12
metrics: 2-col  strong title-sm + small body-sm neutral-650
```
Chrome: line-100 · radius-sm · pad 24 · shadow none · no hover lift.

**R12. Step simple card** *(§4.6 variant A)*
```
step-tag §8.17
title: title-md semibold  mt 16
desc: body-md neutral-650  mt 12
(no in-card CTA — floor btn--primary below grid)
```
Chrome: line-100 · radius-md · pad 32 · shadow none.

Used by: `.simple-card--skill` / `.models-card` marketing row; `.simple-card--step` / hackathon steps.

**R13. Text-card (secondary — variant A)** *(§4.7)*
```
chrome: transparent · pad 0 0 24 · border-bottom line-100 only · no shadow
head: icon 16 + name body-lg semibold
desc: body-sm 2–3 clamp neutral-650  mt 12
chips: optional modality-chip row  mt 14
link: text-card-link arrow 14px  mt auto
```

**R13b. Text-card minimal (secondary — variant B, no tabs)** *(§4.7)*
```
chrome: same as R13
name: body-lg semibold (no icon head)
desc: body-sm 2–3 clamp  mt 12
link: arrow 14px  mt auto
footer: text-card-pager §8.22 (when >1 page)
```

Used by: `.text-card` industry row (A); `.text-card--minimal` solutions catalog (B).

**R14. Logo matrix tile** *(§4.8)*
```
chrome: line-100 · radius-xs · h 64 · pad 0 16 0 20 · bg transparent · shadow none
row: flex center · gap 12
icon: 24×24 contain
name: body-sm medium neutral-950 · truncate
hover: border line-200 only
```
Used by: `.logo-matrix-tile`, `.coding-plan-tools-item`.

**R19. Borderless logo strip item** *(§4.8 variant B)*
```
chrome: none — transparent · no border · no shadow
logo: height 40–48 · width auto · max-w 160 · object-fit contain · brand colors
hover (optional link): opacity only — no scale/lift/border
```
Used by: `.logo-strip-item`, `.logo-strip-item__logo`.

**R20. FAQ accordion row** *(§4.12)*
```
item: border-bottom line-100 only · no shadow
trigger: flex space-between · question body-md semibold · + icon primary-550 right
open: + hidden · content grid 0fr→1fr · answer body-sm neutral-650 pb 24
policy: §8.27 single-open · first open by default
```
Used by: `.faq-item`, `.coding-plan-faq-item` (marketing pages).

**R21. Arena sync accordion row** *(§4.13)*
```
item: border-bottom line-100 · trigger title body-md semibold + + primary-550
open: + hidden · desc body-sm neutral-650 · data-arena-panel=n
visual: .arena-sync-visual-panel[data-panel=n].is-active cross-fade
policy: §8.28 single-open + preview sync · first pair active
```
Used by: `.arena-sync-item`; pairs with `.arena-sync-visual`.

**R15. Tail visual content stack** *(§4.9)*
```
panel: layout-max-wide · radius-lg · h 790 | 370 · overflow hidden · shadow none
backdrop: flower_* / gradient / quiet video · absolute inset
stack (centered): optional tail-visual-kicker + inline link §8.25
h2: 72 tall | 44 compact · ≤1 gradient phrase
subtitle: body-lg neutral-650 · max read-box
cta-row: btn--primary + btn--outline · gap 10–12
```
Used by: `.tail-visual`, `.era-hero-shell`.

**R16. Footer link column** *(§4.10)*
```
title: body-sm semibold neutral-950 · mb 16
list: flex-col gap 12 · no bullets
link: body-sm neutral-650 · hover neutral-950
```
Used by: `.page-footer-nav-col`; grid `repeat(3, 1fr)` inside 65% column.

**R17. Testimonial carousel card** *(§4.11 A)*
```
carousel-card bordered|filled · radius-lg · pad 32 · shadow none
quote icon · body-md 3–4 lines · avatar 40 + name + role caption
```

**R18. Criteria carousel card** *(§4.11 B)*
```
carousel-card bordered|filled · radius-lg · pad 32
metric title-lg · title body-lg semibold · ul body-sm neutral-650
```

### 11.3 Ten "clean & flat" signals

The kit reads as clean and flat because of these specific techniques. Replicate all of them.

1. **No inset border + no shadow on most content cards.** Separation is bg-step, not chrome. The default move when a card sits on a stepped panel is to drop the border entirely.
2. **Hairlines use the smallest available line size** — `var(--pt-line-size-normal)` (1 px), and in dense data UI, literal `0.5px` (`--models-detail-card-line`) or `0.75px` for KV dividers. Hairlines fade toward "almost not there."
3. **Border tokens stay desaturated.** Only `--pt-color-line-100/200/300` — never `neutral-300+`. Boundaries never compete with text.
4. **Hover lift = single low-opacity shadow + small Y translate.** `--pt-shadow-light` + `translateY(-4px)`. No depth stacks, no scale, no border-color flip.
5. **Featured states swap border for a mask-composite gradient rim**, keeping the same outer footprint. `border-color: transparent` + `::before { padding: 1px; mask-composite: xor; background: --pt-gradient-2 }`.
6. **Dropdowns / popovers default to no border + `--pt-shadow-light`.** Bordered popovers are reserved for dense data UI where a border helps anchor a long scrollable list.
7. **Internal dividers are top/bottom only, never box outlines.** `border-top --pt-color-line-100` for the metrics rule; `border-bottom --pt-color-line-200` for stacked accordion rows.
8. **Bg-step nesting instead of chrome-on-chrome.** Stepped panels (`neutral-100`) host `neutral-50` cards. `gradient-card-bg` floors host borderless content rows. Children never re-paint their border.
9. **Pill controls bg-shift for state, never outline.** Active = `neutral-150`; hover = `neutral-100`. `--pt-shadow-light` only on segmented toggles in the *elevated active* role.
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
| Small tile, mini-card | `--pt-radius-xs` | 12 / 16 |
| Mid card (most marketplace / pricing) | `--pt-radius-sm` | 24 / 28 / 32 |
| Standard content card | `--pt-radius-md` | 28 / 32 |
| Panel-as-card (faq, intro, prod) | `--pt-radius-md` | 60 44 (mobile 32 20) |
| Hero / signup / era panel | `--pt-radius-lg` | 32 / 40 48 / 48 |

### 11.6 Panel-as-card: no outer stroke, no grey sub-card inside  ★

When a card's job is to **host multiple items as one block** (recommended models, cost summary, plan benefits, step intro with embedded list, FAQ list, prod-shell prod-group, customer bundle "what you get") it is a **panel-as-card** — and it must follow these two rules **together**:

1. **The outer panel is borderless.** Background is `--pt-gradient-card-bg` (preferred) or one neutral step (`neutral-100`); `border: 0`; `box-shadow: none`. Visual separation from canvas comes from the bg-step alone. No 1px hairline `--pt-color-line-100` wrapping the whole block.
2. **Interior items are not nested grey sub-cards.** Each item sits directly on the panel surface and uses **typography + a single hairline** to read as a row:
   - Title row: `font-semibold` + body-lg/title-md; neutral-950 ink
   - Caption / meta: mono caption-sm uppercase, `0.06em`, `neutral-450/600`
   - Body / description: body-sm, `neutral-650`
   - Numeric / price: `--pt-font-mono`, `func-success` for prices, `neutral-650` for labels
   - Pill chip for tag (single small pill, `primary-50` or `neutral-150` fill) — never a whole grey block to host one piece of info
   - Divider between items: `border-bottom: 1px solid var(--pt-color-line-100)` (standard) or `0.5px var(--pt-color-line-200)` (dense data)
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

- [ ] Outer container: `background: var(--pt-gradient-card-bg)` (or `neutral-100`); `border: 0`; `box-shadow: none`; `border-radius: var(--pt-radius-md)`; padding `60 44` desktop / `32 20` mobile
- [ ] Section caption: mono caption-sm uppercase, `0.06em`, `neutral-450/600`, `margin-bottom: 24`
- [ ] Each row: `padding: 20 0` (or `24 0` airy); `border-bottom: 1px solid var(--pt-color-line-100)` except the last row
- [ ] Tag chip in a row: a single pill (§8.2), not a filled background block
- [ ] Numeric / price: `--pt-font-mono`; price in `--pt-color-func-success`, labels in `neutral-650`
- [ ] No `box-shadow`, no inset `background`, no nested `border` inside the panel

---

## 12. Filter rail & sidebar  *(models, docs, models/detail)*

### 12.1 Sticky filter rail (models marketplace)

- Width: **240 px** (`calc(60px * 4)`)
- Gap to content: **48 px**
- Position: `sticky; top: calc(var(--pt-nav-backdrop-offset) + 12px); max-height: calc(100vh - var(--pt-nav-backdrop-offset) - 12px); overflow: auto; padding-bottom: 48px`
- Internal stack: `display: flex; flex-direction: column; gap: 32px`
- ≤1024 px: hide rail; replace with a floating FAB (`position: fixed; right: 20px; bottom: 20px; border-radius: var(--pt-radius-full); box-shadow: var(--pt-shadow-light)`)

### 12.2 Filter primitives

- **Collapsible group head** (see §8.12): full-width button `padding: 6px 12px 6px 4px; font: medium body-sm`; chevron rotates 180° on expand.
- **Tag-cloud options**: `display: flex; flex-wrap: wrap; gap: 8px; padding: 8px 4px` — pills as §8.2.
- **List variant**: 1-px vertical guide via `::before` at `left: 14px`, indent 32 px; active item gets a 4-px primary dot via `::after`.
- **Range filter**: track 2 px; thumb 8 px; dual-input; values row `display: flex; justify-content: space-between; margin-top: 4px; font-size: var(--pt-body-font-size-sm); font-family: var(--pt-font-mono)`.
- **Toggle row** (§8.4 segmented or `--pt-color-neutral-150` track with 34×20 switch): `display: flex; justify-content: space-between; padding: 6px 4px`.

### 12.3 3-column shell  *(docs, models/detail)*

```
grid-template-columns: 240px minmax(0, 1fr) 240px;
gap: 32–48px;
align-items: start;
```

- Left rail: anchor list (§12.2 list variant)
- Center: `max-width: var(--pt-layout-max-read-box); margin: 16px auto 0` — reader column
- Right rail: "on this page" TOC (same list variant)
- Code-side variant: flips to 2-col with internal `1fr 1fr` for prose/code split

---

## 13. Off-shell pages

Skip `.page-shell` entirely. Don't retrofit.

### Signup
- 2-col page grid: `minmax(420px,1fr) minmax(460px,1fr); gap: 4px; padding: 32px`
- Left = brand panel: `padding: 32px; border-radius: var(--pt-radius-lg)`, absolutely-positioned `.brand-copy { position: absolute; inset: auto 32px 120px 32px }` over background video
- Right = form; pill inputs (`components.md` §08); verification code grid `repeat(6, minmax(0,1fr))` of 48×48 px tiles
- Mobile: 1 column; brand becomes top banner

### Error
- Fullscreen centered flex (`min-height: 100vh; align-items: center; justify-content: center`)
- Headline: `font-size: clamp(45px, 20vw, 160px)` with per-character variable-font interactivity (the only place this kit uses font-variation effects)
- Sub: body-md, color `--pt-color-neutral-650`
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
- **Nav:** desktop 84 px, mobile 62 px → sticky offsets recompute via `--pt-nav-backdrop-offset`.
- **Sidebars:** hide ≤1024 px; replace with floating FAB or top sheet.
- **Subtitle width caps don't change**; the viewport already constrains them.
- **Fluid:** `clamp(min, vw, max)` only on hero h1, hero metric strong, and the panel `height: 60vh`. Never raw `vw` on padding or body text.

---

## 15. Radius vocabulary (the working five)

| Token | px | Use |
|-------|---:|-----|
| `--pt-radius-full` | 999 | Pills, chips, CTAs, FABs, dots, dropdowns trigger |
| `--pt-radius-xs` | 12 | Inner panels, tool tiles, command boxes, notices, docs cards |
| `--pt-radius-sm` | 18 | Mid cards (marketplace, compare, pricing offer), dropdown panel |
| `--pt-radius-md` | 24 | Standard cards, hero frames, gradient panels, customer story outer |
| `--pt-radius-lg` | 36 | Full-bleed heroes, signup brand panel, era CTA, docs panel hero |

Don't use the other tokens (`xl 42, 2xl 48, 2xs 8, 3xs 6, 4xs 2`) unless the Guideline calls for them.

---

## 16. Background steps & elevation

Use background, not borders/shadows, to separate planes.

| Plane | Color | When |
|-------|-------|------|
| Canvas | `--pt-color-neutral-50` | `.page` body; default floor |
| Tinted floor | `--pt-color-neutral-100` | Every 2nd / 3rd floor for visual rhythm; docs panel hero; bulletin |
| Subtle surface | `--pt-color-neutral-150` | Pill segmented track, chips, disabled input, legal note, dropdown hover |
| Card wash | `--pt-gradient-card-bg` (`135deg, neutral-150 → neutral-50`) | Floor wrapped in a single rounded panel (faq, intro showcase, ai-powered-product) — almost flat |

Borders only on: outline buttons, inputs, featured pricing rim, weak card hairline (`--pt-color-line-100`). Default `shadow: none`. Use `--pt-shadow-light` only for: pill segmented selected child, card hover lift, sticky compare bar, floating FAB, search dropdown panel.

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
│ background: --pt-color-neutral-50                                          │
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
  --models-market-control-radius: var(--pt-radius-full);
  --models-market-control-icon-size: 18px;
}
```

All toolbar buttons / inputs / dropdowns share `height: 40px` and `border-radius: --pt-radius-full` — the toolbar reads as a single height across its row.

### 17.2 Search input (pill with gradient focus ring)

```scss
.search {
  display: inline-flex; align-items: center; gap: 6px;
  height: 40px;                                          // --models-market-control-height
  padding: 0 14px;
  border-radius: var(--pt-radius-full);
  background: var(--pt-color-neutral-50);
  border: var(--pt-line-size-normal) solid var(--pt-color-line-100);
  color: var(--pt-color-neutral-550);
  position: relative;
  isolation: isolate;
}
.search input {
  width: calc(48px * 4.6);                               // 221 px default
  border: 0; background: transparent;
  font-size: var(--pt-body-font-size-sm);
  color: var(--pt-color-neutral-750);
}
.search input::placeholder {
  color: var(--pt-color-neutral-400);
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
  background: var(--pt-gradient-4);
  background-size: 140% 140%;
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity var(--pt-motion-fast) ease;
  pointer-events: none;
}
```

Leading icon (`search-outlined`) 18 px; placeholder uses `--pt-color-neutral-400`. Nav search uses the same recipe at `height: 48`, `width: 228 → 490` on focus.

### 17.3 Sort trigger + dropdown

**Trigger** — pill button, same 40-px height. Chevron rotates 90° → -90° on open.

```scss
.sort-trigger {
  width: 100%;
  min-width: calc(48px * 2.9);                           // ~139 px
  height: 40px;
  padding: 0 18px;
  border-radius: var(--pt-radius-full);
  border: 1px solid var(--pt-color-line-100);
  background: var(--pt-color-neutral-50);
  color: var(--pt-color-neutral-750);
  font: medium 14px / 20px var(--pt-font-medium);
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
  border-radius: var(--pt-radius-md);
  background: var(--pt-color-neutral-50);
  box-shadow: var(--pt-shadow-light);
  z-index: 8;
}
.sort-option {
  padding: 8px 16px;
  border-radius: var(--pt-radius-full);
  background: transparent; border: 0;
  display: inline-flex; align-items: center; justify-content: space-between; gap: 8px;
  color: var(--pt-color-neutral-950);
  font-size: var(--pt-body-font-size-sm);
}
.sort-option:hover            { background: var(--pt-color-neutral-100); }
.sort-option.is-selected      { background: var(--pt-color-neutral-150); }
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
  border-radius: var(--pt-radius-full);
  background: var(--pt-color-neutral-150);                // track
}
.view-toggle button {
  width: 32px; height: 28px;
  padding: 6px 8px;
  border-radius: var(--pt-radius-full);
  background: transparent;
  color: var(--pt-color-neutral-550);
  display: inline-flex; align-items: center; justify-content: center;
}
.view-toggle button.is-active {
  background: var(--pt-color-neutral-50);
  color: var(--pt-color-neutral-950);
  box-shadow: var(--pt-shadow-light);                    // only place a shadow lands
}
```

Reuse exactly. The "elevated thumb" inside a `neutral-150` track is the kit's only segmented-control recipe — don't sub in colored fills.

### 17.5 Pill action buttons (reset / compare / compact CTAs)

```scss
.action-btn {
  height: 40px;
  padding: 0 16px;
  border-radius: var(--pt-radius-full);
  display: inline-flex; align-items: center; gap: 4px;
  font: medium 14px var(--pt-font-medium);
}
.action-btn--reset {
  background: transparent;
  border: 1px solid var(--pt-color-line-100);
  color: var(--pt-color-neutral-750);
}
.action-btn--compare {                                    // soft-fill, no border
  background: var(--pt-color-primary-50);
  color: var(--pt-color-primary-550);
  border-color: transparent;
}
.action-btn--compare:hover,
.action-btn--compare.is-active {
  background: var(--pt-color-primary-150);
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
.card-metrics-grid     { transition: opacity var(--pt-motion-fast) ease; }
.card-actions {
  position: absolute; left: 24; right: 24; bottom: 24;
  display: flex; gap: 8;
  opacity: 0;
  transition: opacity var(--pt-motion-fast) ease;
}
.card:hover .card-metrics-grid { opacity: 0; }
.card:hover .card-actions      { opacity: 1; }
.card:hover                    {
  transform: translateY(-4px);
  box-shadow: var(--pt-shadow-light);
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
  border-radius: var(--pt-radius-md);
  background: var(--pt-color-models-compare-bar-bg);
  backdrop-filter: blur(10px);
  box-shadow: var(--pt-shadow-normal);
  z-index: 1000;
  display: inline-flex; align-items: center;
}
.compare-bar-tags    { display: flex; gap: 6; flex-wrap: wrap; max-content; }
.compare-bar-tag     { height: 40; padding: 0 12; border-radius: --pt-radius-lg; }
.compare-bar-actions { margin-left: 40; display: inline-flex; gap: 8; align-items: center; }
.compare-bar-now     { /* primary-fill CTA */ }
.compare-bar-close   { width: 32; height: 32; border-radius: 999; }
```

Mobile (≤1024 px): bar shrinks to `padding: 16 20`; tags wrap; mobile FABs above it `bottom: calc(24 + 44 + 12)`.

### 17.9 Mobile sidebar sheet + FAB stack

```scss
.sidebar.is-open {                                       // mobile sheet
  position: fixed; inset: var(--pt-nav-backdrop-offset) 0 0 0;
  bg: var(--pt-color-neutral-50);
  padding: 20 12 12;
  box-shadow: var(--pt-shadow-normal);
  overflow: auto;
  z-index: 900;
}
.sidebar-fab,                                             // entry button
.sidebar-reset-fab {                                      // 2nd FAB above 1st
  position: fixed; right: 20; bottom: 20;
  height: 40; padding: 0 20;
  border-radius: var(--pt-radius-full);
  background: var(--pt-color-neutral-50);
  border: 1px solid var(--pt-color-line-100);
  box-shadow: var(--pt-shadow-normal);
  display: inline-flex; align-items: center; gap: 6;
  font: medium 14px var(--pt-font-medium);
}
.sidebar-reset-fab    { bottom: calc(20 + 40 + 8); }     // stack rules
.compare-bar ~ .sidebar-fab { bottom: calc(20 + 44 + 12); }
```

The FAB stack always sits above the compare bar. When both are present, recalculate `bottom` so the topmost FAB clears the bar — never let them overlap.

### 17.10 Range filter

```
track 2 px, color --pt-color-neutral-200
thumb 8 px square, color --pt-color-primary-550, border-radius 999
dual <input type="range"> stacked at the same position
values row beneath: display:flex; justify-content:space-between; margin-top:4;
                    font: --pt-font-mono / body-sm
```

### 17.11 Collapsible filter group (sidebar)

```scss
.group-head {
  width: 100%;
  padding: 6 12 6 4;
  font: medium body-sm var(--pt-font-medium);
  color: var(--pt-color-neutral-950);
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
center:     max-width: var(--pt-layout-max-read-box); margin: 16 auto 0
right rail: position: sticky; top: calc(84 + 36); "on this page" TOC
```

Anchor item recipe — reuse across docs/detail:
```scss
.anchor {
  width: 100%; height: 32;
  padding: 6 12 6 32;
  display: flex; align-items: center;
  font-size: var(--pt-body-font-size-sm);
  color: var(--pt-color-neutral-650);
  position: relative;
}
.anchor::before {                                         // vertical guide
  content: ''; position: absolute;
  left: 14; top: 0; bottom: 0;
  width: 1px; background: var(--pt-color-line-100);
}
.anchor.is-active                  { color: var(--pt-color-neutral-950); }
.anchor.is-active::after {                                // active dot
  content: ''; position: absolute;
  left: 12; top: 50%; transform: translateY(-50%);
  width: 4; height: 4; border-radius: 999;
  background: var(--pt-color-primary-550);
}
```

### 17.13 Pricing range segmented tab  *(models/detail)*

Two-level pill: outer `neutral-150` track h36; inner tabs h28 with `radius-full; padding: 6 8`. Active: bg `neutral-50` + `--pt-shadow-light` (the elevated-thumb pattern).

### 17.14 Interaction-layer review checklist

When building a models-like data page:

- [ ] All toolbar controls share `height: 40` and `border-radius: --pt-radius-full`
- [ ] Search has `--pt-color-line-100` resting border that **disappears** on focus and is replaced by the gradient mask-composite rim (`--pt-gradient-4`)
- [ ] Sort trigger chevron rotates 90° → -90° on open
- [ ] Sort dropdown is borderless + `--pt-shadow-light`; options are pills with `neutral-150` selected / `neutral-100` hover
- [ ] View toggle uses the segmented `neutral-150` track + `neutral-50` elevated thumb pattern
- [ ] Soft-fill CTAs (e.g. "Compare") use `primary-50` → `primary-150` hover, **no border**
- [ ] Grid view = `auto-fill, minmax(260, 1fr); gap 24/28`; List view drops columns at breakpoints rather than reflowing
- [ ] Cards reveal secondary actions on hover by fading metrics row, **not** by replacing the card
- [ ] Compare bar is glass + `--pt-shadow-normal`, fixed bottom 24, with FABs computing `bottom` so they clear the bar
- [ ] Sticky rails use `top: calc(var(--pt-nav-backdrop-offset) + 36)` for reading anchors

---

## 18. Layout review checklist

- [ ] **Marketing flat contract (§1.6):** no shadow on §4 floors; bg-step alternation; no nested grey sub-cards
- [ ] **Full marketing page:** floor order matches a §4.0 recipe (Home / Token Plan / Hackathon) when building long-scroll landings
- [ ] Picked the right container layer (inner default; outer only for framed visuals; reader for prose)
- [ ] Hero is exactly one of A–I; ≤1 gradient word; heading sits on canvas (`neutral-50`/`100`), **never** over a photo or video (except §2.3 era exception)
- [ ] **Home / campaign opener (variant B):** centered h1 + subtitle; **Level 1 `btn--primary` + Level 3 `btn--outline`** only; **48–64 px** gap before `.hero-visual` (§2.7)
- [ ] **`.hero-visual`:** `radius-lg`, one mode only — **A** 450–480 px media **or** **B** 420 px showcase (§2.8); title stack stays outside
- [ ] **Card row floor (§4.4):** 3-up or 4-up grid; cards **shadow: none**; `line-100` or single featured gradient rim; R9 interior + §8.16 icon rows; no grey feature sub-cards
- [ ] **Media duo floor (§4.5):** 2-up **borderless**; visual `radius-md` on top; copy left-aligned; text-link CTA + arrow — no pill buttons, no visual border/shadow
- [ ] **Simple card floor (§4.6):** `line-100` + no shadow; variant A (step-tag + floor CTA) **or** B (R11 + price-text §8.18 + chips §8.19)
- [ ] **Secondary showcase (§4.7):** variant A (tabs+R13) or B (stacked head+R13b+pager); text-cards **border-bottom only**
- [ ] **Logo floor (§4.8):** variant **A** 4-col matrix R14 **or** **B** borderless `.logo-strip` R19; not both
- [ ] **Tail visual (§4.9):** one panel 790 or 370 px; R15 centered stack; L1 primary + L3 outline; footer flush below
- [ ] **Site footer (§4.10):** 35/65 main grid; R16 link cols; §8.24 social; legal `line-100` bar
- [ ] **Carousel toggle (§4.11):** 100vw track; bordered or filled cards; §8.26 pager; R17 or R18
- [ ] **FAQ (§4.12):** shell A inner or B wide panel; 38/62 `.faq-layout`; §8.27 single-open; R20
- [ ] **Arena sync (§4.13):** centered head; 42/58 `.arena-sync-layout`; §8.28 visual sync; R21
- [ ] Floor backgrounds alternate canvas / tinted / card-wash — no two adjacent floors with the same tint
- [ ] Floor-head matches pattern A/B/C/D; subtitle respects §9.4 width caps
- [ ] Grid pulls a row from the §7 grid table — column count + gap + mobile collapse all match
- [ ] Sticky offsets use `calc(var(--pt-nav-backdrop-offset) + N)`; sidebar 240, gap 48
- [ ] Reader column = `var(--pt-layout-max-read-box)`; legal/docs body never exceeds it
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

Guideline §08 is a **masonry gallery** of 53 production cards plus shared `ui-*` primitives — same tokens and React runtime as the Qwen Cloud console (`Scripts/ui.js`).

### 19.1 Shell

```
.page-shell.page-home
  Nav (Guideline sticky nav)
  .page
    main.preview-grid[data-surface="chat"]
      .preview-grid__canvas          ← column masonry host
        .preview-grid__item × N      ← absolutely positioned tiles
          <Card specimen />           ← each root from components.md §08.3
```

| Property | Value |
|----------|-------|
| Max width | `var(--pt-layout-max-width)` |
| Top padding | `108px` (clears nav) |
| Column gap | `--gap: 32px` (`--pt-spacing-16`) |
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
- Header/body gap: `24px` (`--pt-spacing-12`)
- Chart cards: fixed aspect or min-height `200–280px`; legend mono `caption-md`
- Forms inside cards: pill inputs per `components.md` §08.2

### 19.4 Pairing with models toolbar (§17)

When a page mixes §08 cards with a models index:

1. Page shell + compact hero D (`layouts.md` §3)
2. Sticky toolbar (`ui-models-filter-*`) — full width inner
3. Card grid **or** §08 analytics stack below — never duplicate filter chrome inside each card
