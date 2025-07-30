import streamlit as st
import pandas as pd

def weekly_table(df):
    PERCENT_COLS = [
        "XL Δ% Baseline→MOCN",
        "XL Δ% Baseline→Latest",
        "SF Δ% Baseline→MOCN",
        "SF Δ% Baseline→Latest"
    ]
    # Ensure float and percent
    for col in PERCENT_COLS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    def highlight(val):
        if pd.isnull(val):
            return ""
        if val < 0:
            return "color: white; background-color: #d0312d"    # Red
        elif val > 0:
            return "color: white; background-color: #1ea75f"    # Green
        else:
            return ""

    # Build styler: percent format + color per cell
    styler = df.style
    for col in PERCENT_COLS:
        if col in df.columns:
            styler = styler.format({col: "{:.2f}%"}).applymap(highlight, subset=[col])

    return styler

def show():
    st.title("📈 Weekly Report")
    st.write("Laporan growth mingguan.")

    df = st.session_state.get("growth_data")
    if df is not None and not df.empty:
        st.dataframe(weekly_table(df), use_container_width=True)
    else:
        st.warning("Data sheet 'Growth' belum tersedia atau kosong.")
