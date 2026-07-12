from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = "866425c31b47809a67415cf43d94d20e0357f0c073eb1f44d5955927b6353998"
#os.getenv("SERPER_API_KEY")

my_mcp = FastMCP("Web Search MCP")

@my_mcp.tool()
def search_news(query : str):
    """
    Performs websearch and gets the news
    """

    url = "https://google.serper.dev/news"

    payload1 = {
        "q" : query,
        "num" : 3
    }

    headers1 = {
        "X_API_KEY" : API_KEY,
        "Content-Type" : "applicaion/json"
    }

    response = requests.post(
        url,
        json=payload1,
        headers=headers1
    )

    if response.status_code != 200:
        return {
            "status_code" : response.status_code,
            "response" : response.text
        }
    data = response.json()

    news_results = data.get("news", [])

    results = []

    for item in news_results:
        results.append({
            "title" : item.get("title"),
            "link" : item.get("link"),
            "snippet" : item.get("snippet")
        })
    return results

my_mcp.run()