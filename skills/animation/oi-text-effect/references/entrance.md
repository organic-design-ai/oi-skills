# 分段进入类（Entrance）

10 种预设 × 4 种分段方式（text/word/character/line），文本按段逐个进入视口。

## Variants

| Variant | 表现 |
|---------|------|
| `fadeIn` | 透明度 + 轻微上移 20px |
| `blurIn` | 模糊 10px → 0 |
| `blurInUp` | 模糊 + 从下方 20px 上来（最常用于 Hero） |
| `blurInDown` | 模糊 + 从上方 20px 落下 |
| `slideUp` / `slideDown` | 纯位移，无模糊 |
| `slideLeft` / `slideRight` | 水平方向位移 |
| `scaleUp` | 0.5 → 1，弹簧（spring） |
| `scaleDown` | 1.5 → 1，弹簧（spring） |

## 分段方式 `by`

| by | 效果 | 推荐场景 |
|----|------|---------|
| `text` | 整段一起出现 | 单一标语 |
| `word` | 按空格切词 | 英文长句 |
| `character` | 逐字符 | 中文、短标题 |
| `line` | 按 `\n` 切行 | 诗歌、多段落 |

## Recommended defaults

| Prop | Default | 备注 |
|------|---------|------|
| `animation` | `fadeIn` | 最稳的兜底 |
| `by` | `word` | 中文长句建议改 `character` |
| `segDuration` | `700ms` | 每个 segment 自身的动画时长 |
| `staggerStep` | `40ms` | 段与段之间的错开步长 |
| `delay` | `0` | 整体起播前延迟 |
| `as` | `h1` | 标题用 `h1`，正文用 `p` |
| `startOnView` | `true` | 进入视口才播，省 LCP |
| `once` | `false` | 默认循环播放 |
| `easing` | `cubic-bezier(0.22, 1, 0.36, 1)` | 流畅的 ease-out 曲线 |
| `accessible` | `true` | 注入 sr-only 全文，保留可读性 |

## Timing 原理

动画的流畅感来自 **段动画时长（segDuration）** 和 **错开步长（staggerStep）** 的配合：

```
第 0 段：delay + 0×40ms 开始，持续 700ms
第 1 段：delay + 1×40ms 开始，持续 700ms
第 2 段：delay + 2×40ms 开始，持续 700ms
...
```

因为 staggerStep（40ms）远小于 segDuration（700ms），多个段的动画会**大幅重叠**，产生"逐渐浮现、波浪涌入"的视觉效果。如果 step 太大（如 200ms+），段之间就会变成"一个播完下一个才开始"的卡顿感。

**调整建议：**
- 想更慢更优雅：增大 `segDuration`（如 900ms-1200ms），保持 `staggerStep` 不变
- 想更快更紧凑：减小 `staggerStep`（如 25ms），保持 `segDuration` 不变
- 想要整体延迟开始：调大 `delay`

## Custom variants（可选）

传 `variants={{ hidden, show, exit }}`，其中 `show` / `exit` 可接 `(i) => ({...})` 拿到段索引做自定义 stagger。

```tsx
<TextAnimate
  by="character"
  variants={{
    hidden: { opacity: 0, y: 30, rotate: 45, scale: 0.5 },
    show: (i: number) => ({
      opacity: 1, y: 0, rotate: 0, scale: 1,
      transition: {
        delay: i * 0.1, duration: 0.4,
        y: { type: "spring", damping: 12, stiffness: 200, mass: 0.8 },
        rotate: { type: "spring", damping: 8, stiffness: 150 },
        scale: { type: "spring", damping: 10, stiffness: 300 },
      },
    }),
    exit: (i: number) => ({
      opacity: 0, y: 30, rotate: 45, scale: 0.5,
      transition: { delay: i * 0.1, duration: 0.4 },
    }),
  }}
>
  Wavy Motion!
</TextAnimate>
```

## React reference

```tsx
import { TextAnimate } from "@/components/ui/text-animate";

<TextAnimate animation="blurInUp" by="character" as="h1" duration={0.6} once>
  Build delightful UIs faster
</TextAnimate>
```

依赖：`pnpm add motion`（v11+）。组件引用 `@/lib/utils` 的 `cn`，如果项目没有，把 `cn(...)` 替换为 `[...].filter(Boolean).join(" ")`。

## Vanilla HTML reference

```html
<h1 data-anim="blurInUp" data-by="character">Hello world</h1>

<style>
  .oi-ta {
    display: inline-block;
    white-space: pre-wrap;
    line-height: 1.4;
  }
  .oi-ta .seg {
    display: inline-block;
    opacity: 0;
    padding-bottom: 0.1em;
    animation-duration: 700ms;
    animation-delay: calc(var(--i, 0) * 40ms);
    animation-fill-mode: both;
    animation-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
    will-change: opacity, transform, filter;
  }
  .oi-ta[data-anim="blurInUp"] .seg { animation-name: oi-blurInUp; }
  @keyframes oi-blurInUp {
    from { opacity:0; filter:blur(10px); transform:translateY(20px); }
    to   { opacity:1; filter:blur(0);    transform:translateY(0); }
  }
</style>
```

**关键参数必须与样板间一致：** `animation-duration: 700ms` + `stagger step: 40ms` + `cubic-bezier(0.22, 1, 0.36, 1)`。这三个值配合才能还原样板间的流畅效果。

## 验证清单

- 进入视口前：文本不可见（`aria-label` 仍可被读屏，`accessible=true`）
- 进入视口后：按选定 `by` 节奏分段播完，不抖动、不跳行
- 中文 / Emoji：用 `by="character"` 时确认 grapheme 切分符合预期
- 移动端：检查 `font-size` 缩放下不会出现行高跳动
- 减弱动效：尊重 `prefers-reduced-motion`
