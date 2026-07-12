import pandas as pd
from sqlalchemy import create_engine
	
#create_engine("mysql+mysqlconnector://<user_name>:<password>@<host_name>:<port>/<db_name>

engine =  create_engine("mysql+mysqlconnector://root:welcome@localhost:3306/sales")

sql_items = "SELECT ITEM_ID, ITEM_NAME, PRICE FROM ITEMS"

df_items = pd.read_sql(sql_items, engine)
print(df_items)
