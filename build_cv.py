from html import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


OUT = "CV_Zihao_Zhang_en.pdf"
PAGE_W, PAGE_H = A4
MARGIN_X = 18 * mm
MARGIN_TOP = 13 * mm
MARGIN_BOTTOM = 12 * mm
INK = colors.HexColor("#101525")
MUTED = colors.HexColor("#657080")
SOFT = colors.HexColor("#7E897C")
ACCENT_HEX = "#4F7FA6"
LINE = colors.HexColor("#D9E5EF")
PANEL = colors.HexColor("#F6F9FC")

YU_GANG_JIANG_SCHOLAR = "https://scholar.google.com/citations?user=f3_FP8AAAAAJ&hl=zh-CN&authuser=1&oi=ao"
ZUXUAN_WU_SCHOLAR = "https://scholar.google.com/citations?user=7t12hVkAAAAJ&hl=zh-CN&authuser=1"
HANG_XU_SCHOLAR = "https://scholar.google.com/citations?user=J_8TX6sAAAAJ&hl=zh-CN&authuser=1&oi=ao"


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="Name",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=25,
    leading=26,
    textColor=INK,
    spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="Subhead",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.8,
    leading=11.5,
    textColor=MUTED,
))
styles.add(ParagraphStyle(
    name="Section",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=12,
    textColor=INK,
    spaceBefore=4,
    spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Meta",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.2,
    leading=11,
    textColor=SOFT,
))
styles.add(ParagraphStyle(
    name="Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.7,
    leading=11.6,
    textColor=MUTED,
    spaceAfter=1.5,
))
styles.add(ParagraphStyle(
    name="BodyInk",
    parent=styles["Body"],
    textColor=INK,
))
styles.add(ParagraphStyle(
    name="Summary",
    parent=styles["Body"],
    fontSize=8.5,
    leading=11.2,
    textColor=INK,
    spaceAfter=1,
))
styles.add(ParagraphStyle(
    name="ThemeTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=8.1,
    leading=10,
    textColor=INK,
    spaceAfter=1.5,
))
styles.add(ParagraphStyle(
    name="ThemeBody",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.6,
    leading=9.5,
    textColor=MUTED,
))
styles.add(ParagraphStyle(
    name="Contribution",
    parent=styles["Body"],
    fontSize=8.25,
    leading=10.7,
    leftIndent=7,
    firstLineIndent=-7,
    spaceAfter=1.5,
))
styles.add(ParagraphStyle(
    name="PaperTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=9.2,
    leading=11.6,
    textColor=INK,
    spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="PaperMeta",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.2,
    leading=10.4,
    textColor=MUTED,
))


def P(text, style="Body"):
    return Paragraph(text, styles[style])


def external_link(text, url):
    return f"<link href='{escape(url, quote=True)}'>{escape(text)}</link>"


def section(title):
    return [P(title.upper(), "Section")]


