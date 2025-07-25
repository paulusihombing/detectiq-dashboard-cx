import streamlit as st

def show():
    with st.sidebar:
        st.markdown("<h1 style='margin-bottom:0px; padding-bottom:0px; padding-top:0px;'>XLSMART CX.</h1>", unsafe_allow_html=True)
        st.markdown("<p style='margin-top:0px;margin-bottom:0px;padding-bottom:0px; padding-top:0px;font-size:16px;'>DetectIQ Dashboard</p>", unsafe_allow_html=True)

        st.divider()

        # Page navigation buttons
        if st.button("Monitoring"):
            st.session_state.page = "Monitoring"
        if st.button("Anomaly Tracker"):
            st.session_state.page = "Anomaly Tracker"
        if st.button("Weekly Report"):
            st.session_state.page = "Weekly Report"

        st.divider()

        # Filter Kabupaten (autocomplete)
        if st.session_state.get("page") == "Monitoring":
            df = st.session_state.get("dashboard_data")
            if df is not None and "Kabupaten" in df.columns:
                kabupaten_list = ["All"] + sorted(df["Kabupaten"].dropna().unique())
                default_kab = "KAB. GUNUNGKIDUL" if "KAB. GUNUNGKIDUL" in kabupaten_list else "All"
                default_index = kabupaten_list.index(default_kab)

                selected_kabupaten = st.selectbox(
                    "Kabupaten",
                    kabupaten_list,
                    index=default_index,
                    key="monitoring_kabupaten"
                )
                st.session_state["selected_kabupaten"] = selected_kabupaten
            else:
                st.info("Data belum dimuat atau kolom 'Kabupaten' tidak ditemukan.")

        st.divider()

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
