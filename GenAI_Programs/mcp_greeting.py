from mcp.server.fastmcp import FastMCP

my_mcp = FastMCP("Greet/Bye the User") 

@my_mcp.tool()
def greet_user(user_name : str):
    """
      Greet and Welcome the User
    """
    result1 = "Hi " + user_name + ", Welcome to the world of MCP"
    return result1

@my_mcp.tool()
def bye_user(user_name : str):
    """
      Say Bye to User
    """
    result2 = "Nice working with you " + user_name + ", See you again soon"
    return result2

my_mcp.run()