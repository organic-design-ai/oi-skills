# 乱码解密类（Scramble / HyperText）

每个字符快速随机跳动（像黑客解密），逐个"锁定"为正确字符。适合科技感标题、加载状态、hover 交互。不使用 `by` 分段。

## Props

| Prop | Type | Default | 说明 |
|------|------|---------|------|
| `children` | `string` | — | 文本内容 |
| `characterSet` | `string[]` | `A-Z` | 乱码字符集，可换数字/符号/中文 |
| `duration` | `number` | `800` | 解密总时长（ms） |
| `delay` | `number` | `2000` | 起播前延迟（ms） |
| `animateOnHover` | `boolean` | `true` | hover 时重新触发 |
| `startOnView` | `boolean` | `false` | 进入视口自动触发 |
| `mode` | `"scramble" \| "cursor"` | `"scramble"` | cursor 模式：从左到右逐字显示+乱码光标 |
| `as` | `ElementType` | `div` | 渲染标签 |
| `className` | `string` | — | 容器类名 |

## React reference

```tsx
import { HyperText } from "@/components/ui/hyper-text";

{/* Hover 触发（默认） */}
<HyperText className="text-4xl font-bold">HOVER ME!</HyperText>

{/* 进入视口触发，数字字符集 */}
<HyperText
  startOnView
  animateOnHover={false}
  characterSet={"0123456789".split("")}
  duration={1000}
>
  DECRYPTING...
</HyperText>

{/* 符号字符集 */}
<HyperText characterSet={"!@#$%^&*()_+-=[]{}|;:',.<>?".split("")}>
  SECRET CODE
</HyperText>

{/* Cursor 模式 — 从左到右逐字打出+乱码光标 */}
<HyperText mode="cursor" duration={1200} startOnView animateOnHover={false}>
  The quick brown fox jumps.
</HyperText>
```

无外部动画依赖。

## Vanilla HTML reference

```html
<h1 data-anim="hyperText" data-duration="800">HOVER ME!</h1>
<h1 data-anim="hyperText" data-duration="800" data-charset="digits">DECRYPTING...</h1>
```

通过 `data-charset` 属性切换字符集：`alpha`(A-Z) / `digits`(0-9) / `symbols`(!@#$...)。JS 运行时自动处理动画。
