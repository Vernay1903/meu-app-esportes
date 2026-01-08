import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário de Esportes e Vídeos
esportes = {
    "🥊 Artes Marciais (UFC)": [
        "https://www.youtube.com/watch?v=v9U8O_UvH-U"
    ],
    "🏃 Atletismo": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "🏎️ Automobilismo": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "🏀 Basquete": [
        "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    ],
    "🏅 Esportes Olímpicos": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "⚽ Futebol": [
        "https://www.youtube.com/watch?v=9Is976o_TMc"
    ]
}

# 3. Interface do Site
st.sidebar.title("📌 NAVEGAÇÃO:")
escolha = st.sidebar.radio("Escolha o esporte:", list(esportes.keys()))

st.title(f"{escolha}")
st.subheader("🔥 Último Corte")

# Pega o primeiro vídeo da lista do esporte escolhido
lista_videos = esportes[escolha]
st.video(lista_videos[0])

# 4. Histórico (se houver mais de um vídeo)
if len(lista_videos) > 1:
    st.write("---")
    st.subheader("📜 Histórico de Vídeos")
    for vid in lista_videos[1:]:
        st.video(vid)




