import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# Banner Principal - AGORA USANDO SUA IMAGEM OFICIAL
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# Barra Lateral
st.sidebar.title("✂️ Menu Principal")
esporte = st.sidebar.selectbox("Escolha a Modalidade:", ["Futebol", "Basquete", "Vôlei", "Surfe"])

st.title("✂️ Corte dos Esportes")
st.subheader(f"Análise e Destaques: {esporte}")

st.write("---")

# Seção de Vídeos
st.markdown(f"### 📺 Últimos Cortes de {esporte}")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 

st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")
