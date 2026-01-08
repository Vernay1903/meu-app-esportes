import streamlit as st

st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário com Histórico (14 categorias em ordem alfabética)
# Para adicionar mais vídeos, basta colocar uma vírgula dentro dos colchetes []
esportes = {
    "🥊 Artes Marciais (UFC)": "🥊 Artes Marciais (UFC)": [
        "https://www.youtube.com/watch?v=SEU_VIDEO_NOVO_1", 
        "https://www.youtube.com/watch?v=VIDEO_ANTIGO_OU_HISTORICO"
    "🏃 Atletismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏎️ Automobilismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏀 Basquete": ["https://www.youtube.com/watch?v=9_pYvYmP1Xg"],
    "🏅 Esportes Olímpicos": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "⚽ Futebol": ["https://www.youtube.com/watch?v=9Is976o_TMc"],
    "🏈 Futebol Americano": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🤾 Handebol": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🛹 Skate": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏄 Surfe": ["https://www.youtube.com/watch?v=l_S6L-Rno4U"],
    "🎾 Tênis": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏓 Tênis de Mesa": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏐 Vôlei": ["https://www.youtube.com/watch?v=mD07R_N9WpY"],
    "🏖️ Vôlei de Praia": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
}

# --- BARRA LATERAL ---
st.sidebar.title("✂️ Corte dos Esportes")
st.sidebar.markdown("---")

escolha = st.sidebar.radio(
    "🎯 NAVEGAÇÃO:",
    list(esportes.keys()),
    key="menu_v3_final"
)

st.sidebar.markdown("---")

# Texto Sobre Nós
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# --- ÁREA PRINCIPAL ---
# Banner (Certifique-se que o nome do arquivo no GitHub é igual a este abaixo)
try:
    st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)
except:
    st.warning("Banner não encontrado. Verifique o nome do arquivo no GitHub.")

st.title(f"✂️ {escolha}")

# Lógica do Vídeo e Histórico
lista_videos = esportes[escolha]

# Vídeo Principal
st.subheader("🔥 Último Corte")
st.video(lista_videos[0])

st.markdown("---")

# Histórico
if len(lista_videos) > 1:
    st.subheader("📜 Histórico de Vídeos")
    for i in range(1, len(lista_videos)):
        with st.expander(f"Vídeo Antigo {i}"):
            st.video(lista_videos[i])
else:
    st.write("✨ Novos vídeos serão adicionados em breve ao histórico!")

# Seção de Notícias
st.header("📰 Plantão Corte dos Esportes")
col1, col2 = st.columns(2)
with col1:
    st.info("**🔥 Mercado da Bola:** As últimas transferências do mundo do futebol.")
with col2:
    st.info("**🏀 NBA na Área:** Confira os destaques das quadras.")

st.sidebar.markdown("---")
st.sidebar.caption("Propriedade de: Corte dos Esportes © 2026")




