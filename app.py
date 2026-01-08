import streamlit as st

st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

esportes = {
    "🥊 Artes Marciais (UFC)": ["https://www.youtube.com/watch?v=F3Fv_rR8G-0"],
    "⚽ Futebol": ["https://www.youtube.com/watch?v=ra6ZalwC19c"],
    "🏀 Basquete": ["https://www.youtube.com/watch?v=9_pYvYmP1Xg"],
    "🏎️ Automobilismo": ["https://www.youtube.com/watch?v=8m9j_vKAnS0"],
    "🛹 Skate": ["https://www.youtube.com/watch?v=2p8N_8F9XmI"],
    "🏄 Surfe": ["https://www.youtube.com/watch?v=w772_2q7t-o"],
    "🏐 Vôlei": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
}

st.sidebar.title("MENU")
escolha = st.sidebar.radio("Selecione:", list(esportes.keys()))
st.sidebar.write("---")
st.sidebar.subheader("Sobre Nós")
st.sidebar.info("Apaixonados por esportes! Acompanhe seus lances favoritos aqui.")

st.title(f"✂️ Corte dos Esportes - {escolha}")
st.video(esportes[escolha][0])



