import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu App de Esportes", layout="wide")

# Banner Principal
st.image("https://images.unsplash.com/photo-1461896836934-ffe607ba8211?q=80&w=2070&auto=format&fit=crop", use_container_width=True)

st.title("🏆 Portal de Esportes")
st.write("Bem-vindo ao seu guia alfabético de modalidades esportivas!")

# Lista de Esportes
esportes = [
    "Atletismo", "Basquete", "Ciclismo", "Esportes Olímpicos", 
    "Futebol", "Ginástica", "Handebol", "Judô", "Karatê", 
    "Natação", "Surfe", "Tênis", "Vôlei"
]

# Criando a interface
escolha = st.selectbox("Selecione um esporte para saber mais:", sorted(esportes))

st.info(f"Você selecionou: **{escolha}**")
st.write("Em breve, traremos mais detalhes sobre esta modalidade!")
