from langchain_openai.chat_models import ChatOpenAI

import os
import langchain_openai
print("Using langchain_openai from:", langchain_openai.__file__)

def get_llm():
    print("Using ChatOpenAI from module:", ChatOpenAI.__module__)
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
