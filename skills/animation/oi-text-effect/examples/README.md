# oi-text-effect · examples

| File | Use it when |
|------|-------------|
| `text-effect-showcase.html` | **Start here.** No-deps showcase: all 23 specimens + interactive Playground (entrance, sweep, scramble, flip, morph, shimmer, typewriters). |
| `TextAnimate.jsx` | Entrance effects (10 variants). React/Next.js with `motion`. Drop into `components/ui/`. |
| `DiaTextReveal.jsx` | Color sweep. React/Next.js with `motion`. |
| `HyperText.jsx` | Scramble/decrypt. React/Next.js, no extra deps. |
| `Text3DFlip.jsx` | Per-character 3D flip on hover. React/Next.js with `motion`. |
| `MorphingText.jsx` | SVG-filter liquid morph between phrases. |
| `TextShimmer.jsx` | Neutral gradient shimmer loop. |
| `TextType.jsx` | Typewriter typing/deleting/loop (merged from former `oi-text-type`). |
| `TextShiftWords.jsx` | Interval phrase cycle with gradient underline (nameslink hero-desc style). |
| `react-demo.jsx` | Reference page for all variants + custom `variants`. |

## React quick install

```bash
pnpm add motion
# copy components from this folder into components/ui/
```

`TextAnimate.tsx` expects a `cn` helper at `@/lib/utils` (shadcn convention). If your
project doesn't have one, either:

1. Add it: `pnpm dlx shadcn@latest init` (or copy the two-liner from shadcn docs).
2. Or replace `cn(a, b, c)` with a `[a, b, c].filter(Boolean).join(" ")` inline.

`DiaTextReveal.tsx` also uses `cn` — same solution applies.

## Vanilla HTML quick start

Open `text-effect-showcase.html` in a browser — no build step.

**Entrance effects:** copy the `.oi-ta` CSS block and the runtime script, then:

```html
<h1 data-anim="blurInUp" data-by="character">Hello world</h1>
```

**Typewriter (`textType`):** copy the `textType` runtime from the showcase, then:

```html
<h1 data-anim="textType" data-texts="Build Fast,Ship Better">Build Fast</h1>
```

**Phrase shift (`textShiftWords`):** copy the `textShiftWords` runtime from the showcase, then:

```html
<p data-anim="textShiftWords" data-texts="Premium domains,Fast checkout,Global DNS">Premium domains</p>
```

**Color sweep:** copy the `[data-anim="colorSweep"]` CSS block, then:

```html
<h1 data-anim="colorSweep" style="--ta-duration:1500ms">Magic UI</h1>
```

Custom colors via `--sweep-c1` through `--sweep-c5` CSS variables.
