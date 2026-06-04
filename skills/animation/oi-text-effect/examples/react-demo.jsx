"use client";

import { TextAnimate } from "./TextAnimate";
import { DiaTextReveal } from "./DiaTextReveal";
import { HyperText } from "./HyperText";
import { Text3DFlip } from "./Text3DFlip";
import { MorphingText } from "./MorphingText";
import { TextShimmer } from "./TextShimmer";
import { TextType } from "./TextType";

// Minimal end-to-end usage. Drop into a Next.js / Vite React page.
// Requires `motion` and a `cn` helper (or remove `cn` from TextAnimate.jsx).

export default function TextAnimateDemo() {
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 32, padding: 48 }}>
      <TextAnimate animation="blurInUp" by="word" as="h1">
        Blur in by word
      </TextAnimate>

      <TextAnimate animation="blurInUp" by="character" once>
        Blur in by character (plays once)
      </TextAnimate>

      <TextAnimate animation="slideUp" by="word">
        Slide up by word
      </TextAnimate>

      <TextAnimate animation="scaleUp" by="text">
        Scale up the whole sentence
      </TextAnimate>

      <TextAnimate animation="fadeIn" by="line" as="p">
        {`Fade in by line\nSecond line\nThird line`}
      </TextAnimate>

      <TextAnimate animation="slideLeft" by="character" duration={0.6} delay={0.2}>
        Slide left, character by character
      </TextAnimate>

      {/* Custom variants — wavy spring motion */}
      <TextAnimate
        by="character"
        variants={{
          hidden: { opacity: 0, y: 30, rotate: 45, scale: 0.5 },
          show: (i) => ({
            opacity: 1,
            y: 0,
            rotate: 0,
            scale: 1,
            transition: {
              delay: i * 0.1,
              duration: 0.4,
              y: { type: "spring", damping: 12, stiffness: 200, mass: 0.8 },
              rotate: { type: "spring", damping: 8, stiffness: 150 },
              scale: { type: "spring", damping: 10, stiffness: 300 },
            },
          }),
          exit: (i) => ({
            opacity: 0,
            y: 30,
            rotate: 45,
            scale: 0.5,
            transition: { delay: i * 0.1, duration: 0.4 },
          }),
        }}
      >
        Wavy Motion!
      </TextAnimate>

      {/* ===== DiaTextReveal (colorSweep) ===== */}

      {/* Basic color sweep */}
      <DiaTextReveal
        className="text-4xl font-bold tracking-tight"
        text="Magic UI"
        colors={["#A97CF8", "#F38CB8", "#FDCC92"]}
      />

      {/* Custom 5-color palette */}
      <DiaTextReveal
        className="text-4xl font-bold tracking-tight"
        text="Design systems"
        colors={["#22d3ee", "#818cf8", "#f472b6", "#34d399", "#6366f1"]}
        duration={2.4}
        delay={0.35}
      />

      {/* Rotating phrases */}
      <h1 className="text-3xl font-semibold tracking-tight">
        Learn to{" "}
        <DiaTextReveal
          repeat
          repeatDelay={1.2}
          text={["build faster", "ship smarter", "scale easier"]}
        />
      </h1>

      {/* ===== HyperText (scramble) ===== */}

      {/* Basic — hover to trigger */}
      <HyperText className="text-4xl font-bold">HOVER ME!</HyperText>

      {/* Start on view, digits charset */}
      <HyperText
        className="text-4xl font-bold"
        startOnView
        animateOnHover={false}
        characterSet={"0123456789".split("")}
        duration={1000}
      >
        DECRYPTING...
      </HyperText>

      {/* Symbols charset */}
      <HyperText
        className="text-4xl font-bold"
        characterSet={"!@#$%^&*()_+-=[]{}|;:',.<>?".split("")}
      >
        SECRET CODE
      </HyperText>

      {/* Cursor mode — typing with scrambling cursor */}
      <HyperText
        className="text-4xl font-bold"
        mode="cursor"
        duration={1200}
        startOnView
        animateOnHover={false}
      >
        The quick brown fox jumps.
      </HyperText>

      {/* ===== Text3DFlip ===== */}

      {/* Basic — ripple flip from top on hover */}
      <Text3DFlip
        className="text-4xl font-bold"
        textClassName="text-foreground"
        flipTextClassName="text-foreground"
        rotateDirection="top"
      >
        Stay hungry, stay foolish
      </Text3DFlip>

      {/* Stagger from center — ripple outward */}
      <Text3DFlip
        className="text-4xl font-bold"
        textClassName="text-foreground"
        flipTextClassName="text-foreground"
        rotateDirection="top"
        staggerFrom="center"
      >
        Design for failure
      </Text3DFlip>

      {/* Flip right, stagger from last */}
      <Text3DFlip
        className="text-4xl font-bold"
        textClassName="text-foreground"
        flipTextClassName="text-foreground"
        rotateDirection="right"
        staggerFrom="last"
      >
        Think different.
      </Text3DFlip>

      {/* ===== MorphingText ===== */}

      {/* Basic — cycles through phrases with liquid morph */}
      <MorphingText
        texts={["Hello", "Morphing", "Text", "Animation", "React"]}
      />

      {/* Custom timing — slower morph, longer cooldown */}
      <MorphingText
        className="text-foreground"
        texts={["Design", "Build", "Ship", "Scale"]}
        morphTime={2}
        cooldownTime={1}
      />

      {/* ===== TextShimmer ===== */}

      {/* Basic — neutral loading shimmer */}
      <TextShimmer className="text-4xl font-bold" as="h1">
        Thinking about your request
      </TextShimmer>

      {/* Custom colors — darker base */}
      <TextShimmer
        className="text-2xl font-semibold"
        baseColor="#374151"
        highlightColor="#d1d5db"
        duration={2.5}
      >
        Generating response
      </TextShimmer>

      {/* ===== TextType (typewriter) ===== */}

      {/* Basic — 3 phrases, defaults match specimen No.22 */}
      <h1 style={{ fontSize: "clamp(28px, 5vw, 56px)", margin: 0 }}>
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

      {/* Single sentence, no loop */}
      <TextType text="Welcome to our platform" loop={false} />

      {/* Variable speed — human-like rhythm */}
      <TextType
        text={["Typing like a human...", "With natural rhythm"]}
        variableSpeed={{ min: 40, max: 120 }}
      />
    </div>
  );
}
