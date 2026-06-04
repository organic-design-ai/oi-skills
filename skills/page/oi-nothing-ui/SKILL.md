---
name: oi-nothing-ui
description: >-
  Nothing-inspired UI/UX design system: monochromatic, typographically driven,
  information-dense without clutter; dark and light modes with equal rigor. TRIGGER
  when user says Nothing style, Nothing design, oi-nothing-ui, nothing-ui, or
  /nothing-design. NEVER trigger for generic UI or design tasks.
version: 3.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep]
---
# Oi Nothing UI — Nothing-Inspired Design System

**Author:** dominikmartn

**Skill path:** `<skill-dir>/` (e.g. `~/.cursor/skills/oi-nothing-ui`).

Reference specs: `styles/references/` (`tokens.md`, `components.md`, `platform-mapping.md`).

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-nothing-ui` or `@nothing-ui` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-nothing-ui`), then ask what they want to accomplish.

**Triggers:** `oi-nothing-ui`, `/oi-nothing-ui`, `nothing-ui`, `/nothing-ui`, `Nothing style`, `Nothing design`, `/nothing-design`, Nothing 风格 / 设计.

**Quick start**
1. Read this `SKILL.md` (philosophy, craft rules, workflow below).
2. Load references as needed: `<skill-dir>/styles/references/`.
3. Declare Google Fonts, ask dark/light, sketch three-layer hierarchy, then implement.

**Example prompts**
- 「用 oi-nothing-ui 做深色仪表盘」
- 「Nothing style landing，先 light mode」
- 「按 tokens 改这组 stat rows」

**Do not use for:** generic UI without explicit Nothing request; multi-style libraries → `oi-awesome-ui` / `oi-taste-ui`; ffmpeg / video (`widget/*`).

## When to use

- User explicitly wants **Nothing-inspired** UI (monochrome, typographic hierarchy, industrial warmth)
- Dashboards, product UI, or marketing pages in this visual language
- Need token-level color, type, spacing, components, and platform mapping

**Do not use** unless the user names Nothing style or this skill — never auto-trigger on generic design tasks.

---

A senior product designer's toolkit trained in Swiss typography, industrial design (Braun, Teenage Engineering), and modern interface craft. Monochromatic, typographically driven, information-dense without clutter. Dark and light mode with equal rigor.

**Before starting any design work, declare which Google Fonts are required and how to load them** (see `styles/references/tokens.md` Section 1 and `platform-mapping.md`). Never assume fonts are already available.

---

## 1. DESIGN PHILOSOPHY

- **Subtract, don't add.** Every element must earn its pixel. Default to removal.
- **Structure is ornament.** Expose the grid, the data, the hierarchy itself.
- **Monochrome is the canvas.** Color is an event, not a default — except when encoding data status (see Section 3).
- **Type does the heavy lifting.** Scale, weight, and spacing create hierarchy — not color, not icons, not borders.
- **Both modes are first-class.** Dark mode: OLED black. Light mode: warm off-white. Neither is "derived" — both get full design attention. Ask the user which mode to start with.
- **Industrial warmth.** Technical and precise, but never cold. A human hand should be felt.

---

## 2. CRAFT RULES — HOW TO COMPOSE

### 2.1 Visual Hierarchy: The Three-Layer Rule

Every screen has exactly **three layers of importance.** Not two, not five. Three.

| Layer | What | How |
|-------|------|-----|
| **Primary** | The ONE thing the user sees first. A number, a headline, a state. | Doto or Space Grotesk at display size. `--text-display`. 48–96px breathing room. |
| **Secondary** | Supporting context. Labels, descriptions, related data. | Space Grotesk at body/subheading. `--text-primary`. Grouped tight (8–16px) to the primary. |
| **Tertiary** | Metadata, navigation, system info. Visible but never competing. | Space Mono at caption/label. `--text-secondary` or `--text-disabled`. ALL CAPS. Pushed to edges or bottom. |

**The test:** Squint at the screen. Can you still tell what's most important? If two things compete, one needs to shrink, fade, or move.

**Common mistake:** Making everything "secondary." Evenly-sized elements with even spacing = visual flatness. Be brave — make the primary absurdly large and the tertiary absurdly small. The contrast IS the hierarchy.

### 2.2 Font Discipline

Per screen, use maximum:
- **2 font families** (Space Grotesk + Space Mono. Doto only for hero moments.)
- **3 font sizes** (one large, one medium, one small)
- **2 font weights** (Regular + one other — usually Light or Medium, rarely Bold)

Think of it as a budget. Every additional size/weight costs visual coherence. Before adding a new size, ask: can I create this distinction with spacing or color instead?

| Decision | Size | Weight | Color |
|----------|:---:|:---:|:---:|
| Heading vs. body | Yes | No | No |
| Label vs. value | No | No | Yes |
| Active vs. inactive nav | No | No | Yes |
| Hero number vs. unit | Yes | No | No |
| Section title vs. content | Yes | Optional | No |

**Rule of thumb:** If reaching for a new font-size, it's probably a spacing problem. Add distance instead.

### 2.3 Spacing as Meaning

Spacing is the primary tool for communicating relationships.

```
Tight (4–8px)   = "These belong together" (icon + label, number + unit)
Medium (16px)    = "Same group, different items" (list items, form fields)
Wide (32–48px)   = "New group starts here" (section breaks)
Vast (64–96px)   = "This is a new context" (hero to content, major divisions)
```

