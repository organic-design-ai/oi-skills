---
name: code-to-design
description: Capture existing web apps as design/ artifacts — static HTML plus DESIGN.md. Chains extract-static-html and extract-design-md.
---
# Code to Design (Local)

Output under **`design/`**:

- `design/pages/<page>.html` — [<skill-dir>/styles/extract-static-html/SKILL.md](<skill-dir>/styles/extract-static-html/SKILL.md)
- `design/DESIGN.md` — [<skill-dir>/styles/extract-design-md/SKILL.md](<skill-dir>/styles/extract-design-md/SKILL.md)
- Apply tokens — [<skill-dir>/styles/manage-design-system/SKILL.md](<skill-dir>/styles/manage-design-system/SKILL.md)
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@code-to-design` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-stitch-ui`), then ask what they want to accomplish.

**Triggers:** **code-to-design**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<skill-dir>/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** Local design/ — HTML + DESIGN.md

**Example prompts**
- 「oi-stitch-ui code-to-design 跑一遍」
- 「按 code-to-design 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

