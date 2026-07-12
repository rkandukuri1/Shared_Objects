from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI


# LLM configuration
client = ChatOpenAI(model="gpt-4o-mini")

# QA Agent
qa_agent = Agent(
    role="Senior QA Automation Engineer",
    goal="Generate complete UI test cases for login and navigation scenarios",
    backstory="""
    You are a highly experienced QA automation engineer who specializes in 
    writing detailed UI test cases including positive scenarios, negative scenarios,
    validation checks and navigation flows.
    """
    # verbose=True
)


# Test Case Task
testcase_task = Task(
    description="""
Generate detailed UI test cases for the following web application scenario.

Application: Demo Web App

Login Page Fields:
- Username
- Password
- Login Button
- Forgot Password Link
- Signup Link

Requirements:

1. Login validation scenarios
2. Invalid username/password scenarios
3. Empty field validation
4. Password masking
5. Navigation after successful login to Dashboard
6. Navigation to Signup page
7. Navigation to Forgot Password page
8. Error message validation
9. Session timeout scenario
10. Logout navigation
""",

expected_output="""
Structured test cases containing:

Test Case ID
Test Scenario
Preconditions
Test Steps
Expected Result
Priority
""",

agent=qa_agent
)


# Crew execution
crew = Crew(
    agents=[qa_agent],
    tasks=[testcase_task],
    verbose=True
)

# Run

crew.kickoff()

# result = crew.kickoff()

# print("\n\nGenerated Test Cases:\n")
# print(result)
