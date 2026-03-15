"use client";

import { useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { SITE_CONFIG, BASE_PATH } from "@/lib/constants";

interface MobileMenuProps {
  isOpen: boolean;
  onClose: () => void;
}

const overlayVariants = {
  closed: { opacity: 0 },
  open: { opacity: 1 },
};

const menuVariants = {
  closed: { x: "100%" },
  open: {
    x: 0,
    transition: {
      type: "spring" as const,
      stiffness: 300,
      damping: 30,
      staggerChildren: 0.05,
      delayChildren: 0.1,
    },
  },
};

const itemVariants = {
  closed: { opacity: 0, x: 20 },
  open: { opacity: 1, x: 0 },
};

export default function MobileMenu({ isOpen, onClose }: MobileMenuProps) {
  const pathname = usePathname();

  // Prevent body scroll when menu is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => {
      document.body.style.overflow = "";
    };
  }, [isOpen]);

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            variants={overlayVariants}
            initial="closed"
            animate="open"
            exit="closed"
            transition={{ duration: 0.2 }}
            className="fixed inset-0 z-40 bg-black/50 backdrop-blur-sm md:hidden"
            onClick={onClose}
            aria-hidden="true"
          />

          {/* Panel */}
          <motion.nav
            variants={menuVariants}
            initial="closed"
            animate="open"
            exit="closed"
            className="fixed right-0 top-0 z-50 flex h-full w-72 flex-col bg-[var(--bg-primary)] border-l border-[var(--border)] p-6 shadow-2xl md:hidden"
            role="dialog"
            aria-modal="true"
            aria-label="Mobile navigation"
          >
            {/* Close button */}
            <div className="flex justify-end">
              <button
                onClick={onClose}
                className="flex h-9 w-9 items-center justify-center rounded-lg border border-[var(--border)] bg-[var(--surface)] transition-colors hover:bg-[var(--surface-hover)]"
                aria-label="Close menu"
              >
                <X className="h-4 w-4 text-[var(--text-secondary)]" />
              </button>
            </div>

            {/* Nav links */}
            <ul className="mt-8 flex flex-col gap-1">
              {SITE_CONFIG.navItems.map((item) => {
                const isExternal = item.href.endsWith(".html");
                const isActive = isExternal
                  ? false
                  : item.href === "/"
                    ? pathname === "/"
                    : pathname.startsWith(item.href);
                const LinkTag = isExternal ? "a" : Link;

                return (
                  <motion.li key={item.href} variants={itemVariants}>
                    <LinkTag
                      href={isExternal ? `${BASE_PATH}${item.href}` : item.href}
                      onClick={onClose}
                      {...(isExternal ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                      className={`block rounded-lg px-4 py-3 text-body-lg font-medium transition-colors ${
                        isActive
                          ? "bg-[var(--accent-muted)] text-[var(--accent)]"
                          : "text-[var(--text-secondary)] hover:bg-[var(--surface-hover)] hover:text-[var(--text-primary)]"
                      }`}
                    >
                      {item.label}
                    </LinkTag>
                  </motion.li>
                );
              })}
            </ul>

            {/* Bottom branding */}
            <div className="mt-auto pt-6 border-t border-[var(--border)]">
              <p className="text-caption text-[var(--text-tertiary)]">
                {SITE_CONFIG.name}
              </p>
            </div>
          </motion.nav>
        </>
      )}
    </AnimatePresence>
  );
}
