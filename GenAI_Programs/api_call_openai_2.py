from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

myclient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    myprompt = input("Enter a prompt: ")

    if myprompt == "exit":
        break

    myresponse = myclient.chat.completions.create(
        messages = [
            {"role" : "user", "content" : myprompt}
        ],
            model = "gpt-4.1-nano"
    )

    print(myresponse.choices[0].message.content)
    print("")
