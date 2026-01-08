import streamlit as st

# 1. Configuração da página - SEMPRE a primeira linha
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário de Vídeos (Links testados que permitem reprodução)
esportes_dict = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY"
}

# --- BARRA LATERAL NATIVA (O segredo para não dar erro) ---
st.sidebar.title("✂️ Corte dos Esportes")
st.sidebar.write("---")

# Menu de escolha sem estilização que cause sobreposição
escolha = st.sidebar.selectbox(
    "SELECIONE O ESPORTE:", 
    list(esportes_dict.keys()),
    key="menu_v3"
)

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito.")

# --- ÁREA PRINCIPAL ---
# Exibição do Banner
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# Título dinâmico
st.header(f"Você está assistindo: {escolha}")

# Vídeo (Usando o link do dicionário)
st.video(esportes_dict[escolha])

st.write("---")

# Seção de Notícias usando colunas padrão
st.subheader("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.info("**🔥 Mercado da Bola:** Acompanhe as últimas transferências mundiais.")

with col2:
    st.info("**🏆 Destaques:** Confira os lances que marcaram a semana.")

st.sidebar.write("---")
st.sidebar.caption("Corte dos Esportes © 2026")




