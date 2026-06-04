---
name: stitch-loop
description: Multi-page build loop using design/SITE.md and design/next-prompt.md baton files.
---
# Multi-Page Build Loop

Requires: `design/DESIGN.md`, `design/SITE.md`, `design/next-prompt.md`.

Each iteration: read baton → implement page in repo → update SITE.md → write next baton.

Schema: [<skill-dir>/styles/stitch-loop/resources/baton-schema.md](<skill-dir>/styles/stitch-loop/resources/baton-schema.md).
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@stitch-loop` without a concrete task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-stitch-ui`), then ask what they want to accomplish.

**Triggers:** **stitch-loop**, or parent **oi-stitch-ui** when this workflow matches.

**Quick start**
1. Parent: `<skill-dir>/SKILL.md`.
2. Follow steps in this file; artifacts live in project **`design/`**.
3. **Summary:** Multi-page baton loop

**Example prompts**
- 「oi-stitch-ui stitch-loop 跑一遍」
- 「按 stitch-loop 更新 design/DESIGN.md」

**Do not use for:** unrelated stitch slugs; video widgets.

