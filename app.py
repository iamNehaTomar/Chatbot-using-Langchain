##from langchain_openai import ChatOpenAi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain_ollama import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
##os.environ["OPEN_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## PROMPT TEMPLATE

prompt = ChatPromptTemplate.from_messages(
[ ("system", "you are a helpful assistant. please respond to queries"),
   ("user", "Question:{question}")
]
)

## STREAMLIT FRAMEWORK

st.title('Langchain Demo with Ollama')
input_text = st.text_input("Search the topic you want")


## OLLAMA LLAMA2 LLM

llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))