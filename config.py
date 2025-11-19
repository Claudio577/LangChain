# config.py
import os
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-4.1-mini",   # <- ESTE É 100% COMPATÍVEL
        temperature=0.1,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
