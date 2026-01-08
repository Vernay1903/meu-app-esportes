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

# 3. BANCO DE DADOS (Organizado de A a Z)
conteudo = {
    "🥊 Artes Marciais (UFC)": {"titulo": "Alex Poatan mira novo cinturão", "texto": "O campeão brasileiro revelou preparação intensa para o próximo desafio histórico."},
    "🏎️ Automobilismo": {"titulo": "F1: Inovações Técnicas", "texto": "Novos carros prometem mais disputas e ultrapassagens."},
    "🏀 Basquete": {"titulo": "NBA: Astro marca 50 pontos", "texto": "Uma performance dominante garantiu a vitória na noite de ontem."},
    "⚽ Futebol": {"titulo": "Mercado da Bola aquecido", "texto": "Grandes clubes brasileiros negociam reforços para a temporada."},
    "🏐 Vôlei": {"titulo": "Seleção Brasileira: Novos talentos", "texto": "Foco na renovação do elenco visando o novo ciclo mundial."}
}

# 4. BARRA LATERAL (Limpa e Sem Menus Duplos)

# AGENDA DO DIA (Lista simples, direta e elegante)
st.sidebar.markdown("### 🗓️ Agenda do Dia")
st.sidebar.write("• **19h00:** Superliga de Vôlei")
st.sidebar.write("• **21h30:** Copa Libertadores")

st.sidebar.write("---")

# MENU DE NOTÍCIAS (Rádio original que você gostou)
st.sidebar.markdown("### 📰 Notícias")
# Gera a lista de A a Z sem o item "Outros"
lista_limpa = sorted(list(conteudo.keys())) 
escolha = st.sidebar.radio("Navegue pelos esportes:", lista_limpa)

st.sidebar.write("---")

# SOBRE NÓS (Texto fixo no final)
st.sidebar.markdown("### 📖 Sobre Nós")
st.sidebar.write("Criado para os apaixonados por esportes ficarem atualizados, com as noticias mais recentes sobre todos os esportes.")

# 5. EXIBIÇÃO DA NOTÍCIA
dados = conteudo[escolha]
st.header(f"{escolha}")
st.subheader(dados["titulo"])
st.write(dados["texto"])

# Botão de Compartilhar
texto_zap = f"Vi no Corte dos Esportes: {dados['titulo']}"
link_zap = f"https://wa.me/?text={urllib.parse.quote(texto_zap)}"
st.link_button("📲 Compartilhar no WhatsApp", link_zap)

st.write("---")
with st.expander("📺 Ver Vídeo Relacionado"):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 6. RODAPÉ
st.markdown("<center><p style='color: gray;'>© 2026 Corte dos Esportes | www.cortedosesportes.com.br</p></center>", unsafe_allow_html=True)


