# 流光类（Shimmer）

中性色渐变高光无限循环横扫文字，类似 ChatGPT/Cursor 的加载/思考状态。纯 CSS 实现，无限循环。不使用 `by` 分段。

## Props

| Prop | Type | Default | 说明 |
|------|------|---------|------|
| `children` | `string` | — | 文本内容 |
| `duration` | `number` | `2` | 一次流光扫过时长（秒） |
| `baseColor` | `string` | `#6b7280` | 基底色（中灰） |
| `highlightColor` | `string` | `#e5e7eb` | 高光色（浅灰） |
| `as` | `ElementType` | `p` | 渲染标签 |
| `className` | `string` | — | 容器额外类名 |

## React reference

```tsx
import { TextShimmer } from "@/components/ui/text-shimmer";

{/* 基础 — 中性色加载流光 */}
<TextShimmer className="text-4xl font-bold" as="h1">
  Thinking about your request...
</TextShimmer>

{/* 自定义颜色 — 深色基底 */}
<TextShimmer
  className="text-2xl font-semibold"
  baseColor="#374151"
  highlightColor="#d1d5db"
  duration={2.5}
>
  Generating response...
</TextShimmer>
```

无外部动画依赖（纯 CSS animation）。

## Vanilla HTML reference

```html
<h1 data-anim="shimmer" style="--ta-duration:2000ms">Thinking about your request...</h1>

<style>
  [data-anim="shimmer"] {
    line-height: 1.4;
    padding-bottom: 0.1em;
    background: linear-gradient(90deg,
      var(--shimmer-base, #6b7280) 0%, var(--shimmer-base, #6b7280) 35%,
      var(--shimmer-hi, #e5e7eb) 50%,
      var(--shimmer-base, #6b7280) 65%, var(--shimmer-base, #6b7280) 100%);
    background-size: 200% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: oi-shimmer var(--ta-duration, 2000ms) linear infinite;
  }
  @keyframes oi-shimmer {
    from { background-position: 100% 0; }
    to   { background-position: -100% 0; }
  }
</style>
```

自定义颜色：通过 CSS 变量 `--shimmer-base` 和 `--shimmer-hi` 覆盖。
