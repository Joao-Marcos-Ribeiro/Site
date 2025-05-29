import streamlit as st
import streamlit.components.v1 as components

# --------------------- CONFIGURAÇÕES DE PÁGINA ---------------------
st.set_page_config(
    page_title="Portfólio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.logo("images/logo.png")
st.markdown("""<style>.stApp {background-color: #050a30;}</style>""",unsafe_allow_html=True)

# --------------------- CONTEÚDO DA PÁGINA --------------------- 

st.markdown("### Abaixo, você encontrará dashboards e frameworks aplicáveis em cenários reais, com o objetivo de tornar os dados mais compreensíveis, acionáveis e estratégicos. 🚀", unsafe_allow_html=True)

st.divider()

st.write("### Dashboard de Vendas")
dashvendas_url = "https://app.powerbi.com/view?r=eyJrIjoiZjM4NTk4OTItYTk3Mi00YzEzLWExMjItYjFkNzdiNDhkMDlkIiwidCI6IjVhYmU5OWNmLTczYWYtNGE2MS04ZTUwLWQzMjM5ZTBiZDM3NCJ9"
st.markdown(
    f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe src="{dashvendas_url}"
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
                allowfullscreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.write("### Ferramenta de Análise de Propostas")
st.write("##### (Em Desenvolvimento)")
dashpropostas_url = "https://app.powerbi.com/view?r=eyJrIjoiYjRlYmNhMzktYzBmNy00MGNhLWIwYTctMTZmNDgzYzZmMjk3IiwidCI6IjVhYmU5OWNmLTczYWYtNGE2MS04ZTUwLWQzMjM5ZTBiZDM3NCJ9&pageName=c9218f635e7910d05575"
st.markdown(
    f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe src="{dashpropostas_url}"
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
                allowfullscreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)




