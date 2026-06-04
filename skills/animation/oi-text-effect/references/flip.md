# 3D 翻转类（Text 3D Flip）

每个字符独立进行 3D 旋转（hover 触发），支持 top/right/bottom/left 四个方向，可从 first/last/center/random 错开产生涟漪波浪感。适合品牌标题、交互式 heading。不使用 `by` 分段。

## Props

| Prop | Type | Default | 说明 |
|------|------|---------|------|
| `children` | `string` | — | 文本内容 |
| `rotateDirection` | `"top" \| "right" \| "bottom" \| "left"` | `"top"` | 翻转方向 |
| `staggerFrom` | `"first" \| "last" \| "center" \| "random" \| number` | `"first"` | 错开起点 |
| `staggerDuration` | `number` | `0.03` | 每字符错开间隔（秒），小值产生涟漪波浪感 |
| `transition` | `object` | `{ type: "spring", damping: 25, stiffness: 160 }` | Motion 过渡配置（低阻尼产生 bounce） |
| `as` | `ElementType` | `p` | 渲染标签 |
| `className` | `string` | — | 容器类名 |
| `textClassName` | `string` | — | 翻转前文字类名 |
| `flipTextClassName` | `string` | — | 翻转后文字类名 |

## React reference

```tsx
import { Text3DFlip } from "@/components/ui/text-3d-flip";

{/* 基础 — hover 从上方翻转 */}
<Text3DFlip
  className="text-4xl font-bold"
  textClassName="text-foreground"
  flipTextClassName="text-primary"
  rotateDirection="top"
>
  Stay hungry, stay foolish
</Text3DFlip>

{/* 从中间向两边错开 */}
<Text3DFlip
  className="text-4xl font-bold"
  rotateDirection="top"
  staggerFrom="center"
  staggerDuration={0.03}
>
  Design for failure
</Text3DFlip>

{/* 向右翻，stagger 从末尾 */}
<Text3DFlip
  className="text-4xl font-bold"
  rotateDirection="right"
  staggerFrom="last"
>
  Think different.
</Text3DFlip>
```

依赖：`pnpm add motion`（v11+）。

## Vanilla HTML reference

```html
<h1 data-anim="text3dFlip" data-dir="top" data-stagger="first">Stay hungry, stay foolish.</h1>
<h1 data-anim="text3dFlip" data-dir="right" data-stagger="center">Design for failure.</h1>
```

通过 `data-dir` 设置翻转方向（top/right/bottom/left），`data-stagger` 设置错开方式（first/last/center/random）。Hover 触发翻转。JS 运行时自动拆分字符并构建 3D 结构。
