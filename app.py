import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário de Vídeos (Links verificados)
esportes_dict = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY"
}

# --- BARRA LATERAL (Sidebar) ---
# Usando apenas comandos nativos para evitar sobreposição no menu
st.sidebar.title("✂️ Corte dos Esportes")
st.sidebar.divider()

escolha = st.sidebar.selectbox(
    "SELECIONE O ESPORTE:", 
    list(esportes_dict.keys()),
    key="menu_reset_final"
)

st.sidebar.divider()
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.write("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito.")

# --- ÁREA PRINCIPAL ---
# Banner Principal
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# Título do Esporte Escolhido
st.header(f"🎥 {escolha}")

# Exibição do Vídeo
st.video(esportes_dict[escolha])

st.divider()

# Seção de Notícias (Plantão)
st.subheader("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.info("**🔥 Mercado da Bola:** Acompanhe as últimas transferências.")

with col2:
    st.info("**🏀 Destaque NBA:** Veja os melhores lances da rodada.")

# Rodapé lateral
st.sidebar.divider()
st.sidebar.caption("Propriedade de: Corte dos Esportes © 2026")




