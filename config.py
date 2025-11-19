# config.py
import os
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",     # modelo estável e 100% compatível
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")  # chave vinda do Streamlit Secrets
    )
