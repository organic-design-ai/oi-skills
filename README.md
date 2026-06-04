<p align="left">
  <img src="Logo.png" width="128" alt="Oi" />
</p>


# Oi Skills

**Oi Skills** is an AI design skill suite originated by Alibaba Cloud Design. Install and invoke it in Qoder, Claude Code, Cursor, terminals, and agents (including QoderWork) via `/oi-*` triggers. The collection is designed and maintained by Alibaba Cloud designers, with curated open-source design skills (copyright remains with original authors). It covers page styles, motion, UX insights, multimodal generation, and ready-to-use design widgets—unified directory layout, triggers, install scripts, Usage templates, and sample projects to lower cross-tool friction and improve delivery consistency. Oi Skills supports individuals and teams with reusable, extensible AI design infrastructure from exploration to production.

The package installs to `<agent-dir>/skills/oi-skills/` and includes **page** (`oi-hue-ui`, `oi-awesome-ui`, `oi-taste-ui`, `oi-nothing-ui`, `oi-pro-ui`, `oi-stitch-ui`), **widget** (`oi-video-crop`, `oi-video-to-gif`, `oi-images-to-gif`), **ppt** (`oi-html-ppt`, `oi-guizang-ppt`), and **animation** (`oi-text-effect`). See [docs/structure.md](./docs/structure.md) for layout and conventions.

**License:** [MIT](./LICENSE) (repository-wide)  
**Third-party notice:** Adapted third-party content remains under its original authors’ licenses and trademarks.

## Quick install (recommended)

One-line install:

```bash
npx skills add organic-design-ai/oi-skills --all -y -g
```

## Local install (from clone)

```bash
./scripts/install-to-agent.sh --args --all -y -g
```

```bash
git clone git@github.com:organic-design-ai/oi-skills.git
cd oi-skills
chmod +x scripts/*.sh
./scripts/install-to-agent.sh --all -y -g
```

Interactive install (pick `.agents` / `.cursor` / `.qoder` / `.claude`):

```bash
./scripts/install-to-agent.sh
./scripts/install-to-agent.sh cursor --global -y
./scripts/list-skills.sh
```

| Target | Example install path |
|--------|------------------------|
| `.agents` (default) | `~/.agents/skills/oi-skills/` |
| `.cursor` | `~/.cursor/skills/oi-skills/` |
| `.qoder` | `~/.qoder/skills/oi-skills/` |
| `.claude` | `~/.claude/skills/oi-skills/` |

Flags, env vars, and single-skill debugging: [scripts/README.md](./scripts/README.md) and `install-to-agent.sh --help`.

## Local development

While developing in this repo, the installer rsyncs from your **working copy** (not GitHub). Re-run install after editing `skills/**/SKILL.md` so agents pick up changes.

```bash
cd /path/to/oi-skills
chmod +x scripts/*.sh

# Sync all child skills (default ~/.agents/skills/oi-skills/)
./scripts/install-to-agent.sh --all -y -g

# Cursor IDE (~/.cursor/skills/oi-skills/)
./scripts/install-to-agent.sh cursor --global -y

# Install or update one child skill
./scripts/install-to-agent.sh --skill oi-text-effect -y

# List skills in the repo
./scripts/list-skills.sh
```

Notes:

- **Dev vs clone install:** dev is for contributors editing the repo; re-run `./scripts/install-to-agent.sh` after each skill change.
- **Project-only:** from repo root, `./scripts/install-to-agent.sh --project -y` installs under `./.cursor/skills/oi-skills/` (path depends on target).
- **Non-interactive / CI:** `OI_SKILLS_AGENT=cursor OI_SKILLS_YES=1 ./scripts/install-to-agent.sh --global`

## Usage

1. Start a new agent chat (Qoder: `/skills reload`).
2. Type `/` and choose **oi-skills** (package menu), or pick a child skill / describe the task in natural language.
3. Each skill’s `skill.yaml` defines triggers; ask `usage` and the agent reads the **Usage** section in `SKILL.md`.

**Claude Code:** after copying skills, append the `<!-- OI_SKILLS -->` block from [docs/templates/AGENTS.snippet.md](./docs/templates/AGENTS.snippet.md) to project `CLAUDE.md` / `AGENTS.md`.

## Dependencies

| Scope | Requirements |
|-------|----------------|
| `oi-pro-ui` | Python 3.9+ |
| `oi-stitch-ui` (some sub-styles) | Python 3.9+ / Node.js |
| `oi-video-crop`, `oi-video-to-gif`, `oi-images-to-gif` | Python 3.9+, ffmpeg/ffprobe (per-skill `check_env.py --install`) |

## Authors and upstream credits

### Alibaba Cloud Design (original)

| Oi Skill | Author |
|----------|--------|
| `oi-video-crop` | Alibaba Cloud Design |
| `oi-video-to-gif` | Alibaba Cloud Design |
| `oi-images-to-gif` | Alibaba Cloud Design |

### Open-source integrations

Integrated and adapted in this repo; copyright belongs to upstream projects.

| Oi Skill | Upstream |
|----------|----------|
| `oi-hue-ui` | [dominikmartn/hue](https://github.com/dominikmartn/hue) |
| `oi-guizang-ppt` | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) |
| `oi-html-ppt` | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) |
| `oi-nothing-ui` | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) |
| `oi-awesome-ui` | [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) |
| `oi-pro-ui` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| `oi-taste-ui` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `oi-stitch-ui` | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) |
| `oi-text-effect` | [Magic UI — Text Animate](https://magicui.design/docs/components/text-animate), [React Bits](https://reactbits.dev/) |

### Disclaimer

- References and adaptations do not imply official partnership, endorsement, or affiliation with upstream authors.
- Third-party names and trademarks belong to their respective owners.
- Report attribution or license issues via Issue or PR; we will correct after review.
- When redistributing, comply with this repo’s [MIT](./LICENSE) and each upstream project’s license.

[中文 README](./README_ZH.md)
