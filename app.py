import streamlit as st
from agents.agente_executivo import criar_agente_executivo

st.set_page_config(page_title="Agente Executivo", layout="wide")

st.title("💼 Agente Executivo – Estratégia Corporativa")

query = st.text_area("Digite sua pergunta:")

if st.button("Enviar"):
    agente = criar_agente_executivo()
    resposta = agente.invoke({"input": query})

    st.markdown("### 📌 Resposta Executiva")
    
    # LangChain retorna dict, pegar chave correta
    if isinstance(resposta, dict):
        if "output" in resposta:
            st.write(resposta["output"])
        elif "text" in resposta:
            st.write(resposta["text"])
        else:
            st.write(resposta)
    else:
        st.write(resposta)
