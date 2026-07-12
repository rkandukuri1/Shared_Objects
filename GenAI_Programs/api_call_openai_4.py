from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

previous_response_id = None

print("Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if previous_response_id is None:
        response = client.responses.create(
            model="gpt-5.5",
            input=user_input
        )
    else:
        response = client.responses.create(
            model="gpt-5.5",
            previous_response_id=previous_response_id,
            input=user_input
        )

    print("\nAssistant:", response.output_text)

    previous_response_id = response.id