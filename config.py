# config.py
import os

# FORÇAR import da biblioteca certa
import langchain_openai.chat_models
from langchain_openai.chat_models import ChatOpenAI

print("Carregando ChatOpenAI de:", ChatOpenAI.__module__)

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.1
    )
