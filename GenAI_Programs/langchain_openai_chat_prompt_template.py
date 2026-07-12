from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
client = ChatOpenAI(model="gpt-4.1-nano", api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a teacher."),
    ("human", "Explain {topic} in 5 lines.") ])

mychain = prompt | client
response = mychain.invoke({"topic":"Neural Networks"})
print(response.text)
