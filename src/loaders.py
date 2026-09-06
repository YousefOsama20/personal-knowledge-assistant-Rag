from pathlib import Path

from pypdf import PdfReader
from docx import Document


def load_txt(file_path: str) -> list[dict]:
    """Load a TXT file while preserving source metadata."""

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        text = file.read()

    return [
        {
            "text": text,
            "metadata": {
                "source": path.name,
                "page": None,
            },
        }
    ]


def load_pdf(file_path: str) -> list[dict]:
    """Load a PDF page by page while preserving page numbers."""

    path = Path(file_path)

    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if not text:
            continue

        documents.append(
            {
                "text": text,
                "metadata": {
                    "source": path.name,
                    "page": page_number,
                },
            }
        )

    return documents


def load_docx(file_path: str) -> list[dict]:
    """Load a DOCX file while preserving source metadata."""

    path = Path(file_path)

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:

        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    text = "\n\n".join(paragraphs)

    return [
        {
            "text": text,
            "metadata": {
                "source": path.name,
                "page": None,
            },
        }
    ]


def load_document(file_path: str) -> list[dict]:
    """Load a document based on its file extension."""

    path = Path(file_path)

    extension = path.suffix.lower()

    if extension == ".txt":
        return load_txt(file_path)

    if extension == ".pdf":
        return load_pdf(file_path)

    if extension == ".docx":
        return load_docx(file_path)

    raise ValueError(
        f"Unsupported file type: {extension}"
    )