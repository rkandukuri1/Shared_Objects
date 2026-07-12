from mcp.server.fastmcp import FastMCP
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

my_mcp = FastMCP("MySQL DB info") 

def get_connection():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port = os.getenv("MYSQL_PORT"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        database = os.getenv("MYSQL_DATABASE")
    )
    return conn


@my_mcp.tool()
def list_tables():
    """
      List all tables in the database
    """

    conn = get_connection()

    my_cursor = conn.cursor()
    my_cursor.execute("SHOW TABLES")
    tables = my_cursor.fetchall()
    my_cursor.close()
    conn.close()

    return [table[0] for table in tables]

@my_mcp.tool()
def run_select_query(query : str):
    """
    Executes the SQL for given NLP query
    """

    query_upper = query.upper()

    if not query_upper.startswith("SELECT"):
        return {
            "error" : "Only SELECT statements are allowed"
        }

    conn = get_connection()
    mycursor = conn.cursor()
    mycursor.execute(query)

    data = mycursor.fetchall()

    mycursor.close()
    conn.close()
    
    return data



my_mcp.run()