
import streamlit as st
from app.pages import monitoring, anomaly_tracker, weekly_report


def load():
    page = st.session_state.get("page", "Monitoring")

    if page == "Monitoring":
        monitoring.show()
    elif page == "Anomaly Tracker":
        anomaly_tracker.show()
    elif page == "Weekly Report":
        weekly_report.show()
