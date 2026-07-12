import pandas as pd

df_order_items = pd.read_excel("sales.xlsx", sheet_name="Order_Items")
df_items = pd.read_excel("sales.xlsx", sheet_name="Items", usecols=["ITEM_ID", "ITEM_PRICE"])

df_joined = pd.merge(df_items, df_order_items, on="ITEM_ID", how="inner")
df_joined["sales_per_trx"] = (df_joined["ITEM_PRICE"] * df_joined["QUANTITY"]) - df_joined["DISCOUNT"]

# print(df_joined)

df_item_sales = df_joined.groupby(["ITEM_ID"]).agg(
   TOTAL_SALES= ("sales_per_trx", "sum"))

print(df_item_sales)
