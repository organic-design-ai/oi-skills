/**
 * TextType — typewriter typing / deleting / phrase rotation.
 * Part of the `oi-text-effect` skill (formerly standalone `oi-text-type`).
 */
import React, { useEffect, useMemo, useRef, useState } from "react";

const DEFAULTS = {
  typingSpeed: 50,
  deletingSpeed: 30,
  pauseDuration: 2000,
  initialDelay: 0,
  loop: true,
  showCursor: true,
  cursorCharacter: "|",
  cursorBlinkDuration: 0.5,
  hideCursorWhileTyping: false,
  textColors: [],
  startOnVisible: false,
  reverseMode: false,
};

const clampPositive = (value, fallback) =>
  Number.isFinite(value) && value >= 0 ? value : fallback;

const normalizeVariableSpeed = (variableSpeed) => {
  if (!variableSpeed) return undefined;
  const min = Math.max(0, variableSpeed.min);
  const max = Math.max(min, variableSpeed.max);
  return { min, max };
};

const randomIntBetween = (min, max) =>
  Math.floor(min + Math.random() * (max - min + 1));

export function TextType({
  text,
  typingSpeed = DEFAULTS.typingSpeed,
  deletingSpeed = DEFAULTS.deletingSpeed,
  pauseDuration = DEFAULTS.pauseDuration,
  initialDelay = DEFAULTS.initialDelay,
  loop = DEFAULTS.loop,
  showCursor = DEFAULTS.showCursor,
  cursorCharacter = DEFAULTS.cursorCharacter,
  cursorBlinkDuration = DEFAULTS.cursorBlinkDuration,
  hideCursorWhileTyping = DEFAULTS.hideCursorWhileTyping,
  textColors = DEFAULTS.textColors,
  variableSpeed,
  startOnVisible = DEFAULTS.startOnVisible,
  reverseMode = DEFAULTS.reverseMode,
  onSentenceComplete,
  className,
}) {
  const list = useMemo(() => {
    const arr = Array.isArray(text) ? text : [text];
    return arr.filter((item) => item.length > 0);
  }, [text]);

  const [textIndex, setTextIndex] = useState(0);
  const [displayed, setDisplayed] = useState("");
  const [isDeleting, setIsDeleting] = useState(false);
  const [isStarted, setIsStarted] = useState(!startOnVisible);

  const rootRef = useRef(null);
  const timeoutRef = useRef(null);

  const safeTypingSpeed = clampPositive(typingSpeed, DEFAULTS.typingSpeed);
  const safeDeletingSpeed = clampPositive(deletingSpeed, DEFAULTS.deletingSpeed);
  const safePauseDuration = clampPositive(pauseDuration, DEFAULTS.pauseDuration);
  const safeInitialDelay = clampPositive(initialDelay, DEFAULTS.initialDelay);
  const safeBlinkDuration = Math.max(0.1, clampPositive(cursorBlinkDuration, DEFAULTS.cursorBlinkDuration));
  const safeVariableSpeed = normalizeVariableSpeed(variableSpeed);

  useEffect(() => {
    if (!startOnVisible) return;
    const node = rootRef.current;
    if (!node) return;

    const observer = new IntersectionObserver(
      (entries) => {
        const entry = entries[0];
        if (entry?.isIntersecting) {
          setIsStarted(true);
          observer.disconnect();
        }
      },
      { threshold: 0.1 },
    );

    observer.observe(node);
    return () => observer.disconnect();
  }, [startOnVisible]);

  useEffect(() => {
    if (!isStarted || list.length === 0) return;

    const currentRaw = list[textIndex] ?? "";
    const current = reverseMode ? currentRaw.split("").reverse().join("") : currentRaw;

    const tick = () => {
      setDisplayed((prev) => {
        const next = isDeleting
          ? current.slice(0, Math.max(0, prev.length - 1))
          : current.slice(0, Math.min(current.length, prev.length + 1));

        const typedDone = !isDeleting && next === current;
        const deletedDone = isDeleting && next.length === 0;

        if (typedDone) {
          onSentenceComplete?.(currentRaw, textIndex);
          timeoutRef.current = window.setTimeout(() => {
            setIsDeleting(true);
          }, safePauseDuration);
          return next;
        }

        if (deletedDone) {
          const last = textIndex === list.length - 1;
          if (!loop && last) return next;
          setIsDeleting(false);
          setTextIndex((idx) => (idx + 1) % list.length);
          return next;
        }

        const delay = safeVariableSpeed
          ? randomIntBetween(safeVariableSpeed.min, safeVariableSpeed.max)
          : isDeleting
            ? safeDeletingSpeed
            : safeTypingSpeed;

        timeoutRef.current = window.setTimeout(tick, delay);
        return next;
      });
    };

    timeoutRef.current = window.setTimeout(tick, safeInitialDelay);
    return () => {
      if (timeoutRef.current !== null) {
        window.clearTimeout(timeoutRef.current);
      }
    };
  }, [
    isStarted,
    list,
    textIndex,
    isDeleting,
    reverseMode,
    loop,
    safeTypingSpeed,
    safeDeletingSpeed,
    safePauseDuration,
    safeInitialDelay,
    safeVariableSpeed,
    onSentenceComplete,
  ]);

  const currentColor = textColors.length ? textColors[textIndex % textColors.length] : undefined;
  const hideCursor = hideCursorWhileTyping && !isDeleting;
  const mergedClassName = ["text-type", className].filter(Boolean).join(" ");

  return (
    <span ref={rootRef} className={mergedClassName} style={{ color: currentColor }}>
      {displayed}
      {showCursor && (
        <span
          className={`text-type__cursor${hideCursor ? " text-type__cursor--hidden" : ""}`}
          style={{ animationDuration: `${safeBlinkDuration}s` }}
        >
          {cursorCharacter}
        </span>
      )}
    </span>
  );
}
