from langchain.agents import create_react_agent
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate
from config import get_llm

EXECUTIVE_PROMPT = """
Você é um Executivo Sênior especializado em estratégia corporativa,
gestão de riscos e tomada de decisão de alto nível.

Seu estilo é:
- direto
- claro
- objetivo
- estruturado
- orientação a resultados

Sempre responda com clareza executiva.
"""

def criar_agente_executivo():
    llm = get_llm()

    # Prompt moderno, compatível com LangChain 0.2.x
    prompt = ChatPromptTemplate.from_messages([
        ("system", EXECUTIVE_PROMPT),
        ("human", "{input}")
    ])

    # Nenhuma tool (por enquanto)
    tools = []

    agente = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
        verbose=False
    )

    return agente
