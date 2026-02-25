import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="SIMPLE CHATBOT USING GROQ"

prompt=ChatPromptTemplate.from_messages([
    ("system","you are a helpful assistant.please response based on the user query"),
    ("user","{question}")
])

def generate_response(question,api_key,llm,temperature,max_tokens):
    Groq(api_key=api_key)
    llm=ChatGroq(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer


##strealit app

st.title("SIMPLE CHATBOT")
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("enter your api key",type="password")
llm=st.sidebar.selectbox("Select AI model:",["llama-3.1-8b-instant","openai/gpt-oss-120b","llama-3.3-70b-versatile"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max_token",min_value=1,max_value=32768,value=16384)

##main interface
st.write("GO Ahead and Ask Your Question")
user_input=st.text_input("You:")
if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("please enter your  question")
