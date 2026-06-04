---
name: oi-text-effect
description: >-
  Drop-in text effects for React and vanilla HTML: 17 presets across 7 categories.
  10 entrance (fadeIn, blurIn[Up/Down], slideUp/Down/Left/Right, scaleUp/Down) × 4 split modes;
  1 sweep (colorSweep) with gradient color-band reveal; 1 scramble (hyperText) with character decrypt;
  1 flip (text3dFlip) with per-character 3D rotation; 1 morph (morphingText) with SVG-filter liquid transition;
  1 shimmer with neutral-color gradient sweep; 2 typewriters (textType, textShiftWords) with typing/deleting/looping animation.
  TRIGGER when user asks for text reveal, headline entrance, blur/slide/scale-in text, color sweep,
  gradient reveal, hyper text, scramble text, decrypt text, 3d flip, morphing text, shimmer, loading text,
  typewriter effect, typing animation, 打字机动画, 文字逐字显示, or "magicui text animate".
  NOT for video/GIF.
---
# Oi Text Effect

**Author:** Magic UI, ReactBits, Alibaba Cloud Design

为标题 / 段落 / Hero 文案生成文字动效。包含七大类效果：

- **分段进入类**（entrance）：10 种预设 × 4 种分段方式
- **扫光类**（sweep）：渐变色带横扫文字，支持多色自定义、多文本轮播
- **乱码解密类**（scramble）：字符快速跳动后逐个锁定为正确字符
- **3D 翻转类**（flip）：每个字符独立 3D 旋转，4 方向 × 多种错开方式
- **变形类**（morph）：SVG 滤镜液态变形，多组文本间平滑切换
- **流光类**（shimmer）：中性色渐变高光无限循环扫过文字
- **打字机类**（typewriter）：逐字输入+删除+轮播，支持经典光标打字机与词组轮播下划线打字机

提供 React 组件版（基于 `motion`）与无依赖的纯 HTML/CSS 版。

**Skill path**: `<skill-dir>/`

## File structure

```
oi-text-effect/
├── SKILL.md                      (this file — routing + defaults)
├── references/                   (per-category API & vanilla snippets; load on demand)
│   ├── entrance.md
│   ├── sweep.md
│   ├── scramble.md
│   ├── flip.md
│   ├── morph.md
│   ├── shimmer.md
│   └── typewriter.md
└── examples/
    ├── text-effect-showcase.html (all specimens + playground)
    ├── TextAnimate.jsx … TextType.jsx / TextShiftWords.jsx
    └── react-demo.jsx
```

> Repo root `docs/` is for the **oi-skills** package only. Inside a skill, agent-facing deep docs live under **`references/`** (same convention as `oi-html-ppt`, `oi-guizang-ppt`).

---

## Usage

