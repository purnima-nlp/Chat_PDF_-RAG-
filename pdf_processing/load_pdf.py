from pypdf import PdfReader
from pathlib import Path


def load_pdf(pdf_path: str) -> str:
    """
    Loads a PDF and returns full extracted text.
    """
    reader = PdfReader(pdf_path)

    pages_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)

    full_text = "\n".join(pages_text)
    return full_text


def load_pdfs_from_folder(folder_path: str) -> list:
    """
    Loads all PDFs from a folder.
    Returns list of dicts: {filename, text}
    """
    folder = Path(folder_path)

    documents = []
    for pdf_file in folder.glob("*.pdf"):
        text = load_pdf(str(pdf_file))
        documents.append({
            "source": pdf_file.name,
            "text": text
        })

    return documents


if __name__ == "__main__":
    docs = load_pdfs_from_folder("data/raw_pdfs")
    print(f"Loaded {len(docs)} PDFs")
    print(docs[0]["text"][:1000])

