import streamlit as st
import langchain
import langchain_openai

st.write("LangChain:", langchain.__version__)
st.write("LangChain-OpenAI:", langchain_openai.__version__)

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
