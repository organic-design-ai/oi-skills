# Nothing UI — Platform Mapping

## 1. HTML / CSS / WEB

Load fonts via Google Fonts `<link>` or `@import`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Doto:wght@400..700&family=Space+Grotesk:wght@300;400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

Use CSS custom properties, `rem` for type, `px` for spacing/borders. Dark/light via `prefers-color-scheme` or class toggle.

```css
:root {
  --black: #000000;
  --surface: #111111;
  --surface-raised: #1A1A1A;
  --border: #222222;
  --border-visible: #333333;
  --text-disabled: #666666;
  --text-secondary: #999999;
  --text-primary: #E8E8E8;
  --text-display: #FFFFFF;
  --accent: #D71921;
  --accent-subtle: rgba(215,25,33,0.15);
  --success: #4A9E5C;
  --warning: #D4A843;
  --interactive: #5B9BF6;
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;
  --space-4xl: 96px;
  --font-display: "Doto", "Space Mono", monospace;
  --font-body: "Space Grotesk", "DM Sans", system-ui, sans-serif;
  --font-mono: "Space Mono", "JetBrains Mono", "SF Mono", monospace;
}
```

Light mode: swap token values per `tokens.md` Dark/Light table on `[data-theme="light"]` or `@media (prefers-color-scheme: light)`.

---

## 2. SWIFTUI / iOS

Register fonts in Info.plist, bundle `.ttf` files. Use `@Environment(\.colorScheme)` for mode switching.

```swift
extension Color {
    static let ndBlack = Color(hex: "000000")
    static let ndSurface = Color(hex: "111111")
    static let ndSurfaceRaised = Color(hex: "1A1A1A")
    static let ndBorder = Color(hex: "222222")
    static let ndBorderVisible = Color(hex: "333333")
    static let ndTextDisabled = Color(hex: "666666")
    static let ndTextSecondary = Color(hex: "999999")
    static let ndTextPrimary = Color(hex: "E8E8E8")
    static let ndTextDisplay = Color.white
    static let ndAccent = Color(hex: "D71921")
    static let ndSuccess = Color(hex: "4A9E5C")
    static let ndWarning = Color(hex: "D4A843")
    static let ndInteractive = Color(hex: "5B9BF6")
}
```

Light mode values in `tokens.md` Dark/Light table. Derive Font extension from font stack table (`.custom("Doto"/"SpaceGrotesk-Regular"/"SpaceMono-Regular", size:)`).

---

## 3. REACT / TAILWIND

Map CSS variables in `globals.css` or `@theme` and reference via arbitrary values, e.g. `text-[var(--text-primary)]`, `font-[family-name:var(--font-mono)]`. Prefer semantic tokens over raw hex in components. Pill buttons: `rounded-full`. Cards: `rounded-2xl` max (16px). No `shadow-*` utilities on surfaces.

---

## 4. DESIGN TOOL (FIGMA / PAPER)

Use `get_font_family_info` (Paper) or font picker verification before writing styles. Direct hex values (no CSS variables). Dark mode as default canvas, light mode as separate artboard.