**If a divider line is needed, the spacing is probably wrong.** Dividers are a symptom of insufficient spacing contrast. Use them only in data-dense lists where items are structurally identical.

### 2.4 Container Strategy (prefer top)

1. **Spacing alone** (proximity groups items)
2. A single divider line
3. A subtle border outline
4. A surface card with background change

Each step down adds visual weight. Use the lightest tool that works. Never box the most important element — let it float on the background.

### 2.5 Color as Hierarchy

In a monochrome system, the gray scale IS the hierarchy. Max 4 levels per screen:

```
--text-display (100%) → Hero numbers. One per screen.
--text-primary (90%)  → Body text, primary content.
--text-secondary (60%) → Labels, captions, metadata.
--text-disabled (40%) → Disabled, timestamps, hints.
```

**Red (#D71921) is not part of the hierarchy.** It's an interrupt — "look HERE, NOW." If nothing is urgent, no red on the screen.

**Data status colors** (success green, warning amber, accent red) are exempt from the "one accent" rule when encoding data values. Apply color to the **value itself**, not labels or row backgrounds. See `styles/references/tokens.md` for the full color system.

### 2.6 Consistency vs. Variance

**Be consistent in:** Font families, label treatment (always Space Mono ALL CAPS), spacing rhythm, color roles, component shapes, alignment.

**Break the pattern in exactly ONE place per screen:** An oversized number, a circular widget among rectangles, a red accent among grays, a Doto headline, a vast gap where everything else is tight.

This single break IS the design. Without it: sterile grid. With more than one: visual chaos.

### 2.7 Compositional Balance

**Asymmetry > symmetry.** Centered layouts feel generic. Favor deliberately unbalanced composition:
- **Large left, small right:** Hero metric + metadata stack.
- **Top-heavy:** Big headline near top, sparse content below.
- **Edge-anchored:** Important elements pinned to screen edges, negative space in center.

Balance heavy elements with more empty space, not with more heavy elements.

### 2.8 The Nothing Vibe

1. **Confidence through emptiness.** Large uninterrupted background areas. Resist filling space.
2. **Precision in the small things.** Letter-spacing, exact gray values, 4px gaps. Micro-decisions compound into craft.
3. **Data as beauty.** `36GB/s` in Space Mono at 48px IS the visual. No illustrations needed.
4. **Mechanical honesty.** Controls look like controls. A toggle = physical switch. A gauge = instrument.
5. **One moment of surprise.** A dot-matrix headline. A circular widget. A red dot. Restraint makes the one expressive moment powerful.
6. **Percussive, not fluid.** Imagine UI sounds: click not swoosh, tick not chime. Design transitions that feel mechanical and precise.

### 2.9 Visual Variety in Data-Dense Screens

When 3+ data sections appear on one screen, vary the visual form:

| Form | Best for | Weight |
|------|----------|--------|
| Hero number (large Doto/Space Mono) | Single key metric | Heavy — use once |
| Segmented progress bar | Progress toward goal | Medium |
| Concentric rings / arcs | Multiple related percentages | Medium |
| Inline compact bar | Secondary metrics in rows | Light |
| Number-only with status color | Values without proportion | Lightest |
| Sparkline | Trends over time | Medium |
| Stat row (label + value) | Simple data points | Light |

Lead section → heaviest treatment. Secondary → different form. Tertiary → lightest. The FORM varies, the VOICE stays the same.

---

## 3. ANTI-PATTERNS — WHAT TO NEVER DO

- No gradients in UI chrome
- No shadows. No blur. Flat surfaces, border separation.
- No skeleton loading screens. Use `[LOADING...]` text or segmented spinner.
- No toast popups. Use inline status text: `[SAVED]`, `[ERROR: ...]`
- No sad-face illustrations, cute mascots, or multi-paragraph empty states
- No zebra striping in tables
- No filled icons, multi-color icons, or emoji as UI
- No parallax, scroll-jacking, or gratuitous animation
- No spring/bounce easing. Use subtle ease-out only.
- No border-radius > 16px on cards. Buttons are pill (999px) or technical (4–8px).
- Data visualization: differentiate with **opacity** (100%/60%/30%) or **pattern** (solid/striped/dotted) before introducing color.

---

## 4. WORKFLOW

1. **Declare fonts** — tell the user which Google Fonts to load (see `styles/references/tokens.md`, `platform-mapping.md`)
2. **Ask mode** — dark or light? Neither is default.
3. **Sketch hierarchy** — identify the 3 layers before writing any code
4. **Compose** — apply craft rules (Sections 2.1–2.9)
5. **Check tokens** — consult `styles/references/tokens.md` for exact values
6. **Build components** — consult `styles/references/components.md` for patterns
7. **Adapt to platform** — consult `styles/references/platform-mapping.md` for output conventions

---

## 5. REFERENCE FILES

| File | Path |
|------|------|
| Tokens | `<skill-dir>/styles/references/tokens.md` |
| Components | `<skill-dir>/styles/references/components.md` |
| Platform mapping | `<skill-dir>/styles/references/platform-mapping.md` |

---

## 6. REVIEW CHECKLIST

- [ ] At most one red accent moment per screen (unless data-status encoding)
- [ ] Three-layer hierarchy passes the squint test
- [ ] Font budget: ≤2 families, ≤3 sizes, ≤2 weights per screen
- [ ] No shadows, gradients in chrome, skeleton loaders, or toast popups
- [ ] Dark and light tokens applied consistently
