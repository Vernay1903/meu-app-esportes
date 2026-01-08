import streamlit as st
import datetime

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. BANCO DE DADOS (Notícias Bombásticas de Hoje)
conteudo = {
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Alex Poatan confirma mudança para os Pesos-Pesados",
        "texto": "O campeão brasileiro revelou que iniciou o processo de ganho de massa para desafiar o topo da categoria no final de 2026, buscando um cinturão histórico."
    },
    "⚽ Futebol": {
        "titulo": "Mercado da Bola: Estrela europeia no radar do Brasil",
        "texto": "Com o contrato chegando ao fim na Europa, um craque internacional sinalizou interesse em retornar ao Brasil, agitando os bastidores dos grandes clubes."
    },
    "🏀 Basquete": {
        "titulo": "NBA: Astro marca 50 pontos e quebra recorde",
        "texto": "Uma performance dominante garantiu a vitória e colocou o time como o principal favorito para as finais da Conferência Oeste nesta temporada."
    },
    "🏎️ Automobilismo": {
        "titulo": "Fórmula 1: Nova equipe anuncia entrada oficial",
        "texto": "O anúncio traz novas tecnologias e promete acirrar a disputa entre as construtoras, mudando o equilíbrio de forças atual no grid."
    },
    "🏐 Vôlei": {
        "titulo": "Seleção Brasileira convoca novos talentos",
        "texto": "O foco é a renovação do elenco visando o novo ciclo olímpico, trazendo jovens destaques da Superliga para o time principal."
    }
}

# Preenchimento para as demais categorias
outros = ["🏅 Esportes Olímpicos", "🏈 Futebol Americano", "🤾 Handebol", "🛹 Skate", "🏄 Surfe", "🎾 Tênis", "🏓 Tênis de Mesa", "🏃 Atletismo", "🏐 Vôlei de Praia"]
for item in outros:
    if item not in conteudo:
        conteudo[item] = {"titulo": f"Destaques de {item}", "texto": f"Acompanhe aqui as últimas atualizações e resultados de {item} em tempo real."}

# 4. BARRA LATERAL
st.sidebar.markdown("### 🗓️ Agenda do Dia") #
st.sidebar.write("• **19h00:** Superliga de Vôlei")
st.sidebar.write("• **21h30:** Copa Libertadores (Oitavas)")

st.sidebar.write("---")

# Menu de Navegação
escolha = st.sidebar.radio("Navegue pelas notícias:", list(conteudo.keys()))

st.sidebar.write("---")

# SEÇÃO SOBRE NÓS
st.sidebar.markdown("### 📖 Sobre Nós") #
frase_site = "Criado para os apaixonados por esportes ficarem atualizados, com as noticias mais recentes sobre todos os esportes." #
st.sidebar.write(frase_site) #

# 5. EXIBIÇÃO DA NOTÍCIA
dados = conteudo[escolha]
st.header(f"{escolha}")
st.subheader(dados["titulo"])
st.write(dados["texto"])

st.write("---")
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 6. RODAPÉ PROFISSIONAL
data_hoje = datetime.date.today().year
st.markdown(f"<center><p style='color: gray;'>© {data_hoje} Corte dos Esportes | www.cortedosesportes.com.br</p></center>", unsafe_allow_html=True)


