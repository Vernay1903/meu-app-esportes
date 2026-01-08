import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. BANCO DE DADOS COMPLETO (Notícias para todos os 14 esportes)
conteudo = {
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Poatan mira novo cinturão histórico",
        "texto": "O campeão brasileiro segue quebrando recordes e planeja subir de categoria para buscar o terceiro cinturão em 2026.",
        "img": "https://images.unsplash.com/photo-1595078475328-1ab05d0a6a0e?w=800",
        "video": "https://www.youtube.com/watch?v=2S69v8X9X4c"
    },
    "🏃 Atletismo": {
        "titulo": "Promessas do Atletismo brilham nos treinos",
        "texto": "A nova geração de velocistas apresenta tempos impressionantes e promete pódios nas próximas competições mundiais.",
        "img": "https://images.unsplash.com/photo-1526676037777-05a232554f77?w=800",
        "video": "https://www.youtube.com/watch?v=19JpUAtX-pM"
    },
    "🏎️ Automobilismo": {
        "titulo": "F1: Mudanças técnicas prometem mais velocidade",
        "texto": "As novas regulamentações de aerodinâmica devem tornar as ultrapassagens mais frequentes e as corridas mais emocionantes.",
        "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800",
        "video": "https://www.youtube.com/watch?v=MIsunv9vW6I"
    },
    "🏀 Basquete": {
        "titulo": "NBA: Play-offs pegam fogo com duelos de gigantes",
        "texto": "A disputa pela conferência oeste está mais acirrada do que nunca, com times empatados na liderança na reta final.",
        "img": "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800",
        "video": "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    },
    "🏅 Esportes Olímpicos": {
        "titulo": "Brasil amplia investimento em esportes de base",
        "texto": "Com foco no próximo ciclo olímpico, novos centros de treinamento de alto rendimento estão sendo inaugurados.",
        "img": "https://images.unsplash.com/photo-1562077772-3bd30422f7e8?w=800",
        "video": "https://www.youtube.com/watch?v=VabT_M_n2O8"
    },
    "⚽ Futebol": {
        "titulo": "Janela de transferências movimenta o mercado",
        "texto": "Clubes brasileiros e europeus iniciam negociações milionárias para reforçar seus elencos para a próxima temporada.",
        "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800",
        "video": "https://www.youtube.com/watch?v=ra6ZalwC19c"
    },
    "🏈 Futebol Americano": {
        "titulo": "NFL: Estratégias inovadoras dominam a liga",
        "texto": "Novos esquemas ofensivos estão desafiando as defesas mais sólidas, resultando em placares históricos e muita emoção.",
        "img": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?w=800",
        "video": "https://www.youtube.com/watch?v=07mBfR8erMY"
    },
    "🤾 Handebol": {
        "titulo": "Seleção Brasileira inicia preparação para o Mundial",
        "texto": "Com uma mistura de atletas experientes e jovens talentos, o Brasil busca surpreender as potências europeias.",
        "img": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800",
        "video": "https://www.youtube.com/watch?v=uXvS9G9S8S4"
    },
    "🛹 Skate": {
        "titulo": "Skate Street: Brasileiros dominam ranking mundial",
        "texto": "Nossos atletas continuam sendo referência técnica e estilo, conquistando pódios nas etapas internacionais mais importantes.",
        "img": "https://images.unsplash.com/photo-1520156582985-31368ba59c95?w=800",
        "video": "https://www.youtube.com/watch?v=2p8N_8F9XmI"
    },
    "🏄 Surfe": {
        "titulo": "WCT: Próxima etapa promete ondas gigantes",
        "texto": "A elite do surfe mundial se prepara para condições extremas em uma das paradas mais icônicas do circuito.",
        "img": "https://images.unsplash.com/photo-1502680390469-be75c86b636f?w=800",



