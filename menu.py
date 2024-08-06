import streamlit as st

def menu():
    with st.sidebar:
        st.header("Configuration")
        st.session_state['openai_api_key'] = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
        st.page_link('app.py',icon="🖥️")
        st.markdown("[Follow me on Medium](https://medium.com/@kshitijkutumbe)")
        st.markdown("[Connect with me on LinkedIn](https://linkedin.com/in/kshitijkutumbe)")