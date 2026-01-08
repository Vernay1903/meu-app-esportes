import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. BANCO DE DADOS (Apenas Texto e Vídeo)
conteudo = {
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Poatan mira novo cinturão histórico",
        "texto": "O campeão brasileiro planeja buscar o terceiro cinturão em 2026. A preparação física já começou para o próximo desafio.",
        "video": "https://www.youtube.com/watch?v=2S69v8X9X4c"
    },
    "⚽ Futebol": {
        "titulo": "Janela de transferências movimenta milhões",
        "texto": "Clubes brasileiros e europeus iniciam negociações para reforçar seus elencos para a próxima temporada.",
        "video": "https://www.youtube.com/watch?v=ra6ZalwC19c"
    },
    "🏀 Basquete": {
        "titulo": "NBA: Play-offs com duelos de gigantes",
        "texto": "A disputa pela conferência oeste está mais acirrada do que nunca, com grandes estrelas brilhando em quadra.",
        "video": "https://www.youtube.com/watch?v=9_pYvYmP1Xg"
    },
    "🏎️ Automobilismo": {
        "titulo": "F1: Mudanças técnicas prometem mais velocidade",
        "texto": "Novas regulamentações aerodinâmicas devem tornar as ultrapassagens mais frequentes nesta temporada.",
        "video": "https://www.youtube.com/watch?v=MIsunv9vW6I"
    },
    "🏃 Atletismo": {
        "titulo": "Promessas brilham nos treinos",
        "texto": "A nova geração de velocistas apresenta tempos impressionantes e promete pódios nas próximas competições.",
        "video": "https://www.youtube.com/watch?v=19JpUAtX-pM"
    }
}

# Outros esportes do menu original
outros = ["🏅 Esportes Olímpicos", "🏈 Futebol Americano", "🤾 Handebol", "🛹 Skate", 
          "🏄 Surfe", "🎾 Tênis", "🏓 Tênis de Mesa", "🏐 Vôlei", "🏐 Vôlei de Praia"]

for item in outros:
    conteudo[item] = {
        "titulo": f"Destaques de {item}",
        "texto": f"Confira aqui as últimas atualizações, resultados e curiosidades sobre o mundo de {item}.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }

# 4. BARRA LATERAL (Menu)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=80)
escolha = st.sidebar.radio("Escolha a categoria:", list(conteudo.keys()))

# 5. EXIBIÇÃO DA NOTÍCIA (Layout limpo e sem o "0")
dados = conteudo[escolha]
st.header(f"{escolha}") # Fogo removido conforme pedido anterior

# Mostra apenas o título e o texto da notícia de forma centralizada ou expandida
st.subheader(dados["titulo"])
st.write(dados["texto"])

st.write("---")

# Vídeo como complemento
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video(dados["video"])

# 6. RODAPÉ - PLANTÃO
st.subheader("🚨 Plantão Corte dos Esportes")
st.error("**ÚLTIMA HORA:** Mercado da bola agita os bastidores hoje!")
st.markdown("<center><p style='color: gray;'>© 2026 Corte dos Esportes</p></center>", unsafe_allow_html=True)


