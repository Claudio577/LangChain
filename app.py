import streamlit as st
import langchain
st.write("API KEY carregada?", os.getenv("OPENAI_API_KEY") is not None)
# tentativa de detectar se o pacote está presente
try:
    import langchain_openai
    st.success("LangChain-OpenAI está instalado e funcionando!")
except Exception as e:
    st.error("Erro ao carregar LangChain-OpenAI")
    st.error(str(e))

except Exception as e:
    st.write("LangChain-OpenAI NÃO INSTALADO:", e)

st.write("LangChain:", langchain.__version__)

from agents.agente_executivo import criar_agente_executivo

st.title("💼 Agente Executivo – Estratégia Corporativa")

query = st.text_area("Digite sua pergunta:")

if st.button("Enviar"):
    agente = criar_agente_executivo()
    resposta = agente.invoke({"input": query})

    st.markdown("### 📌 Resposta Executiva")
    
    if isinstance(resposta, dict):
        if "output" in resposta:
            st.write(resposta["output"])
        elif "text" in resposta:
            st.write(resposta["text"])
        else:
            st.write(resposta)
    else:
        st.write(resposta)

