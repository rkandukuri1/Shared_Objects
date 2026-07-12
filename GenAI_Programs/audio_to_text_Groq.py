from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

with open("Luna.wav", "rb") as audio_file:
    response = client.audio.transcriptions.create(
        file = audio_file,
        model="whisper-large-v3-turbo"
    )
print(response.text)
