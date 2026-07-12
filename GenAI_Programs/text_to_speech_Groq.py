from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

response = client.audio.speech.create(
  model = "canopylabs/orpheus-v1-english",
  voice="daniel",
  response_format="wav",
  input = '''Once upon a time, a gentle unicorn named Luna toched the starry sky with 
  her shimmering horn, lighting up the night for all the sleeping creatures below.'''
)

response.write_to_file("Luna.wav")
