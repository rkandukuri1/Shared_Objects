import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd

#Create engine
engine = create_engine("mysql+pymysql://root:welcome@localhost:3306/sales")

st.header("Display Database table contents")   # Provide SQL Query and Engine
st.divider()   # Draws a line

sql_items = "SELECT ITEM_ID, ITEM_NAME, PRICE FROM ITEMS"
df_items = pd.read_sql(sql_items, engine)
st.dataframe(df_items)   #Display data in a Frame
