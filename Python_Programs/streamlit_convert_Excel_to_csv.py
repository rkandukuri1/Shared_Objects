import streamlit as st
import pandas as pd

# Function to convert source file to csv format and return csv DataFrame
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False).encode('utf-8')

# File Uploader
uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:
    df = pd.read_excel(uploaded_file, 0) # Here 0 means, 1st  sheet in case of multiple sheets
    st.dataframe(df)   # Display the source Excel data for reference
    csv_data = convert_df_to_csv(df) # Call the function to convert given DataFrame to csv

 # Download process
    st.write("### Download the Dataset")
    st.download_button(
        label="Download this data as CSV",
        data=csv_data,
        file_name='dataset.csv',
        mime='text/csv'
    )
