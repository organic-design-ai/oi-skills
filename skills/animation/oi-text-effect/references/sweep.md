# 扫光类（Color Sweep）

多色渐变带从左到右扫过文字，扫完后回到实色。适合 Hero 标题、品牌 slogan、强调单句。不使用 `by` 分段。

## Props

| Prop | Type | Default | 说明 |
|------|------|---------|------|
| `text` | `string \| string[]` | — | 文本内容；数组时配合 `repeat` 轮播 |
| `colors` | `string[]` | `["#c679c4","#fa3d1d","#ffb005","#e1e1fe","#0358f7"]` | 渐变色带颜色 |
| `textColor` | `string` | `var(--foreground)` | 扫完后文字实色 |
| `duration` | `number` | `2` | 扫光总时长（秒） |
| `delay` | `number` | `2` | 起播前延迟（秒） |
| `repeat` | `boolean` | `false` | 多文本轮播 |
| `repeatDelay` | `number` | `0.5` | 轮播间隔（秒） |
| `startOnView` | `boolean` | `true` | 进入视口才播 |
| `once` | `boolean` | `false` | 默认循环播放 |
| `fixedWidth` | `boolean` | `false` | 锁定最大宽度防布局跳动 |
| `className` | `string` | — | 容器额外类名 |

## React reference

```tsx
import { DiaTextReveal } from "@/components/ui/dia-text-reveal";

{/* 基础 */}
<DiaTextReveal
  className="text-4xl font-bold"
  text="Magic UI"
  colors={["#A97CF8", "#F38CB8", "#FDCC92"]}
/>

{/* 自定义 5 色 */}
<DiaTextReveal
  className="text-4xl font-bold"
  text="Design systems"
  colors={["#22d3ee", "#818cf8", "#f472b6", "#34d399", "#6366f1"]}
  duration={2.4}
  delay={0.35}
/>

{/* 多文本轮播 */}
<h1>
  Learn to{" "}
  <DiaTextReveal repeat repeatDelay={1.2} text={["build faster", "ship smarter", "scale easier"]} />
</h1>
```

依赖：`pnpm add motion`（v11+）。

## Vanilla HTML reference

```html
<h1 data-anim="colorSweep" style="--ta-duration:2000ms">Magic UI</h1>

<style>
  [data-anim="colorSweep"] {
    display: inline-block;
    line-height: 1.4;
    padding-bottom: 0.1em;
    background: linear-gradient(90deg,
      var(--sweep-text-color, currentColor) 0%,
      var(--sweep-text-color, currentColor) 35%,
      var(--sweep-c1, #c679c4) 38%, var(--sweep-c2, #fa3d1d) 42%,
      var(--sweep-c3, #ffb005) 46%, var(--sweep-c4, #e1e1fe) 52%,
      var(--sweep-c5, #0358f7) 56%,
      var(--sweep-text-color, currentColor) 60%,
      var(--sweep-text-color, currentColor) 100%);
    background-size: 300% 100%;
    background-position: 100% 0;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: oi-colorSweep var(--ta-duration, 2000ms) var(--ta-delay, 0ms)
               cubic-bezier(0.4, 0, 0.2, 1) both;
  }
  @keyframes oi-colorSweep {
    from { background-position: 100% 0; }
    to   { background-position: 0% 0; }
  }
</style>
```

自定义颜色：通过 CSS 变量 `--sweep-c1` ~ `--sweep-c5` 覆盖。

多文本轮播（HTML 版）：设置 `data-texts="build faster,ship smarter,scale easier"`，JS 运行时自动处理逐字打出 + 宽度过渡。
