# Adding a skill

Each skill is **self-contained** under `skills/<category>/oi-<name>/` (all installable skills use the `oi-` prefix):

```
skills/<category>/oi-<name>/
├── SKILL.md       # Required — agent instructions (installed)
├── skill.yaml     # Triggers, deps — repo only, not installed
├── references/    # Optional — deep docs / catalogs (load on demand; not repo-root docs/)
├── examples/      # Optional — demos, components, showcase HTML
├── scripts/       # Optional — runtime helpers for this skill only
└── assets/        # Optional — static assets (ppt, etc.)
```

Do **not** put skill-internal agent docs in a folder named `docs/` — that name is reserved for the **repository** root (`oi-skills/docs/`). Use `references/` instead (see `oi-html-ppt`, `oi-text-effect`).

Scaffold: copy [templates/new-skill/](./templates/new-skill/).

## Usage section (required)

Every `SKILL.md` must include a **`## Usage`** section near the top (after title/intro). Agents read it when the user asks `usage`, `怎么用`, `help`, or invokes the skill without a concrete task — **reply from Usage**, then ask for the task.

Template: [templates/USAGE.snippet.md](./templates/USAGE.snippet.md). Copy the Usage block from [templates/new-skill/SKILL.md](./templates/new-skill/SKILL.md) when scaffolding; edit per skill.

In `skill.yaml`, add optional `usage` / `usage_zh` one-liners aligned with the Usage section (repo metadata only).

## Author

Unless a skill **explicitly** names another author in both `skill.yaml` and `SKILL.md`, use the repository default:

**`Alibaba Cloud Design`**

```yaml
# skill.yaml (repo metadata, not installed)
author: Alibaba Cloud Design
```

```markdown
# SKILL.md (installed — include under the title)
**Author:** Alibaba Cloud Design
```

Override only when a specific contributor owns the skill (e.g. `author: Haihang` / `author: Shicheng`).

## Steps

1. Create `skills/<category>/oi-<name>/` with `SKILL.md` + `skill.yaml` (`name:` in frontmatter = folder name, e.g. `oi-my-skill`).
2. `./scripts/list-skills.sh` — verify it appears in the manifest.
3. `./scripts/install-to-agent.sh --all -y -g` — default `~/.agents/skills`, or pick `.cursor` / `.qoder` / `.claude` in the TTY menu.
4. If you use Claude Code registration, add a row to [templates/AGENTS.snippet.md](./templates/AGENTS.snippet.md) (`<!-- OI_SKILLS -->` block).
5. Update root [README.md](../README.md) skill table if the skill is user-facing.

Install target: `<agent-dir>/skills/oi-skills/<category>/<name>/` plus package `oi-skills/SKILL.md` (default agent-dir: `.agents`).

Non-interactive install: `OI_SKILLS_AGENT=cursor ./scripts/install-to-agent.sh --global -y` or `./scripts/install-to-agent.sh --args --all -y -g`

## Categories

| Folder | Purpose |
|--------|---------|
| `page/` | Landing pages (reserved) |
| `widget/` | Media / UI utilities |
| `ppt/` | HTML presentation / slide decks |
| `animation/` | Motion / animation workflows |

New category = new folder under `skills/`.
