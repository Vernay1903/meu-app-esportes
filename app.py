import streamlit as st
import json
import urllib.parse
import streamlit.components.v1 as components
from pathlib import Path

# CONFIGURAÇÃO SEO
st.set_page_config(
    page_title="Corte dos Esportes | Notícias Esportivas",
    page_icon="⚽",
    layout="wide"
)

# CARREGAR NOTÍCIAS
with open("data/noticias.json", "r", encoding="utf-8") as f:
    noticias = json.load(f)

# BANNER
if Path("assets/banner.png").exists():
    st.image("assets/banner.png", use_container_width=True)
else:
    st.title("✂️ Corte dos Esportes")

st.markdown("## 📰 As principais notícias do esporte em um só lugar")
st.write("---")

# SIDEBAR
st.sidebar.markdown("### 🗓️ Agenda do Dia")
st.sidebar.write("• **19h00:** Superliga de Vôlei")
st.sidebar.write("• **21h30:** Copa Libertadores")
st.sidebar.write("---")

st.sidebar.markdown("### 📰 Notícias")
categorias = sorted(noticias.keys())
escolha = st.sidebar.radio("Categorias", categorias, label_visibility="collapsed")

st.sidebar.write("---")
st.sidebar.markdown("### 📖 Institucional")
st.sidebar.page_link("pages/1_Sobre.py", label="Sobre")
st.sidebar.page_link("pages/2_Contato.py", label="Contato")
st.sidebar.page_link("pages/3_Politica_de_Privacidade.py", label="Política de Privacidade")
st.sidebar.page_link("pages/4_Termos_de_Uso.py", label="Termos de Uso")

# CONTEÚDO
dados = noticias[escolha]

st.header(escolha)
st.subheader(dados["titulo"])
st.write(dados["texto"])

# ANÚNCIO (ADSENSE)
components.html("""
<!-- SUBSTITUIR PELO SCRIPT REAL DO ADSENSE -->
<div style="width:100%;height:250px;background:#f2f2f2;
display:flex;align-items:center;justify-content:center;">
Publicidade
</div>
""", height=260)

# LINK AFILIADO
st.markdown("### 🛒 Produto Relacionado")
st.link_button("👉 Confira aqui", dados["afiliado"])

# COMPARTILHAMENTO
texto_zap = f"Confira no Corte dos Esportes: {dados['titulo']}"
link_zap = f"https://wa.me/?text={urllib.parse.quote(texto_zap)}"
st.link_button("📲 Compartilhar no WhatsApp", link_zap)

# VÍDEO
with st.expander("📺 Ver vídeo relacionado"):
    st.video(dados["video"])

# RODAPÉ
st.write("---")
st.markdown(
    "<center><small>© 2026 Corte dos Esportes | Todos os direitos reservados</small></center>",
    unsafe_allow_html=True
)



