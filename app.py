import streamlit as st

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. BANCO DE DADOS
conteudo = {
    "🥊 Artes Marciais (UFC)": {"titulo": "Poatan mira novo cinturão", "texto": "Preparação física intensa para o próximo desafio histórico."},
    "⚽ Futebol": {"titulo": "Mercado da bola aquecido", "texto": "Grandes clubes brasileiros negociam reforços para a temporada."},
    "🏀 Basquete": {"titulo": "NBA: Emoção nos Play-offs", "texto": "Duelos de gigantes definem os favoritos ao título este ano."},
    "🏎️ Automobilismo": {"titulo": "F1: Inovações Técnicas", "texto": "Novos carros prometem mais disputas e ultrapassagens."},
    "🏃 Atletismo": {"titulo": "Velocistas batem recordes", "texto": "Brasileiros se destacam nos treinos para o mundial."}
}

outros = ["🏅 Esportes Olímpicos", "🏈 Futebol Americano", "🤾 Handebol", "🛹 Skate", "🏄 Surfe", "🎾 Tênis", "🏓 Tênis de Mesa", "🏐 Vôlei", "🏐 Vôlei de Praia"]
for item in outros:
    conteudo[item] = {"titulo": f"Destaques de {item}", "texto": f"Acompanhe os resultados e as notícias de {item}."}

# 4. BARRA LATERAL (Nova Sugestão: Status do Sistema)
st.sidebar.markdown("### 🟢 Portal Online")
st.sidebar.caption("Última atualização: 2026")
st.sidebar.write("---")

# Menu de Navegação
escolha = st.sidebar.radio("Navegue pelas notícias:", list(conteudo.keys()))

st.sidebar.write("---")
# Espaço para "Sobre Nós" sem a caixa azul grande
st.sidebar.markdown("**Sobre o Corte**")
st.sidebar.write("Informação rápida e cortes precisos do mundo esportivo.")

# 5. EXIBIÇÃO DA NOTÍCIA
dados = conteudo[escolha]
st.header(f"{escolha}")
st.subheader(dados["titulo"])
st.write(dados["texto"])

st.write("---")
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 6. RODAPÉ
st.error("**PLANTÃO:** Novas contratações confirmadas para o campeonato nacional!")
st.markdown("<center><p style='color: gray;'>© 2026 Corte dos Esportes</p></center>", unsafe_allow_html=True)


