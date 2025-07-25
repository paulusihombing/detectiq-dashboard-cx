import streamlit as st
from utils.session import init_session
from app.components import login_form, navbar
from app import page_loader

st.set_page_config(page_title="Streamlit Dashboard", layout="wide")

# Inisialisasi session
init_session()

if not st.session_state["logged_in"]:
    login_form.show()
else:
    navbar.show()
    page_loader.load()
