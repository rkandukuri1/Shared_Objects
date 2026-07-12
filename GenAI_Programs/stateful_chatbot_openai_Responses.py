import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.subheader("My Chat Application")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if "my_history" not in st.session_state:
    st.session_state.my_history = []

if "prev_response_id" not in st.session_state:
    st.session_state.prev_response_id = None                                                                                                                        

# Display Existing Chat
for message in st.session_state.my_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input("Enter your prompt: ")

if user_prompt:
    st.chat_message("user").write(user_prompt)
    st.session_state.my_history.append({"role": "user", "content": user_prompt})

    if st.session_state.prev_response_id is None:
        response = client.responses.create(
            model="gpt-4.1-nano",
            input=user_prompt
        )
    else:
        response = client.responses.create(
            model="gpt-4.1-nano",
            previous_response_id=st.session_state.prev_response_id,
            input=user_prompt
        )

    answer = response.output_text

    st.session_state.prev_response_id = response.id

    st.chat_message("assistant").write(answer)

    st.session_state.my_history.append({"role": "assistant", "content": answer})