from llama_index.readers.file import PDFReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

import os
from dotenv import load_dotenv
import logging

logging.disable(logging.CRITICAL) # To disable intermediate msgs from OpenAIEmbedding model

load_dotenv()

Client = OpenAI(model="gpt-4.1-nano",api_key=os.getenv("OPENAI_API_KEY"))

embed_model = OpenAIEmbedding(model="text-embedding-3-small")

reader = PDFReader()
documents = reader.load_data("VigilantCorp_Company_Profile.pdf")

index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

query_engine = index.as_query_engine(llm=Client)

response = query_engine.query("Summarize the document")
print(response)