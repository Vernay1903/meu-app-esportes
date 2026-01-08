import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Estilo CSS (Fundo Escuro e Título Neon)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #1a1c23; }
    .neon-text {
        color: #00d4ff;
        font-size: 25px;
        font-weight: bold;
        text-transform: uppercase;
        text-shadow: 0 0 10px #00d4ff;
        font-family: 'sans-serif';
    }
    .noticia-box {
        background-color: #1a1c23;
        padding: 15px;
        border-left: 5px solid #00d4ff;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Banner
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# 4. Dicionário de Esportes
esportes_dict = {
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY"
}

# 5. Barra Lateral
st.sidebar.markdown('<p class="neon-text">✂️ CORTE DOS ESPORTES</p>', unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Navegação")
escolha = st.sidebar.selectbox("Escolha a Modalidade:", list(esportes_dict.keys()))
st.sidebar.markdown("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# 6. Área Principal - Vídeo
st.title(f"✂️ {escolha}")
st.video(esportes_dict[escolha]) 

st.write("---")

# 7. SEÇÃO DE NOTÍCIAS
st.header("📰 Plantão Corte dos Esportes")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="noticia-box">
        <h4>🔥 Mercado da Bola</h4>
        <p>As últimas transferências e rumores do mundo do futebol nacional e internacional.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="noticia-box">
        <h4>🏀 NBA na Área</h4>
        <p>Confira os resultados da rodada e quem está brilhando nas quadras americanas.</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")




