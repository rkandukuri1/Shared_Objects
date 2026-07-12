import pandas as pd
import duckdb

df_order_items = pd.read_excel("sales.xlsx", sheet_name="Order_Items")
df_items = pd.read_excel("sales.xlsx", sheet_name="Items", usecols=["ITEM_ID", "ITEM_PRICE"])

sql_item_sales = '''SELECT B.ITEM_ID, SUM(A.ITEM_PRICE * B.QUANTITY - B.DISCOUNT) as ITEM_SALES 
FROM df_items A
INNER JOIN df_order_items B on (A.ITEM_ID = B.ITEM_ID)
GROUP BY B.ITEM_ID
ORDER BY ITEM_SALES DESC
LIMIT 3
'''

print ("\n ***  Output using DuckDB ***")
print(duckdb.sql(sql_item_sales))
