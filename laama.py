import os
from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.openai import OpenAIEmbedding
os.environ["OPENAI_API_KEY"] = "apiavain"
# Lataa tekstitiedostot hakemistosta
documents = SimpleDirectoryReader('data').load_data()



# Määritä haluamasi upotusmalli
embedding_model = OpenAIEmbedding(model="text-embedding-3-small")
# Luo vektori-indeksi dokumenteista
index = GPTVectorStoreIndex.from_documents(documents)

# Tallenna indeksi
index.storage_context.persist(persist_dir="./index")

# Lataa aiemmin tallennettu indeksi
storage_context = StorageContext.from_defaults(persist_dir="./index")
index = load_index_from_storage(storage_context)

# Kysy kysymys indeksoidusta tietokannasta
#query_engine = index.as_query_engine()
#response = query_engine.query("Mitä tietoa löytyy hakemistosta?")
#print(response)