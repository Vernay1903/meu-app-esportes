import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
# Usando o nome exato do arquivo que está no seu GitHub (conforme seu print)
try:
    st.image("banner.jpg.png", use_container_width=True)
except Exception:
    st.write("# ✂️ Corte dos Esportes")

st.write("---")

# 3. DICIONÁRIO COM LINKS QUE FUNCIONAM (TESTADOS)
esportes = {
    "🥊 Artes Marciais (UFC)": "https://www.youtube.com/watch?v=2S69v8X9X4c",
    "🏃 Atletismo": "https://www.youtube.com/watch?v=19JpUAtX-pM",
    "🏎️ Automobilismo": "https://www.youtube.com/watch?v=MIsunv9vW6I",
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

# 6. RODAPÉ - PLANTÃO CORTE DOS ESPORTES
st.write("---")
st.subheader("🚨 Plantão Corte dos Esportes")

col1, col2 = st.columns(2)

with col1:
    st.info("**Transferências:** O mercado da bola está fervendo! Confira as últimas movimentações do seu time.")
    st.info("**Olimpíadas:** Preparativos para os próximos jogos seguem a todo vapor.")

with col2:
    st.info("**Draft NFL:** Quem serão as próximas estrelas do Futebol Americano?")
    st.info("**Resultados:** Confira o placar das rodadas deste final de semana em tempo real.")

st.markdown("<br><center><p style='color: gray;'>© 2026 Corte dos Esportes - Todos os direitos reservados</p></center>", unsafe_allow_html=True)



