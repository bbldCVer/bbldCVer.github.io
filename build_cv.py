from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
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
LINE = colors.HexColor("#DDE1DD")
LIME = colors.HexColor("#C8F169")


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
    spaceBefore=5,
    spaceAfter=4,
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
    fontSize=8.35,
    leading=10.8,
    textColor=MUTED,
    spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="BodyInk",
    parent=styles["Body"],
    textColor=INK,
))
styles.add(ParagraphStyle(
    name="PaperTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=8.35,
    leading=10.2,
    textColor=INK,
    spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="PaperMeta",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.5,
    leading=9.2,
    textColor=MUTED,
))


def P(text, style="Body"):
    return Paragraph(text, styles[style])


def section(title):
    return [P(title.upper(), "Section")]


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
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


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
        super().__init__(filename, pagesize=A4, leftMargin=MARGIN_X, rightMargin=MARGIN_X, topMargin=17 * mm, bottomMargin=12 * mm)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=draw_page)])


story = []
story += [P("Zihao Zhang", "Name")]
story += [P("Master's Student at Fudan University · Advisor: Prof. Zuxuan Wu", "Subhead")]
story += [P("Shanghai, China  ·  <link href='mailto:bbldcver@gmail.com'>bbldcver@gmail.com</link>  ·  <link href='https://github.com/bbldCVer'>GitHub</link>  ·  <link href='https://scholar.google.com/citations?hl=zh-CN&amp;authuser=1&amp;user=_7r2J74AAAAJ'>Google Scholar</link>", "Subhead")]
story += [Spacer(1, 5)]
story += [P("RESEARCH PROFILE", "Section")]
story += [P("My research focuses on efficient and controllable video generation, spatiotemporal modeling, and post-training methods for generative video models. I study diffusion-based video frame interpolation, motion editing, camera-controllable generation, and reinforcement learning with on-policy distillation.", "Body")]

story += section("Education")
story += [education("Sep 2023 — Jun 2026", "Master's degree in Computer Science", "Fudan University", "Shanghai, China", "School of Computer Science · Advisor: Prof. Zuxuan Wu")]
story += [education("Sep 2018 — Jun 2022", "Undergraduate study", "Wuhan University", "Wuhan, China", "School of Chemistry and Molecular Sciences")]

story += section("Research experience")
story += [experience("Apr 2025 — Jan 2026", "Algorithm Intern", "BiliBili Inc.", "Virtual Human Group · Shanghai, China", ["Efficient and controllable visual generation with reinforcement learning."])]
story += [experience("Jul 2024 — Mar 2025", "Algorithm Intern", "Huawei", "Noah's Ark Lab · Shanghai, China", ["Controllable image and video generation."])]

story += section("Research directions")
story += [experience("Oct 2023 — Present", "Efficient and Controllable Video Generation & Spatiotemporal Modeling", "", "", ["Diffusion-based video frame interpolation, motion editing, and camera-controllable generation, with an emphasis on temporal consistency, structural alignment, and high-frequency detail fidelity.", "Multimodal conditioning, spatial reasoning, start/end-frame control, human-pose and camera-trajectory control, pixel-space modeling, one-step generation, and lightweight network design."])]
story += [experience("Jan 2026 — Present", "Reinforcement Learning & On-Policy Distillation for Video Generation", "", "", ["Multi-dimensional reward feedback and student-distribution teacher supervision to improve generation quality, motion, and temporal consistency while reducing train–inference distribution shift."])]

story += section("Selected publications")
story += [publication(1, "EDEN: Enhanced Diffusion for High-quality Large-motion Video Frame Interpolation", "<b>Zihao Zhang</b>, Haoran Chen, Haoyu Zhao, Guansong Lu, Yanwei Fu, Hang Xu, Zuxuan Wu", "CVPR 2025")]
story += [publication(2, "SPEED: One-Step Pixel Diffusion for High-quality Video Frame Interpolation", "<b>Zihao Zhang</b>, Haoyu Zhao, Siqian Yang, Yidi Wu, Yudong Jiang, Zuxuan Wu", "ACM MM 2026")]
story += [publication(3, "CT-1: Vision-Language-Camera Models Transfer Spatial Reasoning Knowledge to Camera-Controllable Video Generation", "Haoyu Zhao*, <b>Zihao Zhang*</b>, Jiaxi Gu, Haoran Chen, Qingping Zheng, Pin Tang, Yeying Jin, Yuang Zhang, Junqi Cheng, Zenghui Lu, Peng Shu, Zuxuan Wu, Yu-Gang Jiang", "ACM MM 2026")]
story += [publication(4, "MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion", "Shuyuan Tu, Qi Dai, <b>Zihao Zhang</b>, Sicheng Xie, Zhi-Qi Cheng, Chong Luo, Xintong Han, Zuxuan Wu, Yu-Gang Jiang", "ICCV 2025")]
story += [publication(5, "VIDiff: Translating Videos via Multi-Modal Instructions with Diffusion Models", "Zhen Xing, Qi Dai, <b>Zihao Zhang</b>, Hui Zhang, Han Hu, Zuxuan Wu, Yu-Gang Jiang", "arXiv:2311.18837, 2023")]
story += [publication(6, "AniME: Adaptive Multi-Agent Planning for Long Animation Generation", "Lisai Zhang, Baohan Xu, Siqian Yang, Mingyu Yin, Jing Liu, Chao Xu, Siqi Wang, Yidi Wu, Yuxin Hong, <b>Zihao Zhang</b>, Yanzhang Liang, Yudong Jiang", "SIGGRAPH Asia 2025 Posters")]
story += [publication(7, "EVA: Enhancing Anime Video Generation via Reinforcement Learning", "Yidi Wu, Bingwen Zhu, <b>Zihao Zhang</b>, Siqian Yang, Lisai Zhang, Baohan Xu, Mingyu Yin, Yanzhang Liang, Yudong Jiang", "ICASSP 2026")]

CVDocTemplate(OUT).build(story)
print(OUT)
