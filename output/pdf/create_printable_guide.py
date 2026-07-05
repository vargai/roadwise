import csv
import re
from collections import defaultdict
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "version2"
OUT = ROOT / "output" / "pdf" / "norway_printable_trip_guide.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 1.35 * cm
MARGIN_Y = 1.25 * cm
ACCENT = colors.HexColor("#1E7D73")
DARK = colors.HexColor("#24343D")
MID = colors.HexColor("#6D7B82")
LIGHT = colors.HexColor("#EEF5F3")
LINE = colors.HexColor("#CBD7D5")
WARN = colors.HexColor("#8A5A00")


def read_csv(name):
    with (DATA_DIR / name).open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def natural_day_key(day):
    m = re.search(r"Day\s+(\d+)", day or "")
    if m:
        return int(m.group(1))
    return 99


def clean_layer_title(layer, day):
    title = layer.replace("Route ", "")
    if day and title.startswith(day):
        title = title[len(day):].strip(" -:")
    return title


def route_snapshot(names):
    unique = []
    for name in names:
        if name not in unique:
            unique.append(name)
    if len(unique) <= 5:
        return " -> ".join(unique)
    return " -> ".join(unique[:2] + ["..."] + unique[-2:])


def para(text, style):
    text = "" if text is None else str(text)
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )
    return Paragraph(escaped, style)


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        "CoverTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=32,
        textColor=DARK,
        alignment=TA_LEFT,
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        "SubTitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        textColor=MID,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=21,
        textColor=DARK,
        spaceBefore=6,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=ACCENT,
        spaceBefore=8,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        "Cell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.4,
        leading=9.2,
        textColor=DARK,
    )
)
styles.add(
    ParagraphStyle(
        "CellSmall",
        parent=styles["Cell"],
        fontSize=6.7,
        leading=8.2,
    )
)
styles.add(
    ParagraphStyle(
        "CellBold",
        parent=styles["Cell"],
        fontName="Helvetica-Bold",
    )
)
styles.add(
    ParagraphStyle(
        "Note",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.8,
        leading=12,
        textColor=DARK,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        "Mini",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7,
        leading=8.5,
        textColor=MID,
    )
)
styles.add(
    ParagraphStyle(
        "Footer",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7,
        leading=8,
        textColor=MID,
        alignment=TA_CENTER,
    )
)


def draw_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    y_top = PAGE_HEIGHT - 0.85 * cm
    canvas.line(MARGIN_X, y_top, PAGE_WIDTH - MARGIN_X, y_top)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(ACCENT)
    canvas.drawString(MARGIN_X, PAGE_HEIGHT - 0.62 * cm, "Norway Road Trip Guide")
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MID)
    canvas.drawRightString(PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 0.62 * cm, "Printable plan from CSV files")
    canvas.setStrokeColor(LINE)
    canvas.line(MARGIN_X, 0.82 * cm, PAGE_WIDTH - MARGIN_X, 0.82 * cm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MID)
    canvas.drawCentredString(PAGE_WIDTH / 2, 0.48 * cm, f"Page {doc.page}")
    canvas.restoreState()


def draw_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_HEIGHT - 4.0 * cm, PAGE_WIDTH, 4.0 * cm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(MARGIN_X, PAGE_HEIGHT - 1.25 * cm, "Bergen - Aurland - Stryn - Vaksdal")
    canvas.setStrokeColor(colors.white)
    canvas.setLineWidth(1)
    canvas.line(MARGIN_X, PAGE_HEIGHT - 3.6 * cm, PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 3.6 * cm)
    canvas.restoreState()


def make_table(headers, rows, widths, small=False):
    cell_style = styles["CellSmall"] if small else styles["Cell"]
    data = [[para(h, styles["CellBold"]) for h in headers]]
    for row in rows:
        data.append([para(value, cell_style) for value in row])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("TEXTCOLOR", (0, 0), (-1, 0), DARK),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFCFC")]),
            ]
        )
    )
    return table


