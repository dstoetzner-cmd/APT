#!/usr/bin/env python3
"""
Example workflow demonstrating PDF processing capabilities
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from pypdf import PdfReader, PdfWriter


def example_info():
    """Example: Get PDF information"""
    print("\n" + "="*60)
    print("Example 1: Get PDF Information")
    print("="*60)

    # This example shows how to get basic PDF info programmatically
    pdf_path = Path("pdfs/input/example.pdf")

    if not pdf_path.exists():
        print(f"Note: {pdf_path} does not exist yet")
        print("Place a PDF file there to run this example")
        return

    reader = PdfReader(pdf_path)

    print(f"File: {pdf_path.name}")
    print(f"Pages: {len(reader.pages)}")

    if reader.metadata:
        print("\nMetadata:")
        for key, value in reader.metadata.items():
            print(f"  {key}: {value}")


def example_custom_merge():
    """Example: Custom merge with page selection"""
    print("\n" + "="*60)
    print("Example 2: Custom Merge with Page Selection")
    print("="*60)

    # This shows how to merge specific pages from multiple PDFs
    input_dir = Path("pdfs/input")
    output_dir = Path("pdfs/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("\nThis example demonstrates merging specific pages:")
    print("- From PDF 1: Take pages 1-3")
    print("- From PDF 2: Take pages 2-4")
    print("- From PDF 3: Take all pages")

    print("\nTo use: Place PDFs in pdfs/input/ and run this script")


def example_extract_pages():
    """Example: Extract and analyze specific pages"""
    print("\n" + "="*60)
    print("Example 3: Extract and Analyze Specific Pages")
    print("="*60)

    print("\nThis example shows how to:")
    print("- Extract specific pages from a PDF")
    print("- Get text content from those pages")
    print("- Analyze page properties")

    print("\nTo implement:")
    print("1. Open PDF with PdfReader")
    print("2. Iterate through desired page numbers")
    print("3. Extract text with page.extract_text()")
    print("4. Access page properties like size, rotation, etc.")


def main():
    print("\n" + "="*60)
    print("PDF Processing - Example Workflows")
    print("="*60)

    example_info()
    example_custom_merge()
    example_extract_pages()

    print("\n" + "="*60)
    print("More Examples")
    print("="*60)
    print("\nFor complete usage examples, see README.md")
    print("\nCommand-line tools:")
    print("  - python src/pdf_extractor.py --help")
    print("  - python src/pdf_merger.py --help")
    print("  - python src/pdf_splitter.py --help")
    print()


if __name__ == '__main__':
    main()
