"use client";

/**
 * DiaTextReveal
 * Source: magicui.design/docs/components/dia-text-reveal (MIT)
 * Re-distributed as part of the `oi-text-effect` skill.
 *
 * Requires: motion >= 11 (https://www.npmjs.com/package/motion)
 *   pnpm add motion
 */

import { memo, useCallback, useEffect, useRef, useState } from "react";
import { motion, useInView } from "motion/react";

import { cn } from "@/lib/utils";

const DEFAULT_COLORS = ["#c679c4", "#fa3d1d", "#ffb005", "#e1e1fe", "#0358f7"];

const DiaTextRevealBase = ({
  text,
  colors = DEFAULT_COLORS,
  textColor = "var(--foreground, currentColor)",
  duration = 1.5,
  delay = 0,
  repeat = false,
  repeatDelay = 0.5,
  startOnView = true,
  once = true,
  className,
  fixedWidth = false,
}) => {
  const texts = Array.isArray(text) ? text : [text];
  const [index, setIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const ref = useRef(null);
  const isInView = useInView(ref, { once, amount: 0.5 });
  const widthRef = useRef(0);

  const shouldPlay = startOnView ? isInView : true;

  useEffect(() => {
    if (shouldPlay && !playing) {
      const timer = setTimeout(() => setPlaying(true), delay * 1000);
      return () => clearTimeout(timer);
    }
  }, [shouldPlay, delay, playing]);

  const handleAnimationEnd = useCallback(() => {
    if (!repeat || texts.length <= 1) return;
    setTimeout(() => {
      setPlaying(false);
      setIndex((prev) => (prev + 1) % texts.length);
      setTimeout(() => setPlaying(true), 50);
    }, repeatDelay * 1000);
  }, [repeat, texts.length, repeatDelay]);

  useEffect(() => {
    if (fixedWidth && ref.current) {
      const el = ref.current;
      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");
      const style = getComputedStyle(el);
      ctx.font = `${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
      const maxW = Math.max(...texts.map((t) => ctx.measureText(t).width));
      widthRef.current = maxW;
      el.style.minWidth = `${Math.ceil(maxW)}px`;
    }
  }, [fixedWidth, texts]);

  const colorStops = colors.map((c, i) => {
    const start = 38 + (i * 18) / colors.length;
    return `${c} ${start.toFixed(1)}%`;
  }).join(", ");
  const gradientStops = `${textColor} 0%, ${textColor} 35%, ${colorStops}, ${textColor} 60%, ${textColor} 100%`;

  return (
    <span
      ref={ref}
      className={cn("inline-block", className)}
      style={{
        background: `linear-gradient(90deg, ${gradientStops})`,
        backgroundSize: "300% 100%",
        backgroundPosition: playing ? undefined : "100% 0",
        WebkitBackgroundClip: "text",
        backgroundClip: "text",
        WebkitTextFillColor: "transparent",
        color: textColor,
        animation: playing
          ? `oi-dia-sweep ${duration}s cubic-bezier(0.4, 0, 0.2, 1) both`
          : "none",
      }}
      onAnimationEnd={handleAnimationEnd}
    >
      {texts[index]}
      <style>{`
        @keyframes oi-dia-sweep {
          from { background-position: 100% 0; }
          to   { background-position: 0% 0; }
        }
      `}</style>
    </span>
  );
};

export const DiaTextReveal = memo(DiaTextRevealBase);
