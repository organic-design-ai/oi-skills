---
name: manage-design-system
description: Maintain design/DESIGN.md and map tokens to Tailwind/CSS/theme config in the repo.
---
# Manage Design System

1. Create or update **`design/DESIGN.md`** via extract-design-md, design-md, or taste-design.
2. Confirm summary with user before repo-wide token refactors.
3. Map tokens to tailwind.config / CSS variables.
4. Example: [<pkg-dir>/page/oi-stitch-ui/styles/design-md/examples/DESIGN.md](<pkg-dir>/page/oi-stitch-ui/styles/design-md/examples/DESIGN.md).
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@manage-design-system` without a concrete task), **reply with this section** (replace `<pkg-dir>` with the installed package path, e.g. `~/.agents/skills/oi-skills`), then ask what they want to accomplish.

**Triggers:** **manage-design-system**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<pkg-dir>/page/oi-stitch-ui/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** design/DESIGN.md and theme tokens

**Example prompts**
- 「oi-stitch-ui manage-design-system 跑一遍」
- 「按 manage-design-system 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

