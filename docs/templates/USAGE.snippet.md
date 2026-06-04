# Usage section template (copy into `SKILL.md`)

Every skill **must** include a `## Usage` section near the top (after title/intro, before workflow steps). Agents use it when the user asks `usage`, `怎么用`, `help`, or invokes the skill without a concrete task.

```markdown
## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@<skill-name>` without a task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-my-skill`), then ask what they want to accomplish.

**Triggers:** …

**Quick start**
1. …

**Example prompts**
- 「…」
- "…"

**Do not use for:** …
```

## `skill.yaml` (repo metadata)

Optional but recommended for manifests and tooling:

```yaml
usage: >-
  One-line English: what to tell the user when they ask for usage.
usage_zh: >-
  一行中文用法摘要。
```

`SKILL.md` remains the source of truth for agents; keep `usage` / `usage_zh` in sync when you change Usage.

## Scaffold

New skills from [new-skill/](./new-skill/) already include a starter Usage block — fill in triggers, steps, and example prompts.
