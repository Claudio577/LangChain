from langchain_openai import ChatOpenAI
import os

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",   # 100% compatível com LangChain
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
