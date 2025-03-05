import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create_cla_tab(data):
    container_cla = st.container()



    df_filtered = data

    # Plot the chart using Streamlit
    # st.line_chart(df_pivot)

    # Group by 'InsuranceType' and sum the 'Claims' (if needed)
    df_grouped = df_filtered.groupby('InsuranceType')['Claims'].sum().reset_index()

    # Create a bar chart
    st.bar_chart(df_grouped.set_index('InsuranceType'))

