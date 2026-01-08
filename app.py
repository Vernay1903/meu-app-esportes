import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Seus vídeos e categorias (Links seguros)
esportes = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY"
}

# --- BARRA LATERAL (Sidebar) ---
st.sidebar.title("✂️ Corte dos Esportes")
st.sidebar.markdown("---")

# Mudamos para 'radio' com uma chave nova para forçar a limpeza do erro
escolha = st.sidebar.radio(
    "🎯 NAVEGAÇÃO:",
    list(esportes.keys()),
    key="menu_v5_final"
)

st.sidebar.markdown("---")

# Seu texto original recuperado com sucesso
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# --- ÁREA PRINCIPAL ---
# Banner
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

st.title(f"✂️ {escolha}")

# Player de Vídeo
st.video(esportes[escolha])

st.markdown("---")

# Seção de Notícias (Plantão) que já estava funcionando bem
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.success("**🔥 Mercado da Bola:** As últimas transferências do mundo do futebol.")

with col2:
    st.warning("**🏀 NBA na Área:** Confira os resultados e destaques das quadras.")

st.sidebar.markdown("---")
st.sidebar.caption("Corte dos Esportes © 2026")




