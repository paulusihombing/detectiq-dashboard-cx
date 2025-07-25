
import streamlit as st

def init_session():
    """Inisialisasi default untuk semua session state yang dibutuhkan."""
    default_states = {
        "logged_in": False,
        "username": None,
        "page": "Dashboard",
    }

    for key, value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = value
