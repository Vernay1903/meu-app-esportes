import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# 2. Dicionário de Esportes e Vídeos (Lista Completa)
esportes = {
    "🥊 Artes Marciais (UFC)": ["https://www.youtube.com/watch?v=v9U8O_UvH-U"],
    "🏃 Atletismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏎️ Automobilismo": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏀 Basquete": ["https://www.youtube.com/watch?v=9_pYvYmP1Xg"],
    "🏅 Esportes Olímpicos": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "⚽ Futebol": ["https://www.youtube.com/watch?v=9Is976o_TMc"],
    "🏈 Futebol Americano": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🤾 Handebol": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🛹 Skate": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏄 Surfe": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🎾 Tênis": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏓 Tênis de Mesa": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏐 Vôlei": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "🏐 Vôlei de Praia": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
}

# 3. Sidebar (Navegação com o novo texto)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=100)
st.sidebar.title("📌 NAVEGAÇÃO:")
escolha = st.sidebar.radio("Escolha o esporte:", list(esportes.keys()))

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos apaixonados por esportes, aqui você acompanha seu esporte favorito e quem sabe pode virar fã de outro esporte")

# 4. Área Principal
st.title(f"{escolha}")
st.subheader("🔥 Último Corte")

# Player de Vídeo Principal
lista_videos = esportes[escolha]
if lista_videos:
    st.video(lista_videos[0])

# 5. Histórico (se houver mais vídeos na lista)
if len(lista_videos) > 1:
    st.write("---")
    st.subheader("📜 Histórico de Vídeos")
    cols = st.columns(2)
    for i, vid in enumerate(lista_videos[1:]):
        with cols[i % 2]:
            st.video(vid)




