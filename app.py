import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário de Esportes e Vídeos
# DICA: Se um vídeo der "indisponível", tente trocar por outro link do YouTube.
esportes_dict = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY"
}

# --- BARRA LATERAL (Sidebar) ---
st.sidebar.title("✂️ Corte dos Esportes")
st.sidebar.markdown("---")

# Menu de Navegação simples para evitar erros visuais
escolha = st.sidebar.selectbox(
    "ESCOLHA A MODALIDADE:", 
    list(esportes_dict.keys())
)

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.write("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito.")

# --- ÁREA PRINCIPAL ---
# Banner
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# Título e Vídeo
st.title(f"✂️ {escolha}")
st.video(esportes_dict[escolha])

st.markdown("---")

# Seção de Notícias (Plantão)
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.info("**🔥 Mercado da Bola:** Confira as últimas transferências.")

with col2:
    st.info("**🏀 NBA na Área:** Os melhores lances da rodada.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.caption("Propriedade de: Corte dos Esportes © 2026")




