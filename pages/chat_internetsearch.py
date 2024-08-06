import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from menu import menu

menu()

if 'openai_api_key' in st.session_state:
    openai_api_key = st.session_state['openai_api_key']
# Main title
st.title("🔎 Chat with Search Capability")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input(placeholder="What do you wish to ask?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Check for API key
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Initialize the language model and search agent
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
    search = DuckDuckGoSearchRun(name="Search")
    search_agent = initialize_agent([search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)
    
    # Get and display the response from the agent
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
