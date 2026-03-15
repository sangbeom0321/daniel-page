"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { motion } from "framer-motion";
import { Menu } from "lucide-react";
import { SITE_CONFIG, BASE_PATH } from "@/lib/constants";
import { useScrollDirection } from "@/hooks/useScrollDirection";
import ThemeToggle from "./ThemeToggle";
import MobileMenu from "./MobileMenu";

export default function Navbar() {
  const pathname = usePathname();
  const scrollDirection = useScrollDirection();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <>
      <motion.header
        initial={{ y: 0 }}
        animate={{ y: scrollDirection === "down" ? -80 : 0 }}
        transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
        className="fixed top-0 left-0 right-0 z-50 h-16 border-b border-[var(--border)] bg-[var(--bg-primary)]/80 backdrop-blur-xl"
      >
        <nav className="section-container flex h-full items-center justify-between">
          {/* Logo */}
          <Link
            href="/"
            className="text-heading-sm font-bold tracking-tight text-[var(--text-primary)] transition-colors hover:text-[var(--accent)]"
          >
            SB
          </Link>

          {/* Desktop nav links */}
          <ul className="hidden items-center gap-1 md:flex">
            {SITE_CONFIG.navItems.map((item) => {
              const isExternal = item.href.endsWith(".html");
              const isActive = isExternal
                ? false
                : item.href === "/"
                  ? pathname === "/"
                  : pathname.startsWith(item.href);
              const LinkTag = isExternal ? "a" : Link;

              return (
                <li key={item.href}>
                  <LinkTag
                    href={isExternal ? `${BASE_PATH}${item.href}` : item.href}
                    {...(isExternal ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                    className={`relative px-3 py-2 text-body-sm font-medium transition-colors ${
                      isActive
                        ? "text-[var(--text-primary)]"
                        : "text-[var(--text-tertiary)] hover:text-[var(--text-primary)]"
                    }`}
                  >
                    {item.label}
                    {isActive && (
                      <motion.span
                        layoutId="navbar-active-indicator"
                        className="absolute inset-x-1 -bottom-[1px] h-[2px] rounded-full bg-[var(--accent)]"
                        transition={{
                          type: "spring",
                          stiffness: 380,
                          damping: 30,
                        }}
                      />
                    )}
                  </LinkTag>
                </li>
              );
            })}
          </ul>

          {/* Right side: theme toggle + mobile hamburger */}
          <div className="flex items-center gap-2">
            <ThemeToggle />

            {/* Mobile menu button */}
            <button
              onClick={() => setMobileMenuOpen(true)}
              className="flex h-9 w-9 items-center justify-center rounded-lg border border-[var(--border)] bg-[var(--surface)] transition-colors hover:bg-[var(--surface-hover)] md:hidden"
              aria-label="Open menu"
            >
              <Menu className="h-4 w-4 text-[var(--text-secondary)]" />
            </button>
          </div>
        </nav>
      </motion.header>

      {/* Mobile menu */}
      <MobileMenu
        isOpen={mobileMenuOpen}
        onClose={() => setMobileMenuOpen(false)}
      />
    </>
  );
}
