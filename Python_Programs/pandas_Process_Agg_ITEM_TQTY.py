import pandas as pd

df_order_items = pd.read_excel("sales.xlsx", sheet_name="Order_Items")

df_item_tqty = df_order_items.groupby(["ITEM_ID"]).agg(
   TOTAL_QTY = ("QUANTITY", "sum"))

print(df_item_tqty)
