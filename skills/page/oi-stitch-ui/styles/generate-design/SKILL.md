---
name: generate-design
description: Structure UI generation prompts from text or images — layout sections, platform, edits, and variants. Implement in the user's stack using design/DESIGN.md tokens.
---
# Generate Design (Prompt & Implementation)

Turn user intent into **implementable UI** in the project codebase. No external design APIs.

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@generate-design` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-stitch-ui`), then ask what they want to accomplish.

**Triggers:** **generate-design**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<skill-dir>/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** Prompt + implement UI in codebase

**Example prompts**
- 「oi-stitch-ui generate-design 跑一遍」
- 「按 generate-design 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

## When to use

- New landing page / screen from description or mockup
- Targeted edits to an existing page
- 2–3 layout or density variants

## Steps

1. Read `design/DESIGN.md` if present; else run `manage-design-system` or `taste-design`.
2. Enhance prompt using [<skill-dir>/styles/generate-design/references/design-mappings.md](<skill-dir>/styles/generate-design/references/design-mappings.md) and [<skill-dir>/styles/generate-design/references/prompt-keywords.md](<skill-dir>/styles/generate-design/references/prompt-keywords.md).
3. Implement in the user's framework.
4. Example: [<skill-dir>/styles/generate-design/examples/enhanced-prompt.md](<skill-dir>/styles/generate-design/examples/enhanced-prompt.md).

## PAGE STRUCTURE template

```markdown
[Purpose]
**PLATFORM:** Web | Mobile
**SECTIONS:** Header, Hero, Content, Footer — with concrete content per section
```
