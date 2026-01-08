import streamlit as st

# 1. TÍTULO NO TOPO E CONFIGURAÇÃO
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# Estilo para garantir que o título apareça de forma limpa
st.markdown("# ✂️ Corte dos Esportes")
st.write("---")

# 2. DICIONÁRIO DE VÍDEOS (Organizado)
esportes = {
    "🥊 Artes Marciais (UFC)": [
        "https://www.youtube.com/watch?v=F3Fv_rR8G-0"
    ],
    "⚽ Futebol": [
        "https://www.youtube.com/watch?v=ra6ZalwC19c"
    ],
    "🏀 Basquete": [
        "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    ],
    "🏎️ Automobilismo": [
        "https://www.youtube.com/watch?v=8m9j_vKAnS0"
    ],
    "🛹 Skate": [
        "https://www.youtube.com/watch?v=2p8N_8F9XmI"
    ],
    "🏄 Surfe": [
        "https://www.youtube.com/watch?v=w772_2q7t-o"
    ]
}

# 3. BARRA LATERAL (Menu e Texto corrigido)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=100)
st.sidebar.title("📌 NAVEGAÇÃO:")
escolha = st.sidebar.radio("Escolha o esporte:", list(esportes.keys()))

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos apaixonados por esportes, aqui você acompanha seu esporte favorito e quem sabe pode virar fã de outro esporte")

# 4. EXIBIÇÃO DO VÍDEO
st.header(f"{escolha}")




