import streamlit as st

def creds_entered():
    if st.session_state.get("username") == "admin" and st.session_state.get("password") == "password123":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state.get("password"):
            st.warning("Please Enter the password.")
        else:
            st.error("Invalid username or password 🤨")

def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username" , value="", key="username",  on_change=creds_entered)
        st.text_input(label="Password",key="password" ,type="password" ,  on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username" , value="", key="username",  on_change=creds_entered)
            st.text_input(label="Password",key="password" ,type="password" ,  on_change=creds_entered)
            return False
