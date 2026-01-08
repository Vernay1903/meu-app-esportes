import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha de código)
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Estilo Visual (Fundo Escuro e Título Neon)
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

# 3. Banner Principal
# Verifique se o nome do arquivo da imagem está exatamente igual ao que você salvou
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# 4. DICIONÁRIO DE VÍDEOS (Aqui é onde você troca os links!)
esportes_dict = {
    "⚽ Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY",
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏄 Surfe": "https://www.youtube.com/watch?v=l_S6L-Rno4U",
    # Para adicionar mais, basta seguir o padrão: "Nome": "Link",
}

# --- BARRA LATERAL ---
st.sidebar.markdown('<p class="neon-text">✂️ CORTE DOS ESPORTES</p>', unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.subheader("🎯 Navegação")
escolha = st.sidebar.selectbox("Escolha a Modalidade:", list(esportes_dict.keys()))

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# --- ÁREA PRINCIPAL ---
st.title(f"✂️ {escolha}")
st.write(f"Assista aos melhores momentos de **{escolha}**.")

# Exibição do Vídeo Escolhido
st.video(esportes_dict[escolha]) 

st.write("---")

# 5. SEÇÃO DE NOTÍCIAS (Plantão)
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="noticia-box"><h4>🔥 Mercado da Bola</h4><p>Confira as últimas movimentações do futebol mundial.</p></div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="noticia-box"><h4>🏆 Destaque da Semana</h4><p>Os lances que pararam o mundo dos esportes nos últimos dias.</p></div>""", unsafe_allow_html=True)

# Rodapé lateral
st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")




