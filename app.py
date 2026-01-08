import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
try:
    st.image("banner.jpg.png", use_container_width=True)
except Exception:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. DICIONÁRIO DE CONTEÚDO (Notícias em vez de Vídeos)
# Aqui você pode atualizar as notícias de cada esporte individualmente
conteudo_esportes = {
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Poatan confirma defesa de cinturão para 2026",
        "texto": "O campeão brasileiro Alex Poatan anunciou que já tem data para voltar ao octógono. Especialistas apontam que este será o maior desafio da sua carreira até agora.",
        "imagem": "https://images.unsplash.com/photo-1595078475328-1ab05d0a6a0e?w=800",
        "video": "https://www.youtube.com/watch?v=2S69v8X9X4c"
    },
    "⚽ Futebol": {
        "titulo": "Mercado da Bola: Estrela europeia a caminho do Brasil?",
        "texto": "Rumores indicam que um grande atacante da Premier League está em negociações avançadas para reforçar um clube da Série A na próxima janela de transferências.",
        "imagem": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800",
        "video": "https://www.youtube.com/watch?v=ra6ZalwC19c"
    },
    "🏀 Basquete": {
        "titulo": "NBA: Recorde histórico batido em Los Angeles",
        "texto": "A noite de ontem entrou para a história do basquete mundial com uma performance nunca antes vista. O ginásio veio abaixo com o último arremesso.",
        "imagem": "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800",
        "video": "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    }
}

# 4. BARRA LATERAL (Menu)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=80)
escolha = st.sidebar.radio("Escolha a categoria:", list(conteudo_esportes.keys()))

st.sidebar.write("---")
st.sidebar.subheader("📖 Sobre o Corte")
st.sidebar.info("As principais notícias e lances do mundo esportivo em um só lugar.")

# 5. EXIBIÇÃO DA NOTÍCIA SELECIONADA
if escolha in conteudo_esportes:
    dados = conteudo_esportes[escolha]
    
    st.header(f"🔥 {escolha}")
    
    # Layout da Notícia
    col_img, col_txt = st.columns([1, 1])
    
    with col_img:
        st.image(dados["imagem"], use_container_width=True)
    
    with col_txt:
        st.subheader(dados["titulo"])
        st.write(dados["texto"])
        st.button(f"Ler mais sobre {escolha}", key=f"btn_{escolha}")

    st.write("---")
    
    # O vídeo agora entra como um "Bônus" abaixo da notícia escrita
    with st.expander("📺 Assistir lances em vídeo"):
        st.video(dados["video"])
        st.caption("Nota: Alguns vídeos podem ser bloqueados para reprodução externa pelo YouTube.")

# 6. RODAPÉ - PLANTÃO
st.write("---")
st.subheader("🚨 Plantão Corte dos Esportes")
st.error("**ÚLTIMA HORA:** Ingressos para a final da Copa do Mundo começam a ser vendidos amanhã!")

st.markdown("<br><center><p style='color: gray;'>© 2026 Corte dos Esportes - Monetizado com Notícias</p></center>", unsafe_allow_html=True)



