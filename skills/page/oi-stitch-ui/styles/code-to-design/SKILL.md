---
name: code-to-design
description: Capture existing web apps as design/ artifacts — static HTML plus DESIGN.md. Chains extract-static-html and extract-design-md.
---
# Code to Design (Local)

Output under **`design/`**:

- `design/pages/<page>.html` — [<pkg-dir>/page/oi-stitch-ui/styles/extract-static-html/SKILL.md](<pkg-dir>/page/oi-stitch-ui/styles/extract-static-html/SKILL.md)
- `design/DESIGN.md` — [<pkg-dir>/page/oi-stitch-ui/styles/extract-design-md/SKILL.md](<pkg-dir>/page/oi-stitch-ui/styles/extract-design-md/SKILL.md)
- Apply tokens — [<pkg-dir>/page/oi-stitch-ui/styles/manage-design-system/SKILL.md](<pkg-dir>/page/oi-stitch-ui/styles/manage-design-system/SKILL.md)
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@code-to-design` without a concrete task), **reply with this section** (replace `<pkg-dir>` with the installed package path, e.g. `~/.agents/skills/oi-skills`), then ask what they want to accomplish.

**Triggers:** **code-to-design**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<pkg-dir>/page/oi-stitch-ui/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** Local design/ — HTML + DESIGN.md

**Example prompts**
- 「oi-stitch-ui code-to-design 跑一遍」
- 「按 code-to-design 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

