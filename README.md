# APT - PDF Artikel Verarbeitung

Ein Python-basiertes Tool-Set zur Verarbeitung von PDF-Dateien: Lesen, Extrahieren, Zusammenführen und Aufteilen.

## Features

- **PDF Text-Extraktion**: Extrahiere Text und Metadaten aus PDF-Dateien
- **PDF Zusammenführen**: Kombiniere mehrere PDFs in eine Datei
- **PDF Aufteilen**: Teile PDFs in einzelne Seiten oder Bereiche
- Unterstützung für Tabellen-Extraktion
- Batch-Verarbeitung möglich

## Installation

1. Python 3.8+ erforderlich
2. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

## Projekt-Struktur

```
APT/
├── src/                    # Haupt-Skripte
│   ├── pdf_extractor.py   # Text-Extraktion
│   ├── pdf_merger.py      # PDFs zusammenführen
│   └── pdf_splitter.py    # PDFs aufteilen
├── pdfs/                   # PDF-Dateien
│   ├── input/             # Eingabe-PDFs
│   └── output/            # Verarbeitete PDFs
├── examples/              # Beispiele
└── requirements.txt       # Python-Abhängigkeiten
```

## Verwendung

### 1. Text aus PDF extrahieren

```bash
# Text extrahieren und in Datei speichern
python src/pdf_extractor.py pdfs/input/dokument.pdf -o pdfs/output/text.txt

# Text auf Console ausgeben
python src/pdf_extractor.py pdfs/input/dokument.pdf --print

# Mit pdfplumber (besser für Tabellen)
python src/pdf_extractor.py pdfs/input/dokument.pdf -m pdfplumber
```

**Optionen:**
- `-o, --output`: Ausgabe-Datei für extrahierten Text
- `-m, --method`: Extraktions-Methode (`pypdf` oder `pdfplumber`)
- `-p, --print`: Text in Console ausgeben

### 2. PDFs zusammenführen

```bash
# Mehrere PDFs zusammenführen
python src/pdf_merger.py pdfs/input/doc1.pdf pdfs/input/doc2.pdf pdfs/input/doc3.pdf \
    -o pdfs/output/combined.pdf -v
```

**Optionen:**
- `-o, --output`: Ausgabe-PDF (erforderlich)
- `-v, --verbose`: Detaillierte Fortschrittsanzeige

### 3. PDF aufteilen

```bash
# In einzelne Seiten aufteilen
python src/pdf_splitter.py pdfs/input/dokument.pdf -o pdfs/output/ -v

# Bestimmte Seitenbereiche extrahieren
python src/pdf_splitter.py pdfs/input/dokument.pdf -o pdfs/output/ \
    -r "1-3" "5" "7-9" -v

# In Chunks von N Seiten aufteilen
python src/pdf_splitter.py pdfs/input/dokument.pdf -o pdfs/output/ -s 10 -v
```

**Optionen:**
- `-o, --output-dir`: Ausgabe-Verzeichnis (erforderlich)
- `-r, --ranges`: Seitenbereiche (z.B. "1-3" "5" "7-9")
- `-s, --size`: Anzahl Seiten pro Datei
- `-v, --verbose`: Detaillierte Fortschrittsanzeige

## Beispiele

### Batch-Verarbeitung: Alle PDFs in einem Ordner verarbeiten

```bash
# Alle PDFs extrahieren
for file in pdfs/input/*.pdf; do
    python src/pdf_extractor.py "$file" -o "pdfs/output/$(basename "$file" .pdf).txt"
done

# Alle PDFs zusammenführen
python src/pdf_merger.py pdfs/input/*.pdf -o pdfs/output/all_merged.pdf -v
```

### Workflow-Beispiel

```bash
# 1. Großes PDF in Kapitel aufteilen
python src/pdf_splitter.py pdfs/input/buch.pdf -o pdfs/output/chapters/ -s 20

# 2. Text aus einem Kapitel extrahieren
python src/pdf_extractor.py pdfs/output/chapters/buch_part_1.pdf -o kapitel1.txt

# 3. Ausgewählte Kapitel wieder zusammenführen
python src/pdf_merger.py pdfs/output/chapters/buch_part_1.pdf \
    pdfs/output/chapters/buch_part_3.pdf -o pdfs/output/selected_chapters.pdf
```

## Verwendete Bibliotheken

- **pypdf**: Schnelle PDF-Manipulation
- **pdfplumber**: Erweiterte Text- und Tabellen-Extraktion
- **reportlab**: PDF-Generierung (für zukünftige Features)
- **Pillow**: Bild-Verarbeitung

## Lizenz

MIT

## Autor

APT Project
