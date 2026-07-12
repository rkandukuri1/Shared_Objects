from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()  
client = ChatOpenAI(model="gpt-4.1-nano", api_key=os.getenv("OPENAI_API_KEY"))

myprompt = PromptTemplate.from_template ("Explain {topic}  for a {audience} in 4 lines")

chain = myprompt | client

response = chain.invoke(
           {"topic": "Machine Learning", "audience": "beginner"}
    )
print(response.text)
