from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

from langchain_community.vectorstores import Chroma

from langchain_classic.chains import RetrievalQA

# ----------------------------
# Load PDF
# ----------------------------

loader = PyPDFLoader("VigilantCorp_Company_Profile.pdf")

documents = loader.load()

# ----------------------------
# Split into chunks
# ----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = text_splitter.split_documents(documents)

# ----------------------------
# Create Embedding Model
# ----------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# ----------------------------
# Store Embeddings in Chroma
# ----------------------------

vector_db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# ----------------------------
# Create Retriever
# ----------------------------

retriever = vector_db.as_retriever()

# ----------------------------
# Local LLM
# ----------------------------
llm = ChatOllama(
    model="llama3.2"
    # model="gemma3:1b"
)

# ----------------------------
# Retrieval QA Chain
# ----------------------------

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# ----------------------------
# Ask Questions
# ----------------------------

while True:

    question = input("\nAsk a question (type exit): ")

    if question.lower() == "exit":
        break

    answer = qa.invoke(question)

    print("\nAnswer:\n")
    print(answer["result"])