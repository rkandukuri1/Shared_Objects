from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()  

client = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))

response = client.invoke("What is Artificial Intelligence in 4 lines?")
print(response.content)
