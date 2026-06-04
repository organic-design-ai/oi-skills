---
name: enhance-prompt
description: Turn vague UI ideas into structured prompts; inject design/DESIGN.md when present.
---
# Enhance Prompt

1. Assess platform, page type, sections — [<skill-dir>/styles/enhance-prompt/references/KEYWORDS.md](<skill-dir>/styles/enhance-prompt/references/KEYWORDS.md).
2. Include **DESIGN SYSTEM** block from `design/DESIGN.md` if it exists.
3. Output numbered sections and component vocabulary.
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@enhance-prompt` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-stitch-ui`), then ask what they want to accomplish.

**Triggers:** **enhance-prompt**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<skill-dir>/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** Polish UI prompts

**Example prompts**
- 「oi-stitch-ui enhance-prompt 跑一遍」
- 「按 enhance-prompt 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

