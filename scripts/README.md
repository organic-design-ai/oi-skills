# Repository scripts

`oi-skills/scripts/` — **repo install tooling only**. Per-skill runtimes live under `skills/<category>/<name>/scripts/` (installed to agents).

**Package version:** edit repo-root [`VERSION`](../VERSION) (one line, semver without `v` prefix). `scripts/lib/ui.sh` reads it for the install/list banner.

| Script | Purpose |
|--------|---------|
| `install.sh` | Thin entry point (forwards to `install-to-agent.sh`) |
| `install-to-agent.sh` | Install package to `~/.agents/skills` (or `.cursor` / `.qoder` / `.claude`) |
| `list-skills.sh` | List skills in this repository |
| `lib/ui.sh` | Bash UI helpers (`source`d by the scripts above) |

## Flags (`install-to-agent.sh` / `install.sh`)

| Flag | Effect |
|------|--------|
| `--all` | Preset: target **`.agents`**, **`--global`**, all child skills, **`-y`** |
| `-y`, `--yes` | Skip path confirmation |
| `--args …` | Parse following tokens as flags (CI / wrapper forwarding) |
| `--skill NAME` | Install one child skill only |
| `--project` | Install under current project’s agent dir |

Environment variables: `OI_SKILLS_AGENT`, `OI_SKILLS_YES`.

## npx skills add workflow

```bash
npx skills add organic-design-ai/oi-skills --all -y -g
~/.agents/skills/oi-skills/scripts/install-to-agent.sh --all -y -g
```

The second command flattens `skills/<category>/oi-*` into `<pkg-dir>/<category>/oi-*` for agent path conventions.

New skills: copy [docs/templates/new-skill/](../docs/templates/new-skill/). Update [docs/templates/AGENTS.snippet.md](../docs/templates/AGENTS.snippet.md) by hand when adding a top-level skill (Claude Code registration).
