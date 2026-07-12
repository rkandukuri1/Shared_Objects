from openai import OpenAI
from dotenv import load_dotenv
import os
import PyPDF2

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

reader = PyPDF2.PdfReader("VigilantCorp_Company_Profile.pdf")
file_content = ""  # This variable will store the extracted text

# Loop through every page in the PDF and extract text
for page in reader.pages:
    text = page.extract_text()
    if text:
        file_content += text

response = client.responses.create(
    model="gpt-4.1-nano",
    input=f"Summarize the following document in 3 lines: {file_content}"
)

print(response.output_text)