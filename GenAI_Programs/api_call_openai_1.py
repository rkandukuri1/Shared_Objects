from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Expands all environment variables located in "".env" file

myclient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))   # API Key input

myresponse = myclient.chat.completions.create(  # Create response object
    messages = [
        {"role" : "user", "content" : "Explain Global Warming in 5 lines"}
    ],
        model = "gpt-4.1-nano"
)

print(myresponse.choices[0].message.content)
