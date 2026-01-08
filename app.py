import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. DICIONÁRIO COM HISTÓRICO (Agora é uma LISTA de links)
# O primeiro link da lista [0] será sempre o vídeo principal (o mais novo)
esportes = {
    "🥊 Artes Marciais (UFC)": [
        "https://www.youtube.com/watch?v=v9U8O_UvH-U", 
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "🏃 Atletismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏎️ Automobilismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏀 Basquete": ["https://www.youtube.com/watch?v=9_pYvYmP1Xg"],
    "🏅 Esportes Olímpicos": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "⚽ Futebol": [
        "https://www.youtube.com/watch?v=9Is976o_TMc",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
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
    key="menu_historico"
)

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos movidos pela paixão ao esporte, criando um ambiente para você acompanhar seu esporte favorito e quem sabe virar fã de outro esporte.")

# --- ÁREA PRINCIPAL ---
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# Título do Esporte
st.title(f"✂️ {escolha}")

# Pegamos a lista de vídeos do esporte escolhido
lista_videos = esportes[escolha]

# VÍDEO PRINCIPAL (O primeiro da lista)
st.subheader("🔥 Último Corte")
st.video(lista_videos[0])

st.markdown("---")

# HISTÓRICO (Se houver mais de um vídeo na lista)
if len(lista_videos) > 1:
    st.subheader("📜 Histórico de Vídeos")
    # Mostra os outros vídeos da lista
    for i in range(1, len(lista_videos)):
        with st.expander(f"Vídeo Antigo {i}"):
            st.video(lista_videos[i])
else:
    st.write("✨ Em breve, mais vídeos neste histórico!")

st.sidebar.markdown("---")
st.sidebar.caption("Corte dos Esportes © 2026")




