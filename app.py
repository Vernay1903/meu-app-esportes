import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Lista Completa de Esportes (Layout Seguro)
esportes = {
    "🥊 Artes Marciais (UFC)": ["https://www.youtube.com/watch?v=F3Fv_rR8G-0"],
    "🏃 Atletismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏎️ Automobilismo": ["https://www.youtube.com/watch?v=8m9j_vKAnS0"],
    "🏀 Basquete": ["https://www.youtube.com/watch?v=9_pYvYmP1Xg"],
    "🏅 Esportes Olímpicos": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "⚽ Futebol": ["https://www.youtube.com/watch?v=ra6ZalwC19c"],
    "🏈 Futebol Americano": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🤾 Handebol": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    " skateboard Skate": ["https://www.youtube.com/watch?v=2p8N_8F9XmI"],
    "🏄 Surfe": ["https://www.youtube.com/watch?v=w772_2q7t-o"],
    "🎾 Tênis": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏓 Tênis de Mesa": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏐 Vôlei": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏐 Vôlei de Praia": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
}

# 3. Barra Lateral (Menu e Sobre Nós Aprovado)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=80)
st.sidebar.title("MENU")
escolha = st.sidebar.radio("Selecione:", list



