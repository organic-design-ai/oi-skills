# Qwen Cloud — Components

Tokens: `references/tokens.md` (`--pt-*`). Page-level composition (page shell, hero variants, section headers, grid tables, sidebar/reader patterns, sub-block vocabulary, preview gallery): **`references/layouts.md`**. Icons/images: `references/assets.md`.

Section numbers match `Guideline.html` TOC (01–14).

## Principles

**Tone:** 简洁 · 平白 · 弱描边 · 淡阴影. Flat surfaces; default `shadow: none` (淡阴影 token only when Guideline needs legibility). Weak 1px borders on outline controls and featured pricing rim — otherwise `neutral-50` / `150` / `100` and whitespace. One accent per view: near-black CTA, or one gradient word, or purple on hover — not all three competing.

**Panel-as-card composition** (`layouts.md` §11.6): when a card hosts a list of repeated rows (recommended models, cost summary, plan benefits, FAQ, bundle items), the outer panel is **borderless** (`gradient-card-bg` or `neutral-100` step, no 1px hairline, no shadow) and interior rows separate via **typography + a single hairline** — never nested grey-bg sub-cards.

**Visual QA:** open CDN `Guideline.html` §08 for live React previews; styles ship in `#ui-components` + `Scripts/ui.js`.

---

## §01 Hero Images

Grid: 3 × 2. Assets: `flower_01` – `flower_06` from `Images.json`.

- Frame: `radius-md`, `16:10`, `object-fit: cover`
- No border, no shadow on frame
- One floral per page, full-bleed in the **visual paragraph** below the title stack — never behind the H1 (`layouts.md` §2)

Mobile: 1 column.

> Pick the appropriate **hero variant (A–I)** from `layouts.md` §3 before composing — the floral grid applies to variant B and showcase blocks.

---

## §04 Buttons

Pill (`radius-full`). No default border on primary / secondary.

| Variant | Fill | Notes |
|---------|------|-------|
| `btn--primary` | `cta-fill` → hover `primary-550` | Light: black rest |
| `btn--secondary` | `primary-50` | Soft fill, no outline |
| `btn--outline` | transparent | Only variant with border (`line-200`) |
| `btn--text` | transparent | Ink → purple hover |

Sizes: default 14 px · `btn--sm` · `btn--xl` 54 px height.

CTA icon: `arrow-up-outlined` via `.qc-icon`.

Production console also ships **`ui-button`** primitives (§08) for app surfaces — same token fills; use `btn--*` on marketing pages.

---

## §05 Gradients

8 tokens (`--pt-gradient-1` … `8`). Text clip only. One word per screen. Featured tier border is the exception (1 px rim, not a fill).

---

## §06 Featured Model Card

Grid: 2 columns. Classes: `model-feature-card-grid` · `model-feature-card` · `model-feature-card--secondary`.

| | Primary | Secondary |
|---|---------|-----------|
| Background | `gradient-card-bg` | `neutral-50` |
| Border | optional `line-100` hairline | same |
| Shadow | none | none |
| Padding | 32 px | 32 px |
| Radius | `radius-md` | `radius-md` |

Inner: `mf-name` · `mf-desc` (2-line clamp) · `mf-tag` (pill, purple outline) · `mf-price-row` · `mf-divider` (`line-100`) · `mf-stats` · `mf-cta`.

Primary CTAs: primary + outline. Secondary card: secondary + text.

**If a model card hosts a sub-list** (recommended models, related items, included assets), treat the card as a panel-as-card (`layouts.md` §11.6): drop the optional `line-100` outer hairline and lay rows directly on the panel with `border-b 1px line-100` between rows. Do **not** wrap each row in its own `neutral-100/150` filled rounded sub-card.

Guideline also demos **`models-card`** + **`models-sidebar`** in §08 (console model browser).

---

## §07 Pricing Tiers

3-up grid. Tier: `neutral-50` fill, `line-100` hairline, `radius-md`, no shadow.

Featured (`.tier.is-featured`): gradient-1 border rim only — no ribbon, no extra shadow. Checkmarks: `check-outlined`.

---

## §08 Components & Primitives

Guideline §08 mounts a **live preview gallery** (`comp-primitives-mount` → `preview-grid`) — 53 production cards plus shared UI primitives from the transpiled bundle (`Scripts/ui.js`, same tokens as `Guideline.html`).

