---
name: react-components
description: Convert design/pages HTML and screenshots into modular Vite/React components with validation.
---
# HTML to React

Inputs: `design/pages/<page>.html`, optional PNG, `design/DESIGN.md`.

Use [<pkg-dir>/page/oi-stitch-ui/styles/react-components/resources/component-template.tsx](<pkg-dir>/page/oi-stitch-ui/styles/react-components/resources/component-template.tsx), [<pkg-dir>/page/oi-stitch-ui/styles/react-components/resources/architecture-checklist.md](<pkg-dir>/page/oi-stitch-ui/styles/react-components/resources/architecture-checklist.md).

Validate: `npm run validate <file>` in `<pkg-dir>/page/oi-stitch-ui/styles/react-components` after `npm install`.
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@react-components` without a concrete task), **reply with this section** (replace `<pkg-dir>` with the installed package path, e.g. `~/.agents/skills/oi-skills`), then ask what they want to accomplish.

**Triggers:** **react-components**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<pkg-dir>/page/oi-stitch-ui/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** HTML → React components

**Example prompts**
- 「oi-stitch-ui react-components 跑一遍」
- 「按 react-components 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

