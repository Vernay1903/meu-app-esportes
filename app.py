import streamlit as st
import pandas as pd

# 1. Nome na aba do navegador
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# Barra Lateral
st.sidebar.header("Menu de Navegação")
esporte_selecionado = st.sidebar.selectbox(
    "Selecione uma modalidade:",
    ["Futebol", "Basquete", "Vôlei", "Natação", "Atletismo", "Surfe"]
)

# Banner Principal (Imagem de Esportes Geral)
st.image("https://images.unsplash.com/photo-1461896836934-ffe607ba8211?q=80&w=2070&auto=format&fit=crop", use_container_width=True)

# 2. Título Principal no topo do site
st.title("✂️ Corte dos Esportes")
st.subheader(f"Análise e Destaques: {esporte_selecionado}")

st.write("---")

# Conteúdo em Colunas
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(f"### 📢 O que há de novo no **{esporte_selecionado}**")
    st.info(f"Aqui você encontra os cortes das melhores jogadas e notícias recentes de {esporte_selecionado}.")
    
    # Exemplo de descrição dinâmica
    if esporte_selecionado == "Futebol":
        st.write("Confira os resultados da rodada e os gols mais bonitos do final de semana.")
    elif esporte_selecionado == "Basquete":
        st.write("Destaques da NBA e os melhores arremessos de três pontos.")
    else:
        st.write("Acompanhe os recordes e as competições mundiais desta modalidade.")

with col2:
    st.markdown("### 📊 Agenda de Transmissões")
    agenda = {
        "Evento": ["Campeonato Nacional", "Copa Ouro", "Desafio de Verão"],
        "Horário": ["16:00", "20:30", "09:00"],
        "Canal": ["Corte Sports TV", "Web Stream", "Corte Play"]
    }
    st.table(pd.DataFrame(agenda))

st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")
