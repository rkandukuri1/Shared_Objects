import pandas as pd
from sqlalchemy import create_engine

engine1 = create_engine("mysql+mysqlconnector://root:welcome@localhost/sales")
sql_items = "SELECT ITEM_ID, ITEM_NAME, PRICE FROM ITEMS"
sql_orders = "SELECT ORDER_ID, DATE_ENTERED, CUSTOMER_ID FROM ORDERS"

df_items = pd.read_sql(sql_items, engine1)
df_orders = pd.read_sql(sql_orders, engine1)

with pd.ExcelWriter("test_items_2.xlsx") as writer:
       df_items.to_excel(writer, sheet_name = 'Items', index=False)
       df_orders.to_excel(writer, sheet_name = 'Orders', index=False)
