import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np


def create_cla_tab(data):
    container_cla = st.container()

# add choice to split by country or lob
# those values are then available in the second selection
# show som of claims, LR ER and frequency charts



    st.subheader('Portfolio Overview', divider = 'gray')


    selector_1, selector_2 = st.columns([1, 2]) 
    with selector_1:
        # LoB selector
        choices_view = ['LoB', 'Country']
        selected_view = st.selectbox('Select a view by: ', choices_view, index = 0)

    with selector_2:
        pass


    df_full = data

    # Plot the chart using Streamlit
    # st.line_chart(df_pivot)



    col1, col2 = st.columns([1, 1]) 
    if selected_view == 'LoB':
        col_group_by = 'InsuranceType'
        col_color = 'Country'
    else:
        col_group_by = 'Country'
        col_color = 'InsuranceType'

    with col1:


        st.subheader('Incurred', divider = 'gray')

        # Group by selected columns and calculate Incurred
        df_grouped_inc = df_full.groupby([col_group_by, col_color])['Claims'].sum().reset_index()

        chart_inc = alt.Chart(df_grouped_inc).mark_bar().encode(
            x=alt.X(f'{col_group_by}:N'),
            y='Claims:Q',
            color=alt.Color(f'{col_color}:N', scale=alt.Scale(scheme='redyellowblue')),
            tooltip=[col_group_by, col_color, 'Claims']
        ).properties(
            width=600,
            height=400
        ).interactive()

        st.altair_chart(chart_inc)

    with col2:
        st.subheader('Claim Count', divider = 'gray')

        # Group by selected columns and count claims
        df_grouped_count = df_full.groupby([col_group_by, col_color])['ClaimNb'].sum().reset_index()

        chart_count = alt.Chart(df_grouped_count).mark_bar().encode(
            x=alt.X(f'{col_group_by}:N'),
            y='ClaimNb:Q',
            color=alt.Color(f'{col_color}:N', scale=alt.Scale(scheme='redyellowblue')),
            tooltip=[col_group_by, col_color, 'ClaimNb']
        ).properties(
            width=600,
            height=400
        ).interactive()

        st.altair_chart(chart_count)

    # Bottom two charts ---------------------------------------------------
    select_options = data[col_color].unique()
    select_val = st.multiselect(
        'Filter for: ', 
        options = select_options, 
        default = select_options  
    )

    # add some space
    st.markdown('<br><br>', unsafe_allow_html=True)



    df_filtered = data[(data[col_color].isin(select_val))]

    col3, col4 = st.columns([1, 1]) 

    with col3:

        # Group by selected columns and calculate Incurred
        df_grouped_lr = df_filtered.groupby([col_group_by])[['Claims', 'premiums']].sum().reset_index()
        df_grouped_lr['Loss Ratio %'] = df_grouped_lr['Claims']/df_grouped_lr['premiums']

        st.subheader('Loss Ratio %', divider = 'gray')

        chart_lr = alt.Chart(df_grouped_lr).mark_bar(color = 'tomato').encode(
            x=f'{col_group_by}:N',
            y='Loss Ratio %:Q',
        ).properties(
            width=600,
            height=400
        ).interactive()

        st.altair_chart(chart_lr)


    with col4:

        # Combined Ratio

        # Group by selected columns and calculate Incurred
        df_grouped_cor = df_filtered.groupby([col_group_by])[[
            'Claims', 
            'premiums', 
            'Expenses'
            ]].sum().reset_index()
        df_grouped_cor['Combined Ratio %'] = (df_grouped_cor['Claims'] +
                                         df_grouped_cor['Expenses']) / \
        df_grouped_cor['premiums']

        st.subheader('Combined Ratio %', divider = 'gray')

        chart_lr = alt.Chart(df_grouped_cor).mark_bar(color = 'orange' ).encode(
            x=f'{col_group_by}:N',
            y='Combined Ratio %:Q',
        ).properties(
            width=600,
            height=400
        ).interactive()

        st.altair_chart(chart_lr)
    

