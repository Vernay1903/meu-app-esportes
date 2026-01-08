import streamlit as st

# 1. Configuração principal (Título na aba do navegador)
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. LISTA DE VÍDEOS (Adicione novos links dentro dos colchetes)
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
        "https://www.youtube.com/watch?v=8m9j_vKAnS0"
    ],
    "🛹 Skate": [
        "https://www.youtube.com/watch?v=2p8N_8F9XmI"
    ],
    "🏄 Surfe": [
        "https://www.youtube.com/watch?v=w772_2q7t-o"
    ]
}

# 3. BARRA LATERAL (Menu e Texto Sobre Nós)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=100)
st.sidebar.title("📌 NAVEGAÇÃO:")
escolha = st.sidebar.radio("Escolha o esporte:", list(esportes.keys()))

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos apaixonados por esportes, aqui você acompanha seu esporte favorito e quem sabe pode virar fã de outro esporte")

# 4. ÁREA DO VÍDEO (Onde o conteúdo aparece)
st.title(f"{escolha}")
st.subheader("🔥 Último Corte")

# Pega os vídeos da categoria escolhida
lista_videos = esportes[escolha]

if lista_videos:
    # Mostra o vídeo principal (o primeiro da lista)
    st.video(lista_videos[0])

    # Se tiver mais vídeos, mostra abaixo como histórico
    if len(lista_videos) > 1:
        st.write("---")
        st.subheader("📜 Histórico de Vídeos")
        cols = st.columns(2)
        for i, vid in enumerate(lista_videos[1:]):
            with cols[i % 2]:
                st.video(vid)




