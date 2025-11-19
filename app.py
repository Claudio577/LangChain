import streamlit as st
from agents.agente_executivo import criar_agente_executivo

st.title("💼 Agente Executivo - Estratégia")

query = st.text_area("Pergunta:")

if st.button("Enviar"):
    agente = criar_agente_executivo()
    resposta = agente.invoke({"input": query})
    st.write("### Resposta:")
    st.write(resposta["output"])
