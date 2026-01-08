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
    "🥊 Artes Marciais (UFC)": {
        "titulo": "Alex Poatan confirma mudança para os Pesos-Pesados",
        "texto": "O campeão brasileiro revelou que iniciou o processo de ganho de massa para desafiar o topo da categoria no final de 2026."
    },
    "⚽ Futebol": {
        "titulo": "Mercado da Bola: Estrela europeia no radar do Brasil",
        "texto": "Um craque internacional sinalizou interesse em retornar ao Brasil, agitando os bastidores dos grandes clubes."
    },
    "🏀 Basquete": {
        "titulo": "NBA: Astro marca 50 pontos e quebra recorde",
        "texto": "Uma performance dominante garantiu a vitória e colocou o time como o favorito para as finais da Conferência Oeste."
    },
    "🏎️ Automobilismo": {"titulo": "F1: Nova equipe no grid", "texto": "Novas tecnologias prometem acirrar a disputa entre as construtoras."},
    "🏐 Vôlei": {"titulo": "Seleção Brasileira convoca novos talentos", "texto": "O foco é a renovação do elenco visando o novo ciclo olímpico."}
}

# Agendas específicas (pode alimentar com horários reais)
agenda_eventos = {
    "⚽ Futebol": "• 21h30: Copa Libertadores (Oitavas)",
    "🏀 Basquete": "• 20h00: Playoffs da NBA",
    "🏐 Vôlei": "• 19h00: Superliga de Vôlei",
    "🥊 Artes Marciais (UFC)": "• 23h00: Card Principal UFC",
    "🏎️ Automobilismo": "• 09h00: Treino Livre F1"
}

# Criando a lista completa de esportes em ordem alfabética para os menus
lista_esportes_ordenada = sorted(list(conteudo.keys()))

# 4. BARRA LATERAL (Totalmente Organizada de A a Z)

# AGENDA DO DIA (Sem "Outros" e em Ordem Alfabética)
st.sidebar.markdown("### 🗓️ Agenda do Dia")
# Usamos a mesma lista ordenada para a agenda
esporte_agenda = st.sidebar.selectbox("Ver eventos de:", lista_esportes_ordenada, key="agenda_select")
# Se não houver evento cadastrado, mostra uma mensagem padrão limpa
st.sidebar.write(agenda_eventos.get(esporte_agenda, "• Sem eventos confirmados para hoje."))

st.sidebar.write("---")

# NAVEGAÇÃO DE NOTÍCIAS (Ordem Alfabética)
st.sidebar.markdown("### 📰 Escolha o Esporte")
escolha = st.sidebar.selectbox("Selecione a categoria:", lista_esportes_ordenada, label_visibility="collapsed")

st.sidebar.write("---")

# SEÇÃO SOBRE NÓS
st.sidebar.markdown("### 📖 Sobre Nós")
st.sidebar.write("Criado para os apaixonados por esportes ficarem atualizados, com as notícias mais recentes sobre todos os esportes.")

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


