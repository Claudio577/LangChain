from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from config import get_llm

EXECUTIVE_PROMPT = """
Você é um Executivo Sênior especializado em planejamento estratégico,
gestão de riscos e tomada de decisão corporativa. 

Seu estilo é:
- direto
- profissional
- estruturado
- orientado a negócios

Sempre responda com clareza executiva.
"""

def criar_agente_executivo():
    llm = get_llm()

    tools = []  # por enquanto sem ferramentas

    agente = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        system_message=EXECUTIVE_PROMPT,
    )

    return agente
