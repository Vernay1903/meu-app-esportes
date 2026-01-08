import streamlit as st

# Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# Banner Principal
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# Dicionário de Esportes e Vídeos
esportes_dict = {
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Boxe": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🚴 Ciclismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏅 Esportes Olímpicos": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏈 Futebol Americano": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "👟 Futsal": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🤾 Handebol": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏊 Natação": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🛹 Skate": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏄 Surfe": "https://www.youtube.com/watch?v=l_S6L-Rno4U",
    "🎾 Tênis": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY",
    "🏖️ Vôlei de Praia": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# --- BARRA LATERAL (Sidebar) ---
st.sidebar.markdown("# ✂️ CORTE DOS ESPORTES")
st.sidebar.markdown("---")

# 1. Menu de Navegação primeiro (para não cobrir o texto)
st.sidebar.subheader("🎯 Navegação")
escolha = st.sidebar.selectbox("Escolha a Modalidade:", list(esportes_dict.keys()))

st.sidebar.markdown("---")

# 2. Seção Sobre Nós logo abaixo
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# --- ÁREA PRINCIPAL ---
st.title(f"✂️ {escolha}")
st.write(f"Confira os melhores momentos e análises de **{escolha.split(' ')[1]}**.")

st.write("---")

# Exibição do Vídeo
st.markdown(f"### 📺 Último Corte: {escolha}")
st.video(esportes_dict[escolha]) 

# Rodapé
st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")


