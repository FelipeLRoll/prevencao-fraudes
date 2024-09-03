import os
import streamlit as st
import streamlit.components.v1 as components

#pasta dos graficos
pasta_html = 'html/'

#arquivos .html da pasta
arquivos_html = [f for f in os.listdir(pasta_html) if f.endswith('.html')]

#dicionario para guardar e abrir os arquivos .html
conteudo_html = {}
for arquivo_html in arquivos_html:
    with open(os.path.join(pasta_html, arquivo_html), 'r', encoding='utf-8') as file:
        conteudo_html[arquivo_html] = file.read()


st.title("Visualização de Gráficos Prontos")

#selectbox para selecionar o grafico
grafico_selecionado = st.selectbox("Selecione um Gráfico", arquivos_html)

#Display the selected chart
if grafico_selecionado:
    st.markdown(f"### {grafico_selecionado}")
    components.html(conteudo_html[grafico_selecionado], height=1500, width=1000, scrolling=True)