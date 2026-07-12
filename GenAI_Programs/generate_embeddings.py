from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="I love cats"
)

embedding = response.data[0].embedding

print("Dimensions:", len(embedding))
print(embedding[:10])      # Display First 10 values
