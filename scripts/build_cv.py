"""
Build an academic-style CV PDF for Sangbum Woo.
Output: daniel-page/public/files/cv.pdf

Layout follows the classic two-column researcher template:
  [ date / meta ]   [ entry title, details ]

Run: python scripts/build_cv.py
"""

from __future__ import annotations

import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    KeepTogether,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "files" / "cv.pdf"

# --- Fonts ---------------------------------------------------------------
# Try to register a nicer serif / sans. Fall back to reportlab built-ins.
SERIF = "Times-Roman"
SERIF_BOLD = "Times-Bold"
SERIF_ITALIC = "Times-Italic"
SANS = "Helvetica"
SANS_BOLD = "Helvetica-Bold"

# --- Colors --------------------------------------------------------------
INK = colors.HexColor("#111111")
MUTED = colors.HexColor("#555555")
FAINT = colors.HexColor("#999999")
ACCENT = colors.HexColor("#1f3a5f")
RULE = colors.HexColor("#d0d0d0")

# --- Styles --------------------------------------------------------------
name_style = ParagraphStyle(
    "name",
    fontName=SERIF_BOLD,
    fontSize=22,
    leading=26,
    textColor=INK,
    spaceAfter=2,
)
sub_style = ParagraphStyle(
    "sub",
    fontName=SERIF_ITALIC,
    fontSize=10.5,
    leading=13,
    textColor=MUTED,
    spaceAfter=2,
)
contact_style = ParagraphStyle(
    "contact",
    fontName=SANS,
    fontSize=9,
    leading=12,
    textColor=MUTED,
)
section_style = ParagraphStyle(
    "section",
    fontName=SERIF_BOLD,
    fontSize=11,
    leading=14,
    textColor=ACCENT,
    spaceBefore=10,
    spaceAfter=2,
    textTransform="uppercase",
)
entry_title_style = ParagraphStyle(
    "etitle",
    fontName=SERIF_BOLD,
    fontSize=10.5,
    leading=13.5,
    textColor=INK,
)
entry_body_style = ParagraphStyle(
    "ebody",
    fontName=SERIF,
    fontSize=10,
    leading=13,
    textColor=INK,
    spaceAfter=1,
)
entry_meta_style = ParagraphStyle(
    "emeta",
    fontName=SERIF_ITALIC,
    fontSize=9.5,
    leading=12,
    textColor=MUTED,
)
date_style = ParagraphStyle(
    "date",
    fontName=SANS,
    fontSize=9,
    leading=12,
    textColor=MUTED,
    alignment=0,  # left
)
bullet_style = ParagraphStyle(
    "bullet",
    fontName=SERIF,
    fontSize=9.5,
    leading=12.5,
    textColor=INK,
    leftIndent=10,
    bulletIndent=0,
    spaceAfter=1,
)


# --- Helpers -------------------------------------------------------------

def section(title: str):
    return [
        Spacer(1, 4),
        Paragraph(title.upper(), section_style),
        HRFlowable(width="100%", thickness=0.6, color=RULE,
                   spaceBefore=0, spaceAfter=4),
    ]


def entry(date: str, body_flowables):
    """Two-column row: [date | body]."""
    if not isinstance(body_flowables, list):
        body_flowables = [body_flowables]
    t = Table(
        [[Paragraph(date, date_style), body_flowables]],
        colWidths=[1.05 * inch, 5.55 * inch],
    )
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return KeepTogether(t)


# --- Content -------------------------------------------------------------

NAME = "Sangbum Woo"
NAME_SUB = "Woo Sangbum &middot; 우상범"
TAGLINE = "PhD Student, Autonomous Driving &amp; Robotics"

CONTACT = (
    "woosangbyum@naver.com &nbsp;&middot;&nbsp; "
    '<link href="https://github.com/sangbeom0321" color="#1f3a5f">github.com/sangbeom0321</link> &nbsp;&middot;&nbsp; '
    '<link href="https://scholar.google.co.kr/citations?user=wiKYF-gAAAAJ" color="#1f3a5f">Google Scholar</link> &nbsp;&middot;&nbsp; '
    '<link href="https://www.linkedin.com/in/woo-247368342/" color="#1f3a5f">LinkedIn</link>'
)

