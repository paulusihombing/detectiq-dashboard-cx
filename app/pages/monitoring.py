import streamlit as st
import plotly.express as px
import pandas as pd

def show():
    df = st.session_state["dashboard_data"]
    
    # FILTER KABUPATEN
    selected_kab = st.session_state.get("selected_kabupaten", "All")
    if selected_kab != "All":
        df = df[df["Kabupaten"] == selected_kab]

    required_cols = [
        "DATE", "national", "traffic", "swe", "e2e_delay", "video_streaming_download_throughput"
    ]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        st.error(f"Kolom berikut tidak ditemukan di data: {missing}")
        return

    # Konversi DATE ke datetime (optional, agar x axis lebih rapi)
    df["DATE"] = pd.to_datetime(df["DATE"])

    def make_line_chart(metric_col, title, y_title, colors):
        # Filter hanya untuk Indonesia-SF dan Indonesia-XL
        chart_df = df[df["national"].isin(["Indonesia-SF", "Indonesia-XL"])]
        fig = px.line(
            chart_df,
            x="DATE",
            y=metric_col,
            color="national",
            color_discrete_map=colors,
            # markers=True,
            title=title,
        )
        fig.update_layout(
            title_font=dict(size=18, family="Roboto, Arial", color="black"),
            font=dict(family="Roboto, Arial"),
            height=250,
            margin=dict(t=40, b=20, l=10, r=10),
            xaxis_title="DATE",
            yaxis_title=y_title,
            legend_title="Operator",
        )
        return fig

    custom_colors = {
        "Indonesia-XL": "#1959a8",   # biru gelap
        "Indonesia-SF": "#b6186b",   # pink gelap
    }

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                make_line_chart("traffic", "Traffic - KQI", "Traffic", custom_colors),
                use_container_width=True
            )
        with col2:
            st.plotly_chart(
                make_line_chart("swe", "SWE - KQI", "swe", custom_colors),
                use_container_width=True
            )

        col3, col4 = st.columns(2)
        with col3:
            st.plotly_chart(
                make_line_chart("e2e_delay", "E2E Latency - KQI", "E2E Latency", custom_colors),
                use_container_width=True
            )
        with col4:
            st.plotly_chart(
                make_line_chart("video_streaming_download_throughput", "DL Throughput - KQI", "DL Throughput", custom_colors),
                use_container_width=True
            )
