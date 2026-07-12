import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.subheader("My Chat Application")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response():
    response = client.chat.completions.create(
        messages=st.session_state.my_history,
        model = "gpt-4.1-nano"
    )
    return response.choices[0].message.content

# ******   Main Program

# Step #1.1

# Initiate the history collection when there is no state maintained so far for the give session
if "my_history" not in st.session_state:
    st.session_state.my_history = [{"role": "system", "content" : "You are a chat assistant"}]

# Step #1.2

# Display the previous messages from History collection
if "my_history" in st.session_state:
   for x in st.session_state.my_history[1:]:
      with st.chat_message(x["role"]):
        st.write(x["content"])

user_prompt = st.chat_input("Enter your prompt")
if user_prompt:
   
    st.chat_message("human").write(user_prompt)    
     
    #Step #2: Append prompt to my_history collection 
    st.session_state.my_history.append({"role" : "user", "content" : user_prompt}) 

    with st.spinner("Thinking", show_time=True): # Calling the Reponse function with "Spiiner" symbol.
        result_txt = get_response()

    st.chat_message("ai").write(result_txt)

    #Step #3 : Append response to my_history collection 
    st.session_state.my_history.append({"role" : "assistant", "content" : result_txt}) 
