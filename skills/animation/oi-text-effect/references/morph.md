# 变形类（Morphing Text）

通过 SVG 滤镜（blur + threshold）实现文字间液态变形过渡，在多组文本间自动循环切换。适合 Hero 标题、品牌展示、加载状态。不使用 `by` 分段。

## Props

| Prop | Type | Default | 说明 |
|------|------|---------|------|
| `texts` | `string[]` | `[]` | 文本数组，至少 2 项 |
| `morphTime` | `number` | `1.5` | 单次变形时长（秒） |
| `cooldownTime` | `number` | `0.5` | 两次变形间的停顿（秒） |
| `className` | `string` | — | 容器额外类名 |

## React reference

```tsx
import { MorphingText } from "@/components/ui/morphing-text";

{/* 基础 — 自动在多组文字间液态变形 */}
<MorphingText texts={["Hello", "Morphing", "Text", "Animation"]} />

{/* 自定义时长 */}
<MorphingText
  texts={["Design", "Build", "Ship", "Scale"]}
  morphTime={2}
  cooldownTime={1}
/>
```

无外部动画依赖（纯 rAF + SVG filter）。

## Vanilla HTML reference

```html
<h1 data-anim="morphingText" data-texts="Hello,Morphing,Text,Animation">Hello</h1>
```

通过 `data-texts` 传入逗号分隔的文本列表。JS 运行时自动构建双层结构 + SVG 滤镜，实现文字间液态变形效果。
