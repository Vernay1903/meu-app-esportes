import streamlit as st
import urllib.parse

# 1. Configuração de Layout
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. Banner Principal
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. Banco de Dados com TODOS os esportes (Organizado internamente)
noticias = {
    "⚽ Futebol": {"titulo": "Mercado da Bola: Estrela europeia no radar", "texto": "Um craque internacional sinalizou interesse em retornar ao Brasil."},
    "🏀 Basquete": {"titulo": "NBA: Astro marca 50 pontos e quebra recorde", "texto": "Uma performance dominante garantiu a vitória na noite de ontem."},
    "🏎️ Automobilismo": {"titulo": "F1: Inovações Técnicas", "texto": "Novos carros prometem mais disputas e ultrapassagens."},
    "🥊 Artes Marciais (UFC)": {"titulo": "Alex Poatan confirma mudança para os Pesos-Pesados", "texto": "O campeão brasileiro revelou o processo de ganho de massa para 2026."},
    "🏐 Vôlei": {"titulo": "Superliga: Duelos decisivos", "texto": "A fase final promete jogos eletrizantes para a torcida."},
    "🏅 Esportes Olímpicos": {"titulo": "Preparação para o ciclo 2028", "texto": "Atletas brasileiros intensificam treinos para as próximas competições."},
    "🏈 Futebol Americano": {"titulo": "NFL: Draft movimenta equipes", "texto": "As novas escolhas prometem mudar o equilíbrio de forças na liga."},
    "🤾 Handebol": {"titulo": "Final do campeonato nacional", "texto": "Um duelo emocionante definiu o grande campeão desta temporada."},
    "🛹 Skate": {"titulo": "Circuito mundial em destaque", "texto": "Manobras incríveis marcam a etapa brasileira do mundial."},
    "🏄 Surfe": {"titulo": "WCT: Ondas gigantes no Hawaii", "texto": "Os melhores surfistas do mundo enfrentam condições extremas."},
    "🎾 Tênis": {"titulo": "Grand Slam: Favoritos avançam", "texto": "As quadras recebem os maiores astros da atualidade."},
    "🏓 Tênis de Mesa": {"titulo": "Destaques do ranking mundial", "texto": "Brasileiros sobem posições e incomodam a elite mundial."},
    "🏃 Atletismo": {"titulo": "Recordes mundiais superados", "texto": "A nova temporada de atletismo começa com marcas históricas."},
    "🏐 Vôlei de Praia": {"titulo": "Circuito na areia", "texto": "As duplas brasileiras dominam as competições internacionais."}
}

# 4. BARRA LATERAL (Layout Idêntico à Foto 1)

# Agenda do Dia (Texto simples no topo)
st.sidebar.markdown("### 🗓️ Agenda do Dia")
st.sidebar.write("• **19h00:** Superliga de Vôlei")
st.sidebar.write("• **21h30:** Copa Libertadores")

st.sidebar.write("---")

# Menu de Notícias (Radio com Ordem Alfabética Forçada)
st.sidebar.markdown("### 📰 Notícias")
st.sidebar.write("**Navegue pelas notícias:**")

# VALIDAÇÃO: Criando a lista alfabética antes de exibir o radio
lista_ordenada = sorted(list(noticias.keys()))

# Exibição via Radio (Bolinhas) e SEM Selectbox
escolha = st.sidebar.radio(
    "Categorias", 
    lista_ordenada, 
    label_visibility="collapsed"
)

st.sidebar.write("---")

# Sobre Nós
st.sidebar.markdown("### 📖 Sobre Nós")
st.sidebar.write("Criado para os apaixonados por esportes ficarem atualizados, com as notícias mais recentes.")

# 5. Conteúdo Principal
dados = noticias[escolha]
st.header(f"{escolha}")
st.subheader(dados["titulo"])
st.write(dados["texto"])

# Botão Compartilhar WhatsApp
texto_zap = f"Confira no Corte dos Esportes: {dados['titulo']}"
link_zap = f"https://wa.me/?text={urllib.parse.quote(texto_zap)}"
st.link_button("📲 Compartilhar no WhatsApp", link_zap)

st.write("---")
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 6. Rodapé
st.markdown("<center><p style='color: gray;'>© 2026 Corte dos Esportes | www.cortedosesportes.com.br</p></center>", unsafe_allow_html=True)


