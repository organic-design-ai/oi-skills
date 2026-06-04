"use client";

/**
 * HyperText
 * Source: magicui.design/docs/components/hyper-text (MIT)
 * Re-distributed as part of the `oi-text-effect` skill.
 *
 * Requires: react >= 18
 * No external animation library needed — uses requestAnimationFrame.
 */

import { memo, useCallback, useEffect, useRef, useState } from "react";
import { cn } from "@/lib/utils";

const DEFAULT_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

const HyperTextBase = ({
  children,
  className,
  mode = "character",
  duration = 800,
  delay = 0,
  as: Component = "div",
  startOnView = false,
  animateOnHover = true,
  characterSet = DEFAULT_CHARSET,
}) => {
  const [displayText, setDisplayText] = useState(children);
  const [isAnimating, setIsAnimating] = useState(false);
  const ref = useRef(null);
  const intervalRef = useRef();

  const animate = useCallback(() => {
    if (isAnimating) return;
    setIsAnimating(true);

    const chars = [...children];
    const randomChar = () => characterSet[Math.floor(Math.random() * characterSet.length)];

    if (mode === "blink") {
      const steps = Math.ceil(duration / 50);
      let frame = 0;
      intervalRef.current = setInterval(() => {
        frame++;
        if (frame >= steps) {
          clearInterval(intervalRef.current);
          setDisplayText(children);
          setIsAnimating(false);
        } else {
          setDisplayText(children + randomChar());
        }
      }, 50);
    } else if (mode === "cursor") {
      const steps = Math.ceil(duration / 50);
      let frame = 0;
      intervalRef.current = setInterval(() => {
        frame++;
        const revealedCount = Math.floor((frame / steps) * chars.length);
        const revealed = chars.slice(0, revealedCount).join("");
        if (frame >= steps) {
          clearInterval(intervalRef.current);
          setDisplayText(children);
          setIsAnimating(false);
        } else {
          setDisplayText(revealed + randomChar());
        }
      }, 50);
    } else {
      const steps = Math.ceil(duration / 50);
      let frame = 0;
      intervalRef.current = setInterval(() => {
        frame++;
        const revealedCount = Math.floor((frame / steps) * chars.length);
        setDisplayText(
          chars
            .map((ch, i) => {
              if (ch === " ") return " ";
              if (i < revealedCount) return ch;
              return randomChar();
            })
            .join("")
        );
        if (frame >= steps) {
          clearInterval(intervalRef.current);
          setDisplayText(children);
          setIsAnimating(false);
        }
      }, 50);
    }
  }, [children, duration, characterSet, mode, isAnimating]);

  useEffect(() => {
    if (!startOnView) {
      const timer = setTimeout(animate, delay);
      return () => clearTimeout(timer);
    }
  }, [startOnView, delay]);

  useEffect(() => {
    if (!startOnView || !ref.current) return;
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setTimeout(animate, delay);
          observer.disconnect();
        }
      },
      { threshold: 0.5 }
    );
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, [startOnView, delay, animate]);

  useEffect(() => {
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
    };
  }, []);

  return (
    <Component
      ref={ref}
      className={cn("inline-block", className)}
      onMouseEnter={animateOnHover ? animate : undefined}
    >
      {displayText}
    </Component>
  );
};

export const HyperText = memo(HyperTextBase);
