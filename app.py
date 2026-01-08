# Personalização de Cores e Efeito Neon no Título
st.markdown("""
    <style>
    /* Fundo do site */
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    
    /* Fundo da barra lateral */
    [data-testid="stSidebar"] {
        background-color: #1a1c23;
    }

    /* Estilo do Título Neon na Lateral */
    .neon-text {
        color: #00d4ff; /* Azul da sua capa */
        font-size: 22px;
        font-weight: bold;
        text-transform: uppercase;
        text-shadow: 0 0 5px #00d4ff, 0 0 10px #00d4ff, 0 0 20px #00d4ff;
        margin-bottom: 20px;
        font-family: 'sans-serif';
    }
    </style>
    """, unsafe_allow_html=True)

# Aplicação do Título Neon na Sidebar
st.sidebar.markdown('<p class="neon-text">✂️ CORTE DOS ESPORTES</p>', unsafe_allow_html=True)
st.sidebar.markdown("---")


