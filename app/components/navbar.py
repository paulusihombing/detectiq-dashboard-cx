import streamlit as st

def show():
    with st.sidebar:
        st.markdown("""
            <style>
            .sidebar-title {
                font-size: 28px;
                font-weight: bold;
                padding-bottom: 0px;
                margin-bottom: 0px;
            }
            .sidebar-subtitle {
                font-size: 18px;
                color: #666;
                padding-top: 0px;
                margin-top: -5px;
                margin-bottom: 10px;
            }
            </style>
            <div class="sidebar-title">XLSMART CX</div>
            <div class="sidebar-subtitle">DetectIQ Dashboard</div>
        """, unsafe_allow_html=True)

        st.divider()

        # Page navigation buttons
        if st.button("Monitoring"):
            st.session_state.page = "Monitoring"
        if st.button("Anomaly Tracker"):
            st.session_state.page = "Anomaly Tracker"
        if st.button("Weekly Report"):
            st.session_state.page = "Weekly Report"

        st.divider()

        # Only show filters when on Monitoring page
        if st.session_state.get("page") == "Monitoring":
            operator = st.selectbox("Operator", ["All", "XL", "SF"], key="monitoring_operator")

        st.divider()

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
