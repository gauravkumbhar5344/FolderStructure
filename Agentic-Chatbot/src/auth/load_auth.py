import streamlit as st

# Simple user database
USER_CREDENTIALS = {
    "gaurav": "1234",
    "admin": "admin123"
}

def login_page():
    st.title("🔐 Login to Agentic Chatbot")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

def logout():
    st.session_state["logged_in"] = False
    st.rerun()
