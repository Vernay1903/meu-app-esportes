import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Estilo Visual (Fundo Escuro e Neon)
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

# 4. DICIONÁRIO DE VÍDEOS (TROQUE APENAS O QUE ESTÁ ENTRE ASPAS)
# Use links completos do YouTube: https://www.youtube.com/watch?v=...
esportes_dict = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# --- BARRA LATERAL ---
st.sidebar.markdown('<p class="neon-text">✂️ CORTE DOS ESPORTES</p>', unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Navegação")
escolha = st.sidebar.selectbox("Escolha a Modalidade:", list(esportes_dict.keys()))

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito.")

# --- ÁREA PRINCIPAL ---
st.title(f"✂️ {escolha}")
st.write(f"Assista aos melhores momentos de **{escolha}**.")

# Tentativa de carregar o vídeo
try:
    st.video(esportes_dict[escolha])
except:
    st.error("Ops! Este link de vídeo parece estar quebrado ou indisponível.")

st.write("---")

# 5. SEÇÃO DE NOTÍCIAS (Plantão)
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="noticia-box"><h4>🔥 Mercado da Bola</h4><p>Confira as últimas movimentações do futebol mundial.</p></div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="noticia-box"><h4>🏀 NBA na Área</h4><p>Resultados e lances da rodada americana.</p></div>""", unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")




