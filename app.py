import streamlit as st

# 1. Configuração básica
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Seus vídeos e categorias
esportes = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY"
}

# --- BARRA LATERAL (Restaurando seus textos) ---
st.sidebar.title("✂️ Corte dos Esportes")
st.sidebar.divider()

# Usando o rádio para evitar que o menu "suma" ou "atropele" as letras
escolha = st.sidebar.radio(
    "🎯 NAVEGAÇÃO:",
    list(esportes.keys())
)

st.sidebar.divider()
st.sidebar.subheader("📖 Sobre Nós")
# Voltei com o seu texto original aqui:
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# --- ÁREA PRINCIPAL ---
# Banner
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

st.title(f"✂️ {escolha}")
st.video(esportes[escolha])

st.divider()

# Seção de Notícias (Plantão)
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.info("**🔥 Mercado da Bola:** Confira as últimas transferências.")

with col2:
    st.info("**🏀 NBA na Área:** Os melhores lances da rodada.")

st.sidebar.divider()
st.sidebar.caption("Propriedade de: Corte dos Esportes © 2026")




