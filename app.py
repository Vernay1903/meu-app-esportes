import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
# Usando o nome exato que funcionou no seu GitHub
try:
    st.image("banner.jpg.png", use_container_width=True)
except Exception:
    st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

st.write("---")

# 3. DICIONÁRIO COM LINKS REAIS E ORDEM ALFABÉTICA
esportes = {
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=F3Fv_rR8G-0",
    "🏃 Atletismo": "https://www.youtube.com/watch?v=19JpUAtX-pM",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=8m9j_vKAnS0",
    "🏀 Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "🏅 Esportes Olímpicos": "https://www.youtube.com/watch?v=VabT_M_n2O8",
    "⚽ Futebol": "https://www.youtube.com/watch?v=ra6ZalwC19c",
    "🏈 Futebol Americano": "https://www.youtube.com/watch?v=07mBfR8erMY",
    "🤾 Handebol": "https://www.youtube.com/watch?v=uXvS9G9S8S4",
    "🛹 Skate": "https://www.youtube.com/watch?v=2p8N_8F9XmI",
    "🏄 Surfe": "https://www.youtube.com/watch?v=w772_2q7t-o",
    "🎾 Tênis": "https://www.youtube.com/watch?v=8S69G_W0-J4",
    "🏓 Tênis de Mesa": "https://www.youtube.com/watch?v=3u_vF_SOfYk",
    "🏐 Vôlei": "https://www.youtube.com/watch?v=N_6_zV_Xz7Y",
    "🏐 Vôlei de Praia": "https://www.youtube.com/watch?v=u6r6uXyS-vM"
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



