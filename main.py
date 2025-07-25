import streamlit as st
from utils.session import init_session
from app.components import login_form, navbar
from app import page_loader
import pandas as pd

# --- CONFIGURASI APLIKASI ---
st.set_page_config(page_title="Streamlit Dashboard", layout="wide")

# --- INISIALISASI SESSION STATE ---
init_session()

# --- AMBIL DATA DARI GOOGLE DRIVE ---
@st.cache_data(show_spinner=True)
def load_data_from_gdrive(file_id):
    url = f"https://drive.google.com/uc?id={file_id}"
    # Jika file kamu CSV besar, bisa pakai chunksize, misal:
    # chunks = pd.read_csv(url, chunksize=50000)
    # df = pd.concat(chunks)
    df = pd.read_csv(url)
    return df

# Masukkan file_id data utama kamu di sini:
DATA_FILE_ID = "1D2SKmVMhZIPD4tgq9FIjItlalBFUH8LR"
try:
    df = load_data_from_gdrive(DATA_FILE_ID)
    st.session_state["dashboard_data"] = df
except Exception as e:
    st.error(f"Gagal memuat data dari Google Drive: {e}")
    st.stop()

# --- LOGIN & HALAMAN DASHBOARD ---
if not st.session_state["logged_in"]:
    login_form.show()
else:
    navbar.show()
    page_loader.load()
