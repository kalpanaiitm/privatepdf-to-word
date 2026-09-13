from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def make_sample_pdf() -> bytes:
    output = BytesIO()
    page = canvas.Canvas(output, pagesize=A4)
    page.setTitle("PrivatePDF fictional sample")
    page.setFont("Helvetica-Bold", 16)
    page.drawString(72, 780, "Fictional Project Summary")
    page.setFont("Helvetica", 11)
    lines = [
        "This fictional document is provided only to test PrivatePDF to Word.",
        "It contains selectable text and no personal or confidential information.",
        "The converter should create an editable Word document from this page.",
        "Always review converted documents for missing content and layout changes.",
    ]
    y = 745
    for line in lines:
        page.drawString(72, y, line)
        y -= 22
    page.save()
    return output.getvalue()
