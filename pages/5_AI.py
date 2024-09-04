
import pandas as pd
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI

df = pd.read_csv(r"dataset/dados_coletados80k.csv")

agente = create_pandas_dataframe_agent(
    ChatGoogleGenerativeAI(model="gemini-pro", language="pt", max_tokens=50000, allow_method_calls=True, handle_parsing_errors=True, timeout=30),
    df,
    allow_dangerous_code=True,
)

resposta_previa = ""

pergunta = st.text_input("Faça uma pergunta sobre o Dataset:")

if st.button("Pergunta"):
    try:
        if resposta_previa:
            pergunta = f"{resposta_previa} {pergunta}" 
        resposta = agente.invoke(pergunta)
        st.write("Resposta:", resposta)
        resposta_previa = resposta
    except Exception as e:
        st.error("Ocorreu um erro ao processar a pergunta. Por favor, tente novamente.")
        st.error(f"Detalhes do erro: {str(e)}")
