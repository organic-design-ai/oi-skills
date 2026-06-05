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
│   [ primary CTA ] [ outline CTA ]                        │    │
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
- Content is **centered**, the panel is `780 px` tall — extreme whitespace inside.
- A **glass / blurred backdrop** sits behind the CTA pill (not the heading) for the form input only.
- This is a closing footer beat — not the page-leading hero.

If you're not building this exact closing-CTA pattern with these constraints, **stack vertically — title paragraph above, visual paragraph below.**

### 2.6 Where headings ARE allowed on a stepped surface

`neutral-100` (tinted floor) is fine. `--pt-gradient-card-bg` (almost-flat 135° wash from `neutral-150` → `neutral-50`) is fine for the two-column panel head (§5 pattern C). These are *quiet neutral bg steps* — they read as canvas, not imagery.

Imagery means: photographs, videos, flower / abstract / liquid renders, animated gradients, glass blur over a photo. Stepped neutrals are NOT imagery.

---

## 3. Hero variants

Pick exactly one per page. Never stack two heroes. All variants follow §2 — title on canvas, imagery framed below or beside.

### A. Split tagline hero  *(home tagline)*

Two-column inside `.layout-max-inner`.

- Grid: `minmax(0,1fr) minmax(320px, 392px)` · `gap: 44px` · `margin-top: 64px`
- Left: H1 `--pt-heading-font-size-xl` (64/68), letter-spacing tight, **one** `<span>` gradient-clipped. Sub `--pt-body-font-size-lg`, `max-width: 680px`. CTA row `inline-flex; gap: 10px; margin-top: 36px`.
- Right: bordered command/code panel — `border: 1px solid var(--pt-color-line-100); border-radius: var(--pt-radius-md)`. Both columns on canvas — no imagery in this hero.
- Mobile: 1 column; right panel drops below.

### B. Stacked floral / video hero  *(home, organic home, marketplace-style pages)*

Two-piece: heading stack in inner → media panel in outer.

```
.layout-max-inner-wrap
  .layout-max-inner
    h1   (centered, --pt-heading-font-size-2xl …3xl, on neutral-50)
    .sub (centered, max-width: var(--pt-layout-max-read-box))
    .cta-row (centered, gap: 12px)
.layout-max-wide
  .hero-panel
    height: 540–720 px, border-radius: var(--pt-radius-lg) (36)
    object-fit: cover
    optional 4-up metric overlay (small only — see §8.1)
```

- H1 size range: `--pt-heading-font-size-2xl` (72) up to `clamp(72px, 10vw, 168px)` for ultra-marketing pages. Always on canvas.
- Sub margin: `32px auto 64px auto`; color `--pt-color-neutral-650`.
- Panel margin from heading stack: `48px`.

### C. Centered intro hero  *(coding-plan, skills-detail)*

`.intro-header { display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center }`

- H1: `--pt-heading-font-size-lg` (60), letter-spacing tight, on canvas.
- `.heading-desc`: body-lg, color `--pt-color-neutral-750`, `max-width: 560–620 px`.
- Below: optional showcase panel `background: var(--pt-gradient-card-bg); border-radius: var(--pt-radius-md); padding: 60px 44px` — quiet wash, not imagery.

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

### F. Era / closing CTA hero  *(closing block)*

The only variant where text overlays imagery (§2.3 exception).

- `height: 780px; border-radius: var(--pt-radius-lg)`, full-bleed in `.layout-max-wide`
- h2 ≤72 px centered; glass / blurred backdrop behind CTA for legibility
- Video designed as quiet backdrop

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

A "floor" is one top-level section of the page. Floors stack vertically with §1.5 rhythm.

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
- **Hero floor:** 540–780 px panel; first floor on most pages.
- **Bulletin floor:** `--pt-bulletin-height: 306px` (24-px padding mobile, 70-px desktop) — pinned strip for announcements.
- **Stacking scroll floor:** `height: 180vh` with `position: sticky` interior — for scroll-choreographed reveals (rare; e.g. featured model stack on home).
- **Closing CTA floor:** 780 px panel (§3 variant F).

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

Heading owns left column, content (accordion / cards) owns right. The whole floor sits in a card-wash panel.

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
| Agent-builder | `repeat(2, minmax(0,1fr))` | 18 | Mobile → 1fr |
| Industry / quick cards | `repeat(4, minmax(0,1fr))` | 36 | Mobile → 1fr; gap 18 |
| Analyst (asymmetric 2/1/1) | `2fr 1fr 1fr` | 24 | Mobile → 1fr; gap 16 |
| Reliability 2×2 | `repeat(2, minmax(0,1fr))` | col 114 / row 64 | Each item itself `100px 1fr; gap 48` |
| Customer logo strip | `repeat(7, minmax(0,1fr))` | `6vw` | Mobile → `repeat(3, …); gap 18` |
| Pricing offer (centered) | `repeat(2, clamp(320px, 30vw, 400px))` | 24 | `justify-content: center` |
| Tools / logo tiles | `repeat(4, minmax(0,1fr))` | 12 | 64-px tall tile, `--pt-radius-xs` |
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
| `.era-hero-shell` 780h | `border-radius: --pt-radius-lg; absolute video media; centered content with h2 72/76 bold + animated-rim email input (variant C)` |
| `.agent-builder-visual` h248 | `border-radius: --pt-radius-xs; 1px line-100 (bordered!); absolute video cover; icon top-left 20×20 white` |

**Pattern:** the heading sits **outside** the media card (above it, in `.layout-max-inner`), not over it (§2). The only text on the media is the overlay panel itself (which is a separate borderless sub-card).

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
| **Synced preview pair** (`.coding-plan-intro-showcase`) | 2-col `1fr 1fr; gap: 64`; left accordion controls right preview via absolute `.coding-plan-preview-panel` with `.is-active` fade. Locked `height: 380`. |
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

- [ ] Picked the right container layer (inner default; outer only for framed visuals; reader for prose)
- [ ] Hero is exactly one of A–I; ≤1 gradient word; heading sits on canvas (`neutral-50`/`100`), **never** over a photo or video (except §2.3 era exception)
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
