import streamlit as st

def show():
    st.title("📈 Weekly Report")

    # Ambil data sheet Growth dari session_state
    df = st.session_state.get("growth_data")

    if df is not None and not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Data sheet 'Growth' belum tersedia atau kosong.")
