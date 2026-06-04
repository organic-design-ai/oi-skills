# Repository structure

```
oi-skills/                          # git repo
├── LICENSE                             # MIT — Alibaba Cloud Design
├── README.md                           # 安装与使用说明
├── SKILL.md                            # 包入口（npx skills add 发现用）
├── scripts/
│   ├── README.md                       # 脚本目录说明（与 skills/*/scripts 区分）
│   ├── install.sh                      # 安装入口（转发 install-to-agent.sh）
│   ├── install-to-agent.sh             # 交互安装（默认 ~/.agents/skills）
│   ├── list-skills.sh                  # 列出仓库内 Skill
│   └── lib/ui.sh                       # Bash 共享库（install/list source）
├── docs/
│   ├── structure.md, contributing-skills.md, …
│   ├── templates/                      # 模板（含 USAGE.snippet.md）
│   └── package/SKILL.md                # → installed as package entry
└── skills/
    ├── page/
    │   ├── oi-hue-ui/                      # SKILL.md + skill.yaml + styles/references|examples/
    │   ├── oi-awesome-ui/                   # SKILL.md + skill.yaml + styles/
    │   ├── oi-taste-ui/                     # SKILL.md + skill.yaml + styles/
    │   ├── oi-nothing-ui/                   # SKILL.md + skill.yaml + styles/
    │   ├── oi-pro-ui/                       # SKILL.md + skill.yaml + scripts/ + data/
    │   └── oi-stitch-ui/                    # SKILL.md + skill.yaml + styles/
    ├── widget/
    │   ├── oi-video-crop/                   # SKILL.md + skill.yaml + scripts/
    │   ├── oi-video-to-gif/                 # SKILL.md + skill.yaml + scripts/
    │   └── oi-images-to-gif/                # SKILL.md + skill.yaml + scripts/
    ├── ppt/
    │   ├── oi-html-ppt/                     # SKILL.md + skill.yaml + assets/ templates/
    │   └── oi-guizang-ppt/                  # SKILL.md + skill.yaml + assets/ references/
    └── animation/
        └── oi-text-effect/                  # SKILL.md + skill.yaml + references/ + examples/
```

Installed (default `.agents` example):

```
~/.agents/skills/oi-skills/
├── SKILL.md                            # package: pick a child skill
├── page/
│   ├── oi-hue-ui/
│   │   ├── SKILL.md
│   │   ├── DESIGN.md
│   │   └── styles/
│   │       ├── references/
│   │       └── examples/
│   ├── oi-awesome-ui/
│   │   ├── SKILL.md
│   │   └── styles/
│   ├── oi-taste-ui/
│   │   ├── SKILL.md
│   │   └── styles/
│   ├── oi-nothing-ui/
│   │   ├── SKILL.md
│   │   └── styles/
│   ├── oi-pro-ui/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── data/
│   └── oi-stitch-ui/
│       ├── SKILL.md
│       └── styles/
├── widget/
│   ├── oi-video-crop/
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── oi-video-to-gif/
│   │   ├── SKILL.md
│   │   └── scripts/
│   └── oi-images-to-gif/
│       ├── SKILL.md
│       └── scripts/
├── ppt/
│   ├── oi-html-ppt/
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   ├── templates/
│   │   └── scripts/
│   └── oi-guizang-ppt/
│       ├── SKILL.md
│       ├── assets/
│       └── references/
└── animation/
    └── oi-text-effect/
        ├── SKILL.md
        ├── references/
        └── examples/
```

- **Not flat** (`~/.agents/skills/oi-video-crop/`) — whole repo lives under **`oi-skills/`**.
- **`<pkg-dir>`** = `~/.agents/skills/oi-skills` (or `~/.cursor/skills/oi-skills`, etc.)
- Child scripts = `<pkg-dir>/widget/oi-video-crop/scripts/...`
- **Author**: default `Alibaba Cloud Design` in `skill.yaml` + `SKILL.md`; override only when explicitly credited to someone else (see [contributing-skills.md](./contributing-skills.md)).
- **Usage**: each `SKILL.md` includes `## Usage` (agent-facing prompt for `usage` / `怎么用`); format in [templates/USAGE.snippet.md](./templates/USAGE.snippet.md).
- **Scripts vs docs**: 仓库根 `docs/` = 包级文档与模板；`scripts/lib/` = 安装脚本 Bash 库；`skills/*/scripts/` = 各 Skill 运行时。Skill 内供 Agent 按需加载的深文档用 **`references/`**（如 `animation/oi-text-effect/references/`、`ppt/oi-html-ppt/references/`），不要用 `docs/` 以免与仓库根混淆。

## Install

```bash
# Recommended (GitHub)
npx skills add organic-design-ai/oi-skills --all -y -g
~/.agents/skills/oi-skills/scripts/install-to-agent.sh --all -y -g

# Local clone
./scripts/list-skills.sh
./scripts/install-to-agent.sh --all -y -g   # non-interactive / CI
./scripts/install-to-agent.sh                    # TTY: pick target → confirm
```

Other targets: `./scripts/install-to-agent.sh cursor --global -y`
