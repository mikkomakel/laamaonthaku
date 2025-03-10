from PyPDF2 import PdfReader

def read_pdf(file_path="data/ohje.pdf"):
    reader = PdfReader(file_path)
    for i, page in enumerate(reader.pages):
        print(f"--- Page {i + 1} ---")
        text = page.extract_text()
        print(text if text else "No text found on this page.")

read_pdf()