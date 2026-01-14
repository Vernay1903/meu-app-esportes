import streamlit as st
import json
import urllib.parse
from pathlib import Path
import streamlit.components.v1 as components

# ================== CONFIGURAÇÃO ==================
st.set_page_config(
    page_title="Corte dos Esportes | Notícias Esportivas",
    page_icon="⚽",
    layout="wide"
)

# ================== CARREGAR DADOS ==================
arquivo = Path("data/noticias.json")

if not arquivo.exists():
    st.error("❌ Arquivo data/noticias.json não encontrado.")
    st.stop()

with open(arquivo, "r", encoding="utf-8") as f:
    noticias = json.load(f)

# ================== BANNER ==================
banner = Path("assets/banner.png")
if banner.exists():
    st.image(str(banner), use_container_width=True)
else:
    st.title("✂️ Corte dos Esportes")

st.markdown("## 📰 As principais notícias do esporte em um só lugar")
st.write("---")

# ================== SIDEBAR ==================
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

# ================== CONTEÚ




