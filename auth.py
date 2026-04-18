import streamlit as st

def login():
    st.sidebar.title("🔐 Login System")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username.strip() == "admin" and password.strip() == "1234":
            st.session_state["login"] = True
        else:
            st.sidebar.error("Wrong credentials")

def check_login():
    return st.session_state.get("login", False)