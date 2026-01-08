import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário de Esportes e Vídeos Reais
esportes = {
    "🥊 Artes Marciais (UFC)": [
        "https://www.youtube.com/watch?v=F3Fv_rR8G-0"
    ],
    "⚽ Futebol": [
        "https://www.youtube.com/watch?v=ra6ZalwC19c"
    ],
    "🏀 Basquete": [
        "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    ],
    "🏎️ Automobilismo": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "🛹 Skate": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "🏄 Surfe": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ]
}

# 3. Sidebar (Navegação e Sobre Nós - CORRIGIDO)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=100)
st.sidebar.title("📌 NAVEGAÇÃO:")
escolha = st.sidebar.radio("Escolha o esporte:", list(esportes.keys()))

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos apaixonados por esportes, aqui você acompanha seu esporte favorito e quem sabe pode virar fã de outro esporte")

# 4. Área Principal (Player de Vídeo)
st.title(f"{escolha}")
st.subheader("🔥 Último Corte")

lista_videos = esportes[escolha]
if lista_videos:
    st.video(lista_videos[0])

# 5. Histórico
if len(lista_videos) > 1:
    st.write("---")
    st.subheader("📜 Histórico de Vídeos")
    cols = st.columns(2)
    for i, vid in enumerate(lista_videos[1:]):
        with cols[i % 2]:
            st.video(vid)




