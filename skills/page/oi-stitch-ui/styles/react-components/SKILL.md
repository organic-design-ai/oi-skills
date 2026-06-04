---
name: react-components
description: Convert design/pages HTML and screenshots into modular Vite/React components with validation.
---
# HTML to React

Inputs: `design/pages/<page>.html`, optional PNG, `design/DESIGN.md`.

Use [<skill-dir>/styles/react-components/resources/component-template.tsx](<skill-dir>/styles/react-components/resources/component-template.tsx), [<skill-dir>/styles/react-components/resources/architecture-checklist.md](<skill-dir>/styles/react-components/resources/architecture-checklist.md).

Validate: `npm run validate <file>` in `<skill-dir>/styles/react-components` after `npm install`.
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@react-components` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-stitch-ui`), then ask what they want to accomplish.

**Triggers:** **react-components**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<skill-dir>/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** HTML → React components

**Example prompts**
- 「oi-stitch-ui react-components 跑一遍」
- 「按 react-components 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

