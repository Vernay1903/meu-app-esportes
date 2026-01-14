import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

# ================= CONFIGURAÇÃO =================
st.set_page_config(
    page_title="Corte dos Esportes",
    page_icon="✂️",
    layout="wide"
)

# ================= BANNER =================
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.markdown("## 📰 As principais notícias do esporte em um só lugar")
st.write("---")

# ================= DADOS =================
noticias = {
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Alex Poatan confirma mudança para os Pesos-Pesados",
        "texto": "O campeão brasileiro iniciou ganho de massa para desafiar o topo da categoria."
    },
    "🏃 Atletismo": {
        "titulo": "Recordes mundiais superados",
        "texto": "A temporada começa com marcas históricas na pista."
    },
    "🏎️ Automobilismo": {
        "titulo": "F1 aposta em novos carros",
        "texto": "Mudanças técnicas prometem mais ultrapassagens."
    },
    "🏀 Basquete": {
        "titulo": "NBA: Astro marca 50 pontos",
        "texto": "Atuação histórica colocou o time como favorito."
    },
    "🏅 Esportes Olímpicos": {
        "titulo": "Ciclo olímpico 2028",
        "texto": "Atletas brasileiros intensificam preparação."
    },
    "⚽ Futebol": {
        "titulo": "Mercado da Bola: Estrela europeia no radar",
        "texto": "Craque internacional sinalizou retorno ao Brasil."
    },
    "🏈 Futebol Americano": {
        "titulo": "NFL Draft movimenta franquias",
        "texto": "Novos talentos prometem mudar a liga."
    },
    "🤾 Handebol": {
        "titulo": "Final nacional emocionante",
        "texto": "Duelo intenso definiu o campeão."
    },
    "🛹 Skate": {
        "titulo": "Circuito mundial em destaque",
        "texto": "Etapa brasileira tem manobras impressionantes."
    },
    "🏄 Surfe": {
        "titulo": "Ondas gigantes no Havaí",
        "texto": "Condições extremas marcam o WCT."
    },
    "🎾 Tênis": {
        "titulo": "Grand Slam esquenta disputa",
        "texto": "Favoritos avançam sem sustos."
    },
    "🏓 Tênis de Mesa": {
        "titulo": "Brasileiros sobem no ranking",
        "texto": "Atletas nacionais se destacam no cenário mundial."
    },
    "🏐 Vôlei": {
        "titulo": "Superliga entra na fase decisiva",
        "texto": "Jogos prometem muita emoção."
    },
    "🏐 Vôlei de Praia": {
        "titulo": "Brasil domina circuito mundial",
        "texto": "Duplas seguem imbatíveis na areia."
    }
}

# ================= SIDEBAR =================
st.sidebar.markdown("### 🗓️ Agenda do Dia")
st.sidebar.write("• **19h00:** Superliga de Vôlei")
st.sidebar.write("• **21h30:** Copa Libertadores")
st.sidebar.write("---")

st.sidebar.markdown("### 📰 Notícias")
opcoes = list(noticias.keys())
escolha = st.sidebar.radio("Categorias", opcoes, label_visibility="collapsed")

st.sidebar.write("---")
st.sidebar.markdown("### 📖 Sobre Nós")
st.sidebar.write("Portal criado para apaixonados por esportes ficarem bem informados.")

# ================= CONTEÚDO =================
dados = noticias[escolha]

st.header(escolha)
st.subheader(dados["titulo"])
st.write(dados["texto"])

# ================= PUBLICIDADE =================
components.html("""
<div style="width:100%;height:250px;background:#f2f2f2;
display:flex;align-items:center;justify-content:center;
font-size:18px;font-weight:bold;">
ESPAÇO PARA PUBLICIDADE
</div>
""", height=260)

# ================= WHATSAPP =================
texto_zap = f"Confira no Corte dos Esportes: {dados['titulo']}"
link_zap = f"https://wa.me/?text={urllib.parse.quote(texto_zap)}"
st.link_button("📲 Compartilhar no WhatsApp", link_zap)

# ================= VÍDEO =================
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# ================= RODAPÉ =================
st.write("---")
st.markdown(
    "<center><small>© 2026 Corte dos Esportes | Todos os direitos reservados</small></center>",
    unsafe_allow_html=True
)






