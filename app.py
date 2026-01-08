import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL (Corrigido para o nome exato do seu arquivo no GitHub)
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. BANCO DE DADOS (Links de imagens atualizados e estáveis)
conteudo = {
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Poatan mira novo cinturão histórico",
        "texto": "O campeão brasileiro planeja buscar o terceiro cinturão em 2026.",
        "img": "https://cdn.pixabay.com/photo/2016/03/31/18/34/boxing-1294429_960_720.png",
        "video": "https://www.youtube.com/watch?v=2S69v8X9X4c"
    },
    "⚽ Futebol": {
        "titulo": "Janela de transferências movimenta milhões",
        "texto": "Clubes iniciam negociações para reforçar elencos na próxima temporada.",
        "img": "https://cdn.pixabay.com/photo/2013/07/13/10/51/football-157930_960_720.png",
        "video": "https://www.youtube.com/watch?v=ra6ZalwC19c"
    },
    "🏀 Basquete": {
        "titulo": "NBA: Play-offs com duelos de gigantes",
        "texto": "A disputa pela conferência oeste está mais acirrada do que nunca.",
        "img": "https://cdn.pixabay.com/photo/2012/04/24/23/31/basketball-41154_960_720.png",
        "video": "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    },
    "🏎️ Automobilismo": {
        "titulo": "F1: Mudanças técnicas prometem mais velocidade",
        "texto": "Novas regulamentações devem tornar as ultrapassagens mais frequentes.",
        "img": "https://cdn.pixabay.com/photo/2012/04/12/23/48/car-31039_960_720.png",
        "video": "https://www.youtube.com/watch?v=MIsunv9vW6I"
    },
    "🏃 Atletismo": {
        "titulo": "Promessas brilham nos treinos",
        "texto": "Nova geração de velocistas apresenta tempos impressionantes.",
        "img": "https://cdn.pixabay.com/photo/2012/04/18/19/01/runner-37583_960_720.png",
        "video": "https://www.youtube.com/watch?v=19JpUAtX-pM"
    }
}

# Parte 2: Outros esportes (Sem o fogo e com imagens reserva)
outros = ["🏅 Esportes Olímpicos", "🏈 Futebol Americano", "🤾 Handebol", "🛹 Skate", 
          "🏄 Surfe", "🎾 Tênis", "🏓 Tênis de Mesa", "🏐 Vôlei", "🏐 Vôlei de Praia"]

for item in outros:
    conteudo[item] = {
        "titulo": f"Destaques de {item}",
        "texto": "Confira as últimas notícias e resultados desta modalidade aqui no Corte.",
        "img": "https://cdn.pixabay.com/photo/2016/05/27/14/33/sport-1419954_960_720.png",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }

# 4. BARRA LATERAL (Menu)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=80)
escolha = st.sidebar.radio("Escolha a categoria:", list(conteudo.keys()))

# 5. EXIBIÇÃO (Sem fogo e Proteção contra erro de imagem)
dados = conteudo[escolha]
st.header(f"{escolha}")

c1, c2 = st.columns([1, 1.5])
with c1:
    # A mágica para sumir com o "0": tentamos carregar, se der erro, não mostra nada
    try:
        st.image(dados["img"], use_container_width=True)
    except:
        st.info("Imagem em carregamento...") 

with c2:
    st.subheader(dados["titulo"])
    st.write(dados["texto"])

st.write("---")
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video(dados["video"])

# 6. RODAPÉ
st.subheader("🚨 Plantão Corte dos Esportes")
st.error("**ÚLTIMA HORA:** Mercado da bola agita os bastidores hoje!")
st.markdown("<center><p style='color: gray;'>© 2026 Corte dos Esportes</p></center>", unsafe_allow_html=True)


