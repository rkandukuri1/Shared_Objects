import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

client = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),  model="gpt-4.1-nano")

# Embedding Model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

print("Loading PDF files...")
loader = PyPDFLoader("VigilantCorp_Company_Profile.pdf")
documents = loader.load()
print(f"{len(documents)} PDF pages loaded.")

# Split into Chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)
print(f"{len(chunks)} chunks created.")

# Create Chroma Vector Database
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vigilant_VectorDB",
    collection_name="vigilant"
)

print("Vector database created.")

# Create Retriever
retriever = db.as_retriever(search_kwargs={"k":3})

# Question Loop
while True:
    question = input("\nAsk a question (exit to quit): ")
    if question.lower() == "exit":
        break

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    context = ""
    for doc in docs:
        context = context + doc.page_content + "\n\n"

    prompt = f''' You are a helpful assistant. Answer ONLY using the context below. 
	If the answer is not found in the context, 
               reply: "I couldn't find that information in the provided documents."
Question:
{question}

Context:
{context}
'''
    response = client.invoke(prompt)
    print("\nAnswer\n")
    print(response.content)
