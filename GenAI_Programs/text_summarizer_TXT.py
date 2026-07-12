from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("gdp.txt", "r", encoding="utf-8") as f:
    file_content = f.read()

response = client.responses.create(
    model="gpt-4.1-nano",
    input=f"Summarize the following article in 3 lines: {file_content}"
)

print(response.output_text)