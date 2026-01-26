#!/usr/bin/env python3
"""
PDF Extractor - Extract text, metadata, and images from PDF files
"""

import argparse
import sys
from pathlib import Path
from pypdf import PdfReader
import pdfplumber


def extract_text_pypdf(pdf_path):
    """Extract text using pypdf"""
    try:
        reader = PdfReader(pdf_path)
        text_content = []

        print(f"\n{'='*60}")
        print(f"PDF: {pdf_path.name}")
        print(f"{'='*60}")
        print(f"Number of pages: {len(reader.pages)}")

        # Extract metadata
        if reader.metadata:
            print(f"\nMetadata:")
            for key, value in reader.metadata.items():
                print(f"  {key}: {value}")

        # Extract text from each page
        for i, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            text_content.append(f"\n--- Page {i} ---\n{text}")

        return "\n".join(text_content)

    except Exception as e:
        print(f"Error reading PDF with pypdf: {e}", file=sys.stderr)
        return None


def extract_text_pdfplumber(pdf_path):
    """Extract text using pdfplumber (better for tables)"""
    try:
        text_content = []

        with pdfplumber.open(pdf_path) as pdf:
            print(f"\n{'='*60}")
            print(f"PDF: {pdf_path.name}")
            print(f"{'='*60}")
            print(f"Number of pages: {len(pdf.pages)}")

            for i, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                text_content.append(f"\n--- Page {i} ---\n{text}")

                # Extract tables if present
                tables = page.extract_tables()
                if tables:
                    text_content.append(f"\nTables found on page {i}:")
                    for table in tables:
                        text_content.append(str(table))

        return "\n".join(text_content)

    except Exception as e:
        print(f"Error reading PDF with pdfplumber: {e}", file=sys.stderr)
        return None


def save_extracted_text(text, output_path):
    """Save extracted text to file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"\nText saved to: {output_path}")
    except Exception as e:
        print(f"Error saving text: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description='Extract text and metadata from PDF files')
    parser.add_argument('pdf_file', type=str, help='Path to PDF file')
    parser.add_argument('-o', '--output', type=str, help='Output text file path')
    parser.add_argument('-m', '--method', choices=['pypdf', 'pdfplumber'],
                       default='pypdf', help='Extraction method (default: pypdf)')
    parser.add_argument('-p', '--print', action='store_true',
                       help='Print extracted text to console')

    args = parser.parse_args()

    pdf_path = Path(args.pdf_file)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Extract text
    if args.method == 'pypdf':
        text = extract_text_pypdf(pdf_path)
    else:
        text = extract_text_pdfplumber(pdf_path)

    if text is None:
        sys.exit(1)

    # Print to console if requested
    if args.print:
        print("\nExtracted Text:")
        print(text)

    # Save to file if output path specified
    if args.output:
        output_path = Path(args.output)
        save_extracted_text(text, output_path)
    elif not args.print:
        # If no output and no print, save to default location
        output_path = pdf_path.with_suffix('.txt')
        save_extracted_text(text, output_path)


if __name__ == '__main__':
    main()
