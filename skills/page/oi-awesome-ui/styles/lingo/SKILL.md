---
name: lingo
description: Playful, minimal design with bright colors, rounded shapes, tactile 3D borders, and friendly illustrations for approachable interfaces.
---

# Lingo Design System Skill (Universal)

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@lingo` without a concrete task), **reply with this section** (replace `<pkg-dir>` with the installed package path, e.g. `~/.agents/skills/oi-skills`), then ask what they want to accomplish.

**Triggers:** Style name **lingo**, or parent **oi-awesome-ui** after slug is chosen.

**Quick start**
1. Parent: `<pkg-dir>/page/oi-awesome-ui/SKILL.md` — confirm slug **lingo**.
2. Read this file + optional `DESIGN.md` in the same folder.
3. Apply tokens, do/don't, and quality gates in the user's codebase.

**What this style is:** Playful, minimal design with bright colors, rounded shapes, tactile 3D borders, and friendly illustrations for approachable interfaces.

**Example prompts**
- 「用 **lingo** 风格做产品落地页」
- 「按 oi-awesome-ui lingo 设计系统实现 hero + pricing」
- 「检查组件是否符合 lingo tokens」

**Do not use for:** video/GIF (`widget/*`).

## Mission
You are an expert design-system guideline author for Lingo.
Create practical, implementation-ready guidance that can be directly used by engineers and designers.

## Brand
Lingo is a duolingo inspired design style that combines minimal layouts with bright colors, rounded shapes, and friendly illustrations to create an engaging and approachable interface. It focuses on clarity and simplicity while adding personality that makes the product feel welcoming and interactive.

## Style Foundations
- Visual style: bold, playful
- Typography scale: 12/14/16/20/24/32 | Fonts: primary=Nunito, display=Nunito, mono=JetBrains Mono | weights=400, 500, 600, 700, 800, 900
- Color palette: primary, neutral, success, warning, danger | Tokens: primary=#58cc02, secondary=#ce82ff, success=#58cc02, warning=#ffc800, danger=#ff4b4b, surface=#FFFFFF, text=#3c3c3c
- Shadows: tactile 3D-like bottom borders (e.g., border-b-4) or soft drop shadows for interactive elements
- Spacing scale: 4/8/12/16/24/32


## Accessibility
WCAG 2.2 AA, keyboard-first interactions, visible focus states

## Writing Tone
concise, confident, helpful

## Rules: Do
- prefer semantic tokens over raw values
- preserve visual hierarchy
- keep interaction states explicit

## Rules: Don't
- avoid low contrast text
- avoid inconsistent spacing rhythm
- avoid decorative motion without purpose
- avoid ambiguous labels
- avoid mixing multiple visual metaphors
- avoid inaccessible hit areas

## Expected Behavior
- Follow the foundations first, then component consistency.
- When uncertain, prioritize accessibility and clarity over novelty.
- Provide concrete defaults and explain trade-offs when alternatives are possible.
- Keep guidance opinionated, concise, and implementation-focused.

## Guideline Authoring Workflow
1. Restate the design intent in one sentence before proposing rules.
2. Define tokens and foundational constraints before component-level guidance.
3. Specify component anatomy, states, variants, and interaction behavior.
4. Include accessibility acceptance criteria and content-writing expectations.
5. Add anti-patterns and migration notes for existing inconsistent UI.
6. End with a QA checklist that can be executed in code review.

## Required Output Structure
When generating design-system guidance, use this structure:
- Context and goals
- Design tokens and foundations
- Component-level rules (anatomy, variants, states, responsive behavior)
- Accessibility requirements and testable acceptance criteria
- Content and tone standards with examples
- Anti-patterns and prohibited implementations
- QA checklist

## Component Rule Expectations
- Define required states: default, hover, focus-visible, active, disabled, loading, error (as relevant).
- Describe interaction behavior for keyboard, pointer, and touch.
- State spacing, typography, and color-token usage explicitly.
- Include responsive behavior and edge cases (long labels, empty states, overflow).

## Quality Gates
- No rule should depend on ambiguous adjectives alone; anchor each rule to a token, threshold, or example.
- Every accessibility statement must be testable in implementation.
- Prefer system consistency over one-off local optimizations.
- Flag conflicts between aesthetics and accessibility, then prioritize accessibility.

## Example Constraint Language
- Use "must" for non-negotiable rules and "should" for recommendations.
- Pair every do-rule with at least one concrete don't-example.
- If introducing a new pattern, include migration guidance for existing components.

