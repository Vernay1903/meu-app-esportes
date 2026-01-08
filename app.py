import streamlit as st

# 1. LAYOUT DA PÁGINA
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. TÍTULO NO TOPO (EXATAMENTE COMO VOCÊ APROVOU)
st.title("✂️ Corte dos Esportes")
st.write("---")

# 3. DICIONÁRIO COMPLETO (14 CATEGORIAS)
esportes = {
    "🥊 Artes Marciais (UFC)": ["https://www.youtube.com/watch?v=F3Fv_rR8G-0"],
    "🏃 Atletismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏎️ Automobilismo": ["https://www.youtube.com/watch?v=8m9j_vKAnS0"],
    "🏀 Basquete": ["https://www.youtube.com/watch?v=9_pYvYmP1Xg"],
    "🏅 Esportes Olímpicos": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "⚽ Futebol": ["https://www.youtube.com/watch?v=ra6ZalwC19c"],
    "🏈 Futebol Americano": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🤾 Handebol": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🛹 Skate": ["https://www.youtube.com/watch?v=2p8N_8F9XmI"],
    "🏄 Surfe": ["https://www.youtube.com/watch?v=w772_2q7t-o"],
    "🎾 Tênis": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏓 Tênis de Mesa": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏐 Vôlei": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏐 Vôlei de Praia": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
}

# 4. MENU LATERAL (ORGANIZADO)
st.sidebar.title("📌 MENU")
escolha = st.sidebar.radio("Escolha o esporte:", list(esportes.keys()))

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos apaixonados por esportes! Aqui você acompanha os melhores cortes e lances do mundo esportivo.")

# 5. ÁREA DO VÍDEO
st.header(f"🔥 Categoria: {escolha}")
st.video(esportes[escolha][0])



