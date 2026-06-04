---
name: design-md
description: Synthesize design/DESIGN.md from HTML exports, screenshots, or visual references.
---
# Design.md from Visual Assets

Inputs: `design/pages/*.html`, screenshots, or user notes.

1. Inventory UI patterns.
2. Extract colors, type, spacing, radius.
3. Write **`design/DESIGN.md`** using [<skill-dir>/styles/design-md/examples/DESIGN.md](<skill-dir>/styles/design-md/examples/DESIGN.md).
4. Apply via [<skill-dir>/styles/manage-design-system/SKILL.md](<skill-dir>/styles/manage-design-system/SKILL.md).
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@design-md` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-stitch-ui`), then ask what they want to accomplish.

**Triggers:** **design-md**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<skill-dir>/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** DESIGN.md from HTML/images

**Example prompts**
- 「oi-stitch-ui design-md 跑一遍」
- 「按 design-md 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

