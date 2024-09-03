import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data()
def load_data():
    df = pd.read_excel(r"previsao/previsoes.xlsx")
    df = df.drop(["Unnamed: 0", "UF_Cliente", "Contrato", "Idade", "Valor_Renda", "Probabilidades", "Data_Contratacao"], axis=1)
    return df

df = load_data()

#selecionado uma coluna para o eixo X
coluna_x = st.selectbox("Selecione a coluna X", df.columns)

#selecionado uma coluna para o eixo Y
coluna_y = st.selectbox("Selecione a coluna Y", df.columns)

#selectbox para escolher o tipo de grafico
tipo_grafico = st.selectbox("Selecione o tipo de Gráfico", ["Histograma", "Gráfico de Barras", "Scatter", "Pizza", "Violino"])


#mostrando o grafico selecionado
if tipo_grafico == "Histograma":
    fig = px.histogram(df, x=coluna_x, color="Sexo", title=f"Histograma de: {coluna_x}")
    st.plotly_chart(fig)
elif tipo_grafico == "Gráfico de Barras":
    fig = px.bar(df, x=coluna_x, y=coluna_y, color=coluna_y, barmode="group", title=f"Gráfico de: {coluna_x} e {coluna_y}")
    st.plotly_chart(fig)
elif tipo_grafico == "Scatter":
    fig = px.scatter(df, x=coluna_x, y=coluna_y, color="Sexo", title=f"Gráfico de: {coluna_x} e {coluna_y}")
    st.plotly_chart(fig)
elif tipo_grafico == "Pizza":
    fig = px.pie(df, values=coluna_x, names=coluna_y, title=f"Gráfico de: {coluna_x} e {coluna_y}")
    st.plotly_chart(fig)
elif tipo_grafico == "Violino":
    fig = px.violin(df, y=coluna_y, x=coluna_x, color="Sexo",box=True, title=f"Gráfico de: {coluna_x} e {coluna_y}")
    st.plotly_chart(fig)

