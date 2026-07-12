from llama_index.readers.file import PDFReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import os
from dotenv import load_dotenv
import logging

logging.disable(logging.CRITICAL) # To disable intermediate msgs from Embeddings 

load_dotenv()
Client = OpenAI(model="gpt-4.1-nano",api_key=os.getenv("OPENAI_API_KEY"))

embed_model = OpenAIEmbedding(model="text-embedding-3-small")

pdf_file = "VigilantCorp_Company_Profile.pdf"

print("\nReading PDF file", pdf_file)
reader = PDFReader()
documents = reader.load_data(pdf_file)
print("   -> Done")

print("\nCreating Vector Embeddings")
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
print("   -> Done") 

query_engine = index.as_query_engine(llm=Client)

while True:
    user_prompt = input("\nEnter your question: ")
    if user_prompt == "exit":
        break
    response = query_engine.query(user_prompt)
    print(response)
