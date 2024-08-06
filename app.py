import streamlit as st

from menu import menu



st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
menu()
st.subheader("Generative AI Applications using Langchain",divider='blue')

st.page_link(r'pages/chat_internetsearch.py',icon='🔍')