# Repository structure

```
oi-skills/                          # git repo (no root SKILL.md — see qwencloud layout)
├── LICENSE
├── README.md
├── docs/
│   ├── structure.md, contributing-skills.md, …
│   ├── templates/
│   └── package/SKILL.md                # repo catalog only (not installed)
└── skills/
    ├── page/       # oi-hue-ui, oi-awesome-ui, …
    ├── widget/     # oi-video-crop, …
    ├── ppt/        # oi-html-ppt, oi-guizang-ppt
    └── animation/  # oi-text-effect
```

Installed (global example — **one folder per skill**, like qwencloud):

```
~/.agents/skills/
├── oi-hue-ui/
│   ├── SKILL.md
│   └── styles/
├── oi-video-crop/
│   ├── SKILL.md
│   └── scripts/
├── oi-html-ppt/
│   ├── SKILL.md
│   └── assets/
└── …
```

- **No monorepo copy** — `npx skills add` discovers each `skills/<category>/oi-<name>/SKILL.md` and installs **that folder only** (no README, docs, or repo root).
- **`<skill-dir>`** = `~/.agents/skills/oi-<name>` (or `~/.cursor/skills/oi-<name>`, etc.)
- **Author**: default `Alibaba Cloud Design`; see [contributing-skills.md](./contributing-skills.md).
- **Usage**: each `SKILL.md` includes `## Usage`; format in [templates/USAGE.snippet.md](./templates/USAGE.snippet.md).

## Install

```bash
npx skills add organic-design-ai/oi-skills --all -y -g

cd .. && npx skills add ./oi-skills --all -y -g   # local
```
