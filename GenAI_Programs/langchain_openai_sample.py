from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()  

client = ChatOpenAI(model="gpt-4.1-nano", api_key=os.getenv("OPENAI_API_KEY"))

response = client.invoke("What is Artificial Intelligence in 4 lines?")
print(response.content)
