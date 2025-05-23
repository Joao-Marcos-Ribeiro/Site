import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------- DEFININDO LOCAIS --------------------- 
diretory = "e:/Backup/Programação/Projeto Site"

# --------------------- CONFIGURAÇÕES DE PÁGINA ---------------------
st.set_page_config(
    page_title="João Ribeiro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.logo("images/logo.png")
st.markdown("""<style>.stApp {background-color: #050a30;}</style>""",unsafe_allow_html=True)

# --------------------- CONTEÚDO DA PÁGINA --------------------- 

col1, col2 = st.columns(2) # Criar duas colunas

with col1: # Coluna 1 - Texto
    st.image("images/logo.png",width=180)
    st.markdown("# Gestão<br>Inteligente,<br>Resultados Reais", unsafe_allow_html=True)
    st.write("### Transforme dados em decisões inteligentes e impulsione o crescimento do seu negócio")
    st.write("")
    st.write("")
    linkedin_url = "https://www.linkedin.com/in/jo%C3%A3o-marcos-ribeiro-066b891a1/"
    st.markdown(
    f"""
    <a href="{linkedin_url}" target="_blank">
        <button style="background-color: #0A66C2; color: white; border: none; padding: 15px 32px; 
                       text-align: center; text-decoration: none; display: inline-block; 
                       font-size: 16px; border-radius: 8px; cursor: pointer;">
            🔗 Conectar no LinkedIn
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

with col2: # Coluna 2 - Imagem
    st.image("images/celular.gif")

st.write("")
st.write("")
st.write("")
st.write("")

st.markdown("<h1 style='text-align: center;'>Consultoria de soluções personalizadas, pensadas para os desafios do seu negócio</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Engenharia de Produção aplicada com uma missão: transformar estratégias em resultados tangíveis. Abordagem direta e focada em desempenho, com planejamento estratégico para desenvolver análises que direcionam ações precisas, eficazes e objetivas.</h4>", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")

st.markdown("<h1 style='text-align: center;'>Principais Recursos<br></h1>", unsafe_allow_html=True)

col3, col4, col5, col6, col7, col8, col9 = st.columns(7)

with col4:
    st.image("images/processos.png", use_container_width=True)
    st.markdown(
        """
        <div style='border: 2px solid white; border-radius: 15px; padding: 10px;'>
            <h5 style='text-align: center;'>
                Estruture operações eficientes e otimizadas, garantindo um fluxo de trabalho ágil e eficaz.
            </h5>
        </div>
        """,
        unsafe_allow_html=True
    )

with col6:
    st.image("images/dashboards.png", use_container_width=True)
    st.markdown(
        """
        <div style='border: 2px solid white; border-radius: 15px; padding: 10px;'>
            <h5 style='text-align: center;'>
                Transforme dados em decisões. Com painéis personalizados, visualize insights cruciais que impulsionam o crescimento da sua empresa.
            </h5>
        </div>
        """,
        unsafe_allow_html=True
    )

with col8:
    st.image("images/planestrat.png", width=50, use_container_width=True)
    st.markdown(
        """
        <div style='border: 2px solid white; border-radius: 15px; padding: 10px;'>
            <h5 style='text-align: center;'>
                Construa o futuro da sua empresa com estratégias claras e eficazes que posicionam seu negócio para alcançar metas ambiciosas e resultados duradouros.
            </h5>
        </div>
        """,
        unsafe_allow_html=True
    )