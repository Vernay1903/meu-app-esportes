import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. BANCO DE DADOS (Dividido para evitar cortes no código)
# Parte 1: Esportes principais
conteudo = {
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Poatan mira novo cinturão histórico",
        "texto": "O campeão brasileiro planeja buscar o terceiro cinturão em 2026.",
        "img": "https://images.unsplash.com/photo-1595078475328-1ab05d0a6a0e?w=800",
        "video": "https://www.youtube.com/watch?v=2S69v8X9X4c"
    },
    "⚽ Futebol": {
        "titulo": "Janela de transferências movimenta milhões",
        "texto": "Clubes iniciam negociações para reforçar elencos na próxima temporada.",
        "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800",
        "video": "https://www.youtube.com/watch?v=ra6ZalwC19c"
    },
    "🏀 Basquete": {
        "titulo": "NBA: Play-offs pegam fogo com duelos de gigantes",
        "texto": "A disputa pela conferência oeste está mais acirrada do que nunca.",
        "img": "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800",
        "video": "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    },
    "🏎️ Automobilismo": {
        "titulo": "F1: Mudanças técnicas prometem mais velocidade",
        "texto": "Novas regulamentações devem tornar as ultrapassagens mais frequentes.",
        "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800",
        "video": "https://www.youtube.com/watch?v=MIsunv9vW6I"
    },
    "🏃 Atletismo": {
        "titulo": "Promessas brilham nos treinos",
        "texto": "Nova geração de velocistas apresenta tempos impressionantes.",
        "img": "https://images.unsplash.com/photo-1526676037777-05a232554f77?w=800",
        "video": "https://www.youtube.com/watch?v=19JpUAtX-pM"
    }
}

# Parte 2: Adicionando os demais esportes de forma automática para evitar erros de sintaxe
outros = ["🏅 Esportes Olímpicos", "🏈 Futebol Americano", "🤾 Handebol", "🛹 Skate", 
          "🏄 Surfe", "🎾 Tênis", "🏓 Tênis de Mesa", "🏐 Vôlei", "🏐 Vôlei de Praia"]

for item in outros:
    conteudo[item] = {
        "titulo": f"Destaques de {item}",
        "texto": "Confira as últimas notícias e resultados desta modalidade aqui no Corte.",
        "img": "https://images.unsplash.com/photo-1461896744630-47b7178d4944?w=800",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }

# 4. BARRA LATERAL
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=80)
escolha = st.sidebar.radio("Escolha a categoria:", list(conteudo.keys()))

# 5. EXIBIÇÃO
dados = conteudo[escolha]
st.header(f"🔥 {escolha}")

c1, c2 = st.columns([1, 1])
with c1:
    st.image(dados["img"], use_container_width=True)
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


