import streamlit as st

st.set_page_config(
    page_title="Página Inicial",
    page_icon="👋",
)
st.write("# Previsão de Fraude")
st.divider()
st.markdown("#### WebApp que permite visualizar informações de uma tabela gerada através de um modelo de Machine Learning para prever fraudes.")
st.divider()
st.image("screenshots/parcela.jpg")

st.sidebar.success("Selecione uma Página acima.")