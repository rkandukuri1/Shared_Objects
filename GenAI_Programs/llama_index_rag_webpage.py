from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4.1-nano")

my_url="https://edition.cnn.com/2026/06/22/business/brexit-anniversary-uk-economy-impact-intl"


text_data = SimpleWebPageReader(html_to_text=True).load_data(urls=[my_url])

index = VectorStoreIndex.from_documents(text_data)

query_engine = index.as_query_engine(llm=client)

while True:
    user_prompt=input("\nEnter a prompt: ")
    if user_prompt == "exit":
        break
    response = query_engine.query(user_prompt + ", show as bullet points")
    print(response)
