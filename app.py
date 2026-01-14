import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

# ================== CONFIGURAÇÃO ==================
st.set_page_config(
    page_title="Corte dos Esportes | Notícias Esportivas",
    page_icon="⚽",
    layout="wide"
)

# ================== DADOS (INLINE - SEM JSON) ==================
noticias = {
    "⚽ Futebol": {
        "titulo": "Mercado da Bola: Estrela europeia no radar",
        "texto": "Um craque internacional sinalizou interesse em retornar ao Brasil.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "afiliado": "https://www.amazon.com.br/"
    },
    "🏀 Basquete": {
        "titulo": "NBA: Astro marca 50 pontos",
        "texto": "Atuação histórica colocou o time como favorito ao título.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "afiliado": "https://www.netshoes.com.br/"
    }
}

# ================== BANNER ==================
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

# ================== CONTEÚDO ==================
dados = noticias[escolha]

st.header(escolha)
st.subheader(dados["titulo"])
st.write(dados["texto"])

# ================== ANÚNCIO ==================
components.html("""
<div style="width:100%;height:250px;background:#f2f2f2;
display:flex;align-items:center;justify-content:center;font-weight:bold;">
ESPAÇO PARA PUBLICIDADE
</div>
""", height=260)

# ================== AFILIADO ==================
st.markdown("### 🛒 Produto Relacionado")
st.link_button("👉 Confira aqui", dados["afiliado"])

# ================== WHATSAPP ==================
texto_zap = f"Confira no Corte dos Esportes: {dados['titulo']}"
link_zap = f"https://wa.me/?text={urllib.parse.quote(texto_zap)}"
st.link_button("📲 Compartilhar no WhatsApp", link_zap)

# ================== VÍDEO ==================
with st.expander("📺 Ver vídeo relacionado"):
    st.video(dados["video"])

# ================== RODAPÉ ==================
st.write("---")
st.markdown(
    "<center><small>© 2026 Corte dos Esportes | Todos os direitos reservados</small></center>",
    unsafe_allow_html=True
)





