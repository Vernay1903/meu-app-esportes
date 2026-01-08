import streamlit as st

# 1. Configuração básica (obrigatório ser a primeira linha)
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. Lista de vídeos (links seguros)
esportes = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 UFC": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# --- BARRA LATERAL LIMPA ---
st.sidebar.header("✂️ CORTE DOS ESPORTES")

# Criamos um menu sem nenhuma frescura para não dar erro
escolha = st.sidebar.radio(
    "MENU DE NAVEGAÇÃO:",
    list(esportes.keys())
)

st.sidebar.divider()
st.sidebar.info("Somos apaixonados por esportes e cortes épicos!")

# --- ÁREA PRINCIPAL ---
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

st.title(f"Assistindo: {escolha}")

# Exibe o vídeo
st.video(esportes[escolha])

st.divider()
st.subheader("📰 Notícias Rápidas")
st.write("🔥 **Mercado:** Fique de olho nas contratações de hoje!")




