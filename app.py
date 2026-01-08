import streamlit as st
import urllib.parse

# 1. Configuração da Página
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. Banner
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. Banco de Dados (Todos os 14 esportes das suas imagens)
noticias = {
    "🥊 Artes Marciais (UFC)": {"titulo": "Alex Poatan mira novo cinturão", "texto": "O campeão brasileiro revelou preparação intensa para o próximo desafio histórico."},
    "🏃 Atletismo": {"titulo": "Recordes mundiais superados", "texto": "A nova temporada de atletismo começa com marcas históricas na pista."},
    "🏎️ Automobilismo": {"titulo": "F1: Inovações Técnicas", "texto": "Novos carros prometem mais disputas e ultrapassagens."},
    "🏀 Basquete": {"titulo": "NBA: Astro marca 50 pontos", "texto": "Uma performance dominante garantiu a vitória na noite de ontem."},
    "🏅 Esportes Olímpicos": {"titulo": "Preparação para 2028", "texto": "Atletas brasileiros intensificam treinos para o próximo ciclo."},
    "⚽ Futebol": {"titulo": "Mercado da bola aquecido", "texto": "Grandes clubes brasileiros negociam reforços para a temporada."},
    "🏈 Futebol Americano": {"titulo": "NFL: Draft movimenta equipes", "texto": "As novas escolhas prometem mudar o equilíbrio de forças na liga."},
    "🤾 Handebol": {"titulo": "Final do campeonato nacional", "texto": "Um duelo emocionante definiu o grande campeão desta temporada."},
    "🛹 Skate": {"titulo": "Circuito mundial em destaque", "texto": "Manobras incríveis marcam a etapa brasileira do mundial de skate."},
    "🏄 Surfe": {"titulo": "WCT: Ondas gigantes no Hawaii", "texto": "Os melhores surfistas do mundo enfrentam condições extremas."},
    "🎾 Tênis": {"titulo": "Grand Slam: Favoritos avançam", "texto": "As quadras de tênis recebem os maiores astros da atualidade."},
    "🏓 Tênis de Mesa": {"titulo": "Destaques do ranking mundial", "texto": "Brasileiros sobem posições e incomodam a elite do esporte."},
    "🏐 Vôlei": {"titulo": "Superliga: Duelos decisivos", "texto": "A fase final da Superliga promete jogos eletrizantes para a torcida."},
    "🏐 Vôlei de Praia": {"titulo": "Circuito na areia", "texto": "As duplas brasileiras dominam as competições internacionais."}
}

# 4. Barra Lateral (Layout Validado)

# Agenda (Texto limpo no topo)
st.sidebar.markdown("### 🗓️ Agenda do Dia")
st.sidebar.write("• **19h00:** Superliga de Vôlei")
st.sidebar.write("• **21h30:** Copa Libertadores")

st.sidebar.write("---")

# Menu de Notícias (Radio de A a Z)
st.sidebar.markdown("### 📰 Notícias")
st.sidebar.write("**Navegue pelas notícias:**")

# GARANTE A ORDEM ALFABÉTICA REAL
lista_abc = sorted(list(noticias.keys()))

# Seleção via Radio (bolinhas)
escolha = st.sidebar.radio(
    "Categorias", 
    lista_abc, 
    label_visibility="collapsed"
)

st.sidebar.write("---")

# Sobre Nós
st.sidebar.markdown("### 📖 Sobre Nós")
st.sidebar.write("Criado para os apaixonados por esportes ficarem atualizados, com as notícias mais recentes sobre todos os esportes.")

# 5. Conteúdo Central
dados = noticias[escolha]
st.header(f"{escolha}")
st.subheader(dados["titulo"])
st.write(dados["texto"])

# Botão Compartilhar
texto_zap = f"Confira no Corte dos Esportes: {dados['titulo']}"
link_final = f"https://wa.me/?text={urllib.parse.quote(texto_zap)}"
st.link_button("📲 Compartilhar no WhatsApp", link_final)

st.write("---")
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 6. Rodapé
st.markdown("<center><p style='color: gray;'>© 2026 Corte dos Esportes | www.cortedosesportes.com.br</p></center>", unsafe_allow_html=True)


