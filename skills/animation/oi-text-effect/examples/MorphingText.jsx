"use client";

/**
 * MorphingText
 * Source: magicui.design/docs/components/morphing-text (MIT)
 * Re-distributed as part of the `oi-text-effect` skill.
 *
 * Cycles through an array of text strings with a blur+threshold SVG filter
 * that creates a liquid morphing transition between phrases.
 *
 * Requires: react >= 18
 * No external animation library needed — uses requestAnimationFrame.
 */

import { useCallback, useEffect, useRef } from "react";
import { cn } from "@/lib/utils";

function useMorphingText(texts, morphDuration = 1.5, cooldown = 0.5) {
  const textIndexRef = useRef(0);
  const morphRef = useRef(0);
  const cooldownRef = useRef(0);
  const timeRef = useRef(new Date());

  const text1Ref = useRef(null);
  const text2Ref = useRef(null);

  const setStyles = useCallback(
    (fraction) => {
      const [current1, current2] = [text1Ref.current, text2Ref.current];
      if (!current1 || !current2) return;

      current2.style.filter = `blur(${Math.min(8 / fraction - 8, 100)}px)`;
      current2.style.opacity = `${Math.pow(fraction, 0.4) * 100}%`;

      const invertedFraction = 1 - fraction;
      current1.style.filter = `blur(${Math.min(8 / invertedFraction - 8, 100)}px)`;
      current1.style.opacity = `${Math.pow(invertedFraction, 0.4) * 100}%`;

      current1.textContent = texts[textIndexRef.current % texts.length];
      current2.textContent = texts[(textIndexRef.current + 1) % texts.length];
    },
    [texts]
  );

  const doMorph = useCallback(() => {
    morphRef.current -= cooldownRef.current;
    cooldownRef.current = 0;

    let fraction = morphRef.current / morphDuration;

    if (fraction > 1) {
      cooldownRef.current = cooldown;
      fraction = 1;
    }

    setStyles(fraction);

    if (fraction === 1) {
      textIndexRef.current++;
    }
  }, [setStyles, morphDuration, cooldown]);

  const doCooldown = useCallback(() => {
    morphRef.current = 0;

    const [current1, current2] = [text1Ref.current, text2Ref.current];
    if (current1 && current2) {
      current2.style.filter = "none";
      current2.style.opacity = "100%";
      current1.style.filter = "none";
      current1.style.opacity = "0%";
    }
  }, []);

  useEffect(() => {
    let animationFrameId;

    const animate = () => {
      animationFrameId = requestAnimationFrame(animate);

      const newTime = new Date();
      const dt = (newTime.getTime() - timeRef.current.getTime()) / 1000;
      timeRef.current = newTime;

      cooldownRef.current -= dt;

      if (cooldownRef.current <= 0) doMorph();
      else doCooldown();
    };

    animate();
    return () => cancelAnimationFrame(animationFrameId);
  }, [doMorph, doCooldown]);

  return { text1Ref, text2Ref };
}

const SvgFilters = () => (
  <svg className="fixed h-0 w-0" preserveAspectRatio="xMidYMid slice">
    <defs>
      <filter id="threshold">
        <feColorMatrix
          in="SourceGraphic"
          type="matrix"
          values="1 0 0 0 0
                  0 1 0 0 0
                  0 0 1 0 0
                  0 0 0 255 -140"
        />
      </filter>
    </defs>
  </svg>
);

export function MorphingText({
  texts,
  className,
  morphTime: morphDuration = 1.5,
  cooldownTime: cooldown = 0.5,
}) {
  const { text1Ref, text2Ref } = useMorphingText(texts, morphDuration, cooldown);

  return (
    <div
      className={cn(
        "relative mx-auto h-16 w-full max-w-3xl text-center font-sans text-[40pt] leading-none font-bold md:h-24 lg:text-[6rem]",
        className
      )}
      style={{ filter: "url(#threshold) blur(0.6px)" }}
    >
      <span
        className="absolute inset-x-0 top-0 m-auto inline-block w-full"
        ref={text1Ref}
      />
      <span
        className="absolute inset-x-0 top-0 m-auto inline-block w-full"
        ref={text2Ref}
      />
      <SvgFilters />
    </div>
  );
}
