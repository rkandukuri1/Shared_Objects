from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4.1-nano")

user_prompt = input("Enter any prompt: ")

response = client.complete(user_prompt)
print(response)