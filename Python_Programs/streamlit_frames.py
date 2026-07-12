import streamlit as st

st.subheader("Streamlit Frames")
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Column - 1")
    st.write("Data for 1st Frame")
    st.write("Data Continued...")

with col2:
    st.write("Column - 2")
    st.write("Data for 2nd Frame")
    st.write("Data Continued...")

with col3:
    st.write("Column - 3")
    st.write("Data for 3rd Frame")
    st.write("Data Continued...")

