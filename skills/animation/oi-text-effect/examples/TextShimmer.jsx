"use client";

/**
 * TextShimmer
 * A neutral-color gradient shimmer that sweeps across text infinitely,
 * similar to ChatGPT/Cursor loading state.
 *
 * Requires: react >= 18
 * No external animation library needed — pure CSS animation.
 */

import { cn } from "@/lib/utils";

export function TextShimmer({
  children,
  className,
  as: Component = "p",
  duration = 2,
  baseColor = "#6b7280",
  highlightColor = "#e5e7eb",
}) {
  return (
    <Component
      className={cn("inline-block", className)}
      style={{
        background: `linear-gradient(90deg, ${baseColor} 0%, ${baseColor} 35%, ${highlightColor} 50%, ${baseColor} 65%, ${baseColor} 100%)`,
        backgroundSize: "200% 100%",
        WebkitBackgroundClip: "text",
        backgroundClip: "text",
        WebkitTextFillColor: "transparent",
        animation: `text-shimmer ${duration}s linear infinite`,
      }}
    >
      {children}
      <style>{`@keyframes text-shimmer { from { background-position: 100% 0; } to { background-position: -100% 0; } }`}</style>
    </Component>
  );
}
