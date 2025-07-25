import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def show():
    df = pd.DataFrame({
        'Index': np.arange(10),
        'XL_Traffic': np.random.randint(50, 150, 10),
        'SF_Traffic': np.random.randint(60, 160, 10),
        'XL_SWE': np.random.randint(40, 100, 10),
        'SF_SWE': np.random.randint(50, 110, 10),
        'XL_E2E': np.random.randint(30, 90, 10),
        'SF_E2E': np.random.randint(40, 100, 10),
        'XL_DL': np.random.randint(70, 170, 10),
        'SF_DL': np.random.randint(80, 180, 10),
    })

    def make_chart(metric, xl_col, sf_col):
        df_long = df[['Index', xl_col, sf_col]].melt(
            id_vars='Index', var_name='Operator', value_name='Value')
        df_long['Operator'] = df_long['Operator'].str.extract('(XL|SF)')
        custom_colors = {'XL': '#1f77b4', 'SF': '#e377c2'}

        fig = px.line(
            df_long, x='Index', y='Value',
            color='Operator', markers=True,
            title=metric, height=400
        )
        fig.update_layout(
            title=metric,
            title_font=dict(size=18, family="Arial", color="black"),  # ⬅️ Adjust title styling here
            height=250,
            margin=dict(t=40, b=20, l=10, r=10),
            xaxis_title="Index",
            yaxis_title=metric,
            legend_title="Operator"
        )
        fig.for_each_trace(lambda t: t.update(line_color=custom_colors[t.name]))
        return fig

    with st.container():
        col1, col2 = st.columns([1, 1])
        with col1:
            st.plotly_chart(make_chart("Traffic - KQI", "XL_Traffic", "SF_Traffic"), use_container_width=True)
        with col2:
            st.plotly_chart(make_chart("SWE - KQI", "XL_SWE", "SF_SWE"), use_container_width=True)

        col3, col4 = st.columns([1, 1])
        with col3:
            st.plotly_chart(make_chart("E2E Latency - KQI", "XL_E2E", "SF_E2E"), use_container_width=True)
        with col4:
            st.plotly_chart(make_chart("DL Throughput - KQI", "XL_DL", "SF_DL"), use_container_width=True)
