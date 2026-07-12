from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

prompt = """
Provide the following information in JSON format.

id=101
Student Name: John Smith
Age: 21
Course: Computer Science
Grade: A

id=102
Student Name: Steve Horn
Age: 24
Course: Computer Science
Grade: A+
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

data = json.loads(response.output_text)

print(data)