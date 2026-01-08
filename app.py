import streamlit as st
import datetime
import urllib.parse

# 1. Configuração da Aba
st.set_page_config(page_title="Corte dos Esportes", layout="wide")

# 2. BANNER PRINCIPAL
try:
    st.image("banner.jpg.png", use_container_width=True)
except:
    st.title("✂️ Corte dos Esportes")

st.write("---")

# 3. BANCO DE DADOS (Notícias e Agenda)
conteudo = {
    "🥊 Artes Marciais (UFC)": {"titulo": "Poatan mira novo cinturão", "texto": "Preparação física intensa para o próximo desafio histórico."},
    "🏎️ Automobilismo": {"titulo": "F1: Inovações Técnicas", "texto": "Novos carros prometem mais disputas."},
    "🏀 Basquete": {"titulo": "NBA: Emoção nos Play-offs", "texto": "Duelos de gigantes definem os favoritos."},
    "⚽ Futebol": {"titulo": "Mercado da bola aquecido", "texto": "Clubes brasileiros negociam reforços."},
    "🏐 Vôlei": {"titulo": "Velocistas batem recordes", "texto": "Destaques nos treinos para o mundial."}
}

agenda_eventos = {
    "⚽ Futebol": "• 21h30: Copa Libertadores",
    "🏀 Basquete": "• 20h00: Playoffs da NBA",
    "🏐 Vôlei": "• 19h00: Superliga de Vôlei",
    "🥊 Artes Marciais (UFC)": "• 23h00: Card Principal UFC",
    "🏎️ Automobilismo": "• 09h00: Treino Livre F1"
}

# Criando a lista completa de esportes em ordem alfabética
lista_esportes_ordenada = sorted(list(conteudo.keys()))

# 4. BARRA LATERAL ORGANIZADA (Sem confusão)

# Menu de Notícias Principal (Sempre visível)
st.sidebar.markdown("### 📰 Notícias")
escolha = st.sidebar.selectbox("Escolha um esporte para ler:", lista_esportes_ordenada)

st.sidebar.write("---")

# Agenda em um Expansor (Gaveta que abre e fecha)
with st.sidebar.expander("🗓️ Ver Agenda do Dia"):
    esporte_agenda = st.selectbox("Selecione o esporte:", lista_esportes_ordenada, key="agenda_select")
    st.write(agenda_eventos.get(esporte_agenda, "• Sem eventos para hoje."))

# Sobre Nós em um Expansor
with st.sidebar.expander("📖 Sobre Nós"):
    st.write("Criado para os apaixonados por esportes ficarem atualizados, com as noticias mais recentes sobre todos os esportes.")

# 5. EXIBIÇÃO DA NOTÍCIA
dados = conteudo[escolha]
st.header(f"{escolha}")
st.subheader(dados["titulo"])
st.write(dados["texto"])

# Botão de Compartilhar
texto_para_zap = f"Confira no Corte dos Esportes: {dados['titulo']}"
link_final = f"https://wa.me/?text={urllib.parse.quote(texto_para_zap)}"
st.link_button("📲 Compartilhar no WhatsApp", link_final)

st.write("---")
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 6. RODAPÉ
data_hoje = datetime.date.today().year
st.markdown(f"<center><p style='color: gray;'>© {data_hoje} Corte dos Esportes | www.cortedosesportes.com.br</p></center>", unsafe_allow_html=True)


