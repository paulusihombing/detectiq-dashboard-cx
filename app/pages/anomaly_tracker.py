import streamlit as st
import pandas as pd

def show():
    st.title("🚨 Anomaly Tracker")
    st.write("Historical Anomaly Report.")

    df = st.session_state.get("kabupaten_level_data")
    if df is not None and not df.empty:
        PERCENT_COLS = [
            "XL Δ% Baseline→MOCN",
            "XL Δ% Baseline→Latest",
            "SF Δ% Baseline→MOCN",
            "SF Δ% Baseline→Latest"
        ]
        for col in PERCENT_COLS:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
                df[col] = df[col].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Data sheet 'Kabupaten_Level' belum tersedia atau kosong.")