### 08.1 Gallery shell

| Piece | Class / attr | Rule |
|-------|----------------|------|
| Mount | `.comp-primitives-mount[data-ui-style="qwencloud"]` | React root; uses Guideline top nav |
| Page | `.page-shell.page-home` · `.page` · `main.preview-grid` | Full-width masonry canvas |
| Masonry | `.preview-grid__canvas` · `.preview-grid__item` | CSS columns via `--columns` (4 desktop) · `--gap: 32px`; JS positions items |
| Card shell | `ui-card` pattern (`da` / header / body / footer slots) | `radius-sm`, `neutral-50`, hairline rim via `box-shadow: 0 0 0 1px color-mix(...)`, `gap: 24px`, padding `24px 0` |

See `layouts.md` §19 for gallery layout numbers.

### 08.2 UI primitives (shared building blocks)

Use these inside console / dashboard pages. All respect `--pt-*` tokens.

| Primitive | BEM root | Use |
|-----------|----------|-----|
| Button | `ui-button` | Inline-flex pill; color/border transitions `--pt-motion-fast` |
| Dialog | `ui-dialog` | Overlay `rgba(0,0,0,.8)`; content `radius-sm` |
| Sheet | `ui-sheet` | Side / bottom panels |
| Select | `ui-select` | Pill trigger + popover list |
| Checkbox / radio | `ui-checkbox` · `ui-radio-group` | Forms, notification matrix |
| Switch | `ui-switch` | Settings toggles |
| Slider | `ui-slider` | Playground parameters (`kitchen-island`) |
| Progress | `ui-progress` | Upload / sync states |
| Spinner | `ui-spinner` | Loading affordance |
| Table | `ui-table` | Tabular billing / usage |
| Accordion | `ui-accordion` | FAQ, dense settings |
| Breadcrumb | `ui-breadcrumb` | Docs / wayfinding |
| Calendar | `ui-calendar` | Date pickers (`upcoming-payments`) |
| Chart wrappers | `ui-chart` | Recharts host; pair with `analytics-card`, `bar-chart-card`, `pie-chart-card` |
| Tooltip | `ui-tooltip` | Copy / hint (`ui-copy-tooltip-button`) |
| Sidebar | `ui-sidebar` · `sidebar-nav` | Console nav rail |
| Models filters | `ui-models-filter-*` | Toolbar: list, range, section, tags, toggle-row (`layouts.md` §17) |
| Price / unit text | `ui-price-text` · `ui-unit-text` | Mono pricing rows |
| Field separator | `ui-field-separator` | Form section breaks |
| Style switch | `ui-style-switch` | Guideline theme / kit toggle |

**Forms:** `forms-specimen` demonstrates pill inputs — border `line-200`, focus `primary-550`, labels 12 px uppercase mono. Pair with `file-upload`, `environment-variables`, `shipping-address`, `invite-team`.

### 08.3 Production card catalog (53)

Grouped by domain. Each item is a self-contained `ui-card` specimen in the §08 masonry grid. Reuse the BEM root + header/body/footer anatomy; do not invent parallel class names.

**Foundation & tokens**

| Root | Title (Guideline) |
|------|-------------------|
| `palette-overview` | Palette |
| `typography-specimen` | Typography scales |
| `icon-preview-grid` | Icon grid (manifest glyphs) |
| `skills-code-block` | Add skills |

**Models & playground**

| Root | Title |
|------|-------|
| `models-card` | Model card (console) |
| `models-sidebar` | Models sidebar |
| `kitchen-island` | Model playground |
| `buy-investment` | Model summary |
| `not-found` | 404 / missing endpoint |

**Usage & analytics**

| Root | Title |
|------|-------|
| `visitors` | API requests |
| `analytics-card` | Usage analytics |
| `usage-card` | Usage summary |
| `bar-chart-card` | Bar chart card |
| `pie-chart-card` | Requests by model |
| `power-usage` | Token usage |
| `sleep-report` | Token usage report |
| `weekly-fitness-summary` | Weekly tokens-cost recap |
| `contribution-history` | Usage history |
| `index-investing` | Token-cost averaging |
| `live-waveform` | Realtime transcription stream |

**Billing & payments**

