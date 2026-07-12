from crewai import Agent, Task, Crew

email_agent = Agent (
    role = "Email Assistant Agent",
    goal = "Improve emails and make them look professional",
    backstory = "A highly experenced expert in coommuncation skills and professional email writer",
    verbose = True
)

email_text = '''Team, the demo is not ready, I am tired of testing and see hell lot of issues. 
    I am not attending the client call, you handle it. I dont care'''

email_task = Task (
    description = f''' Take the following email which is a rough draft and rewrte it into a professional
     and polished version. 
     {email_text}
    ''',
    expected_output = "A professionally written email with proper format and politeful content",
    agent=email_agent
)

crew = Crew(
    agents = [email_agent],
    tasks = [email_task],
    verbose=True
)

t