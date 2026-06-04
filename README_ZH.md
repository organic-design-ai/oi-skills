<p align="left">
  <img src="Logo.png" width="128" alt="Oi" />
</p>


# Oi Skills

**Oi Skills** 是一套由 Alibaba Cloud Design 原创发起的 Skills 设计套件，通过 `/oi-*` 字眼在 Qoder、Claude Code、Cursor 等主流 AI 工具、终端（Terminal）以及 Agent（QoderWork）中安装与唤起使用。Oi Skills 内容由 Alibaba Cloud 设计师持续进行设计与自主开发，并迭代、增加及维护；同时收集行业优秀的开源设计 Skills 进行整理与分类（开源 Skills 版权归属原作者），支持从页面风格、页面动效、体验分析洞察、多模态内容生成到开箱即用的设计小工具等一站式 AI 设计能力包。并通过统一的目录规范、触发词体系、安装脚本、Usage 模板与示例工程，降低团队在跨工具、跨场景协作中的使用门槛，提升设计生产效率与交付一致性。Oi Skills 面向个人创作者与组织团队，提供可复用、可扩展、可持续迭代的 AI 设计基础设施，支持从灵感探索到规模化落地的完整工作流闭环。

整包安装在 `<agent-dir>/skills/oi-skills/`，内含 **page**（`oi-hue-ui`、`oi-awesome-ui`、`oi-taste-ui`、`oi-nothing-ui`、`oi-pro-ui`、`oi-stitch-ui`）、**widget**（`oi-video-crop`、`oi-video-to-gif`、`oi-images-to-gif`）、**ppt**（`oi-html-ppt`、`oi-guizang-ppt`）与 **animation**（`oi-text-effect`）。目录与约定见 [docs/structure.md](./docs/structure.md)。

**License:** [MIT](./LICENSE)（仓库整体）
**Third-party notice:** 仓库中引用/改编的第三方内容，其版权与商标归原作者或权利人所有，具体以对应原项目仓库许可证为准。

## 快速安装（推荐）

一键安装：

```bash
npx skills add organic-design-ai/oi-skills --all -y -g
```

## 本地安装 (Dev)

```bash
./scripts/install-to-agent.sh --args --all -y -g
```

```bash
git clone git@github.com:organic-design-ai/oi-skills.git
cd oi-skills
chmod +x scripts/*.sh
./scripts/install-to-agent.sh --all -y -g
```

交互式安装（选择 `.agents` / `.cursor` / `.qoder` / `.claude`）：

```bash
./scripts/install-to-agent.sh
./scripts/install-to-agent.sh cursor --global -y
./scripts/list-skills.sh
```

| 目标 | Skills安装后用户目录示例 |
|------|----------------|
| `.agents`（默认） | `~/.agents/skills/oi-skills/` |
| `.cursor` | `~/.cursor/skills/oi-skills/` |
| `.qoder` | `~/.qoder/skills/oi-skills/` |
| `.claude` | `~/.claude/skills/oi-skills/` |

安装参数、环境变量、单 Skill 调试见 [scripts/README.md](./scripts/README.md) 与 `install-to-agent.sh --help`。

## 本地开发环境（Dev）

在本仓库根目录开发、调试 Skill 时，安装器会从**当前工作副本** rsync 到 Agent 目录（不经过 GitHub）。修改 `skills/**/SKILL.md` 后需重新执行安装命令，Agent 才会读到最新内容。

```bash
cd /path/to/oi-skills    # 本机 clone 路径
chmod +x scripts/*.sh

# 同步全部子 Skill（默认 ~/.agents/skills/oi-skills/）
./scripts/install-to-agent.sh --all -y -g

# Cursor IDE（~/.cursor/skills/oi-skills/）
./scripts/install-to-agent.sh cursor --global -y

# 仅安装/更新一个子 Skill
./scripts/install-to-agent.sh --skill oi-text-effect -y

# 核对仓库内 Skill 清单
./scripts/list-skills.sh
```

说明：

- 与上文「本地 clone 安装」区别：dev 面向**已在仓库内改代码**的贡献者；每次改 Skill 后重跑 `./scripts/install-to-agent.sh` 即可同步。
- 仅对当前 Git 项目生效：在项目根目录执行 `./scripts/install-to-agent.sh --project -y`（安装到 `./.cursor/skills/oi-skills/` 等，视 TARGET 而定）。
- 非交互 / CI：`OI_SKILLS_AGENT=cursor OI_SKILLS_YES=1 ./scripts/install-to-agent.sh --global`

## 使用

1. 新开 Agent 对话（Qoder：`/skills reload`）。
2. 输入 `/` 选 **oi-skills**（包菜单），或直接选子 Skill / 自然语言描述任务。
3. 各 Skill 的 `skill.yaml` 含触发词；问 `usage` / `怎么用` 时 Agent 会读对应 `SKILL.md` 的 **Usage** 小节。

**Claude Code**：复制 Skill 后建议在项目 `CLAUDE.md` / `AGENTS.md` 追加 [docs/templates/AGENTS.snippet.md](./docs/templates/AGENTS.snippet.md) 中的 `<!-- OI_SKILLS -->` 段。

## 依赖

| 范围 | 要求 |
|------|------|
| `oi-pro-ui` | Python 3.9+ |
| `oi-stitch-ui`（部分子风格） | Python 3.9+ / Node.js |
| `oi-video-crop`、`oi-video-to-gif`、`oi-images-to-gif` | Python 3.9+、ffmpeg/ffprobe（可用各 Skill 的 `check_env.py --install`） |

## 作者与来源清单

### Alibaba Cloud Design Skills

| Oi Skill | 作者 |
|----------|------|
| `oi-video-crop` | Alibaba Cloud Design 原创 |
| `oi-video-to-gif` | Alibaba Cloud Design 原创 |
| `oi-images-to-gif` | Alibaba Cloud Design 原创 |

### 开源 Skills 来源（附原作者）

开源 Skills 来源与版权归原作者，本仓库内为集成整理版本

| Oi Skill | 原作者项目 |
|----------|------------------|----------|
| `oi-hue-ui` | [dominikmartn/hue](https://github.com/dominikmartn/hue) |
| `oi-guizang-ppt` | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) |
| `oi-html-ppt` | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) |
| `oi-nothing-ui` | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) |
| `oi-awesome-ui` | [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) |
| `oi-pro-ui` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| `oi-taste-ui` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `oi-stitch-ui` | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) |
| `oi-text-effect` | [Magic UI — Text Animate](https://magicui.design/docs/components/text-animate)、[React Bits](https://reactbits.dev/) |


为避免歧义与潜在风险，特此声明：

- 本项目对第三方项目的引用、改编与收录不代表与原作者存在官方合作、背书或隶属关系。
- 第三方项目名称、商标与相关标识归其各自权利人所有。
- 如有归属信息缺漏或许可证适配问题，请通过 Issue 或 PR 提交，我们将在核实后及时修正。
- 分发与使用本仓库时，请同时遵循本仓库 [MIT](./LICENSE) 与各原作者项目许可证要求（以对应原项目仓库声明为准）。

[English README](./README.md)
