import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd
   
engine = create_engine("mysql+pymysql://root:welcome@localhost:3306/sales")

sql_show_tables = "SHOW TABLES"  # Gets all table names
df_tables = pd.read_sql(sql_show_tables, engine)  # Storing table names in a DataFrame

selected_table = st.sidebar.selectbox(label="Select a table:", options=df_tables) # DataFrame to Dropdown
submit_btn = st.sidebar.button("View Data")

if selected_table and submit_btn:
    st.subheader("Table:    " + selected_table)
    st.divider()

    sql_view_data = "SELECT * FROM " +  selected_table
    df_view_data = pd.read_sql(sql_view_data, engine)
    st.dataframe(df_view_data)