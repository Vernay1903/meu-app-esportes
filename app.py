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

# 3. Sidebar (Navegação e Sobre Nós corrigido)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=100)
st.sidebar.title("📌 NAVEGAÇÃO:")
escolha = st




