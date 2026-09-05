from pathlib import Path 

from pypdf import PdfReader
from docx import Document

def load_docx(file_path: str) -> str:
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
    