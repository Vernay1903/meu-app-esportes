import streamlit as st

# Configuração da página
st.set_page_config(page_title="Corte dos Esportes", layout="wide", page_icon="✂️")

# Banner Principal
st.image("Captura de tela 2026-01-08 092841.png", use_container_width=True)

# Lista de Esportes em Ordem Alfabética (Atualizada!)
lista_esportes = [
    "Artes Marciais (UFC)", "Automobilismo", "Basquete", "Boxe", 
    "Ciclismo", "Esportes Olímpicos", "Futebol", "Futebol Americano", 
    "Futsal", "Handebol", "Natação", "Skate", "Surfe", "Tênis", 
    "Vôlei", "Vôlei de Praia"
]

# Barra Lateral
st.sidebar.title("✂️ Menu Principal")
esporte = st.sidebar.selectbox("Escolha a Modalidade:", lista_esportes)

st.title("✂️ Corte dos Esportes")
st.subheader(f"Análise e Destaques: {esporte}")

st.write("---")

# Dicionário de Vídeos Dinâmicos
videos = {
    "Artes Marciais (UFC)": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Automobilismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Basquete": "https://www.youtube.com/watch?v=9_pYvYmP1Xg",
    "Boxe": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Ciclismo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Esportes Olímpicos": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Futebol": "https://www.youtube.com/watch?v=9Is976o_TMc",
    "Futebol Americano": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Futsal": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Handebol": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Natação": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Skate": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Surfe": "https://www.youtube.com/watch?v=l_S6L-Rno4U",
    "Tênis": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Vôlei": "https://www.youtube.com/watch?v=mD07R_N9WpY",
    "Vôlei de Praia": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# Exibição do Vídeo
st.markdown(f"### 📺 Últimos Cortes de {esporte}")
st.video(videos.get(esporte, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")) 

st.sidebar.write("---")
st.sidebar.write("Propriedade de: **Corte dos Esportes © 2026**")
