from langchain.agents import initialize_agent, AgentType
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

    agente = initialize_agent(
        tools=[],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        system_message=EXECUTIVE_PROMPT
    )

    return agente
