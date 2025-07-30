import streamlit as st
import pandas as pd

def weekly_table(df):
    PERCENT_COLS = [
        "XL Δ% Baseline→MOCN",
        "XL Δ% Baseline→Latest",
        "SF Δ% Baseline→MOCN",
        "SF Δ% Baseline→Latest"
    ]
    # Pastikan tipe data float
    for col in PERCENT_COLS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    def highlight(val):
        if pd.isnull(val):
            return ""
        if val < 0:
            return "color: white; background-color: #d0312d"
        elif val > 0:
            return "color: white; background-color: #1ea75f"
        else:
            return ""

    # Format semua kolom persentase sekaligus
    format_dict = {col: "{:.2f}%" for col in PERCENT_COLS if col in df.columns}
    styler = df.style.format(format_dict)
    # Apply coloring per kolom
    for col in PERCENT_COLS:
        if col in df.columns:
            styler = styler.applymap(highlight, subset=[col])
    return styler

def show():
    st.title("📈 Weekly Report")
    st.write("Laporan growth mingguan.")

    df = st.session_state.get("growth_data")
    if df is not None and not df.empty:
        st.dataframe(weekly_table(df), use_container_width=True)
    else:
        st.warning("Data sheet 'Growth' belum tersedia atau kosong.")
