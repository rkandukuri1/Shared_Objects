import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from pydantic import BaseModel


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ResolutionStep(BaseModel):
    step_number: int
    action: str

class ComplaintAnalysis(BaseModel):
    customer_name: str
    category: str
    sentiment: str
    priority: str
    key_issues: list[str]
    resolution_steps: list[ResolutionStep]

# Sample Complaint

email_text = """
Hi, this is John.

I was charged twice for my subscription this month.
I tried contacting support but got no response.
This is very frustrating and disappointing.

Please resolve this immediately.
"""

# LLM Call

response = client.beta.chat.completions.parse(
    model="gpt-4.1-nano",
    messages = [
        {"role" : "user", "content" : f"""
    Analyze the following customer complaint. Extract structured information.
    Complaint:
    {email_text}
    """}
    ],
    response_format=ComplaintAnalysis
)

analysis = response.choices[0].message.parsed

# Output

print("\nCustomer Name:", analysis.customer_name)
print("Category:", analysis.category)
print("Sentiment:", analysis.sentiment)
print("Priority:", analysis.priority)                                                               

print("\nKey Issues:")
for issue in analysis.key_issues:
    print("-", issue)

print("\nResolution Steps:")
for step in analysis.resolution_steps:
    print(f"{step.step_number}. {step.action}")