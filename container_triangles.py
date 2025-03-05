import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_triangle_tab(data):
    container_triangle = st.container()

    # Arrange the toggle and LOB selector side by side
    col1, col2 = st.columns([1, 3]) 
    with col1:
        # Toggle for Incurred vs Paid
        view_label = st.radio(
            "Select View",
            options=['Incurred', 'Paid'],
            index=0
        )
        if view_label == 'Incurred':
            view_value = 'inc'
        else:
            view_value = 'paid'

    with col2:
        # LoB selector
        unique_lobs = data['lob'].unique()
        selected_lobs = st.multiselect(
            "Select LOB", 
            options = unique_lobs, 
            default = unique_lobs  
        )
    
    col_s1, col_space, col_s2 = st.columns([4, 1, 4]) 

    with col_s1:  
        # Slider for selecting a year between 2011 and 2020
        selected_year_range = st.slider(
            'Select years',
            min_value = data['year'].min(),
            max_value = data['year'].max(),
            value=(data['year'].min(), data['year'].max())  # Default value
        )

    with col_s2:  
        # Slider for selecting a year between 2011 and 2020
        selected_dev_range = st.slider(
            'Select number of development periods',
            min_value = data['dev'].min(),
            max_value = data['dev'].max(),
            value=(data['dev'].min(), data['dev'].max())  # Default value
        )



    df_filtered = data[(data['trs'] == view_value) & 
                       (data['lob'].isin(selected_lobs)) &
                       (data['year'] >= selected_year_range[0]) &
                       (data['year'] <= selected_year_range[1]) &
                       (data['dev'] >= selected_dev_range[0]) &
                       (data['dev'] <= selected_dev_range[1])
                       ]
    
    df_pivot = df_filtered.pivot_table(index='dev', columns='year', values='value')

    # Plot with Matplotlib instead
    fig, ax = plt.subplots(figsize=(8, 4))
    for column in df_pivot.columns:
        # Drop NaN values before plotting
        series = df_pivot[column].dropna()
        ax.plot(
            series.index, 
            series, 
            markersize = 3, 
            marker = 'o', 
            label = column
            )

    # Set x-axis to show integer values only
    ax.set_xticks(range(0, int(df_pivot.index.max()) + 1))
    ax.set_xlabel('Development Year')
    ax.set_ylabel('Value')
    ax.set_title(f'Development {view_label}')
    ax.legend(title='Year', loc='center left', bbox_to_anchor=(1, 0.5))
    max_value = df_pivot.max().max()
    ax.set_ylim(0, max_value * 1.1)


    # Display the plot using Streamlit
    st.pyplot(fig)