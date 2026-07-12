import streamlit as st

kb = st.sidebar.selectbox(
    "Choose Knowledge Base",
    ["Wikipedia", "Google News", "OpenAI"]
)

subject = st.sidebar.selectbox(
         "select subject",
        ["History", "Science", "Math"]
)

submit = st.sidebar.button("Get Info")

st.title("Subject Info")
st.divider()

st.header(f"Knowledge Base: {kb}" )
st.subheader(f"Subject: {subject}")
