import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL (Link de internet confiável)
# Usei uma imagem de esportes genérica de alta qualidade que funciona sempre
st.image("https://images.unsplash.com/photo-1461896836934-ffe607ba8211?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
st.markdown("<h1 style='text-align: center;'>✂️ Corte dos Esportes</h1>", unsafe_allow_html=True)
st.write("---")

# 3. DICIONÁRIO ORGANIZADO (Ordem Alfabética Correta)
esportes = {
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=F3Fv_rR8G-0",
    "🏃 Atletismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=8m9j_vKAnS0",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🏅 Esportes Olímpicos": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "⚽ Futebol": "https://www.youtube.com/watch?v=ra6ZalwC19c",
    "🏈 Futebol Americano": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🤾 Handebol": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🛹 Skate": "https://www.youtube.com/watch?v=2p8N_8F9XmI",
    "🏄 Surfe": "https://www.youtube.com/watch?v=w772_2q7t-o",
    "🎾 Tênis": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏓 Tênis de Mesa": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "🏐 Vôlei de Praia": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# 4. BARRA LATERAL
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=80)
escolha = st.sidebar.radio("Escolha o esporte:", list(esportes.keys()))

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre Nós")
st.sidebar.info("Somos apaixonados por esportes! Aqui você acompanha seu esporte favorito e fica por dentro dos melhores lances.")

# 5. ÁREA DO VÍDEO
st.header(f"🔥 {escolha}")
st.video(esportes[escolha])



