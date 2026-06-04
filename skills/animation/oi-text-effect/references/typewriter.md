# 打字机类（Typewriter）

逐字输入 + 删除 + 多句轮播的打字机动画。当前提供两种组件：

- `TextType`：经典打字机，支持光标闪烁、变速模拟真人输入
- `TextShiftWords`：词组轮播型打字机（nameslink hero-desc 风格），支持渐变下划线与可见区域触发

## Props

| Prop | Type | Default | 说明 |
|------|------|---------|------|
| `text` | `string \| string[]` | — | 单句或多句轮播文本 |
| `typingSpeed` | `number` | `50` | 打字速度（ms/字符） |
| `deletingSpeed` | `number` | `30` | 删除速度（ms/字符） |
| `pauseDuration` | `number` | `2000` | 句末暂停时长（ms） |
| `initialDelay` | `number` | `0` | 起播前延迟（ms） |
| `loop` | `boolean` | `true` | 是否循环 |
| `showCursor` | `boolean` | `true` | 显示光标 |
| `cursorCharacter` | `string` | `"\|"` | 光标字符 |
| `cursorBlinkDuration` | `number` | `0.5` | 光标闪烁周期（秒） |
| `hideCursorWhileTyping` | `boolean` | `false` | 打字时隐藏光标 |
| `textColors` | `string[]` | `[]` | 按句索引循环颜色 |
| `variableSpeed` | `{ min, max }` | — | 随机区间模拟真人节奏 |
| `startOnVisible` | `boolean` | `false` | 元素可见后才开始 |
| `reverseMode` | `boolean` | `false` | 反转文本后逐字输出 |
| `onSentenceComplete` | `(value, index) => void` | — | 每句完成后的回调 |

## Recommended defaults

| Prop | Default | 备注 |
|------|---------|------|
| `typingSpeed` | `50` | ms/字符 |
| `deletingSpeed` | `30` | 删除比打字快 |
| `pauseDuration` | `2000` | 句末停顿 2 秒 |
| `loop` | `true` | 默认循环 |
| `showCursor` | `true` | 显示闪烁光标 |
| `cursorCharacter` | `"\|"` | 竖线光标 |

默认文案（用户未给时）：`["Build Fast", "Ship Better", "Design With Motion"]`

## React reference

```tsx
import { TextType } from "@/components/ui/text-type";
import { TextShiftWords } from "@/components/ui/text-shift-words";

{/* 基础 — 三句循环（参数与样板间 No.22 一致） */}
<h1>
  <TextType
    text={["Build Fast", "Ship Better", "Design With Motion"]}
    typingSpeed={50}
    deletingSpeed={30}
    pauseDuration={2000}
    loop={true}
    showCursor={true}
    cursorCharacter="|"
  />
</h1>

{/* 单句不循环 */}
<TextType text="Welcome to our platform" loop={false} />

{/* 变速 — 模拟真人 */}
<TextType
  text={["Typing like a human...", "With natural rhythm"]}
  variableSpeed={{ min: 40, max: 120 }}
/>

{/* TextShiftWords — hero 描述词组轮播 */}
<TextShiftWords
  text="Premium domains,Fast checkout,Global DNS"
  typeIntervalMs={70}
  deletingIntervalMs={70}
  pauseMs={600}
  loop={true}
  showUnderline={true}
/>
```

无外部动画依赖。

## TextShiftWords Props

| Prop | Type | Default | 说明 |
|------|------|---------|------|
| `text` | `string \| string[]` | — | 逗号分隔短语（或数组） |
| `phrases` | `string \| string[]` | — | `text` 的别名，优先于 `text` |
| `typeIntervalMs` | `number` | `70` | 输入速度（ms/字符） |
| `deletingIntervalMs` | `number` | `70` | 删除速度（ms/字符） |
| `pauseMs` | `number` | `600` | 打满/删空前停顿（ms） |
| `initialDelay` | `number` | `0` | 初始延迟（ms） |
| `loop` | `boolean` | `true` | 是否循环 |
| `startOnVisible` | `boolean` | `false` | 元素可见后再开始 |
| `visibleThreshold` | `number` | `0.1` | 可见触发阈值（0~1） |
| `textColors` | `string[]` | `[]` | 按短语索引轮播颜色 |
| `onSentenceComplete` | `(value, index) => void` | — | 每句打满时回调 |
| `showUnderline` | `boolean` | `true` | 显示渐变下划线 |
| `underlineHeight` | `number` | `2` | 下划线粗细（px） |
| `underlineGradient` | `string` | 预设渐变 | 下划线 `border-image` 渐变 |
| `className` / `textClassName` / `underlineClassName` | `string` | — | 根节点/文本/下划线类名扩展 |

## Base CSS

```css
.text-type {
  display: inline;
  white-space: pre-wrap;
  line-height: 1.4;
}
.text-type__cursor {
  display: inline;
  font-weight: 100;
  animation: blink 0.5s step-end infinite;
}
.text-type__cursor--hidden {
  opacity: 0 !important;
}
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
```

## Vanilla HTML reference

```html
<h1 id="typewriter"></h1>

<style>
  #typewriter { font-size: 2.5rem; line-height: 1.4; }
  .cursor { font-weight: 100; animation: blink 0.5s step-end infinite; }
  @keyframes blink { 0%,100% { opacity:1 } 50% { opacity:0 } }
</style>

<script>
(function() {
  const el = document.getElementById("typewriter");
  const texts = ["Build Fast", "Ship Better", "Design With Motion"];
  let ti = 0, ci = 0, deleting = false;
  function tick() {
    const t = texts[ti];
    ci += deleting ? -1 : 1;
    el.innerHTML = t.slice(0, ci) + '<span class="cursor">|</span>';
    if (!deleting && ci === t.length) {
      setTimeout(() => { deleting = true; tick(); }, 2000);
      return;
    }
    if (deleting && ci === 0) {
      deleting = false;
      ti = (ti + 1) % texts.length;
    }
    setTimeout(tick, deleting ? 30 : 50);
  }
  tick();
})();
</script>
```
