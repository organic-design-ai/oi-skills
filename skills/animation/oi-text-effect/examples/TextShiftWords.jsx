/**
 * TextShiftWords — phrase cycle: type → pause → delete → next phrase.
 * Interval-driven typewriter (nameslink hero-desc-typewriter style) with an
 * optional gradient underline that tracks the typed text width.
 *
 * Part of the `oi-text-effect` skill.
 *
 * Requires: react >= 18
 * No external animation library needed.
 */
import React, { useEffect, useMemo, useRef, useState } from "react";

const DEFAULTS = {
  typeIntervalMs: 70,
  deletingIntervalMs: 70,
  pauseMs: 600,
  initialDelay: 0,
  loop: true,
  startOnVisible: false,
  textColors: [],
  showUnderline: true,
  underlineHeight: 2,
  underlineGradient:
    "linear-gradient(270deg, #11ce37 10%, #633eff 53%, #b06dfd 98%)",
};

const clampPositive = (value, fallback) =>
  Number.isFinite(value) && value >= 0 ? value : fallback;

function normalizePhrases(phrases, text) {
  const source = phrases ?? text;
  const list = Array.isArray(source) ? source : source != null ? [source] : [];
  return list
    .flatMap((item) => String(item).split(","))
    .map((p) => p.trim())
    .filter(Boolean);
}

const clampVisibleThreshold = (value) => {
  const num = Number(value);
  if (!Number.isFinite(num)) return 0.1;
  return Math.max(0, Math.min(1, num));
};

export function TextShiftWords({
  phrases,
  text,
  typeIntervalMs = DEFAULTS.typeIntervalMs,
  deletingIntervalMs = DEFAULTS.deletingIntervalMs,
  pauseMs = DEFAULTS.pauseMs,
  initialDelay = DEFAULTS.initialDelay,
  loop = DEFAULTS.loop,
  startOnVisible = DEFAULTS.startOnVisible,
  textColors = DEFAULTS.textColors,
  onSentenceComplete,
  visibleThreshold = 0.1,
  showUnderline = DEFAULTS.showUnderline,
  underlineHeight = DEFAULTS.underlineHeight,
  underlineGradient = DEFAULTS.underlineGradient,
  className,
  textClassName,
  underlineClassName,
}) {
  const wordsKey = useMemo(
    () => normalizePhrases(phrases, text).join("\u0001"),
    [phrases, text],
  );
  const words = useMemo(
    () => (wordsKey ? wordsKey.split("\u0001") : []),
    [wordsKey],
  );

  const [displayText, setDisplayText] = useState("");
  const [phraseIndex, setPhraseIndex] = useState(0);
  const [isStarted, setIsStarted] = useState(!startOnVisible);
  const rootRef = useRef(null);
  const timeoutRef = useRef(null);

  const safeTypeInterval = clampPositive(
    typeIntervalMs,
    DEFAULTS.typeIntervalMs,
  );
  const safeDeletingInterval = clampPositive(
    deletingIntervalMs,
    DEFAULTS.deletingIntervalMs,
  );
  const safePause = clampPositive(pauseMs, DEFAULTS.pauseMs);
  const safeInitialDelay = clampPositive(initialDelay, DEFAULTS.initialDelay);
  const safeThreshold = clampVisibleThreshold(visibleThreshold);
  const safeUnderlineHeight = Math.max(
    1,
    clampPositive(underlineHeight, DEFAULTS.underlineHeight),
  );

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
      { threshold: safeThreshold },
    );
    observer.observe(node);
    return () => observer.disconnect();
  }, [startOnVisible, safeThreshold]);

  useEffect(() => {
    if (!isStarted || !words.length) {
      setDisplayText("");
      setPhraseIndex(0);
      return undefined;
    }

    let currentPhraseIndex = 0;
    let currentLength = 1;
    let deleting = false;
    let stopped = false;

    setPhraseIndex(0);
    setDisplayText(words[0].slice(0, 1));

    const clearTick = () => {
      if (timeoutRef.current !== null) {
        window.clearTimeout(timeoutRef.current);
        timeoutRef.current = null;
      }
    };

    const tick = () => {
      if (stopped) return;
      const currentPhrase = words[currentPhraseIndex] ?? "";

      if (!deleting) {
        const nextLength = Math.min(currentPhrase.length, currentLength);
        setDisplayText(currentPhrase.slice(0, nextLength));
        if (nextLength >= currentPhrase.length) {
          onSentenceComplete?.(currentPhrase, currentPhraseIndex);
          deleting = true;
          timeoutRef.current = window.setTimeout(tick, safePause);
          return;
        }
        currentLength += 1;
        timeoutRef.current = window.setTimeout(tick, safeTypeInterval);
        return;
      }

      const nextLength = Math.max(0, currentLength - 1);
      setDisplayText(currentPhrase.slice(0, nextLength));
      currentLength = nextLength;

      if (nextLength === 0) {
        const isLast = currentPhraseIndex === words.length - 1;
        if (!loop && isLast) {
          stopped = true;
          return;
        }
        currentPhraseIndex = (currentPhraseIndex + 1) % words.length;
        setPhraseIndex(currentPhraseIndex);
        deleting = false;
        currentLength = 1;
        timeoutRef.current = window.setTimeout(tick, safePause);
        return;
      }

      timeoutRef.current = window.setTimeout(tick, safeDeletingInterval);
    };

    timeoutRef.current = window.setTimeout(tick, safeInitialDelay);

    return () => {
      stopped = true;
      clearTick();
    };
  }, [
    words,
    isStarted,
    loop,
    safeTypeInterval,
    safeDeletingInterval,
    safePause,
    safeInitialDelay,
    onSentenceComplete,
  ]);

  if (!words.length) return null;

  const rootClass = ["text-shift-words", className].filter(Boolean).join(" ");
  const textCls = ["text-shift-words__text", textClassName]
    .filter(Boolean)
    .join(" ");
  const underlineCls = ["text-shift-words__underline", underlineClassName]
    .filter(Boolean)
    .join(" ");

  const reservedMinHeight = `calc(1.5em + 0.25rem + ${safeUnderlineHeight}px)`;
  const currentColor = textColors.length
    ? textColors[phraseIndex % textColors.length]
    : undefined;

  return (
    <span
      ref={rootRef}
      className={rootClass}
      style={{
        display: "inline-flex",
        flexDirection: "column",
        alignItems: "stretch",
        width: "max-content",
        maxWidth: "100%",
        verticalAlign: "bottom",
        minHeight: showUnderline ? reservedMinHeight : undefined,
        color: currentColor,
      }}
    >
      <span
        className={textCls}
        style={{
          display: "block",
          minHeight: "1.5em",
          whiteSpace: "nowrap",
        }}
      >
        {displayText}
      </span>
      {showUnderline ? (
        <span
          className={underlineCls}
          aria-hidden="true"
          style={{
            marginTop: "0.25rem",
            display: "block",
            height: 0,
            width: "100%",
            minWidth: 0,
            boxSizing: "border-box",
            border: 0,
            borderBottom: `${safeUnderlineHeight}px solid transparent`,
            borderImage: underlineGradient
              ? `${underlineGradient} 1`
              : undefined,
          }}
        />
      ) : null}
    </span>
  );
}
