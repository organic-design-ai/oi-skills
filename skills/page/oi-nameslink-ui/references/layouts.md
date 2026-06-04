# Nameslink — Page Layouts

Page-level composition. Tokens: `tokens.md` (`--pt-*`). Components: `components.md`. Icons/photos: manifest (`icons.md`, `assets.md`).

**Stack:** Tailwind utility classes + small CSS-in-JS strings (`styles.ts` per section) + scoped `.css` under `src/styles/components/*` + token CSS at `src/css/token.css`. Spacing follows Tailwind's 4-px scale; raw px is used when 4-px doesn't land cleanly (e.g. `px-[70px]`, `mt-[280px]`).

**Reuse existing tokens. Do not invent new ones.**

---

## 1. Page shell & container scope

### 1.1 Three-layer container model

```
┌─ viewport (100vw) ────────────────────────────────────────────────┐
│                                                                   │
│   ┌─ .layout-max-wide (outer) ─────────────────────────────┐    │  desktop: 50-px gutter
│   │   max-w-layout-wide  +  px-[50px] (tablet: px-5)        │    │  mobile:  20-px gutter
│   │                                                         │    │
│   │   ┌─ .layout-max-inner (inner) ───────────────┐        │    │  desktop: extra 70-px each
│   │   │   max-w-layout-inner  (no internal pad)    │        │    │           side via token
│   │   │                                            │        │    │
│   │   │   ┌─ reader / focused col ────┐           │        │    │  cap 768 px
│   │   │   │ max-w-layout-read         │           │        │    │
│   │   │   └────────────────────────────┘           │        │    │
│   │   └────────────────────────────────────────────┘        │    │
│   └─────────────────────────────────────────────────────────┘    │
└───────────────────────────────────────────────────────────────────┘
```

Token widths (`css/token.css`):

| Token | Value | Tailwind alias | Used by |
|-------|-------|----------------|---------|
| `--pt-layout-limit-width` | `1920px` | — | Absolute cap |
| `--pt-layout-max-width` | `min(100vw - 140px, 1920px)` | `max-w-layout-wide` | `.layout-max-wide` (outer) |
| `--pt-layout-max-inner` | `min(100vw - 280px, 1920px - 140px)` | `max-w-layout-inner` | `.layout-max-inner` (inner) |
| `--pt-layout-max-read-box` | `768px` | `max-w-layout-read` | Reader column (legal, long-form, dock prompts) |

Mobile (`≤1024 px`) override in `token.css`:
- `--pt-layout-max-width: calc(100vw - 20px)`
- `--pt-layout-max-inner: calc(var(--pt-layout-max-width) - 20px)`

### 1.2 Layer decision rule

- **Outer (`layout-max-wide`)** — full-bleed framed visuals: hero card, deals dock track, era CTA, full-bleed banners.
- **Inner (`layout-max-inner`)** — **default for everything else**: section heads, grids, copy, plan cards, services, FAQ list.
- **Reader cap** — long-form copy only; rare on this site.

**A hero typically uses both:** heading + subtitle live in inner, the rounded hero card lives in inner OR a full-bleed card in outer. The big H1 is **never** placed inside the imagery card — see §2.

### 1.3 Page shell (`lib/tw/presets.ts:38-43`)

```tsx
<div className={layoutShell.page}>                       {/* page-shell relative isolate z-[5] */}
  <Nav />
  <main className="relative z-[5] min-h-screen bg-neutral-100 pb-[140px] text-neutral-950
                   tablet:pb-8 pt-9 tablet:pt-5">
    <div className={layoutShell.maxWide}>
      <div className={layoutShell.maxInner}>
        {/* sections */}
      </div>
    </div>
  </main>
  <Footer />                                             {/* h: --pt-footer-bottom-height = 640 px (320 ≤639) */}
</div>
```

- Body bg: `--pt-color-neutral-100` (`#f7f7f9` light / `#0d0d0e` dark). Note: **not** `neutral-50` like other kits — Nameslink uses 100 as canvas, 50 as card surface.
- Default text: `--pt-color-neutral-750`; default font: `--pt-font-regular` (Inter).
- Scrollbar: 3 px width, custom.

### 1.4 Section vertical rhythm (between floors)

Desktop top margins (real values from the site, all 4-px aligned except `[280px]`):

| Value | Floor |
|-------|-------|
| `mb-4` | Hero bottom |
| `mt-20` (80 px) | Services |
| `pt-[120px]` | Steps |
| `mt-[140px]` | Deals, FAQ |
| `mt-[170px]` | Why-choose |
| `mt-[280px]` | Plan (load-bearing chapter gap) |

Tablet (`≤1024 px`) collapses uniformly to `mt-[70px]` or `mt-[100px]` (steps). **Never** introduce intermediate values — pick from the set above.

Heading→body inside a floor: `mb-15` (60 px) desktop / `mb-10` (40 px) tablet on the section title.

---

## 2. Heading vs imagery — the cleanliness rule  **★ most important rule ★**

> **Big Playfair headings sit on canvas. Imagery sits in its own rounded card. Title + subtitle are their own clean paragraph block, with breathing room above the visual.**
>
> Violating this is the single biggest way to make the page look wrong. This rule overrides almost every other consideration.

### 2.1 ❌ WRONG vs ✅ RIGHT — burn this in

