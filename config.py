import os
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-4o",  # modelo 100% compatível com essa versão
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
