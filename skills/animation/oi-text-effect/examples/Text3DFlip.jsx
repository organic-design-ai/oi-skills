"use client";

/**
 * Text3DFlip
 * Source: magicui.design/docs/components/text-3d-flip (MIT)
 * Re-distributed as part of the `oi-text-effect` skill.
 *
 * Split-flap style: each character has overflow:hidden clipping,
 * on hover the inner container slides up (translateY) with a slight
 * rotateX for 3D depth, revealing a second copy from below.
 *
 * Requires: react >= 18, motion >= 11
 */

import { useMemo, useState } from "react";
import { motion } from "motion/react";
import { cn } from "@/lib/utils";

function computeStaggerDelays(len, from, staggerDuration) {
  const indices = new Array(len);

  if (typeof from === "number") {
    const anchor = Math.min(Math.max(from, 0), len - 1);
    for (let i = 0; i < len; i++) indices[i] = Math.abs(i - anchor);
  } else if (from === "last") {
    for (let i = 0; i < len; i++) indices[i] = len - 1 - i;
  } else if (from === "center") {
    const mid = (len - 1) / 2;
    for (let i = 0; i < len; i++) indices[i] = Math.abs(i - mid);
  } else if (from === "random") {
    const order = Array.from({ length: len }, (_, i) => i);
    for (let i = order.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [order[i], order[j]] = [order[j], order[i]];
    }
    for (let i = 0; i < len; i++) indices[order[i]] = i;
  } else {
    for (let i = 0; i < len; i++) indices[i] = i;
  }

  return indices.map((idx) => idx * staggerDuration);
}

const flippedTransform = {
  top: "translateY(-50%) rotateX(8deg)",
  bottom: "translateY(50%) rotateX(-8deg)",
  left: "translateY(-50%) rotateY(-8deg)",
  right: "translateY(-50%) rotateY(8deg)",
};

export function Text3DFlip({
  children,
  as: Component = "p",
  className,
  textClassName,
  flipTextClassName,
  staggerDuration = 0.03,
  staggerFrom = "first",
  transition = { type: "spring", damping: 30, stiffness: 200 },
  rotateDirection = "top",
}) {
  const [isFlipped, setIsFlipped] = useState(false);
  const text = typeof children === "string" ? children : String(children);
  const chars = useMemo(() => [...text], [text]);

  const delays = useMemo(
    () => computeStaggerDelays(chars.length, staggerFrom, staggerDuration),
    [chars.length, staggerFrom, staggerDuration]
  );

  const target = flippedTransform[rotateDirection];

  return (
    <Component
      className={cn("inline-flex flex-wrap cursor-pointer", className)}
      style={{ perspective: "600px" }}
      onMouseEnter={() => setIsFlipped(true)}
      onMouseLeave={() => setIsFlipped(false)}
    >
      {chars.map((char, i) => (
        <span
          key={i}
          style={{
            display: "inline-block",
            overflow: "hidden",
            height: "1.2em",
            whiteSpace: "pre",
          }}
        >
          <motion.span
            style={{ display: "flex", flexDirection: "column" }}
            animate={{ transform: isFlipped ? target : "translateY(0%) rotateX(0deg)" }}
            transition={{ ...transition, delay: delays[i] }}
          >
            <span
              className={textClassName}
              style={{ display: "block", height: "1.2em", lineHeight: "1.2em" }}
            >
              {char}
            </span>
            <span
              className={flipTextClassName}
              style={{ display: "block", height: "1.2em", lineHeight: "1.2em" }}
            >
              {char}
            </span>
          </motion.span>
        </span>
      ))}
    </Component>
  );
}
