#!/usr/bin/env python3
"""
PDF Splitter - Split PDF files into individual pages or ranges
"""

import argparse
import sys
from pathlib import Path
from pypdf import PdfWriter, PdfReader


def split_pdf_by_pages(pdf_path, output_dir, page_ranges=None, verbose=False):
    """
    Split PDF into separate files

    Args:
        pdf_path: Input PDF file path
        output_dir: Directory for output files
        page_ranges: List of page ranges (e.g., ['1-3', '5', '7-9'])
                    If None, split into individual pages
        verbose: Print progress information
    """
    try:
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)

        if verbose:
            print(f"\n{'='*60}")
            print(f"Splitting: {pdf_path.name}")
            print(f"Total pages: {total_pages}")
            print(f"{'='*60}")

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        base_name = pdf_path.stem

        if page_ranges is None:
            # Split into individual pages
            for i in range(total_pages):
                writer = PdfWriter()
                writer.add_page(reader.pages[i])

                output_path = output_dir / f"{base_name}_page_{i+1}.pdf"
                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                if verbose:
                    print(f"Created: {output_path.name}")

            if verbose:
                print(f"\nSplit into {total_pages} individual pages")

        else:
            # Split by specified ranges
            for range_str in page_ranges:
                writer = PdfWriter()

                if '-' in range_str:
                    # Range like "1-3"
                    start, end = map(int, range_str.split('-'))
                    start = max(1, start)
                    end = min(total_pages, end)

                    for i in range(start - 1, end):
                        writer.add_page(reader.pages[i])

                    output_path = output_dir / f"{base_name}_pages_{start}-{end}.pdf"

                else:
                    # Single page like "5"
                    page_num = int(range_str)
                    if 1 <= page_num <= total_pages:
                        writer.add_page(reader.pages[page_num - 1])
                        output_path = output_dir / f"{base_name}_page_{page_num}.pdf"
                    else:
                        print(f"Warning: Page {page_num} out of range, skipping", file=sys.stderr)
                        continue

                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                if verbose:
                    print(f"Created: {output_path.name}")

        return True

    except Exception as e:
        print(f"Error splitting PDF: {e}", file=sys.stderr)
        return False


def split_pdf_by_size(pdf_path, output_dir, pages_per_file, verbose=False):
    """
    Split PDF into chunks of specified size

    Args:
        pdf_path: Input PDF file path
        output_dir: Directory for output files
        pages_per_file: Number of pages per output file
        verbose: Print progress information
    """
    try:
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)

        if verbose:
            print(f"\n{'='*60}")
            print(f"Splitting: {pdf_path.name}")
            print(f"Total pages: {total_pages}")
            print(f"Pages per file: {pages_per_file}")
            print(f"{'='*60}")

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        base_name = pdf_path.stem
        file_count = 0

        for start_page in range(0, total_pages, pages_per_file):
            writer = PdfWriter()
            end_page = min(start_page + pages_per_file, total_pages)

            for i in range(start_page, end_page):
                writer.add_page(reader.pages[i])

            file_count += 1
            output_path = output_dir / f"{base_name}_part_{file_count}.pdf"

            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

            if verbose:
                print(f"Created: {output_path.name} (pages {start_page+1}-{end_page})")

        if verbose:
            print(f"\nSplit into {file_count} files")

        return True

    except Exception as e:
        print(f"Error splitting PDF: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='Split PDF files into smaller parts')
    parser.add_argument('pdf_file', type=str, help='Input PDF file')
    parser.add_argument('-o', '--output-dir', type=str, required=True,
                       help='Output directory for split files')
    parser.add_argument('-r', '--ranges', nargs='+',
                       help='Page ranges to extract (e.g., "1-3" "5" "7-9")')
    parser.add_argument('-s', '--size', type=int,
                       help='Split into chunks of N pages')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Print detailed progress information')

    args = parser.parse_args()

    pdf_path = Path(args.pdf_file)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    if args.size:
        success = split_pdf_by_size(pdf_path, args.output_dir, args.size, args.verbose)
    else:
        success = split_pdf_by_pages(pdf_path, args.output_dir, args.ranges, args.verbose)

    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
