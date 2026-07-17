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
    fontSize=8.7,
    leading=11.6,
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
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return table


def internship(date, company, team, location, projects):
    left = P(f"<b>{date}</b>", "Meta")
    right = [P(f"<b>{company}</b>", "BodyInk"), P(f"{team} · {location}", "Meta")]
    for title, note, description in projects:
        right.append(P(f"<b>{title}</b> — {note}", "BodyInk"))
        right.append(P(description, "Body"))
        right.append(Spacer(1, 3))
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
        super().__init__(filename, pagesize=A4, leftMargin=MARGIN_X, rightMargin=MARGIN_X, topMargin=17 * mm, bottomMargin=12 * mm)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=draw_page)])


story = []
story += [P("Zihao Zhang", "Name")]
story += [P("Master's Student at Fudan University · Advisor: Prof. Zuxuan Wu", "Subhead")]
story += [P("Shanghai, China  ·  <link href='mailto:bbldcver@gmail.com'>bbldcver@gmail.com</link>  ·  <link href='https://github.com/bbldCVer'>GitHub</link>  ·  <link href='https://scholar.google.com/citations?hl=zh-CN&amp;authuser=1&amp;user=_7r2J74AAAAJ'>Google Scholar</link>", "Subhead")]
story += [Spacer(1, 7)]

story += section("Education")
story += [education("Sep 2023 — Jun 2026", "Master's Degree", "Fudan University", "Shanghai, China", "School of Computer Science · Advisor: Prof. Zuxuan Wu")]
story += [education("Sep 2018 — Jun 2022", "Bachelor's Degree", "Wuhan University", "Wuhan, China", "School of Chemistry and Molecular Sciences")]

story += section("Research Experience")
story += [internship(
    "Apr 2025 — Mar 2026",
    "BiliBili Inc.",
    "Virtual Human Group · Image and Video Generation",
    "Shanghai, China",
    [
        (
            "SPEED: One-Step Pixel Diffusion for High-quality Video Frame Interpolation",
            "Co-first author, ACM MM 2026",
            "Led model design, training optimization, and experimental validation. Proposed a one-step pixel-space diffusion framework to address detail loss from latent compression and the cost of multi-step sampling. Designed a progressive multi-stage DiT, Noise-Update-Only Attention, and Drift-aware Timestep Sampling. SPEED runs 63.3% faster with 10.6% lower memory usage than prior diffusion baselines, supports 4K interpolation, and substantially improves high-frequency detail fidelity.",
        ),
        (
            "CT-1: Vision-Language-Camera Models for Camera-Controllable Video Generation",
            "Co-first author, ACM MM 2026",
            "Contributed to the Vision-Language-Camera model, training-data pipeline, and video-generation system. Transferred spatial reasoning from vision-language models to camera-trajectory prediction and video diffusion. Helped construct CT-200K with more than 47 million frames, improving camera-control accuracy by 25.7% over prior methods.",
        ),
    ],
)]
story += [internship(
    "Jul 2024 — Mar 2025",
    "Huawei",
    "Noah's Ark Lab · Image and Video Generation",
    "Shanghai, China",
    [
        (
            "EDEN: Enhanced Diffusion for High-quality Large-motion Video Frame Interpolation",
            "First author, CVPR 2025",
            "Led framework design, training, and evaluation. Introduced a Transformer Tokenizer to strengthen intermediate-frame representations, together with temporal attention and start/end-frame difference conditioning in the Diffusion Transformer. EDEN improves spatiotemporal consistency under complex nonlinear motion, reducing LPIPS by nearly 10% on DAVIS and SNU-FILM and by about 8% on the high-resolution DAIN-HD benchmark.",
        ),
        (
            "MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion",
            "Third author, ICCV 2025",
            "Contributed to diffusion-based video motion editing with lightweight pose and appearance controllers and dual-branch score guidance. The method preserves subject appearance and background consistency while modifying motion, reduces GPU memory usage by approximately 80%, and supports large human and camera motions.",
        ),
    ],
)]

story += [PageBreak()]
story += [P("Publications", "Name"), Spacer(1, 6)]
story += [publication(1, "EDEN: Enhanced Diffusion for High-quality Large-motion Video Frame Interpolation", "<b>Zihao Zhang</b>, Haoran Chen, Haoyu Zhao, Guansong Lu, Yanwei Fu, Hang Xu, Zuxuan Wu", "CVPR 2025")]
story += [publication(2, "SPEED: One-Step Pixel Diffusion for High-quality Video Frame Interpolation", "<b>Zihao Zhang*</b>, Haoyu Zhao*, Siqian Yang, Yidi Wu, Yudong Jiang, Zuxuan Wu", "ACM MM 2026 · * Equal contribution")]
story += [publication(3, "CT-1: Vision-Language-Camera Models Transfer Spatial Reasoning Knowledge to Camera-Controllable Video Generation", "Haoyu Zhao*, <b>Zihao Zhang*</b>, Jiaxi Gu, Haoran Chen, Qingping Zheng, Pin Tang, Yeying Jin, Yuang Zhang, Junqi Cheng, Zenghui Lu, Peng Shu, Zuxuan Wu, Yu-Gang Jiang", "ACM MM 2026")]
story += [publication(4, "MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion", "Shuyuan Tu, Qi Dai, <b>Zihao Zhang</b>, Sicheng Xie, Zhi-Qi Cheng, Chong Luo, Xintong Han, Zuxuan Wu, Yu-Gang Jiang", "ICCV 2025")]
story += [publication(5, "VIDiff: Translating Videos via Multi-Modal Instructions with Diffusion Models", "Zhen Xing, Qi Dai, <b>Zihao Zhang</b>, Hui Zhang, Han Hu, Zuxuan Wu, Yu-Gang Jiang", "arXiv:2311.18837, 2023")]
story += [publication(6, "AniME: Adaptive Multi-Agent Planning for Long Animation Generation", "Lisai Zhang, Baohan Xu, Siqian Yang, Mingyu Yin, Jing Liu, Chao Xu, Siqi Wang, Yidi Wu, Yuxin Hong, <b>Zihao Zhang</b>, Yanzhang Liang, Yudong Jiang", "SIGGRAPH Asia 2025 Posters")]
story += [publication(7, "EVA: Enhancing Anime Video Generation via Reinforcement Learning", "Yidi Wu, Bingwen Zhu, <b>Zihao Zhang</b>, Siqian Yang, Lisai Zhang, Baohan Xu, Mingyu Yin, Yanzhang Liang, Yudong Jiang", "ICASSP 2026")]

CVDocTemplate(OUT).build(story)
print(OUT)
