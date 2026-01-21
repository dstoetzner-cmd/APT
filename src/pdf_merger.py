#!/usr/bin/env python3
"""
PDF Merger - Combine multiple PDF files into one
"""

import argparse
import sys
from pathlib import Path
from pypdf import PdfWriter, PdfReader


def merge_pdfs(pdf_files, output_path, verbose=False):
    """
    Merge multiple PDF files into one

    Args:
        pdf_files: List of PDF file paths
        output_path: Output file path
        verbose: Print progress information
    """
    writer = PdfWriter()
    total_pages = 0

    if verbose:
        print(f"\n{'='*60}")
        print("Merging PDFs")
        print(f"{'='*60}")

    for pdf_file in pdf_files:
        try:
            pdf_path = Path(pdf_file)
            if not pdf_path.exists():
                print(f"Warning: File not found, skipping: {pdf_path}", file=sys.stderr)
                continue

            reader = PdfReader(pdf_path)
            num_pages = len(reader.pages)

            if verbose:
                print(f"Adding: {pdf_path.name} ({num_pages} pages)")

            # Add all pages from this PDF
            for page in reader.pages:
                writer.add_page(page)

            total_pages += num_pages

        except Exception as e:
            print(f"Error processing {pdf_file}: {e}", file=sys.stderr)
            continue

    if total_pages == 0:
        print("Error: No pages to merge", file=sys.stderr)
        return False

    # Write merged PDF
    try:
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        if verbose:
            print(f"\n{'='*60}")
            print(f"Success! Merged {len(pdf_files)} PDFs ({total_pages} pages)")
            print(f"Output: {output_path}")
            print(f"{'='*60}")

        return True

    except Exception as e:
        print(f"Error writing merged PDF: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='Merge multiple PDF files into one')
    parser.add_argument('pdf_files', nargs='+', help='PDF files to merge')
    parser.add_argument('-o', '--output', type=str, required=True,
                       help='Output PDF file path')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Print detailed progress information')

    args = parser.parse_args()

    output_path = Path(args.output)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Merge PDFs
    success = merge_pdfs(args.pdf_files, output_path, args.verbose)

    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
