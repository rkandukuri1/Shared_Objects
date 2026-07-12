from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

qq = ""
while qq != "exit":
    if qq == "exit":
         break

    qq = input("Enter your prompt: ")

    response = client.models.generate_content(
        model = "gemini-2.5-flash-image",
        contents = qq,
        config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"])
    )

    print(response)

    for x in response.candidates[0].content.parts:
        if x.inline_data is not None:
            img = Image.open(BytesIO(x.inline_data.data))
            img.show()
            # img.save("kids_lion.jpeg")
