from pathlib import Path

from pypdf import PdfReader
from docx import Document

def load_txt(file_path: str) -> str:
    """Load text from a TXT file."""

    path = Path(file_path)
    
    with path.open('r', encoding='utf-8') as file:
        return file.read()

def load_pdf(file_path: str) -> str:
    """Load text from a PDF file."""
    reader = PdfReader(file_path)

    pages =[]
    for page in reder.pages:
        text = page.extract_text() 
        
        if text:
            pages.append(text)

    return '\n\n'.join(pages)

def load_docx(file_path: str) -> str:
    """Load text from a DOCX file."""

    document =Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n\n".join(paragraphs)
    
def load_document(file_path: str) -> str:
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
