import pandas as pd

df_items = pd.read_excel("sales.xlsx" , sheet_name = "Items", usecols = ["ITEM_ID", "ITEM_PRICE"])

print(df_items)
