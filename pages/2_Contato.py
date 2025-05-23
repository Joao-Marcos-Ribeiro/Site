import streamlit as st

# --------------------- CONFIGURAÇÕES DE PÁGINA ---------------------
st.set_page_config(
    page_title="Contato",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.logo("images/logo.png")
st.markdown("""<style>.stApp {background-color: #050a30;}</style>""",unsafe_allow_html=True)

# --------------------- CONTEÚDO DA PÁGINA ---------------------

st.markdown("# Contato", unsafe_allow_html=True)

st.write("")

whatsapp_number = "5521984292505"
message = "Oi, João!"
whatsapp_url = f"https://wa.me/{whatsapp_number}?text={message.replace(' ', '%20')}"

st.markdown(
    f"""
    <a href="{whatsapp_url}" target="_blank">
        <button style="background-color: #25D366; color: white; border: none; padding: 15px 32px; 
                       text-align: center; text-decoration: none; display: inline-block; 
                       font-size: 16px; border-radius: 8px; cursor: pointer;">
            💬 Falar no WhatsApp
        </button>
    </a>
    """,
    unsafe_allow_html=True
)


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

st.write("")

email = "jaomarcosribeiro@gmail.com"
st.markdown(
    f"""
    <a href="mailto:{email}" target="_blank">
        <button style="background-color: #D44638; color: white; border: none; padding: 15px 32px; 
                       text-align: center; text-decoration: none; display: inline-block; 
                       font-size: 16px; border-radius: 8px; cursor: pointer;">
            📧 Enviar E-mail
        </button>
    </a>
    """,
    unsafe_allow_html=True
)