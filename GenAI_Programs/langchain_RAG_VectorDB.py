# Convert source files to Text (if needed)
# Create the chunks out of above Text, These are called Embeddings
    # Vectors are number representation of the data
    # Embeddings are Vector representation of the data
# Store the chunks in any Vector Database (Example# Chromadb)
# Perform Upsert operation 

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
import chromadb


load_dotenv()

client = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4.1-nano")

# Read the source folder
print("Reading/Converting the Source Documents")
src_folder = "C:\\Ramesh\\GenAI_Class\\Training\\Jan-2026\\BATCH-2\\GenAI_Programs\\Books"
loader = PyPDFDirectoryLoader(src_folder)
text_data = loader.load()

# Create the chunks
print("Creating chunks")
chunk_properties = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 25
)
chunks = chunk_properties.split_documents(text_data)
# print(chunks)

# Store chunks in VectorDB
print("Storing chunks in VectorDB")

vectordb_folder = chromadb.PersistentClient(path="my_VectorDB")
collection_name = vectordb_folder.get_or_create_collection(name = "sample")

docs = []
metadata = []
chunk_id = []

for i, src_chunk in enumerate(chunks):
    docs.append(src_chunk.page_content)
    metadata.append(src_chunk.metadata)
    chunk_id.append(f"ID({i})")

collection_name.upsert(
    documents=docs,
    metadatas=metadata,
    ids=chunk_id
)

qq = ""
while qq != "exit":
    if qq == "exit":
        break

    qq = input("Enter your question: ")
    results = collection_name.query(query_texts=qq, n_results=3)


    my_prompt = f'''
    You are a helpful assistant. Answer the questions based only on the provided data, dont use
    your existing knowledge.

    Question: {qq}
    Context: {str(results['documents'])}
    '''

    response = client.invoke(my_prompt)
    print (response.text)
