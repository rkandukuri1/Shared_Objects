from sqlalchemy import create_engine
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4.1-nano")

# db_con = "mysql+pymysql://root:welcome@localhost:3306/sales"
db_engine = create_engine("mysql+pymysql://root:welcome@localhost:3306/sales")
sql_db = SQLDatabase(db_engine)

query_engine = NLSQLTableQueryEngine(sql_db)

while True:
    user_prompt=input("\nEnter a prompt: (Type exit to quit): ")
    if user_prompt == "exit":
        break
    response = query_engine.query(user_prompt + " show the results in tabular format")
    print("")

    print(response.metadata.get("sql_query"))
    print("")
    print(response)