> **Agent:** If the user asks how to use this skill (`usage`, `怎么用`, `help`, `@oi-text-effect` without a task), **reply with this section** (replace `<skill-dir>` with this skill's install path, e.g. `~/.agents/skills/oi-text-effect`), then ask what they want to accomplish.

**Triggers:** `oi-text-effect`, text effect, text animate, text reveal, blur in text, color sweep, hyper text, scramble text, 3d flip, morphing text, shimmer, typewriter effect, typing animation, 打字机动画, 文字逐字显示, 文字动效, magicui text-animate 等。

**快速开始：**
1. 告诉 agent 你想要什么类型的文字动效（如 “blurInUp”、”colorSweep”、”textType”），agent 会自动生成预览。
2. 不确定选哪个？说 “文字动效” 或 “text effect”，agent 会引导你打开样板页 `text-effect-showcase.html` 挑选。
3. 选定效果后，可以直接生成独立预览 HTML，也可以给已有项目文件添加动效。

**支持的 7 大类效果：**

| 类别 | 效果名 | 说明 |
|------|--------|------|
| 分段进入 | fadeIn, blurIn, blurInUp, blurInDown, slideUp/Down/Left/Right, scaleUp/Down | 10 种预设 × 4 种分段方式 |
| 扫光 | colorSweep | 渐变色带横扫，支持多色、多文本轮播 |
| 乱码解密 | hyperText | 字符跳动后逐个锁定 |
| 3D 翻转 | text3dFlip | 每字符独立 3D 旋转 |
| 变形 | morphingText | SVG 滤镜液态变形 |
| 流光 | shimmer | 中性色渐变高光循环 |
| 打字机 | textType, textShiftWords | 逐字输入+删除+轮播 |

**示例提问：**
- “给我做一个 blurInUp 的标题动画”
- “用 colorSweep 效果做一个渐变扫光标题”
- “做一个打字机效果的 Hero 文案轮播”
- “给 index.html 的 h1 加个 shimmer 动效”

**不适用于：** 视频转 GIF / 视频裁剪（用 `widget/*`）。

---

## Agent Instructions

### 语气与交互风格（强制）

整个交互过程中，使用**友好、有引导感**的语气。像一个热心的设计搭档，而不是冷冰冰的工具。

核心原则：
- 每次回复必须有**清晰的下一步行动指引**（用户不需要猜"接下来该做什么"）
- 遇到问题时给出具体解决方案，不要只报错
- 适当使用鼓励性语言（"这个效果很适合你的场景"、"马上就好"）
- 回复末尾始终告诉用户可以做什么（2-3 个选项）

**话术示例（供参考，不要机械照搬）：**

打开 demo 时：
> 给你打开了效果预览页，里面有 23 种文字动效可以挑选~ 滚动看看哪个最合你心意，选好了告诉我名字就行！

生成预览后：
> 好啦，预览已经在浏览器打开了！看看效果怎么样？
> - 满意的话告诉我，我帮你放进项目里
> - 想微调的话，比如"快一点"、"字符逐个出现"、"换个颜色"，直接说就好
> - 也可以打开 Demo 页的 Playground 自己拖拖参数，调好了把数值告诉我

修改已有文件后：
> 搞定了！刷新一下页面就能看到效果。如果觉得动画太快/太慢，或者想换个样式，随时跟我说~

遇到问题时（如路径报错、依赖缺失）：
> 遇到了一个小问题：{具体问题}。不过没关系，我们可以这样解决：{方案}。要我帮你处理吗？

---

### 帮用户浏览效果（用户未指定效果时）

当用户调用 oi-text-effect 但**未明确指定** effect 类型时（只说"text effect"、"text animate"、"有哪些效果"、"文字动效"、问 usage/help），**优先引导用户打开已配置好的样板 Showcase HTML**，不要直接生成效果。

1. **尝试打开 Demo 文件**（可能成功也可能失败，都没关系）：
   ```bash
   open "<skill-dir>/examples/text-effect-showcase.html"
   ```
   注意：部分 IDE 沙箱环境（如 Cursor）无法调起系统浏览器，这是正常的，不要报错给用户。

2. **无论 open 是否成功，都给用户这段友好引导**（根据实际路径替换 `<skill-dir>`）：

   > 我帮你准备了一个动效样板页，里面有 23 种文字动效可以直接看效果~
   >
   > 请打开这个文件：
   > `<完整路径>/examples/text-effect-showcase.html`
   >
   > 打开方式（任选一种）：
   > - 在 IDE 文件树中找到它，右键 → 在浏览器中打开
   > - 在你自己的终端执行：`open "<完整路径>/examples/text-effect-showcase.html"`
   > - 直接在 Finder / 文件管理器里双击
   >
   > 挑一个你喜欢的，告诉我效果名字（比如 blurInUp、colorSweep、shimmer），我马上帮你做！
   >
   > 或者不想挑也行，说"直接来一个"，我帮你用经典的 Fade In 效果先做个预览~

3. **等用户选定后再继续。** 如果用户说"直接来一个" / "随便给我看一个"，按场景 A 的默认效果（fadeIn）生成预览。

**跳过条件**（直接进入实现）：用户已指定 animation 类型（如 "blurInUp"、"colorSweep"），或已给出完整输入。

---

### 按需加载 reference

确认用户想要的类别后，**只读取对应 reference**（不要全部加载）：

| 用户选择 | 读取文件 |
|---------|---------|
| fadeIn / blurIn / blurInUp / blurInDown / slideUp / slideDown / slideLeft / slideRight / scaleUp / scaleDown | [references/entrance.md](references/entrance.md) |
| colorSweep | [references/sweep.md](references/sweep.md) |
| hyperText | [references/scramble.md](references/scramble.md) |
| text3dFlip | [references/flip.md](references/flip.md) |
| morphingText | [references/morph.md](references/morph.md) |
| shimmer | [references/shimmer.md](references/shimmer.md) |
| textType / textShiftWords / typewriter / 打字机 | [references/typewriter.md](references/typewriter.md) |

---

### 响应规则（强制）— 区分两种场景

用户选定动画类型后，根据场景走不同流程。**不要追问参数，用默认值直接出效果。**

---

#### 场景 A：新建动效（用户未指定目标文件）

用户说了想要什么动画效果，没有指向具体项目文件。目标：**让用户最快看到效果。**

**默认效果**：如果用户没有指定任何 animation 类型但坚持要直接看一个效果，使用 **fadeIn**（No.01 Fade In），参数：`by="word"`, `duration=0.7`, `delay=2`, `once=false`。

**默认文案**：如果用户没有给文案，使用 `Build delightful UIs faster`。

**流程：**
1. 读取对应子文档，用 Recommended defaults + 用户文案（未给则用默认文案）生成一个**独立预览 HTML 文件**（单文件，无外部依赖）。
2. 将文件写入用户当前工作目录（如 `./text-effect-preview.html`）。
3. 尝试 `open` 打开文件（可能因沙箱限制失败，这没关系）。
4. **无论 open 是否成功**，都用友好语气回复，告知文件路径并给出打开方式 + 下一步选项：

   > 预览文件已生成：`./text-effect-preview.html`
   >
   > 打开看看效果吧~ 方式任选：
   > - 在 IDE 文件树中找到它，右键 → 在浏览器中打开
   > - 或在你的终端执行：`open ./text-effect-preview.html`
   >
   > 当前参数：{duration=0.7s, delay=2s, by=word, once=false（循环）}
   >
   > 看完之后你可以：
   > 1. 说"可以"→ 我帮你放进项目文件
   > 2. 说"快一点"/"换成按字符"/"颜色改成紫色" → 我马上调整重新生成
   > 3. 说"给 xxx 文件加上" → 我直接改你的目标文件

5. 用户确认满意后，询问放进哪个文件 / 用什么技术栈，帮用户集成。

**预览 HTML 模板要求：**
- 单文件，可直接浏览器打开
- **白色背景**，文字水平垂直居中，大号字体（`2.5rem`+）
- 包含动画效果的完整 CSS + JS（从子文档 Vanilla HTML reference 获取）
- 页面**底部**小字浅灰色（`#999`）显示当前参数值（animation / by / duration / delay / once），方便用户对照
- 用户明确指定其他背景样式时才改，否则始终白底
- **防止字母裁切（必须）：** 所有文字动效元素必须设置 `line-height: 1.4` 以上 + `padding-bottom: 0.1em`。`display: inline-block` + `background-clip: text` 等技术会导致字母下延部分（g/y/p/q/j 的尾巴）被裁切，这两个属性能避免此问题。适用于所有效果类型，不仅限于 colorSweep。

---

#### 场景 B：给已有文件加动效（用户指定了目标文件）

用户说"给 xxx 文件的标题加个动效"或在已有项目上下文中工作。

**流程：**
1. 读取目标文件，找到用户指定的文案位置。
2. 读取对应子文档，用 Recommended defaults 直接修改文件，加入动画代码。
3. 用友好语气告知用户已改好，提醒刷新预览，并说明可以调什么。
4. 用户要求修改 → 只改对应参数，更新文件。

---

#### 场景判断规则

| 信号 | 场景 |
|------|------|
| 用户提到具体文件名/路径 | B |
| 当前对话上下文有明确的项目文件在编辑 | B |
| 用户说"做一个"、"生成"、"试试"、无具体文件指向 | A |

**最低必要信息（只需 1-2 项）：**
- animation 类型（已通过选择/触发词确定）
- 目标文件（场景 B）或不需要（场景 A 自动生成预览）

技术栈在场景 B 中从文件后缀自动判断。场景 A 始终生成 HTML 预览。**不要发提问模板、不要追问参数列表。**

---

## Quick start（给 agent 的决策参考）

确定 animation 后，按子文档的 Recommended defaults 表直接出码。各类别的智能默认：

| 类别 | 默认关键参数 |
|------|-------------|
| entrance | `by="word"`, `segDuration=700ms`, `staggerStep=40ms`, `easing=cubic-bezier(0.22,1,0.36,1)`, `once=false` |
| colorSweep | 5 色默认色板, `duration=2s`, `once=false` |
| hyperText | `characterSet=A-Z`, `animateOnHover=true`, `duration=800ms` |
| text3dFlip | `rotateDirection="top"`, `staggerFrom="first"` |
| morphingText | `morphTime=1.5`, `cooldownTime=0.5` |
| shimmer | `duration=2s`, 中灰基底 + 浅灰高光 |
| typewriter | textType: `typingSpeed=50`, `deletingSpeed=30`, `pauseDuration=2000`, `loop=true`, `showCursor=true`; textShiftWords: `typeIntervalMs=70`, `deletingIntervalMs=70`, `pauseMs=600`, `loop=true`, `showUnderline=true` |

**全局默认原则：**
- **所有效果的默认参数必须与样板间（`text-effect-showcase.html`）中对应 specimen 卡片的参数完全一致。** 用户未自行指定的参数，一律使用样板间的值，不得自行调整。用户明确要求修改参数时才可偏离。
- `once=false`（循环播放），除非用户明确要求只播一次
- entrance 类的核心三参数必须与样板间一致：`segDuration=700ms` + `staggerStep=40ms` + `cubic-bezier(0.22, 1, 0.36, 1)`，这三个配合才有流畅的波浪涌入感
- 生成 HTML 预览时，直接从样板间 demo 的 CSS 复制时序参数，不要自行计算或简化

---

## Demo & Examples

- `<skill-dir>/examples/text-effect-showcase.html` — 23 种效果 + Playground 一站式预览
- `<skill-dir>/examples/TextAnimate.jsx` — 分段进入 React 组件
- `<skill-dir>/examples/DiaTextReveal.jsx` — 扫光 React 组件
- `<skill-dir>/examples/HyperText.jsx` — 乱码解密 React 组件
- `<skill-dir>/examples/Text3DFlip.jsx` — 3D 翻转 React 组件
- `<skill-dir>/examples/MorphingText.jsx` — 变形 React 组件
- `<skill-dir>/examples/TextShimmer.jsx` — 流光 React 组件
- `<skill-dir>/examples/TextType.jsx` — 打字机 React 组件
- `<skill-dir>/examples/TextShiftWords.jsx` — 词组轮播打字机 React 组件
- `<skill-dir>/examples/react-demo.jsx` — 全部变体使用示例