```
❌ WRONG — Playfair heading laid over a flower/gradient/photo, fighting the visual
┌─────────────────────────────────────────────────────────────────┐
│   ╔═══════════════════════════════════════════════════════╗    │
│   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║    │
│   ║░░░░░░░ purple flower / abstract / video poster ░░░░░░║    │
│   ║░░░░░                                          ░░░░░░░║    │
│   ║░░░░░     Playfair 64 px hero heading on the  ░░░░░░░║   ← 64+ px Playfair
│   ║░░░░░     gradient flower image — busy & low- ░░░░░░░║     PHYSICALLY ON
│   ║░░░░░     contrast                             ░░░░░░░║     the imagery.
│   ║░░░░░                                          ░░░░░░░║     This looks BAD.
│   ║░░░░░     subtitle paragraph also on imagery   ░░░░░░░║    │
│   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║    │
│   ╚═══════════════════════════════════════════════════════╝    │
└─────────────────────────────────────────────────────────────────┘

✅ RIGHT — heading + typewriter on clean canvas; rounded card below carries the visual
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │   ← whitespace
│   Find the perfect name.            Achieve More_              │   ← H1 (Playfair 64)
│   ────────────────────              ────────────────────       │     on neutral-100
│                                                                 │     + typewriter
│                                                                 │   ← whitespace
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ trust strip (small avatars + small text)                │  │
│   │                                                         │  │
│   │   ░░░░ poster image absolute inset-0 ░░░░               │  │   ← rounded card
│   │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                   │  │     bg-neutral-50
│   │                                                         │  │     rounded-[20px]
│   │   ┌───── glass search (anchored bottom) ─────────┐     │  │     Photo is INSIDE
│   │   └───────────────────────────────────────────────┘    │  │     this panel.
│   └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

Reference: Qwen Cloud "Ship the next" — heading clean on white at top-left; flower image is a separate band below. Cohere — line icons + heading on white above their text; the hill photo is a separate full-width section below. The right way is to keep heading and imagery in different rectangles.

### 2.2 Anti-patterns — never do these

- ❌ Playfair H1 / section-title (≥36 px) physically overlapping a photo, video, abstract gradient, or any visual asset
- ❌ Hero card that contains both the giant Playfair heading AND the imagery in the same rounded rectangle
- ❌ Adding `text-shadow`, blur layer, or dark overlay to "make the heading readable on the photo" — if you need that, the heading is in the wrong place
- ❌ Heading positioned `absolute` inside a card that has `background-image` or holds an absolute poster
- ❌ Centering a Playfair section title on top of `--pt-gradient-card-bg` so the gradient ladders behind the type
- ❌ Sliding the heading down to "fill" whitespace above an image

### 2.3 The canonical arrangement

```
┌── .layout-max-inner ─────────────────────────────────────┐    ↑ on --pt-color-neutral-100
│                                                          │    │
│   H1   (Playfair 64/80, neutral-950)                     │    │   PARAGRAPH 1
│        on canvas, NOT on imagery                         │    │   text only, on canvas
│   subtitle / typewriter  (Inter 16/22, neutral-650)      │    │   margin-bottom: 60 px
│   [ primary CTA ]                                        │    │
│                                                          │    │
└──────────────────────────────────────────────────────────┘    ↓
                                                                    ← whitespace ≥ 32 px
