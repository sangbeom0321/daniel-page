"use client";

import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";

export default function PhilosophySection() {
  const sectionRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start end", "end start"],
  });

  const flowerScale = useTransform(scrollYProgress, [0.2, 0.5], [0.6, 1]);
  const flowerOpacity = useTransform(scrollYProgress, [0.2, 0.4], [0, 1]);
  const universeOpacity = useTransform(scrollYProgress, [0.05, 0.2], [0, 1]);

  return (
    <section
      ref={sectionRef}
      className="relative py-32 sm:py-40 overflow-hidden"
    >
      {/* Subtle background gradient */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(ellipse at 30% 20%, var(--accent-muted) 0%, transparent 50%), radial-gradient(ellipse at 70% 80%, rgba(249,168,212,0.08) 0%, transparent 50%)",
        }}
      />

      <div className="section-container relative">
        {/* Title */}
        <motion.p
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-caption tracking-[0.3em] uppercase text-[var(--text-tertiary)] mb-16 text-center"
        >
          Philosophy
        </motion.p>

        {/* Universe — the vast */}
        <motion.div
          style={{ opacity: universeOpacity }}
          className="max-w-2xl mx-auto mb-20"
        >
          <h3 className="text-display-sm sm:text-display-md font-display font-bold text-[var(--text-primary)] tracking-tight text-center mb-8">
            세상에서 가장 큰 것
          </h3>
          <p className="text-body-lg text-[var(--text-secondary)] leading-relaxed text-center">
            우주가 떠올랐다.
            <br />
            우리가 상상할 수 있는 가장 큰 공간.
            <br />
            <span className="text-[var(--text-tertiary)]">
              너무나 거대해서 그 크기가 감도 안 잡히는.
            </span>
          </p>
        </motion.div>

        {/* Divider — tiny dots like stars */}
        <div className="flex justify-center items-center gap-2 my-12">
          {[...Array(5)].map((_, i) => (
            <motion.span
              key={i}
              initial={{ opacity: 0, scale: 0 }}
              whileInView={{ opacity: 0.4, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1, duration: 0.4 }}
              className="block w-1 h-1 rounded-full"
              style={{ backgroundColor: "var(--pastel-purple)" }}
            />
          ))}
        </div>

        {/* Flower — the small but infinite */}
        <motion.div
          style={{ scale: flowerScale, opacity: flowerOpacity }}
          className="max-w-2xl mx-auto mb-20"
        >
          <h3 className="text-display-sm sm:text-display-md font-display font-bold text-[var(--text-primary)] tracking-tight text-center mb-8">
            그리고, 꽃
          </h3>
          <div className="space-y-6 text-body-lg text-[var(--text-secondary)] leading-relaxed text-center">
            <p>
              꽃은 작다. 손가락보다 작은 꽃들도 있다.
            </p>
            <p>
              그렇지만, 이 꽃은 정말 작은 걸까?
            </p>
            <p className="text-[var(--text-primary)] font-medium">
              인류가 발생한 시점부터 꽃에는
              <br />
              삶과 죽음, 행복과 슬픔, 괴로움, 외로움 —
              <br />
              인간이 감히 상상조차 할 수 없는
              <br />
              거대한 정신과 감정이 담겨 있다.
            </p>
          </div>
        </motion.div>

        {/* The contrast — core message */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="max-w-xl mx-auto text-center"
        >
          {/* Decorative flower symbol */}
          <div className="mb-8 flex justify-center">
            <svg
              width="48"
              height="48"
              viewBox="0 0 48 48"
              fill="none"
              className="opacity-60"
            >
              {/* Simple abstract flower */}
              {[0, 60, 120, 180, 240, 300].map((angle) => (
                <ellipse
                  key={angle}
                  cx="24"
                  cy="14"
                  rx="5"
                  ry="10"
                  fill="var(--pastel-pink)"
                  opacity="0.5"
                  transform={`rotate(${angle} 24 24)`}
                />
              ))}
              <circle cx="24" cy="24" r="4" fill="var(--pastel-purple)" opacity="0.7" />
            </svg>
          </div>

          <blockquote className="relative">
            <p className="text-heading-md sm:text-heading-lg font-display font-semibold text-[var(--text-primary)] leading-snug">
              내 몸은 거대하고 창대한 우주 위에 존재하지만,
            </p>
            <p className="mt-3 text-heading-md sm:text-heading-lg font-display font-semibold leading-snug" style={{ color: "var(--accent)" }}>
              나의 정신과 이념, 창의와 논리는
              <br />
              이 작은 꽃에 담길 수 있다.
            </p>
          </blockquote>

          <div className="mt-10 text-body-sm text-[var(--text-tertiary)]">
            — 우상범
          </div>
        </motion.div>
      </div>
    </section>
  );
}
