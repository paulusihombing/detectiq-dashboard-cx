import streamlit as st

def show():
    st.title("🚨 Anomaly Tracker")
    st.write("Track anomalies here.")

    # Ambil data sheet Kabupaten_Level dari session_state
    df = st.session_state.get("kabupaten_level_data")

    if df is not None and not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Data sheet 'Kabupaten_Level' belum tersedia atau kosong.")