def callout(title, lines, color=ACCENT):
    data = [[para(title, styles["CellBold"])]]
    data.extend([[para(line, styles["Note"])] for line in lines])
    t = Table(data, colWidths=[PAGE_WIDTH - 2 * MARGIN_X], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.7, color),
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return t


def notes_block():
    rows = [["Notes", ""]]
    for _ in range(4):
        rows.append(["", ""])
    t = Table(rows, colWidths=[2.3 * cm, PAGE_WIDTH - 2 * MARGIN_X - 2.3 * cm], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("SPAN", (0, 1), (0, -1)),
                ("TEXTCOLOR", (0, 0), (0, 0), MID),
                ("FONTNAME", (0, 0), (0, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#D8E1DF")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F7FAF9")),
                ("ROWHEIGHT", (0, 1), (-1, -1), 0.75 * cm),
            ]
        )
    )
    return t


def route_files():
    return sorted(DATA_DIR.glob("[0-9][0-9]_Route_*.csv"))


def build_story():
    accommodations = read_csv("01_Accommodation.csv")
    must = read_csv("02_Must_See_Points.csv")
    optional = read_csv("03_Optional_Points.csv")
    ferries = read_csv("04_Ferries.csv")
    ev = read_csv("05_EV_Hubs.csv")
    routes = []
    for file in route_files():
        rows = read_csv(file.name)
        if rows:
            routes.append((file.name, rows[0]["Layer"], rows[0]["Day"], rows))

    story = [NextPageTemplate("Normal")]
    story.append(Spacer(1, 4.2 * cm))
    story.append(para("Norway Road Trip Printable Guide", styles["CoverTitle"]))
    story.append(para("July 6-13 | Bergen, Aurland, Laerdalsoyri, Stryn, Geiranger option, Vaksdal, Bergen Airport", styles["SubTitle"]))
    story.append(
        callout(
            "Use this on paper",
            [
                "Treat distances and times as planning estimates from the CSVs, not live navigation.",
                "Before each driving day, verify ferry times, weather, road closures, charger status and rental-car return charge rules.",
                "Day 7 has two routes: scenic Vikafjell in good weather, or the E39 backup if conditions are poor.",
            ],
        )
    )
    story.append(Spacer(1, 0.35 * cm))

    overview_rows = []
    for _, layer, day, rows in routes:
        names = [r["Name"] for r in rows]
        approx = rows[-1].get("Approx_Time", "")
        overview_rows.append([day, clean_layer_title(layer, day), route_snapshot(names), approx])
    story.append(make_table(["Day", "Plan", "Route Snapshot", "End / Timing"], overview_rows, [1.5 * cm, 4.2 * cm, 7.5 * cm, 4.5 * cm], small=True))
    story.append(PageBreak())

    story.append(para("Accommodation Checkpoints", styles["H1"]))
    acc_rows = [
        [
            a["Day"],
            a["Name"],
            a["Address"],
            a["Approx_Time"],
            a["Notes"],
        ]
        for a in accommodations
    ]
    story.append(make_table(["Night", "Stay", "Address", "Length", "Confirmation / Details"], acc_rows, [1.5 * cm, 3.2 * cm, 4.2 * cm, 1.8 * cm, 7.0 * cm], small=True))
    story.append(Spacer(1, 0.3 * cm))
    story.append(
        callout(
            "Check before leaving each stay",
            [
                "Keys, chargers/cables, passports, wallet, medicine, and printed confirmations.",
                "Photos of parking location and self-check-in instructions can save time later.",
            ],
        )
    )
    story.append(PageBreak())

    highlights_by_day = defaultdict(list)
    for row in must + optional:
        highlights_by_day[row["Day"]].append(row)

    for _, layer, day, rows in routes:
        story.append(KeepTogether([para(f"{day}: {clean_layer_title(layer, day)}", styles["H1"])]))
        first, last = rows[0], rows[-1]
        summary_lines = [
            f"Start: {first['Name']} | Finish: {last['Name']}",
            f"Expected finish/timing note: {last.get('Approx_Time', '')}",
        ]
        if "Backup" in day or "Backup" in layer:
            summary_lines.append("Backup route: use when Vikafjell weather or road conditions are not favorable.")
        story.append(callout("Day Summary", summary_lines, WARN if "Backup" in day or "Backup" in layer else ACCENT))
        story.append(Spacer(1, 0.2 * cm))
        route_rows = []
        for r in rows:
            km_time = " / ".join(x for x in [r.get("Approx_Km", ""), r.get("Approx_Time", "")] if x)
            route_rows.append([r["Order"], r["Name"], r["Type"], r["Priority"], km_time, r["Notes"]])
        story.append(make_table(["#", "Stop", "Type", "Priority", "Km / Time", "Notes"], route_rows, [0.7 * cm, 3.2 * cm, 2.7 * cm, 2.1 * cm, 3.0 * cm, 6.0 * cm], small=True))

        if highlights_by_day.get(day):
            story.append(Spacer(1, 0.2 * cm))
            h_rows = [[h["Name"], h["Priority"], h["Approx_Time"], h["Notes"]] for h in highlights_by_day[day]]
            story.append(make_table(["Highlight", "Priority", "Time", "Planning Note"], h_rows, [4.0 * cm, 2.7 * cm, 3.0 * cm, 8.0 * cm], small=True))

        story.append(Spacer(1, 0.25 * cm))
        story.append(notes_block())
        story.append(PageBreak())

    story.append(para("Ferry Reference", styles["H1"]))
    ferry_rows = [[f["Day"], f["Name"], f["Priority"], f["Approx_Time"], f["Notes"]] for f in ferries]
    story.append(make_table(["Day", "Ferry", "Priority", "Time", "Notes"], ferry_rows, [3.0 * cm, 4.2 * cm, 2.5 * cm, 3.2 * cm, 4.8 * cm], small=True))
    story.append(Spacer(1, 0.35 * cm))
    story.append(para("EV Charging Reference", styles["H1"]))
    ev_rows = [[e["Day"], e["Name"], e["Priority"], e["Notes"]] for e in ev]
    story.append(make_table(["Day", "Hub", "Priority", "Notes"], ev_rows, [3.2 * cm, 4.2 * cm, 2.4 * cm, 7.9 * cm], small=True))
    story.append(PageBreak())

    story.append(para("Must-See And Optional Stops", styles["H1"]))
    must_rows = [[m["Day"], m["Name"], m["Type"], m["Priority"], m["Approx_Time"], m["Notes"]] for m in must]
    story.append(make_table(["Day", "Stop", "Type", "Priority", "Time", "Notes"], must_rows, [2.8 * cm, 3.4 * cm, 2.8 * cm, 2.5 * cm, 2.5 * cm, 3.7 * cm], small=True))
    story.append(Spacer(1, 0.3 * cm))
    optional_rows = [[o["Day"], o["Name"], o["Type"], o["Priority"], o["Approx_Time"], o["Notes"]] for o in optional]
    story.append(make_table(["Day", "Optional Stop", "Type", "Priority", "Time", "Notes"], optional_rows, [2.8 * cm, 3.4 * cm, 2.8 * cm, 2.5 * cm, 2.5 * cm, 3.7 * cm], small=True))

    return story


def build_pdf():
    frame = Frame(
        MARGIN_X,
        MARGIN_Y,
        PAGE_WIDTH - 2 * MARGIN_X,
        PAGE_HEIGHT - 2.2 * MARGIN_Y,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
        id="main",
    )
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        rightMargin=MARGIN_X,
        leftMargin=MARGIN_X,
        topMargin=MARGIN_Y,
        bottomMargin=MARGIN_Y,
        title="Norway Road Trip Printable Guide",
        author="Codex",
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="Cover", frames=[frame], onPage=draw_cover),
            PageTemplate(id="Normal", frames=[frame], onPage=draw_header_footer),
        ]
    )
    doc.build(build_story())


if __name__ == "__main__":
    build_pdf()
    print(OUT)
