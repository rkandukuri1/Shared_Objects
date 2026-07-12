from mcp.server.fastmcp import FastMCP
from github import Github, Auth
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
auth1 = Auth.Token(token)
github_client = Github(auth=auth1)

my_mcp = FastMCP("Github MCP Server")

@my_mcp.tool()
def list_repositories():
    """
      List all mrepositories for the authenticated user
    """
    user = github_client.get_user()
    repos = []

    for repository in user.get_repos():
        repos.append({
            "name" : repository.name,
            "private" : repository.private,
            "url" : repository.html_url
        })
    return repos

my_mcp.run()