import pandas as pd

df_order_items = pd.read_excel("sales.xlsx", sheet_name="Order_Items")
df_items = pd.read_excel("sales.xlsx", sheet_name="Items", usecols=["ITEM_ID", "ITEM_PRICE"])

df_joined_tmp = pd.merge(df_items, df_order_items, on="ITEM_ID", how="inner")

df_orders = pd.read_excel("sales.xlsx", sheet_name="Orders", usecols=["ORDER_ID", "DATE_ENTERED"])
df_joined = pd.merge(df_joined_tmp, df_orders, on="ORDER_ID", how="inner") 

df_joined["sales_per_trx"] = (df_joined["ITEM_PRICE"] * df_joined["QUANTITY"]) - df_joined["DISCOUNT"]

df_joined["DATE_ENTERED"] = pd.to_datetime(df_joined["DATE_ENTERED"])
df_joined["YR"] = df_joined["DATE_ENTERED"].dt.year
df_joined["QR"] = df_joined["DATE_ENTERED"].dt.quarter

df_year_qrtr_sales = df_joined.groupby(["YR", "QR"]).agg(
   SALES = ("sales_per_trx", "sum")
)
print(df_year_qrtr_sales)
