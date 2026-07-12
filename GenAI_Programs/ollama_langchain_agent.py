from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# Initialize the Local LLM

client = ChatOllama(model="gemma3:1b")

# Create Prompt Template

prompt = ChatPromptTemplate.from_template("""
You are a professional customer support executive.

Generate a polite and professional email for the following customer.

Customer Name: {name}

Issue:
{issue}

The email should:
1. Thank the customer.
2. Acknowledge the issue.
3. Apologize if necessary.
4. Explain the next steps.
5. End with a professional closing.
""")

# Create the LangChain Pipeline
# Below stmt means, Prompt will be sent to client as input, client is defined above
chain = prompt | client

# Get User Input
customer_name = input("Enter Customer Name: ")
customer_issue = input("Enter Customer Issue: ")

# Generate Response
response = chain.invoke(
    {
        "name": customer_name,
        "issue": customer_issue
    }
)

print("\nGenerated Email\n")
print(response.content)