┌── .layout-max-inner ────────────────────────────────────────┐ ↑ rounded card
│  ┌────────────────────────────────────────────────────┐    │ │
│  │  bg-neutral-50, rounded-[20px], min-h-[588px]      │    │ │   PARAGRAPH 2
│  │  ┌─ trust strip (small, OK on imagery) ─┐          │    │ │   visual only
│  │  └────────────────────────────────────────┘          │    │ │   inside its own card
│  │  ░░ poster image absolute inset-0 ░░               │    │ │
│  │  ┌─ GlassSearch (anchored bottom) ──────┐          │    │ │
│  │  └────────────────────────────────────────┘          │    │ │
│  └────────────────────────────────────────────────────┘    │ │
└─────────────────────────────────────────────────────────────┘ ↓
```

Two **separate paragraphs**, in this order:

1. **Title paragraph** — H1 (Playfair) + subtitle/typewriter + optional CTA. Lives in `.layout-max-inner`. Background: `--pt-color-neutral-100` (page canvas). Nothing visual, just type.
2. **Visual paragraph** — the hero card (`bg-neutral-50, rounded-[20px], min-h-[588px]`) holding the poster image, trust strip, and glass search. Whitespace above (≥ 32 px) cleanly separates it from the title paragraph.

This is what makes the Nameslink home feel calm — title and visual are **never in the same rectangle**.

### 2.4 Hard rules

- **Playfair heading (≥36 px) sits on `--pt-color-neutral-100`** (canvas). Not on any photo, video, gradient, or flower image.
- **Subtitle / typewriter** sits with the heading on the same canvas, never on imagery.
- **Poster image / video lives in the hero card** — `bg-neutral-50; border-radius: 20`. The image is `absolute inset-0; object-cover; z-[1]`. Image's top edge is **at least 32 px** below the bottom of the title paragraph (use `mb-15` on the heading row).
- **Permitted overlays on the hero card** — small text only:
  - Trust strip (`text-sm` with one `text-base font-medium` emphasis word)
  - Glass-search (the search shell, not a heading)
  - Dock prompt pills (caption / small label inside the deals dock — never a heading)
  - Per-card pill tags on dock cards (chips sit absolute `-top-7` **outside** the card, not on the image)
- **Upper bound for text on imagery: title-sm 20 px.** Anything ≥36 px belongs in the title paragraph above.
- **No text-shadow, no dark overlay, no blur backdrop "for legibility."** If the heading needs help reading, it's in the wrong place — move it up to the canvas.
- **CTAs live with the heading** on canvas. The only exception is the glass-search bar inside the hero card (which is a search affordance, not a CTA pill).

### 2.5 Section titles follow the same rule

The Playfair 40/54 `home-section-title` always sits on its floor's bg plane (`neutral-100` canvas, `primary-50` lavender wash for services, or `gradient-card-bg`). **Never on a photo, dock card, or steps card image.** Cards live as their own row beneath the title paragraph, with `mb-15` (60 px) separating title from content.

### 2.6 Where headings ARE allowed on a stepped surface

- `--pt-color-neutral-100` (canvas) — fine; that's the default
- `--pt-color-primary-50` (lavender wash, services floor) — fine; quiet brand tint
- `--pt-gradient-card-bg` (almost-flat 135° `neutral-150 → neutral-50`) — fine for tinted card-as-floor panels

These are *quiet neutral tints*, not imagery. Imagery means: photographs, videos, flower/abstract/liquid renders, animated gradients, glass blur over a photo. Stepped neutrals are NOT imagery.

---

## 3. Hero variant

Nameslink home has exactly one hero (see §2.1). Treat it as canonical:

- **Heading row** (`HomeHeroHead`): `flex flex-row flex-nowrap items-end justify-between` desktop; stacks vertical at ≤1024.
- **H1**: `font-playfair text-[64px] font-semibold leading-[80px] tracking-normal`; tablet `text-[clamp(40px,9vw,56px)] leading-[1.15]`. **Raw px** — the heading-lg token is 60/64; the hero is its own 64/80.
- **Subtitle**: typewriter `text-base` (16 px); right-aligned desktop; gradient underline `border-image: var(--pt-gradient-2)`.
- **Hero card**: `min-h-[588px]; rounded-[20px]; bg-neutral-50; overflow-hidden; relative isolate`. Tablet `min-h-[420px]`.
- **Trust strip**: `px-[70px] py-[30px]` desktop / `px-[18px] pt-6 pb-0 mb-[140px]` mobile; z-[2].
- **Poster image**: `absolute inset-0 -z-0 h-full w-full object-cover object-[right_center]; z-[1]`.
- **Glass-search**: `mt-auto mb-0` (anchored bottom); z-[3].

For new heroes that aren't the home hero, follow the same arrangement — heading on canvas, rounded card below.

---

## 4. Floor (section) taxonomy

A "floor" is one top-level section. Floors stack vertically with §1.4 rhythm.

### 4.1 Section title pattern

The repeated recipe (`type.sectionTitle` in `lib/tw/presets.ts:17`):

```scss
.home-section-title {
  font-family: var(--pt-font-playfair);
  font-size: 40px;
  line-height: 54px;
  font-weight: 600;
  /* tablet ≤1024 */
  font-size: clamp(24px, 6vw, 32px);
  line-height: clamp(32px, 6vw, 48px);
  margin-bottom: 60px;                                   /* mb-15; tablet mb-10 = 40px */
}
```

### 4.2 Floor catalog

| Floor | Layout | Bg plane | Top gap (desktop) | Notes |
|-------|--------|----------|-------------------|-------|
| **Hero** | inner | `neutral-100` (canvas) + `neutral-50` card | (first) | See §3 |
| **Services** | `grid grid-cols-4 items-start gap-2.5` (title is cell 1) | `bg-primary-50` (light) / `bg-neutral-50` (dark), optional 1440-px deco poster centered behind | `mt-20` | Title sits **inside** the 4-col grid; tablet collapses to `grid-cols-1 gap-5` |
| **Why-choose** | head + `flex items-start justify-between gap-6` (left visual 290 px + right `grid-cols-2 gap-x-6 gap-y-3`) | `neutral-100` (no surface) | `mt-[170px]` | Items are borderless rows with `border-b border-line1` only |
| **Deals** | centered head + horizontal-dock track @ `h-[var(--dock-active-height)]` | `neutral-100` canvas; dock cards `bg-neutral-50` | `mt-[140px]` | Dock cards `rounded-[10px]` with `img-frame` overlay |
| **Steps** | head row (`flex-wrap items-end justify-between`: title left max-440 + disclaimer right `flex-[1_1_280px]`); scroll-stacked 3 cards desktop / vertical flex stack mobile | `bg-neutral-100`; cards `bg-neutral-50` or `bg-primary-50` "lavender" | `pt-[120px]` | Stage `h-[280vh]` sticky; JS-driven `translateY scale` |
| **Plan** | centered head + `grid grid-cols-[repeat(2,minmax(0,590px))] items-stretch justify-center gap-5` | `bg-neutral-100`; cards `bg-neutral-50`, pro card uses `card_bg.jpg` cover | `mt-[280px]` | The biggest chapter gap on the site |
| **FAQ** | left head (`mb-15`) + `flex flex-col` accordion list | `bg-neutral-100`, no card chrome | `mt-[140px]` | Items separated by `border-b border-line1` only |
| **Quick-nav** *(when used as section)* | `grid-cols-[repeat(auto-fit,minmax(280px,1fr))]` + container-query upgrade to 4-col @ 1160 px | `neutral-100` | `mt-10` | Container queries: `container-type: inline-size` |

### 4.3 Floor-head patterns

Three patterns:

**A — Centered head** *(deals, plan)*
```
text-align: center; max-w-[840px] mx-auto;
.title (Playfair 40/54)
.subtitle (mt-5 text-lg leading-[30px], text-neutral-600)
```

**B — Left + right split head** *(steps)*
```
flex flex-wrap items-end justify-between gap-6;
left:  Playfair 40/54, max-w-[440px]
right: text-sm leading-[26px] text-neutral-600, flex-[1_1_280px]
```

**C — Multi-line dynamic head** *(why-choose)*
3 lines desktop / 5 lines narrow-mode, toggled via `narrow:hidden`/`narrow:block`. Each line wrapped in `<SplitColorfulText tone='highlight' splitMode='word'>` with periodic 1500-ms auto-flash on random words.

**D — Title inside grid** *(services)*
Title becomes the first cell of the 4-col grid; doesn't get its own row.

---

## 5. Card archetypes

**Nameslink cards are borderless by default.** Differentiation is bg + radius + (rare) hover-shadow. The only `border` declarations on cards are: why-choose item bottom rule, faq item rules, mobile-menu profile chip, and a handful of tag chips. Treat borderless as the rule, bordered as the exception.

### 5.1 Borderless cards (the default)

| Card | Bg | Radius | Padding | Min-height | Hover | Used |
|------|----|-------:|---------|------------|-------|------|
| **Hero card** | `neutral-50` | 20 | (children pad) | 588 (tablet 420) | none | `sections/hero/styles.ts:5` |
| **Services card** | `neutral-50` via LiquidGlass | 10 | `pl-[30px] pr-8 py-10` | 276 | white overlay fades 0→100% 0.15 s + `inset 0 0 0 1px var(--pt-color-line1)` rim | `sections/services/styles.ts:20-39` |
| **Quick-nav card** | `neutral-50` | 10 | (`layout.cardBg` recipe) | 84 | `hover:shadow-light`; icon `opacity-0 → 100` | `sections/quick-nav/styles.ts:25-46` |
| **Deals dock card** | transparent + inner `img-frame bg-neutral-50` | 10 | (image fills) | per JS | active: bg fades + image scales 1.08 | `sections/deals/horizontal-dock/styles.ts:53-77` |
| **Steps card** | `neutral-50` or `primary-50` (lavender) | **28** desktop / 20 tablet | `px-[70px] pb-[60px] pt-10` (`p-5` tablet) | `h-[460px]` | `shadow-card` baseline; scroll-driven transform | `sections/steps/styles.ts:45-63` |
| **Plan card (lite)** | `neutral-50` | 10 | `px-10 pb-10 pt-11` | (content) | none | `sections/plan/styles.ts:14-30` |
| **Plan card (pro)** | `neutral-50` + `card_bg.jpg` cover | 10 | `px-10 pb-10 pt-11` | (content) | none | same |

**Steps is the outlier** with `rounded-[28px]` (the largest radius in use) and `shadow-card`. Every other card sticks to `rounded-[10px]` or `rounded-[20px]` with no shadow.

### 5.2 Bordered "cards" (rare — list rules and tag-strokes only)

| Surface | Border | Notes |
|---------|--------|-------|
| **Why-choose item** | `border-b border-solid border-line1` (bottom only) | Not a box border. `py-[26px] pb-6`, no bg, no radius. |
| **FAQ item** | `border-b border-line1; first:border-t; last:border-b-0` | Top + bottom rules; no bg. |
| **Mobile-menu profile chip** | `border border-solid border-[#E6E8EB]` *(hard-coded, not token)* | The single real "bordered card" — only inside the user-menu drawer. |
| **Tag chips** (`gray`, `plan-green-outline`, `dock-muted`) | 1 px `border` | The only chip variants with strokes; default chips are solid-fill. |

### 5.3 Card internal recipes

**R1 — Plan card** (`sections/plan/index.tsx` + `styles.ts:14-30`)
```
.tags-row         (flex gap-2.5)          ← TagNormal 'plan' chips, 13 px
.name-row         (flex items-center gap)  ← Inter semibold 32 px + sparkle iconfont 30 px
.price-row        (flex items-baseline gap)
   .amount        Playfair 56/60 bold (text-cta-fill or text-primary-550)
   .currency      Playfair 18 (decimal / cycle suffix)
.price-secondary  text-sm neutral-600
.desc             text-sm leading-[22px] tracking-[-0.01em] neutral-600
.cta              Cta size=lg, variant='plan-lite' or 'plan-pro' (mt-6 w-full)
.benefits-block
   .benefits-label  Inter caption-style, neutral-650
   .benefits-grid   grid grid-cols-2 gap-y-2.5 gap-x-6
     .item          flex gap-2.5  ← iconfont check (a2 green) + text-sm
```

**R2 — Services card**
```
.icon          30 px outline, currentColor
.title         Inter text-lg leading-7 tracking-[-0.02em] text-neutral-950
.desc          text-sm leading-5 text-neutral-600  (mt-2.5)
.action-chip   absolute top-6 right-6, size-8 rounded-full
               bg-neutral-950 text-neutral-50 → hover bg-primary-550
```

**R3 — Steps card**
```
grid [500px_minmax(0,1fr)]; gap (none — columns butt)
left:   visual (image or graphic)
right:  .eyebrow   (caption, Inter)
        .title     (Inter text-lg leading-7 tracking-[-0.02em])
        .points    (list: iconfont check + text-sm, gap-3)
        .cta       (Cta size=md, mt-[30px] self-start)
```

**R4 — Quick-nav card**
```
flex items-center px gap
   .text   (Inter font-medium)
   .icon   (absolute right; opacity-0 → 100 on hover)
```

**R5 — Why-choose item** (borderless row)
```
border-b border-line1, py-[26px] pb-6
flex flex-col gap-2.5
   .icon-row    (icon + label inline)
   .title       (Inter text-lg leading-7 text-neutral-950 tracking-[-0.02em])
   .desc        (mt-2.5 text-sm leading-5 text-neutral-600)
```

**R6 — Deals dock card**
```
.frame            absolute inset-0 rounded-[10px] bg-neutral-50  (the visible surface)
.img              fills frame, transitions scale 1 → 1.08 on .is-active
.prompt-pill      absolute top-40 left-1/2 -translate-x-1/2,
                  glass variant: min-w-[156px] h-[44px] rounded-[100px]
.tags-row         absolute -top-7 left-2   ← chips sit OUTSIDE the frame
.context-bg       absolute layer, fades in on .is-active over 0.35 s
```

**R7 — FAQ item** (accordion)
```
.trigger          py-[30px]; min-h --pt-faq-trigger-min when collapsed
   .q-label       Playfair 16 semibold, cycles primary-{250,350,450,550,650} per index
   .question      text-[18px] leading-7 font-medium tracking-[-0.02em]
   (no chevron icon)
.answer           role='region'; transition-[height] 0.5s ease-linear; inline height set via JS
                  text-neutral-600 (Inter body default)
```

### 5.4 Decision tree

```
Q1. Is the card a single list row (faq, why-choose) — should it look like data?
    └─ Yes → borderless row with a bottom `border-b border-line1` only. No bg, no radius.

Q2. Is it a content card sitting on canvas (neutral-100)?
    └─ Yes → borderless `bg-neutral-50` + `rounded-[10px]` (or 20 for hero, 28 for steps).
              No border, no shadow unless interactive (hover:shadow-light).

Q3. Is it a "frosted" service card with liquid-glass treatment?
    └─ Yes → wrap in <LiquidGlassBackdrop>; rim painted via inset shadows on the glass layers, not on the card itself.

Q4. Is it a featured / dark plan card?
    └─ plan-lite: bg-accent-a1 button + neutral-50 card body
    └─ plan-pro:  bg-primary-550 button + neutral-50 card body + card_bg.jpg cover art

Q5. Does it need a stroke at all?
    └─ Only for: tertiary CTA outline, tag chip outline variants, mobile profile chip, faq/why list rules.
```

### 5.5 Padding & radius defaults

| Card type | Radius | Padding |
|-----------|-------:|---------|
| List-row card (why, faq) | none | `py-[26px]` / `py-[30px]` |
| Quick-nav, dock card | 10 | (children own) |
| Services card | 10 | `pl-[30px] pr-8 py-10` |
| Plan card | 10 | `px-10 pb-10 pt-11` |
| Hero card | 20 | (children own) |
| Steps card | **28** | `px-[70px] pb-[60px] pt-10` (tablet `p-5`) |

---

## 6. Sub-block vocabulary

### 6.1 Tag chip  *(`components/tag-normal`)*

Base: `inline-flex rounded-full font-body whitespace-nowrap`.

| Size | Height | px | Font |
|------|-------:|----|------|
| `xs` | 20 | 8 | 12 |
| `sm` | 22 | 10 | 13 |
| `md` | 24 | 12 | 14 |
| `plan` | 28 | 12 | 13 |

Fills (no `border` unless flagged):
- `gray` — `bg-neutral-150 text-neutral-650` + 1 px border
- `purple` — `bg-brand-550 text-func-white` (solid)
- `green` — `bg-success-500 text-func-white`
- `plan-green` — `bg-accent-a2 text-func-white`
- `plan-green-outline` — `border bg-transparent text-accent-a2` (outline)
- `dock-muted` — `h-6 border bg-transparent text-neutral-600`
- `dock-brand` — `bg-brand-600 text-func-white`
- `dock-hot` — `bg-success-500 text-func-white`

Pick one fill — never mix chip styles within a card.

### 6.2 Mode pill rack  *(search-modes, deals tabs)*

```
rounded-full bg-primary-50 (light) / bg-neutral-150 (dark)
p-0 (search) or p-1 (deals)
sliding thumb: bg-primary-550 (search) or bg-brand-500 (deals)
transition: transform + width, 280 ms
pill: h-full rounded-full px-4 font-medium text-sm
       active: text-func-white
       inactive: text-neutral-800
```

Thumb width is JS-set from the active button's measured offsetWidth.

### 6.3 Glass search

```
shell:    overflow-hidden rounded-none  (the shape comes from LiquidGlassBackdrop cornerRadiusPx={15})
inside:   px-[70px] py-6 (tablet px-[18px]), gap-2.5 column

bar outer rim:  h-[76px] rounded-full p-px
                bg-[image:var(--pt-gradient-home-search-border)]
                bg-[length:250%_250%]
                animate-glass-search-border-pan  (12 s)

bar inner:      bg-neutral-50 rounded-[calc(var(--pt-radius-full)-1px)]
                px-10 py-[27px] (tablet px-2.5 py-2)

input:          15 px Inter, text-neutral-900

placeholder:    sibling <span>, bg-[image:var(--pt-gradient-home-search-placeholder)]
                bg-clip-text text-transparent
                animate-glass-search-placeholder-pan  (8 s)
                hidden via peer-selectors when input has focus or content

submit:         h-10 rounded-full bg-transparent px-[18px] + magic-wand GIF 24
```

This is the only place gradient animation runs on background-position — keep it scoped here.

### 6.4 Nav dropdown  *(`components/nav`)*

```
panel:       absolute left-0 top-[calc(100%+10px)]
             w-max max-w-[calc(100vw-40px)]
             rounded-xs (12) bg-neutral-50 shadow-normal p-0
             z-[5]
open anim:   opacity + translateY(6px → 0), 0.18 s
chevron:     rotates 180° on .is-open

lang panel:  min-w-[168px] rounded-xs p-2 shadow-normal origin-top-right

item:        px-4 py-2 rounded-2xs text-body-sm
             hover: bg-neutral-100
```

### 6.5 User menu  *(`components/nav/styles.ts:201-219`)*

```
trigger:        size-[34px] rounded-full bg-[#6940FF]
                hover: brightness-105

panel:          w-[296px] rounded-xs p-3 bg-neutral-50 shadow-normal

profile chip:   h-[84px] w-[296px] rounded-[10px]
                border border-[#E6E8EB]   ← the only real bordered card
                px-4

item row:       h-9 rounded-full px-4 gap-2.5
                hover: bg-neutral-100

divider:        my-1.5 h-px bg-line1
```

### 6.6 Horizontal-dock cursor  *(`sections/deals/horizontal-dock`)*

```
custom cursor:  fixed h-[43px] rounded-full bg-neutral-950 px-[18px]
                font-playfair text-base text-neutral-50
                box-shadow: 0 8px 20px rgba(17,19,23,0.12)
                label: '< Drag >'
```

The dock is the one place a "shadow on a chip" appears — the cursor is a free-floating control, not a card.

### 6.7 Gradual-blur backdrop  *(nav drawer)*

`<GradualBackdrop divCount={8} strength={2} height='40em' />` — 8 stacked layers of progressive `backdrop-filter` blur, anchored bottom. Tinted by an inline plate `bg-[color-mix(in srgb, neutral-50 26%, transparent)]`.

### 6.8 Accordion (FAQ)

See R7 in §5.3. Trigger is unstyled-looking; expansion is implicit (no chevron). Height animated via JS-set inline `height`.

### 6.9 List item with check

```
flex items-center gap-3        (steps) or gap-2.5 (plan)
.check    iconfont &#xe63a; size-3.5 text-[14px]
          color: text-cta-fill (steps) or text-accent-a2 (plan)
.text     text-sm leading-[26px] (steps) or text-sm (plan)
```

---

## 7. Typography arrangement

### 7.1 Font families

| Token | Family | Where used |
|-------|--------|-----------|
| `--pt-font-regular` / `medium` / `semibold` | Inter | Body, nav, all buttons/CTAs, descriptions, card titles, glass-search input |
| `--pt-font-playfair` | Playfair Display | Hero h1, every `home-section-title`, plan price amount, dock price numerals, FAQ Q-labels, drag cursor chip |
| (no mono token) | — | No Roboto Mono in this codebase |

**Playfair scope is broader than "floors only"** — confirmed by the audit. Specifically: hero h1 (64), all section titles (40), plan price (56), dock price integer (56) + decimal (18), FAQ Q-marker (16), drag cursor (16). Inter for everything else.

### 7.2 Size scale (tokens + raw px)

Tokens (`token.css`):

| Token | Size / lh |
|-------|----------:|
| `--pt-heading-font-size-lg` / `lh-lg` | 60 / 64 |
| `--pt-heading-font-size-md` / `lh-md` | 44 / 50 |
| `--pt-title-font-size-md` / `lh-md` | 24 / 30 |
| `--pt-title-font-size-sm` / `lh-sm` | 20 / 26 |
| `--pt-body-font-size-md` / `lh-md` | 16 / 22 |
| `--pt-body-font-size-sm` / `lh-sm` | 14 / 20 |

Out-of-token sizes used at site level (write as raw px or Tailwind arbitrary):

| Size | Surface |
|------|---------|
| 64 / 80 | Hero h1 (Playfair) |
| 56 / 60 | Plan price amount (Playfair), dock price integer (Playfair) |
| 40 / 54 | Section title (Playfair) |
| 32 / 32 | Plan card name (Inter semibold) |
| 18 / 30 | Section subtitle (Inter, `text-lg leading-[30px]`) |
| 18 / 28 | Card title (Inter, `tracking-[-0.02em]`) |
| 15 / — | Glass-search input |
| 13 / — | Tag chip body |
| 14 / 26 | Steps points body |
| 14 / 22 | Plan card desc (`tracking-[-0.01em]`) |

When token doesn't fit, **prefer the raw px arbitrary value over inventing a token**.

### 7.3 Type pairing by surface

| Surface | Title | Sub | Body |
|---------|-------|-----|------|
| Hero | Playfair 64/80 | typewriter 16 | trust strip 14 |
| Section head A (centered) | Playfair 40/54 | `text-lg` 18/30 neutral-600 | — |
| Section head B (split) | Playfair 40/54 max-440 | text-sm 14/26 neutral-600 | — |
| Section head D (in-grid) | Playfair 40/54 | — | — |
| Card (services/why/steps) | Inter `text-lg leading-7 tracking-[-0.02em]` neutral-950 | — | text-sm leading-5 neutral-600 |
| Plan card | Inter 32 semibold + Playfair 56/60 price | text-sm 14/22 | text-sm benefits |
| FAQ item | Inter 18/28 medium `tracking-[-0.02em]` + Playfair 16 Q-label | — | Inter body default neutral-600 |
| Nav link | Inter 14/20 normal | — | — |

### 7.4 Subtitle width caps

| Context | Cap |
|---------|-----|
| Centered floor head subtitle (deals, plan) | natural width up to inner gutter; `max-w-[840px]` typical |
| Split head left title (steps) | `max-w-[440px]` |
| Split head right description (steps) | `flex-[1_1_280px]` (basis 280, grows) |
| Card description | width of card (no explicit cap) |
| Reader / long-form | `--pt-layout-max-read-box` = 768 |
| Hero typewriter | natural width inside flex row |

### 7.5 Gradient text rule

- **At most one gradient `<span>` per visible floor.**
- Reserved slots:
  - Logo nib → `--pt-gradient-1`
  - Search placeholder → `--pt-gradient-home-search-placeholder`
  - Search border rim → `--pt-gradient-home-search-border`
  - AI Tools nav link → `--pt-gradient-nav-link`
  - Optional hero subtitle underline → `--pt-gradient-2` (used as `border-image`)
- **Never** on buttons, page backgrounds, card surfaces.

---

## 8. Spacing rhythm

Tailwind 4-px scale + arbitrary values when needed. Anchor every value to:

`4 · 6 · 8 · 10 · 12 · 14 · 16 · 18 · 20 · 24 · 26 · 30 · 36 · 40 · 44 · 50 · 60 · 70 · 80 · 100 · 120 · 140 · 170 · 280`

The 70-px gutter recurs because it's half of `--pt-layout-max-inner`'s 140-px difference; treat 70 as a first-class number.

Defaults:

| Context | Value |
|---------|-------|
| Tight inline gap (chips, list items) | `gap-2.5` (10) |
| Default content gap | `gap-3` / `gap-3.5` (12 / 14) |
| Card grid gap | `gap-5` (20) — plan, steps stage |
| Wide grid gap | `gap-6` (24) — why-choose, nav links |
| Inner card padding | `pt-10 pb-10 px-10` (40) for plan; `py-10 pl-[30px] pr-8` for services |
| Hero card padding | `px-[70px] py-[30px]` (mobile `px-[18px]`) |
| Steps card padding | `px-[70px] pb-[60px] pt-10` (mobile `p-5`) |
| Glass-search inner bar | `px-10 py-[27px]` |
| Section title bottom | `mb-15` (60) / mobile `mb-10` (40) |
| Floor top gap | from `mt-20 / mt-[140px] / mt-[170px] / mt-[280px]` set (§1.4) |

---

## 9. Radius vocabulary

Nameslink uses fewer radii in practice than the token set offers. Working set:

| Token | px | Use |
|-------|---:|-----|
| `--pt-radius-full` | 999 | All CTAs, pills, chips, FABs, search shell rim |
| `--pt-radius-2xs` | 8 | Item rows in dropdowns (`rounded-2xs`) |
| `--pt-radius-xs` | 12 | Nav dropdown panels (`rounded-xs`) |
| 10 (raw) | 10 | **The house default for content cards** (services, plan, quick-nav, dock-card-inner, mobile profile chip) |
| 20 (raw) | 20 | Hero card |
| 28 (raw) | 28 | Steps card (largest in use) |

Tokens 3xs (6), sm (18), md (24), lg (36), xl (42), 2xl (48) exist but are seldom used in marketing chrome. Note: `--pt-radius-sm` is 18 px (not 10) — the docs at 10 / 20 / 28 are raw px because they don't map cleanly to existing tokens.

---

## 10. Background steps & elevation

Nameslink reverses the usual canvas/surface ordering: **`neutral-100` is canvas, `neutral-50` is card surface.**

| Plane | Light | Dark | When |
|-------|-------|------|------|
| **Canvas** | `--pt-color-neutral-100` (`#f7f7f9`) | `--pt-color-neutral-100` (`#0d0d0e`) | `.page` body; default floor bg |
| **Card surface** | `--pt-color-neutral-50` (`#ffffff`) | `--pt-color-neutral-50` (`#000000`) | Borderless content cards |
| **Subtle surface** | `--pt-color-neutral-150` (`#f2f4f8`) | `--pt-color-neutral-150` (`#0f1115`) | Pill segmented track, chip bg |
| **Soft accent wash** | `--pt-color-primary-50` (`#edefff`) | (overridden to `neutral-50`) | Services floor bg, mode-pill rack track |
| **Card wash** | `--pt-gradient-card-bg` | (auto-inverts via neutral tokens) | Tinted card-as-floor panel |

Borders: **only when listed** (faq + why list rules, mobile profile chip, tag outline variants, tertiary CTA). Default `border: none` everywhere else.

Shadows: **default none**. Allowed: `shadow-card` (steps), `hover:shadow-light` (quick-nav), `shadow-normal` (nav dropdowns, user menu, mobile nav drawer). Never stack shadows.

---

## 11. CTA / button patterns

Source: `components/cta/styles.ts`.

All CTAs are pills (`rounded-full`).

### 11.1 Sizes

| Size | H | px | Font | Use |
|------|---|----|------|-----|
| `xs` | 30 | 14 | body-sm | Inline / dense |
| `sm` | 36 | 18 | body-sm | Compact |
| `md` | 40 | 20 | body-sm | Card actions (steps cards) |
| `md-plus` | 44 | 30 | body-sm | Wide CTA |
| `lg` | 48 | 22 | body-sm | **Default** |
| `xl` | 54 | 26 | body-md | Hero, plan |
| `2xl` | 60 | 32 | body-md | Hero featured (tablet `52` / `px-6`) |

### 11.2 Variants

| Variant | Fill | Text | Hover |
|---------|------|------|-------|
| `primary` (default) | `--pt-cta-color-fill` (light: `neutral-950` / dark: `primary-550`) | `--pt-cta-color-font-fill` | `--pt-cta-color-fill-hover` = `primary-650` (purple) |
| `secondary` | neutral pair | `primary-550` | `primary-150` lavender wash |
| `tertiary` | transparent | `neutral-950` | only stroked button — 1 px `line-100`, hover `line-300` |
| `nav-signup` | `neutral-950 → neutral-850` light; `primary-550` dark | white | flat |
| `plan-lite` | `accent-a1` (`#2c56ff` blue) | white | (no change) |
| `plan-pro` | `primary-550` (purple) | white | (no change) |

The "near-black at rest, purple on hover" pattern of `primary` is the kit's signature CTA move. Don't override it.

### 11.3 Context modifiers

- `steps` / `steps-stack-1` add `mt-[30px] self-start`
- Compound: `primary + steps-stack-1` in dark mode swaps to `bg-func-black text-func-white` (cards on lavender bg need black buttons in dark)

### 11.4 Disabled state

`neutral-400` fill / `neutral-550` text. No interaction.

---

## 12. Responsive

- **Breakpoint:** **1024 px** (`tablet:`). Below `639 px` is the secondary mobile threshold (changes only `--pt-footer-bottom-height`).
- **Outer gutters:** desktop 50 px (`maxWide px-[50px]`), mobile 20 px (`tablet:px-5`). Token gutters add another 70 px each side via the layout-max-inner formula.
- **Mobile collapses:**
  - All multi-column grids → 1 column
  - Floor top gaps → `mt-[70px]` (services, why, faq, plan) or `mt-[100px]` (steps)
  - Section title → `clamp(24px, 6vw, 32px)` / `clamp(32px, 6vw, 48px)`; `mb-10` (down from `mb-15`)
  - Hero h1 → `clamp(40px, 9vw, 56px) / 1.15`
  - Steps stage degrades from scroll-stack to plain `flex flex-col gap-5`
  - Plan grid → `grid-cols-1`
  - Nav becomes mobile drawer with gradual-blur backdrop
- **Container queries:** quick-nav uses `container-type: inline-size; container-name: quick-nav;` and switches to 4-col @ 1160 px container width. This is the only container-query site in the codebase — don't introduce more.

---

## 13. Light / Dark mode  *(see `tokens.md` §Dark/Light)*

Mode is set on `<html data-prefers-color='light'|'dark'>`. Token blocks live in `css/token.css:2-94`. Key rules:

- **Both modes are first-class.** Always ask which mode and verify in both.
- **Heading-on-canvas rule holds in both modes** — in dark, "canvas" is `neutral-100` (`#0d0d0e`), card surface is `neutral-50` (`#000000`).
- **CTA inverts:** light = `neutral-950` (black) → `primary-650` hover; dark = `primary-550` → `primary-650` hover. The "purple-on-hover" feel survives.
- **Imagery:** prefer per-mode hero JPGs (`light_hero_1–3.jpg` ↔ `dark_hero_1–3.jpg`); pick by `data-prefers-color`.
- **Shadows differ by mode token** — light `rgba(83,91,107,0.04)`, dark `rgba(0,0,0,0.22)`. Don't replace with one-mode-fits-all.
- **Quirks:**
  - `--pt-color-primary-50` stays `#edefff` in both modes (lavender wash is brand-constant).
  - Services floor bg is `bg-primary-50` light → `bg-neutral-50` dark (no lavender on dark canvas).
  - Steps `bg-primary-450` lavender card swaps its primary CTA to `bg-func-black` in dark.

---

## 14. Layout review checklist

- [ ] Picked the right container layer: outer (`layout-max-wide`) for framed visuals; inner (`layout-max-inner`) for everything else; reader cap for long-form
- [ ] H1 / section title sits on canvas (`neutral-100`); photography lives in its own rounded card — **never** an overlaid giant heading
- [ ] Floor top gaps from the {20, 100, 120, 140, 170, 280} set; tablet → {70, 100}
- [ ] Section title is Playfair 40/54 with `mb-15` (10 mobile); subtitle is Inter `text-lg leading-[30px]` neutral-600
- [ ] Cards are **borderless by default** — `bg-neutral-50 + rounded-[10/20/28]` with no border, no shadow unless interactive
- [ ] Borders appear only on: faq + why list rules, mobile profile chip, tag outline variants, tertiary CTA
- [ ] Playfair restricted to: hero h1, section titles, plan/dock price numerals, FAQ Q-labels — never on body, cards, nav
- [ ] CTAs are pills; `primary` uses near-black rest → purple hover (light) / purple → deeper-purple (dark)
- [ ] At most one gradient text per visible floor; gradient-token slots only (logo / search / nav-link / hero subtitle underline)
- [ ] Tag chips pick one fill family — never mix outline + filled within one card
- [ ] Mode pill rack uses sliding thumb 280 ms; thumb width JS-computed from active button
- [ ] Spacing values land on Tailwind's 4-px scale or the 70-px gutter; no orphan numbers
- [ ] Both light + dark modes verified — `data-prefers-color` attribute set; per-mode imagery; shadow tokens differ
- [ ] `prefers-reduced-motion` respected (no scroll-stack steps animation; no border/placeholder gradient panning)
