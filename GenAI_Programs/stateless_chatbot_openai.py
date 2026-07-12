import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

st.subheader("My First Chat Application")
st.divider()

def get_response(question):
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
           messages=[  {"role" : "user", "content" : question}  ]
        )   
        return response.choices[0].message.content

user_prompt = st.chat_input("Enter your prompt")
if user_prompt:
   with st.spinner("Thinking", show_time=True):
        result_txt = get_response(user_prompt)

   st.chat_message("human").write(user_prompt)
   st.chat_message("ai").write(result_txt)
