import streamlit as st

# 1. Configuração da página (DEVE SER A PRIMEIRA COISA)
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Estilo CSS para o Fundo Escuro e o Título Neon
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    [data-testid="stSidebar"] {
        background-color: #1a1c23;
    }
    /* Estilo do Título Neon Azul */
    .neon-text {
        color: #00d4ff;
        font-size: 25px;
        font-weight: bold;
        text-transform: uppercase;
        text-shadow: 0 0 5px #00d4ff, 0 0 10px #00d4ff, 0 0 20px #00bfff;
        font-family: 'sans-serif';
        margin-bottom: -10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Banner Principal
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# 4. Dicionário de Esportes e Vídeos
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

# 5. Barra Lateral com Título Neon
st.sidebar.markdown('<p class="neon-text">✂️ CORTE DOS ESPORTES</p>', unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.subheader("🎯 Navegação")
escolha = st.sidebar.selectbox("Escolha a Modalidade:", list(esportes_dict.keys()))

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# 6. Área Principal
st.title(f"✂️ {escolha}")
st.write(f"Confira os melhores momentos de **{escolha}**.")
st.video(esportes_dict[escolha]) 

st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")


