from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

client = ChatOpenAI(model="gpt-4o-mini")

# Agent 1
market_research_agent = Agent(
    role="Market Research Analyst",
    goal="""
    Research the target market and identify market size, 
    customer segments, opportunities and challenges.
    """,
    backstory="""
    You are an experienced market research analyst with expertise
    in identifying market trends, customer needs and business opportunities.
    """
    # verbose=True
)

# Agent 2
competitor_analysis_agent = Agent(
    role="Competitor Analyst",
    goal="Analyze competitors and compare their products, pricing and market position.",
    backstory="You specialize in competitor intelligence, benchmarking and strategic analysis"
    # verbose=True
)

# Agent 3
business_strategy_agent = Agent(
    role="Business Strategy Consultant",
    goal="Prepare a business strategy report using the research and competitor analysis",
    backstory="""
    You are a senior business consultant who advises
    startups and enterprises on market entry strategies.
    """
    # verbose=True
)

# Task 1
market_research_task = Task(
    description="""
Research the market for {industry}.

Include the following:

- Market Overview
- Market Size
- Growth Potential
- Customer Segments
- Opportunities
- Challenges
""",

    expected_output="""
A detailed market research report.
""",

    agent=market_research_agent
)

# Task 2
competitor_analysis_task = Task(
    description="""
Analyze the top competitors in the market.

Include:

- Top competitors
- Products or Services
- Pricing Strategy
- Strengths
- Weaknesses
- Competitive Advantages
""",

    expected_output="""
A detailed competitor analysis report.
""",

    context=[market_research_task],

    agent=competitor_analysis_agent
)

# Task 3
business_strategy_task = Task(
    description="""
Using the previous reports,

Create:

- SWOT Analysis
- Market Entry Strategy
- Pricing Strategy
- Marketing Strategy
- Executive Summary

Generate a professional business report.
""",

    expected_output="""
A complete market research report with business recommendations.
""",

    context=[
        market_research_task,
        competitor_analysis_task
    ],

    agent=business_strategy_agent
)

industry = input("Enter an industry to research: ")

market_research_crew = Crew(
    agents=[
        market_research_agent,
        competitor_analysis_agent,
        business_strategy_agent
    ],

    tasks=[
        market_research_task,
        competitor_analysis_task,
        business_strategy_task
    ],
    process=Process.sequential
    # verbose=True
)

result = market_research_crew.kickoff(inputs={"industry": industry})

print("\n")
print("=" * 70)
print("FINAL MARKET RESEARCH REPORT")
print("=" * 70)
print(result)