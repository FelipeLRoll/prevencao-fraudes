import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

@st.cache_data()
def load_data():
    df = pd.read_excel(r"previsao/previsoes.xlsx")
    df = df.drop(["Unnamed: 0", "UF_Cliente"], axis=1)
    return df

#carregando os dados
df= load_data()

#titulo da [agina]
st.header("Visualizando o DataFrame gerado pelo modelo")
st.divider()

#filtros
dynamic_filters = DynamicFilters(df, filters=["Sexo", "Regiao_UF_Cliente", "Previsoes", "Faixa_Etaria", "Faixa_Salarial", "Faixa_Dias_Atraso", "Faixa_Total_Pago", "Faixa_Saldo_Devedor", "Faixa_Prazo_Emprestimo", "Faixa_Prazo_Restante"])
dynamic_filters.display_filters(location="sidebar")
dynamic_filters.display_df()

