from llama_index.core import GPTVectorStoreIndex, Document, StorageContext
from PyPDF2 import PdfReader

# Lataa PDF-teksti
def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Määritä PDF-tiedoston polku
pdf_path = "data/ont.pdf"

# Lue PDF-tiedoston teksti
pdf_text = read_pdf(pdf_path)

# Luo dokumentti LlamaIndexille
document = Document(text=pdf_text)


# Luo vektorivarasto
index = GPTVectorStoreIndex.from_documents([document])

# Persistoi indeksi
index.storage_context.persist(persist_dir="./index")

query_engine = index.as_query_engine()

# Tee kysely
response = query_engine.query("Summarize the document.")
print(response)

# Hae tietyistä osista
response = query_engine.query("What does the document say about XYZ?")
print(response)