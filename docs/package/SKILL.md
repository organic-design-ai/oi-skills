---
name: oi-skills-catalog
description: >-
  Repo-only catalog for Oi Skills (not installed by npx skills add). Each child
  skill under skills/ installs separately to ~/.agents/skills/oi-<name>/.
---

# Oi Skills — repo catalog

**Author:** Alibaba Cloud Design

> **Not installed:** There is no root `SKILL.md` in this repo. `npx skills add` discovers
> the 12 skills under `skills/` and installs each to `{agent-dir}/skills/oi-<name>/`
> (same layout as [qwencloud/qwencloud-ai](https://github.com/qwencloud/qwencloud-ai)).

Install all (global):

```bash
npx skills add organic-design-ai/oi-skills --all -y -g
```

## Child skills (installed paths)

| Skill | Global example |
|-------|----------------|
| `oi-hue-ui` | `~/.agents/skills/oi-hue-ui/SKILL.md` |
| `oi-awesome-ui` | `~/.agents/skills/oi-awesome-ui/SKILL.md` |
| `oi-taste-ui` | `~/.agents/skills/oi-taste-ui/SKILL.md` |
| `oi-nothing-ui` | `~/.agents/skills/oi-nothing-ui/SKILL.md` |
| `oi-pro-ui` | `~/.agents/skills/oi-pro-ui/SKILL.md` |
| `oi-stitch-ui` | `~/.agents/skills/oi-stitch-ui/SKILL.md` |
| `oi-video-crop` | `~/.agents/skills/oi-video-crop/SKILL.md` |
| `oi-video-to-gif` | `~/.agents/skills/oi-video-to-gif/SKILL.md` |
| `oi-images-to-gif` | `~/.agents/skills/oi-images-to-gif/SKILL.md` |
| `oi-html-ppt` | `~/.agents/skills/oi-html-ppt/SKILL.md` |
| `oi-guizang-ppt` | `~/.agents/skills/oi-guizang-ppt/SKILL.md` |
| `oi-text-effect` | `~/.agents/skills/oi-text-effect/SKILL.md` |

**Triggers:** `oi-skills`, `Oi Skills`, `设计技能`, or vague design/media task — infer the child skill from intent (see [AGENTS.snippet.md](../templates/AGENTS.snippet.md)).

**Do not use for:** tasks that already name a child skill — open that skill's `SKILL.md` directly.
