from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
import os
from dotenv import load_dotenv

load_dotenv()

client = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4.1-nano")

my_file = "VigilantCorp_Company_Profile.pdf"

loader = PyPDFLoader(my_file)
docs = loader.load()

user_prompt = ""
while user_prompt != "exit":
    if user_prompt == "exit":
        break
    print("")
    user_prompt = input("Enter your question: ")

    my_prompt = f'''
        You are a helpful assistant. Answer the questions based only on the provided data, dont use
        your existing knowledge.

        Question: {user_prompt}
        Document: {docs}
        '''

    response = client.invoke(my_prompt)
    print (response.content)


