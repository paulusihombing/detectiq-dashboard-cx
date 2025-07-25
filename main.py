import streamlit as st
from utils.session import init_session
from app.components import login_form, navbar
from app import page_loader
import pandas as pd

# --- CONFIGURASI APLIKASI ---
st.set_page_config(page_title="Streamlit Dashboard", layout="wide")

# --- INISIALISASI SESSION STATE ---
init_session()

# --- PILIH SUMBER DATA (LOKAL ATAU GDRIVE) ---
USE_LOCAL = True  # Ganti ke False jika ingin ambil dari Google Drive

@st.cache_data(show_spinner=True)
def load_local_data():
    df = pd.read_csv("data/kab_kec_daily_kqi_plmn.csv")  # Ganti dengan file lokal kamu
    return df

@st.cache_data(show_spinner=True)
def load_data_from_gdrive(file_id):
    url = f"https://drive.google.com/uc?id={file_id}"
    df = pd.read_csv(url)
    return df

DATA_FILE_ID = "1D2SKmVMhZIPD4tgq9FIjItlalBFUH8LR"  # GDrive file_id

try:
    if USE_LOCAL:
        df = load_local_data()
    else:
        df = load_data_from_gdrive(DATA_FILE_ID)
    st.session_state["dashboard_data"] = df
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    st.stop()

# --- LOGIN & HALAMAN DASHBOARD ---
if not st.session_state["logged_in"]:
    login_form.show()
else:
    navbar.show()
    page_loader.load()
