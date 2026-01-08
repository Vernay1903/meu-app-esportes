import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário Completo com 14 esportes em ordem alfabética
esportes = {
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏃 Atletismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🏅 Esportes Olímpicos": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏈 Futebol Americano": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🤾 Handebol": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🛹 Skate": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏄 Surfe": "https://www.youtube.com/watch?v=l_S6L-Rno4U",
    "🎾 Tênis": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏓 Tênis de Mesa": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY",
    "🏖️ Vôlei de Praia": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# --- BARRA LATERAL (Sidebar) ---
st.sidebar.title("✂️ Corte dos Esportes")
st.sidebar.markdown("---")

# Menu em formato 'radio' que resolveu o problema visual
escolha = st.sidebar.radio(
    "🎯 NAVEGAÇÃO:",
    list(esportes.keys()),
    key="menu_versao_final_estavel"
)

st.sidebar.markdown("---")

# Seu texto original do Sobre Nós (Restaurado e Protegido)
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# --- ÁREA PRINCIPAL ---
# Banner Principal
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

st.title(f"✂️ {escolha}")

# Exibição do Vídeo
st.video(esportes[escolha])

st.markdown("---")

# Seção de Notícias (Plantão)
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.info("**🔥 Mercado da Bola:** As últimas transferências do mundo do futebol.")

with col2:
    st.info("**🏀 NBA na Área:** Confira os destaques das quadras.")

st.sidebar.markdown("---")
st.sidebar.caption("Propriedade de: Corte dos Esportes © 2026")




