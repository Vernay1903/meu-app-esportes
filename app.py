import streamlit as st

# 1. Configuração da página (Sempre no topo)
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Estilo Visual - Fundo Escuro e Organização
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #1a1c23; min-width: 300px; }
    
    /* Título na Lateral */
    .sidebar-title {
        color: #00d4ff;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 10px #00d4ff;
        margin-bottom: 20px;
    }
    
    /* Box de Notícias */
    .noticia-box {
        background-color: #1a1c23;
        padding: 15px;
        border-left: 5px solid #00d4ff;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Dicionário de Vídeos (Links testados e funcionando)
esportes_dict = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=v9U8O_UvH-U",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# --- MONTAGEM DA BARRA LATERAL ---
st.sidebar.markdown('<p class="sidebar-title">✂️ CORTE DOS ESPORTES</p>', unsafe_allow_html=True)

st.sidebar.subheader("🎯 Navegação")
# O segredo para o menu não quebrar é garantir que ele tenha uma chave única (key)
escolha = st.sidebar.selectbox("Escolha a Modalidade:", list(esportes_dict.keys()), key="menu_principal")

st.sidebar.write("---")

st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito.")

# --- ÁREA PRINCIPAL ---
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

st.title(f"✂️ {escolha}")

# Exibição do Vídeo
video_url = esportes_dict[escolha]
st.video(video_url)

st.write("---")

# 4. SEÇÃO DE NOTÍCIAS
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="noticia-box"><h4>🔥 Mercado da Bola</h4><p>As últimas transferências e rumores do futebol mundial.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="noticia-box"><h4>🏀 NBA na Área</h4><p>Confira os resultados e quem brilhou nas quadras americanas.</p></div>', unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")




