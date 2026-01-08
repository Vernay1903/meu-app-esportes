import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Estilo CSS Simplificado (Foco em corrigir o menu)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { 
        background-color: #1a1c23; 
    }
    /* Estilo do Título Neon */
    .sidebar-title {
        color: #00d4ff;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 10px #00d4ff;
        padding: 20px 0px;
    }
    /* Ajuste para o texto não ficar colado */
    .stSelectbox { margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Dicionário de Esportes e Vídeos
esportes_dict = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY"
}

# --- BARRA LATERAL (Apenas o Título e a Navegação) ---
st.sidebar.markdown('<p class="sidebar-title">✂️ CORTE DOS ESPORTES</p>', unsafe_allow_html=True)

st.sidebar.write("---")
escolha = st.sidebar.selectbox("ESCOLHA A MODALIDADE:", list(esportes_dict.keys()))
st.sidebar.write("---")

# --- ÁREA PRINCIPAL ---
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

st.title(f"✂️ {escolha}")
st.video(esportes_dict[escolha])

st.write("---")

# Seção Sobre Nós e Notícias (Agora no corpo principal para não travar o menu)
col_noticia1, col_noticia2 = st.columns(2)

with col_noticia1:
    st.subheader("📖 Sobre Nós")
    st.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito.")

with col_noticia2:
    st.subheader("📰 Plantão")
    st.success("Mercado da Bola: Fique por dentro das últimas contratações do seu time!")

st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")




