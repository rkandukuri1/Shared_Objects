from dotenv import load_dotenv
import os

from llama_index.readers.file import PDFReader

from llama_index.core import (
    VectorStoreIndex
)

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.core.tools import QueryEngineTool
from llama_index.core.query_engine import RouterQueryEngine


# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = OpenAI(
    model="gpt-4.1-nano",
    api_key=api_key
)

# --------------------------------------------------
# Embedding Model
# --------------------------------------------------

embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_key=api_key
)

# --------------------------------------------------
# Load PDFs
# --------------------------------------------------

reader = PDFReader()

hr_docs = reader.load_data("hr.pdf")

tech_docs = reader.load_data("tech.pdf")

finance_docs = reader.load_data("finance.pdf")


# --------------------------------------------------
# Create Indexes
# --------------------------------------------------

print("Creating HR Index...")
hr_index = VectorStoreIndex.from_documents(
    hr_docs,
    embed_model=embed_model
)

print("Creating Tech Index...")
tech_index = VectorStoreIndex.from_documents(
    tech_docs,
    embed_model=embed_model
)

print("Creating Finance Index...")
finance_index = VectorStoreIndex.from_documents(
    finance_docs,
    embed_model=embed_model
)


# --------------------------------------------------
# Create Query Engines
# --------------------------------------------------

hr_engine = hr_index.as_query_engine(
    llm=llm
)

tech_engine = tech_index.as_query_engine(
    llm=llm
)

finance_engine = finance_index.as_query_engine(
    llm=llm
)


# --------------------------------------------------
# Create QueryEngineTools
# --------------------------------------------------

hr_tool = QueryEngineTool.from_defaults(
    query_engine=hr_engine,
    description="""
    Contains HR policies, leave policies,
    employee benefits, recruitment information,
    holidays and attendance rules.
    """
)

tech_tool = QueryEngineTool.from_defaults(
    query_engine=tech_engine,
    description="""
    Contains technical documentation,
    architecture documents,
    APIs, deployment guides,
    software development information.
    """
)

finance_tool = QueryEngineTool.from_defaults(
    query_engine=finance_engine,
    description="""
    Contains finance documents,
    revenue reports, budgets,
    invoices, expenses and accounting data.
    """
)

# --------------------------------------------------
# Create Router
# --------------------------------------------------

router = RouterQueryEngine.from_defaults(
    query_engine_tools=[
        hr_tool,
        tech_tool,
        finance_tool
    ],
    llm=llm
)


# --------------------------------------------------
# Chat Loop
# --------------------------------------------------

print("\nRouter Ready...")
print("Type exit to quit.\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        break

    response = router.query(question)

    print("\nAnswer:")
    print(response)
    print("-" * 80)