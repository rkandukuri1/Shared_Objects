from ddgs import DDGS
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

prompt = "Research latest Generative AI trends"

def safe_web_search(query: str) -> str:
        """Search the web for up-to-date information, news, or general knowledge."""
        with DDGS() as ddgs:
                results = [r["body"] for r in ddgs.text(query, max_results=3)]
                return "\n\n".join(results) if results else "No results found."

# Construct the agent
agent = create_agent(
        model="gpt-4.1-nano",
        tools=[safe_web_search],
        system_prompt="You are a research bot. Search the web to provide precise answers on any topic."
        )

response = agent.invoke({"messages": [("user", prompt)]})

print(response["messages"][-1].content)