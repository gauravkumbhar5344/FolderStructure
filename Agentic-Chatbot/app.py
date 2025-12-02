import streamlit as st
from src.auth.load_auth import login_page, logout
from src.langgraph_agenticai.main import load_langgraph_agenticai_app

st.set_page_config(page_title="Agentic Chatbot", page_icon="🤖")

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # If logged in → show chatbot
    if st.session_state["logged_in"]:
        st.sidebar.success(f"👋 Welcome, {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            logout()
        
        # Load your chatbot UI
        load_langgraph_agenticai_app()

    else:
        # Show login page only
        login_page()

if __name__ == "__main__":
    main()
