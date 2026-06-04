<p align="left">
  <img src="Logo.png" width="128" alt="Oi" />
</p>

# Oi Skills

**Oi Skills** 是一套由 Alibaba Cloud Design 原创发起的 Skills 设计套件，通过 `/oi-*` 在 Qoder、Claude Code、Cursor、终端与各类 Agent 中安装与唤起。内容由 Alibaba Cloud 设计师持续设计与维护，并整理行业优秀的开源设计 Skills（开源部分版权归属原作者），覆盖页面风格、动效、体验洞察、多模态生成与设计小工具等能力。

## 安装

在目标项目目录执行。

### 1. 整仓安装

```bash
npx skills add organic-design-ai/oi-skills --all -y
```

给具体的工具安装:

```bash
npx skills add organic-design-ai/oi-skills --all -y -a claude-code
npx skills add organic-design-ai/oi-skills --all -y -a cursor
npx skills add organic-design-ai/oi-skills --all -y -a qoder
```

### 2. 单个 Skill 安装（以 `oi-qwencloud-ui` 为例）

```bash
npx skills add organic-design-ai/oi-skills --skill oi-qwencloud-ui -y
npx skills add organic-design-ai/oi-skills --skill oi-qwencloud-ui -y -a claude-code
npx skills add organic-design-ai/oi-skills --skill oi-qwencloud-ui -y -a cursor
npx skills add organic-design-ai/oi-skills --skill oi-qwencloud-ui -y -a qoder
```

将 `oi-qwencloud-ui` 换成其他 `oi-*` skill 名即可。

### 3. 本地开发安装

```bash
npx skills add ../oi-skills --all -y -g
```

## 作者与贡献

### Alibaba Cloud Design（原创）

| Oi Skill | 原创作者 |
|----------|------|
| `oi-qwencloud-ui` | Alibaba Cloud Design |
| `oi-nameslink-ui` | Alibaba Cloud Design |
| `oi-video-crop` | Alibaba Cloud Design |
| `oi-video-to-gif` | Alibaba Cloud Design |
| `oi-images-to-gif` | Alibaba Cloud Design |

### 开源集成

| Oi Skill | 开源原作者项目 |
|----------|------------|
| `oi-hue-ui` | [dominikmartn/hue](https://github.com/dominikmartn/hue) |
| `oi-guizang-ppt` | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) |
| `oi-html-ppt` | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) |
| `oi-nothing-ui` | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) |
| `oi-awesome-ui` | [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) |
| `oi-pro-ui` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| `oi-taste-ui` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `oi-stitch-ui` | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) |
| `oi-text-effect` | [Magic UI — Text Animate](https://magicui.design/docs/components/text-animate)、[React Bits](https://reactbits.dev/) |

[English README](./README.md)
