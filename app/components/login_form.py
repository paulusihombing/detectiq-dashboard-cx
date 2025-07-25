import streamlit as st
from utils.auth import check_credentials

def show():
    st.title("Welcome to XLSMART CX DetectIQ")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["page"] = "Monitoring"
            st.success("Login berhasil. Mengarahkan...")
            st.rerun()  # gunakan ini, bukan st.experimental_rerun()
        else:
            st.error("Username atau password salah")
