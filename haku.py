from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
import os
import openai
openai.api_key = os.environ['OPENAI_API_KEY']

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.6)
storage_context = StorageContext.from_defaults(persist_dir="./index")
index = load_index_from_storage(storage_context)

# Tee kysely
query_engine = index.as_query_engine(llm=llm)
response = query_engine.query("mitä suosituksia annetan kyberturvallisuuden parantamiseen?")
print(response)