def themes(items):
    cells = []
    for title, description in items:
        cells.append([
            P(title, "ThemeTitle"),
            P(description, "ThemeBody"),
        ])
    table = Table([cells], colWidths=[58.3 * mm] * 3, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PANEL),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def honor(date, title, detail):
    left = P(f"<b>{date}</b>", "Meta")
    right = P(f"<b>{title}</b> · {detail}", "Body")
    table = Table([[left, right]], colWidths=[31 * mm, 144 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return table


def experience(date, title, company, detail, bullets):
    left = P(f"<b>{date}</b>", "Meta")
    right_parts = [P(f"{title} · <b>{company}</b>", "BodyInk"), P(detail, "Meta")]
    for bullet in bullets:
        right_parts.append(P(f"• {bullet}", "Body"))
    table = Table([[left, right_parts]], colWidths=[31 * mm, 144 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def education(date, degree, school, location, detail):
    left = P(f"<b>{date}</b>", "Meta")
    right = [P(f"<b>{school}</b>", "BodyInk"), P(f"{degree} · {location}", "Meta"), P(detail, "Body")]
    table = Table([[left, right]], colWidths=[31 * mm, 144 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def publication(number, title, authors, venue):
    left = P(f"<font color='#7E897C'><b>{number:02d}</b></font>", "Meta")
    right = [P(title, "PaperTitle"), P(authors, "PaperMeta"), P(venue, "PaperMeta")]
    table = Table([[left, right]], colWidths=[11 * mm, 164 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return table


def internship(date, company, team, location, projects):
    left = P(f"<b>{date}</b>", "Meta")
    right = [P(f"Research Intern · <b>{company}</b>", "BodyInk"), P(f"{team} · {location}", "Meta")]
    for title, note, contributions in projects:
        right.append(P(f"<b>{title}</b> — {note}", "BodyInk"))
        for contribution in contributions:
            right.append(P(f"<font color='{ACCENT_HEX}'>•</font>&nbsp;&nbsp;{contribution}", "Contribution"))
        right.append(Spacer(1, 2))
    table = Table([[left, right]], colWidths=[31 * mm, 144 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether(table)


def draw_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN_X, PAGE_H - 11 * mm, PAGE_W - MARGIN_X, PAGE_H - 11 * mm)
    canvas.setFillColor(SOFT)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(MARGIN_X, 9 * mm, "Zihao Zhang · Curriculum Vitae")
    canvas.drawRightString(PAGE_W - MARGIN_X, 9 * mm, f"{doc.page}")
    canvas.restoreState()


class CVDocTemplate(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(filename, pagesize=A4, leftMargin=MARGIN_X, rightMargin=MARGIN_X, topMargin=15 * mm, bottomMargin=10 * mm)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=draw_page)])


story = []
story += [P("Zihao Zhang", "Name")]
story += [P(
    "Master's Student at Fudan University · Advisors: "
    f"{external_link('Prof. Yu-Gang Jiang', YU_GANG_JIANG_SCHOLAR)} &amp; "
    f"{external_link('Prof. Zuxuan Wu', ZUXUAN_WU_SCHOLAR)}",
    "Subhead",
)]
story += [P("Shanghai, China  ·  <link href='mailto:bbldcver@gmail.com'>bbldcver@gmail.com</link>  ·  <link href='https://github.com/bbldCVer'>GitHub</link>  ·  <link href='https://scholar.google.com/citations?hl=zh-CN&amp;authuser=1&amp;user=_7r2J74AAAAJ'>Google Scholar</link>", "Subhead")]
story += [Spacer(1, 5)]

story += section("Research Profile")
story += [P(
    "Researcher at the intersection of <b>embodied intelligence</b> and generative visual modeling. I develop controllable and efficient video models for camera-aware scene evolution, large-motion temporal prediction, and human-motion editing—visual foundations for embodied agents. First/co-first author at CVPR 2025 and ACM MM 2026, with seven publications across CVPR, ICCV, ACM MM, SIGGRAPH Asia, and ICASSP.",
    "Summary",
)]

story += section("Research Themes")
story += [themes([
    (
        "Generative World Models",
        "Camera- and motion-conditioned video synthesis for modeling how scenes evolve under embodied viewpoints and interactions.",
    ),
    (
        "Spatial &amp; Motion Intelligence",
        "Multimodal spatial reasoning, camera planning, large motion, and temporally coherent scene understanding.",
    ),
    (
        "Efficient Visual Generation",
        "One-step pixel diffusion and lightweight control for scalable, high-resolution visual-dynamics simulation.",
    ),
])]

story += section("Education")
story += [education(
    "Sep 2023 — Jun 2026",
    "Master's Degree",
    "Fudan University (QS 26)",
    "Shanghai, China",
    "School of Computer Science · GPA: 3.5 · Advisors: "
    f"{external_link('Prof. Yu-Gang Jiang', YU_GANG_JIANG_SCHOLAR)} &amp; "
    f"{external_link('Prof. Zuxuan Wu', ZUXUAN_WU_SCHOLAR)}",
)]
story += [education("Sep 2018 — Jun 2022", "Bachelor's Degree", "Wuhan University (QS 165)", "Wuhan, China", "School of Chemistry and Molecular Sciences")]

story += section("Awards &amp; Honors")
story += [honor("2025", "First-Class Academic Scholarship", "Fudan University")]
story += [honor("2020 &amp; 2021", "First-Class Scholarship and Grant", "Wuhan University")]
story += [honor("2025", "EDEN Patent Application", "Huawei Noah's Ark Lab · Large-motion video frame interpolation")]

story += section("Research Experience")
story += [internship(
    "Apr 2025 — Mar 2026",
    "BiliBili Inc.",
    "Virtual Human Group",
    "Shanghai, China",
    [
        (
            "SPEED: One-Step Pixel Diffusion for High-quality Video Frame Interpolation",
            "Co-first author, ACM MM 2026",
            [
                "Led the one-step pixel-space diffusion framework and designed a progressive multi-stage DiT, Noise-Update-Only Attention, and Drift-aware Timestep Sampling to learn motion, structure, and appearance from coarse to fine.",
                "Achieved state-of-the-art visual-dynamics prediction: 8.8% lower LPIPS on SNU-FILM, 63.3% faster inference, 10.6% less memory, and up to 51.5% lower LPIPS on 4K benchmarks.",
            ],
        ),
        (
            "CT-1: Vision-Language-Camera Models for Camera-Controllable Video Generation",
            "Co-first author, ACM MM 2026",
            [
                "Co-developed a Vision-Language-Camera model that grounds visual observations and language instructions in SE(3) camera trajectories, enabling spatially aware and temporally stable viewpoint planning.",
                "Contributed to the CT-200K curation pipeline (>47M frames) and controllable video-diffusion system, improving camera-control success by 25.7% and advancing spatially grounded generative world modeling.",
            ],
        ),
    ],
)]
story += [internship(
    "Jul 2024 — Mar 2025",
    "Huawei",
    f"Noah's Ark Lab · Advised by {external_link('Hang Xu', HANG_XU_SCHOLAR)}",
    "Shanghai, China",
    [
        (
            "EDEN: Enhanced Diffusion for High-quality Large-motion Video Frame Interpolation",
            "First author, CVPR 2025",
            [
                "Led EDEN's architecture and training, developing a Transformer Tokenizer, dual-stream temporal attention, and frame-difference conditioning for large, nonlinear motion.",
                "Reduced LPIPS by nearly 10% on DAVIS and SNU-FILM and by about 8% on DAIN-HD, improving high-fidelity temporal state prediction under fast scene changes.",
            ],
        ),
        (
            "MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion",
            "Third author, ICCV 2025",
            [
                "Contributed lightweight pose/reference controllers and two-branch score guidance to transfer target body motion while retaining subject identity, background details, and camera dynamics.",
                "Reduced GPU memory by approximately 80% versus MotionEditor while improving videos with large camera motion and complex backgrounds, enabling efficient motion-conditioned human-scene synthesis.",
            ],
        ),
    ],
)]

story += [PageBreak()]
story += [P("Publications", "Name"), Spacer(1, 6)]
story += [publication(1, "EDEN: Enhanced Diffusion for High-quality Large-motion Video Frame Interpolation", "<b>Zihao Zhang</b>, Haoran Chen, Haoyu Zhao, Guansong Lu, Yanwei Fu, Hang Xu, Zuxuan Wu", "CVPR 2025")]
story += [publication(2, "SPEED: One-Step Pixel Diffusion for High-quality Video Frame Interpolation", "<b>Zihao Zhang*</b>, Haoyu Zhao*, Siqian Yang, Yidi Wu, Yudong Jiang, Zuxuan Wu", "ACM MM 2026")]
story += [publication(3, "CT-1: Vision-Language-Camera Models Transfer Spatial Reasoning Knowledge to Camera-Controllable Video Generation", "Haoyu Zhao*, <b>Zihao Zhang*</b>, Jiaxi Gu, Haoran Chen, Qingping Zheng, Pin Tang, Yeying Jin, Yuang Zhang, Junqi Cheng, Zenghui Lu, Peng Shu, Zuxuan Wu, Yu-Gang Jiang", "ACM MM 2026")]
story += [publication(4, "MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion", "Shuyuan Tu, Qi Dai, <b>Zihao Zhang</b>, Sicheng Xie, Zhi-Qi Cheng, Chong Luo, Xintong Han, Zuxuan Wu, Yu-Gang Jiang", "ICCV 2025")]
story += [publication(5, "VIDiff: Translating Videos via Multi-Modal Instructions with Diffusion Models", "Zhen Xing, Qi Dai, <b>Zihao Zhang</b>, Hui Zhang, Han Hu, Zuxuan Wu, Yu-Gang Jiang", "arXiv:2311.18837, 2023")]
story += [publication(6, "AniME: Adaptive Multi-Agent Planning for Long Animation Generation", "Lisai Zhang, Baohan Xu, Siqian Yang, Mingyu Yin, Jing Liu, Chao Xu, Siqi Wang, Yidi Wu, Yuxin Hong, <b>Zihao Zhang</b>, Yanzhang Liang, Yudong Jiang", "SIGGRAPH Asia 2025 Posters")]
story += [publication(7, "EVA: Enhancing Anime Video Generation via Reinforcement Learning", "Yidi Wu, Bingwen Zhu, <b>Zihao Zhang</b>, Siqian Yang, Lisai Zhang, Baohan Xu, Mingyu Yin, Yanzhang Liang, Yudong Jiang", "ICASSP 2026")]

CVDocTemplate(OUT).build(story)
print(OUT)
