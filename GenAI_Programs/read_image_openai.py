from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
my_url = '''https://media.gettyimages.com/id/524880870/photo/people-queing-up-on-coffee-
and-snackbar.jpg'''

response = client.responses.create(

        model="gpt-4.1-nano",

        input= [
           { 
            "role" : "user", "content" : [
                {"type": "input_text", "text" : "what is the image about, provide including smallest possible detail"},
                {"type":"input_image", "image_url" : my_url}
               ]
           }
        ]
)

print(response.output_text)
