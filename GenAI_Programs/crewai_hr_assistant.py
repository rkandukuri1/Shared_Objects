from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from employee_data import employees
import json

class EmployeeLookupTool(BaseTool):
    name: str = "Employee Lookup Tool"
    description: str = (
        "Retrieve employee information from a JSON file using Employee ID."
    )

    def _run(self, employee_id: str) -> str:
        """
        Reads employee details from employee_data.json
        """

        with open("employee_data.json", "r") as file:
            employees = json.load(file)
            employee = employees.get(employee_id)

            if employee is None:
                return f"No employee found with ID '{employee_id}'."
            else:
                return employee

records_agent = Agent(
    role="Employee Records Specialist",
    goal="Retrieve employee information.",
    backstory="Expert in employee records.",
    tools=[EmployeeLookupTool()]
)

employee_task = Task(
    description="""
Retrieve the information for employee ID:

{employee_id}

Use the Employee Lookup Tool.

Find required columns using the user question and make them only as part of Employee details.
{question}

""",

    expected_output="Employee details",

    agent=records_agent
)

hr_crew = Crew(
    agents = [records_agent],
    tasks = [employee_task],
)

emp_id = input("Enter employee id: ")
emp_question = input("Enter your question: ")

result = hr_crew.kickoff(
    inputs={
        "employee_id": emp_id,
        "question": emp_question
    }
)

print(result)
