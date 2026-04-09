export const BASE_PATH = "/daniel-page";

export const SITE_CONFIG = {
  name: "Sangbum Woo",
  nameKo: "우상범",
  url: "https://sangbum.github.io",
  description:
    "Personal homepage of Sangbum Woo (우상범). PhD Student at Hanyang AUTO Lab. Research in End-to-End Autonomous Driving, SLAM, and Robotics.",
  locale: "ko_KR",
  ogImage: "/og-image.png",
  navItems: [
    { label: "Home", href: "/" },
    { label: "Publications", href: "/publications" },
    { label: "Projects", href: "/projects" },
    { label: "CV", href: "/cv" },
    { label: "Blog", href: "/blog" },
    { label: "AI Papers", href: "/ai_papers_timeline.html" },
  ],
  social: {
    github: "https://github.com/sangbeom0321",
    googleScholar:
      "https://scholar.google.co.kr/citations?user=wiKYF-gAAAAJ&hl=ko",
    linkedin: "https://www.linkedin.com/in/woo-247368342/",
    email: "woosangbyum@naver.com",
    orcid: "",
  },
  giscus: {
    repo: "sangbeom0321/daniel-page" as `${string}/${string}`,
    repoId: "",
    category: "Announcements",
    categoryId: "",
  },
} as const;

export type NavItem = (typeof SITE_CONFIG.navItems)[number];