RESEARCH_INTERESTS = (
    "End-to-End Autonomous Driving &middot; "
    "SLAM &amp; Localization &middot; "
    "Path Planning and Decision Making &middot; "
    "Real-vehicle Autonomous Systems and Robotics"
)


def build() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(OUT),
        pagesize=LETTER,
        leftMargin=0.9 * inch,
        rightMargin=0.9 * inch,
        topMargin=0.8 * inch,
        bottomMargin=0.8 * inch,
        title="Curriculum Vitae — Sangbum Woo",
        author="Sangbum Woo",
        subject="Curriculum Vitae",
    )
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height,
        id="normal", showBoundary=0,
    )

    def on_page(canvas, _doc):
        canvas.saveState()
        canvas.setFont(SANS, 8)
        canvas.setFillColor(FAINT)
        canvas.drawString(
            doc.leftMargin,
            0.45 * inch,
            "Sangbum Woo  \u2014  Curriculum Vitae",
        )
        canvas.drawRightString(
            LETTER[0] - doc.rightMargin,
            0.45 * inch,
            f"Page {_doc.page}  \u2014  Last updated April 2026",
        )
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=on_page)])

    story = []

    # ---- Header --------------------------------------------------------
    story.append(Paragraph(NAME, name_style))
    story.append(Paragraph(NAME_SUB, sub_style))
    story.append(Paragraph(TAGLINE, sub_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(CONTACT, contact_style))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=0.8, color=INK,
                            spaceBefore=6, spaceAfter=6))

    # ---- Research interests -------------------------------------------
    story += section("Research Interests")
    story.append(Paragraph(RESEARCH_INTERESTS, entry_body_style))

    # ---- Education -----------------------------------------------------
    story += section("Education")
    story.append(entry(
        "2026 – present",
        [
            Paragraph(
                "<b>Ph.D.</b> in Automotive Engineering (AUTO Lab)",
                entry_title_style,
            ),
            Paragraph(
                "Hanyang University, Seoul, Republic of Korea",
                entry_meta_style,
            ),
            Paragraph(
                "Department of Automotive Engineering. Focus on end-to-end autonomous driving on real vehicles.",
                entry_body_style,
            ),
        ],
    ))
    story.append(entry(
        "2023 – 2026",
        [
            Paragraph(
                "<b>M.S.</b> in Computer Engineering, Future Convergence Engineering",
                entry_title_style,
            ),
            Paragraph(
                "Korea University of Technology and Education (KOREATECH)",
                entry_meta_style,
            ),
            Paragraph(
                "HPC Lab (SPIN). GPA 3.95 / 4.5.",
                entry_body_style,
            ),
        ],
    ))
    story.append(entry(
        "2019 – 2023",
        [
            Paragraph(
                "<b>B.S.</b> in Computer Science and Software",
                entry_title_style,
            ),
            Paragraph(
                "Korea University of Technology and Education (KOREATECH)",
                entry_meta_style,
            ),
            Paragraph(
                "Minor in Human Resource Development. GPA 3.31 / 4.5.",
                entry_body_style,
            ),
        ],
    ))

    # ---- Research experience ------------------------------------------
    story += section("Research Experience")
    story.append(entry(
        "2023 – 2026",
        [
            Paragraph(
                "<b>Participating Researcher</b>, Autonomous Driving SW Architecture",
                entry_title_style,
            ),
            Paragraph(
                "Korea Institute of Machinery &amp; Materials (KIMM)",
                entry_meta_style,
            ),
            Paragraph(
                "Autonomous agricultural machinery for orchards. "
                "Contributed to SLAM-based mapping, Voronoi navigation, "
                "and the end-to-end ROS 2 autonomy stack on a real UGV platform.",
                entry_body_style,
            ),
            Paragraph("\u2022 Developed topology-preserving incremental mapping for repetitive tree-row scenes.", bullet_style),
            Paragraph("\u2022 Designed Voronoi-based tree-row path planners for full-orchard coverage.", bullet_style),
            Paragraph("\u2022 Led architecture-level integration of perception, planning, and control modules on ROS 2.", bullet_style),
            Paragraph("\u2022 Conducted field experiments on a real UGV in working orchards.", bullet_style),
        ],
    ))
    story.append(entry(
        "2023 – 2026",
        [
            Paragraph(
                "<b>Graduate Research Assistant</b>",
                entry_title_style,
            ),
            Paragraph(
                "KOREATECH HPC Lab &rarr; SPIN",
                entry_meta_style,
            ),
            Paragraph(
                "SLAM parallelization, multi-robot exploration, and "
                "autonomous driving systems research.",
                entry_body_style,
            ),
            Paragraph("\u2022 Real-time map construction via parallelized SLAM pipelines.", bullet_style),
            Paragraph("\u2022 Space-partitioning-based exploration for multi-UGV teams.", bullet_style),
            Paragraph("\u2022 First-author submissions to IEEE Access and ICROS journals.", bullet_style),
        ],
    ))
    story.append(entry(
        "2021 – 2023",
        [
            Paragraph(
                "<b>President &amp; Planning/Decision Team Lead</b>",
                entry_title_style,
            ),
            Paragraph(
                "K-ROAD, KOREATECH Undergraduate Autonomous Vehicle Society",
                entry_meta_style,
            ),
            Paragraph(
                "Led the autonomous-driving undergraduate research society for three years, "
                "establishing its technical foundation and competition track record.",
                entry_body_style,
            ),
            Paragraph("\u2022 Developed planning and decision algorithms for on-campus autonomous vehicles.", bullet_style),
            Paragraph("\u2022 Silver Prize, Creative Car Competition (2022); Hyundai AD Challenge Virtual Track (2023).", bullet_style),
            Paragraph("\u2022 Mentored junior members and oversaw long-term research planning.", bullet_style),
        ],
    ))

    # ---- Publications --------------------------------------------------
    story += section("Publications")
    story.append(entry(
        "2025",
        [
            Paragraph(
                "<b>S. Woo</b>, C. Lee, and G. Jung. "
                "&ldquo;Topology-Preserving Incremental Mapping and Voronoi-Based "
                "Tree-Row Navigation for Orchard Unmanned Ground Vehicles.&rdquo;",
                entry_body_style,
            ),
            Paragraph(
                "<i>IEEE Access</i>, under review (SCIE).",
                entry_meta_style,
            ),
        ],
    ))
    story.append(entry(
        "2023",
        [
            Paragraph(
                "<b>S. Woo</b> and C. Lee. "
                "&ldquo;Space Partitioning and Path Planning for Mission Area "
                "Exploration Using Multiple UGVs.&rdquo;",
                entry_body_style,
            ),
            Paragraph(
                "<i>Journal of Institute of Control, Robotics and Systems (ICROS)</i> (SCOPUS).",
                entry_meta_style,
            ),
        ],
    ))

    # ---- Patents -------------------------------------------------------
    story += section("Patents")
    story.append(entry(
        "Registered",
        [
            Paragraph(
                "<b>Real-Time Streaming Broadcast Chat Summarization System and Method</b>",
                entry_title_style,
            ),
            Paragraph(
                "Republic of Korea, Korean Intellectual Property Office (KIPRIS).",
                entry_meta_style,
            ),
        ],
    ))

    # ---- Awards --------------------------------------------------------
    story += section("Awards &amp; Honors")
    story.append(entry(
        "2024",
        Paragraph(
            "<b>2nd Prize</b> (Korea Institute for Robot Industry Advancement President&#39;s Award) "
            "and <b>Special Prize</b>, Baemin Robot Delivery Challenge — Autonomous Driving Mission. "
            "<i>Woowa Brothers.</i>",
            entry_body_style,
        ),
    ))
    story.append(entry(
        "2022",
        Paragraph(
            "<b>Grand Prize</b>, Graduation Project Idea Competition. <i>KOREATECH.</i>",
            entry_body_style,
        ),
    ))
    story.append(entry(
        "2022",
        Paragraph(
            "<b>Best Paper Award</b>, Korea Software Congress (KSC). "
            "<i>Korean Institute of Information Scientists and Engineers (KIISE).</i>",
            entry_body_style,
        ),
    ))
    story.append(entry(
        "2022",
        Paragraph(
            "<b>Silver Prize</b>, Creative Car Competition — Autonomous Driving Division. <i>CARSA.</i>",
            entry_body_style,
        ),
    ))

    # ---- Skills --------------------------------------------------------
    story += section("Technical Skills")
    story.append(entry(
        "Languages",
        Paragraph(
            "Python, C++, C, MATLAB, TypeScript, Bash.",
            entry_body_style,
        ),
    ))
    story.append(entry(
        "Frameworks",
        Paragraph(
            "ROS / ROS 2, PyTorch, OpenCV, Point Cloud Library (PCL), Open3D, "
            "TensorRT, ONNX, NumPy / SciPy.",
            entry_body_style,
        ),
    ))
    story.append(entry(
        "Tools",
        Paragraph(
            "Linux (Ubuntu), Git, Docker, CUDA, Gazebo, CARLA Simulator, RViz, CMake, Weights &amp; Biases.",
            entry_body_style,
        ),
    ))
    story.append(entry(
        "Domains",
        Paragraph(
            "3D object detection; LiDAR&ndash;camera sensor fusion; point-cloud processing; "
            "SLAM and localization; path, behavior, and motion planning; vehicle dynamics; "
            "PID / MPC control; trajectory tracking; Kalman filtering; deep learning; computer vision.",
            entry_body_style,
        ),
    ))

    # ---- Selected projects --------------------------------------------
    story += section("Selected Projects")
    story.append(entry(
        "2023 – 2025",
        [
            Paragraph(
                "<b>Autonomous Driving for Orchard UGVs</b>",
                entry_title_style,
            ),
            Paragraph(
                "Full stack for tree-row orchards: topology-preserving mapping, "
                "Voronoi row-navigation, and ROS 2 autonomy. With KIMM.",
                entry_body_style,
            ),
        ],
    ))
    story.append(entry(
        "2024",
        [
            Paragraph(
                "<b>Baemin Robot Delivery Challenge</b>",
                entry_title_style,
            ),
            Paragraph(
                "Outdoor last-mile delivery robot, autonomous-driving mission track. "
                "2nd Prize + Special Prize.",
                entry_body_style,
            ),
        ],
    ))
    story.append(entry(
        "2023",
        [
            Paragraph(
                "<b>Hyundai Autonomous Driving Challenge — Virtual Track</b>",
                entry_title_style,
            ),
            Paragraph(
                "End-to-end autonomy stack in a high-fidelity urban simulator.",
                entry_body_style,
            ),
        ],
    ))
    story.append(entry(
        "2022",
        [
            Paragraph(
                "<b>Creative Car Competition — Autonomous Driving</b>",
                entry_title_style,
            ),
            Paragraph(
                "Self-built autonomous vehicle on a closed circuit. Silver Prize.",
                entry_body_style,
            ),
        ],
    ))

    # ---- Media coverage -----------------------------------------------
    story += section("Media Coverage &amp; Outreach")
    media_items = [
        ("2024", "&ldquo;Woowa Brothers Wraps Up Baemin Robot Delivery Challenge.&rdquo; <i>Robot News.</i>"),
        ("2023", "&ldquo;KOREATECH Excels Across Robotics and Autonomous-Driving Competitions.&rdquo; <i>Nate News.</i>"),
        ("2023", "&ldquo;KOREATECH Wins Grand and Gold Prizes at the 2023 Creative Mobility Competition.&rdquo; <i>Daejeon Today.</i>"),
        ("2023", "MBC public-relations feature on KOREATECH autonomous-driving research. <i>MBC.</i>"),
        ("2022", "&ldquo;KOREATECH Wins Gold at the International Creative Car Competition.&rdquo; <i>Daehan Economic Daily.</i>"),
    ]
    for year, text in media_items:
        story.append(entry(year, Paragraph(text, entry_body_style)))

    doc.build(story)
    print(f"Wrote {OUT}  ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()
