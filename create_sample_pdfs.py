#!/usr/bin/env python3
"""
Create sample PDF files for testing
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from pathlib import Path


def create_article_pdf(filename, title, content_pages=3):
    """Create a sample article PDF"""
    doc = SimpleDocTemplate(str(filename), pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 0.5*cm))

    # Author and Date
    story.append(Paragraph("Autor: Max Mustermann", styles['Normal']))
    story.append(Paragraph("Datum: 22. Januar 2026", styles['Normal']))
    story.append(Spacer(1, 1*cm))

    # Content
    for page in range(content_pages):
        story.append(Paragraph(f"Kapitel {page + 1}", styles['Heading1']))
        story.append(Spacer(1, 0.3*cm))

        content = f"""
        Dies ist ein Beispiel-Artikel zum Testen der PDF-Verarbeitungstools.
        Dieser Text demonstriert die Extraktion von Inhalten aus PDF-Dateien.

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

        Seite {page + 1} von {content_pages}
        """

        story.append(Paragraph(content, styles['Normal']))
        story.append(Spacer(1, 0.5*cm))

        # Add a simple table on page 2
        if page == 1:
            data = [
                ['Kategorie', 'Wert', 'Status'],
                ['Artikel', '42', 'Aktiv'],
                ['Downloads', '1.337', 'Steigend'],
                ['Bewertung', '4.5/5', 'Gut'],
            ]
            t = Table(data)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            story.append(t)
            story.append(Spacer(1, 0.5*cm))

    doc.build(story)
    print(f"Created: {filename}")


def main():
    output_dir = Path("/home/user/APT/pdfs/input")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create sample PDFs
    create_article_pdf(
        output_dir / "artikel1.pdf",
        "Einführung in die PDF-Verarbeitung",
        content_pages=3
    )

    create_article_pdf(
        output_dir / "artikel2.pdf",
        "Fortgeschrittene Techniken",
        content_pages=2
    )

    create_article_pdf(
        output_dir / "artikel3.pdf",
        "Best Practices und Tipps",
        content_pages=4
    )

    print("\n" + "="*60)
    print("3 Beispiel-PDFs wurden erstellt in: pdfs/input/")
    print("="*60)
    print("\nDu kannst sie jetzt mit den Tools verarbeiten:")
    print("- python src/pdf_extractor.py pdfs/input/artikel1.pdf --print")
    print("- python src/pdf_merger.py pdfs/input/*.pdf -o pdfs/output/alle.pdf -v")
    print("- python src/pdf_splitter.py pdfs/input/artikel3.pdf -o pdfs/output/ -v")


if __name__ == '__main__':
    main()
