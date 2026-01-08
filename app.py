import streamlit as st
import datetime
import urllib.parse

# 1. Configuração do Layout
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. Banner Principal
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. Banco de Dados com TODOS os Esportes (Sem "Outros")
noticias = {
    "🥊 Artes Marciais (UFC)": {"titulo": "Alex Poatan mira novo cinturão", "texto": "O campeão brasileiro revelou preparação intensa para o próximo desafio nos Pesos-Pesados."},
    "🏃 Atletismo": {"titulo": "Recordes mundiais superados", "texto": "A nova temporada de atletismo começa com marcas históricas na pista."},
    "🏎️ Automobilismo": {"titulo": "F1: Inovações Técnicas", "texto": "Novos carros prometem mais disputas e ultrapassagens na próxima temporada."},
    "🏀 Basquete": {"titulo": "NBA: Astro marca 50 pontos", "texto": "Uma performance dominante garantiu a vitória e colocou o time como o favorito para as finais."},
    "🏅 Esportes Olímpicos": {"titulo": "Preparação para o ciclo 2028", "texto": "Atletas brasileiros intensificam treinos para as próximas competições internacionais."},
    "⚽ Futebol": {"titulo": "Mercado da Bola aquecido", "texto": "Grandes clubes brasileiros negociam reforços de peso para a temporada."},
    "🏈 Futebol Americano": {"titulo": "NFL: Draft movimenta equipes", "texto": "As novas escolhas prometem mudar o equilíbrio de forças na liga este ano."},
    "🤾 Handebol": {"titulo": "Final do campeonato nacional", "texto": "Um duelo emocionante definiu o grande campeão desta temporada competitiva."},
    " skate Skate": {"titulo": "Circuito mundial em destaque", "texto": "Manobras incríveis marcam a etapa brasileira do mundial de skate."},
    "🏄 Surfe": {"titulo": "WCT: Ondas gigantes no Hawaii", "texto": "Os melhores surfistas do mundo enfrentam condições extremas nas praias havaianas."},
    "🎾 Tênis": {"titulo": "Grand Slam: Favoritos avançam", "texto": "As quadras recebem os maiores astros da atualidade para o torneio."},
    "🏓 Tênis de Mesa": {"titulo": "Destaques do ranking mundial", "texto": "Brasileiros sobem posições e incomodam a elite do esporte mundial."},
    "🏐 Vôlei": {"titulo": "Superliga: Duelos decisivos", "texto": "A fase final da Superliga promete jogos eletrizantes para a torcida."},
    "🏐 Vôlei de Praia": {"titulo": "Circuito na areia", "texto": "As duplas brasileiras dominam as competições internacionais nas areias mundiais."}
}

# 4. Barra Lateral (Sidebar)

# Agenda do Dia (Texto simples e direto)
st.sidebar.markdown("### 🗓️ Agenda do Dia")
st.sidebar.write("• **19h00:** Superliga de Vôlei")
st.sidebar.write("• **21h30:** Copa Libertadores")

st.sidebar.write("---")

# MENU DE NOTÍCIAS (Seleção via Radio - De A a Z)
st.sidebar.markdown("### 📰 Notícias")
# Garante a ordem alfabética e remove o "Outros"
opcoes_ordenadas = sorted(list(noticias.keys()))
escolha = st.sidebar.radio("Navegue pelos esportes:", opcoes_ordenadas)

st.sidebar.write("---")

# Sobre Nós
st.sidebar.markdown("### 📖 Sobre Nós")
st.sidebar.write("Criado para os apaixonados por esportes ficarem atualizados, com as notícias mais recentes sobre todos os esportes.")

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


