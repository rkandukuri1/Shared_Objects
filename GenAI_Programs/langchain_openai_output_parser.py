from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel

# Define schema
class Employee(BaseModel):
    name: str
    age: int
    department: str

# Create an object
emp = Employee(
    name="John",
    age=34,
    department="SALES"
)

# Plain text
print("Plain Text")
print(emp)

# JSON
print("\nJSON")
print(emp.model_dump_json(indent=4))

# LangChain Output Parser
parser = JsonOutputParser(pydantic_object=Employee)

print("\nParser")
print(parser)