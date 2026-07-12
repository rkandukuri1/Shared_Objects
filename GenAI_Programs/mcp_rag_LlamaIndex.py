from dotenv import load_dotenv
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from mcp.server.fastmcp import FastMCP
from pathlib import Path

# Load environment variables
load_dotenv()

# Configure the OpenAI LLM
Settings.llm = OpenAI(model="gpt-4.1-mini", temperature=0)

# Configure the embedding model
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# Load the PDF document
print("Loading PDF...")
BASE_DIR = Path(__file__).parent

pdf_file = BASE_DIR / "VigilantCorp_Company_Profile.pdf"
documents = SimpleDirectoryReader(input_files=[str(pdf_file)]).load_data()

# Build the Vector Index
print("Building Vector Index...")
index = VectorStoreIndex.from_documents(documents)

# Create the Query Engine
query_engine = index.as_query_engine()

# Create the MCP Server
mcp = FastMCP("Company Policy Assistant")

# Register an MCP Tool
@mcp.tool()
def search_pdf(question: str) -> str:
    """
    Search the company policy PDF and answer questions.

    Args:
        question: User's question.

    Returns:
        Answer generated using Retrieval-Augmented Generation (RAG).
    """

    print(f"\nQuestion: {question}")
    response = query_engine.query(question)
    print("Answer Generated.\n")
    return str(response)

# Start the MCP Server
if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run()