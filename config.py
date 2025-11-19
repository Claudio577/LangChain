# config.py
import os
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",       # modelo compatível
        temperature=0.1,
        openai_api_key=os.getenv("OPENAI_API_KEY")  # <- parâmetro CORRETO
    )
