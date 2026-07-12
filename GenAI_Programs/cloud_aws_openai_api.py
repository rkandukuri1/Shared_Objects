from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(base_url="https://bedrock-runtime.ap-south-1.amazonaws.com/openai/v1", api_key=os.getenv("AMAZON_API_KEY"))

user_prompt = input("Enter your query: ")

response = client.chat.completions.create(
    model = "openai.gpt-oss-20b-1:0",
    messages=[
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)