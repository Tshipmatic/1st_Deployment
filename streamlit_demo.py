from langchain_openai import ChatOpenAI
import streamlit as st


st.title("Ask Anything")

with st.sidebar:
    st.title("Enter your API key")
    OPENAI_API_KEY = st.text_input("Enter your OPENAI_API_KEY: ", type="password")

if not OPENAI_API_KEY:
    st.info("Enter your OPENAI_API_KEY to continue.")
    st.stop()

 
llm=ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)