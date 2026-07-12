import streamlit as st

image = st.file_uploader(
    "Upload Image",
       type=["jpg", "png"]
)
if image:
    st.image(image)