| Root | Title |
|------|-------|
| `invoice` | Invoice |
| `payments` | Payments |
| `recent-transactions` | Recent usage |
| `transfer-funds` | Transfer credits |
| `receiving-method` | Payment method |
| `claimable-balance` | Claimable credits |
| `card-overview` | Credit balance |
| `payout-threshold` | Spend alert threshold |
| `savings-targets` | Token budgets |
| `new-milestone` | Set a new spend cap |
| `upcoming-payments` | Upcoming charges |
| `shipping-address` | Billing address |

**Workspace & access**

| Root | Title |
|------|-------|
| `sidebar-nav` | Console sidebar |
| `account-access` | Account access |
| `invite-team` | Invite team |
| `no-team-members` | Empty team |
| `contributors` | Contributors |
| `github-profile` | Profile |
| `preferences` | Preferences |
| `notification-settings` | Notifications |
| `environment-variables` | Environment variables |
| `shortcuts` | Keyboard shortcuts |

**Integrations & catalog**

| Root | Title |
|------|-------|
| `codespaces-card` | Codespaces / dev environment |
| `social-links` | Integration links |
| `release-catalog` | Release catalog |
| `syncing-state` | Syncing state |
| `empty-connect-bank` | Empty bank connect |
| `empty-distribute-track` | Empty distribute track |

**Support & misc**

| Root | Title |
|------|-------|
| `faq` | FAQ (tabs + accordion) |
| `report-bug` | Report bug |
| `book-appointment` | Book a call |
| `file-upload` | Upload training data |
| `skeleton-loading` | Skeleton loading |

### 08.4 Card composition rules (§08)

- **Header slot:** `title` (`ha`) + optional `description` (`ma`) — body-md, `neutral-650`
- **Body:** grid, chart, form, or list — no nested grey sub-cards unless the specimen explicitly shows one
- **Footer:** primary action right-aligned; secondary ghost left
- **Charts:** host inside `__chart` child; axis labels mono `caption-md`
- **Empty states:** centered illustration + one CTA — no stock art; use manifest icons only
- **Loading:** `skeleton-loading` pulse on `neutral-150` bars — no spinner unless async action

---

## §09 Tags & Badges

Small pills. Supporting bg + tint pairs. No border on filled variants. `is-outline` badge is the only outlined tag.

| Scale | Class | Radius | Size |
|-------|-------|--------|------|
| Badge | `.badge.is-*` | `radius-4xs` (2 px) | 10 px caps, mono uppercase |
| Chip | `.chip.is-*` | `radius-full` | 11 px sentence case |

Variants: `accent` · `success` · `warning` · `danger` · `info` · `pro` · `gray` · `gradient` (chip only, one gradient word via `data-label`).

Do not put badges and chips on the same card.

---

## §10 Customer Card Grid

2 × 2. Assets: `card_1` – `card_4` from `Images.json`.

- Card: full-bleed image, `radius-md`, no outer border
- Panel: white fill, `radius-xs`, right-aligned — typography only, no logo
- Prefer flat panel (no shadow) in new work; guideline demo may use light shadow on busy art

Quote · headline · body · name + title (bottom-right).

---

## Page chrome

Page-level composition lives in **`layouts.md`** — page shell, container utilities (`.layout-max-wide` / `.layout-max-inner`), hero variants A–I, section header patterns A/B/C, grid table, filter rail, reader column, sub-block vocabulary, preview gallery (§19), and the layout review checklist (§18).

Quick pointers when assembling a page:

- **Nav:** sticky, frosted, no bottom border. Height 84 px desktop / 62 px mobile (`--pt-nav-backdrop-offset`).
- **Section background steps:** alternate `neutral-50` ↔ `neutral-100` for visual rhythm — not bordered boxes.
- **Theme toggle:** `sun-outlined` · `moon-outlined`.
- **Breakpoint:** 1024 px; grids collapse to `1fr`; gutters 36 → 20 px (utilities handle it).

---

## Assets

**Images:** CDN `Images.json` — `card_1–4.jpg` · `flower_01–06.jpg` (`assets.md`)

**Icons:** CDN `Icons.json` — 48 outlined SVGs; Tabler outlined as fallback for missing glyphs (`icons.md`)

**Live bundle:** `Guideline.html` + `Scripts/ui.js` for §08 component QA (`assets.md`)
