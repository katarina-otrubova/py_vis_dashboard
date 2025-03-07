import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff    


def create_motor_tab(data):

    container_motor = st.container()
    st.subtitle("Geographical distribution of claims")

    selector_1, selector_2 = st.columns([1, 2]) 
    with selector_1:
        # slider for claim size 
        selected_size_range = st.slider(
            'Filter claim size',
            min_value = data['Claims'].min(),
            max_value = data['Claims'].max(),
            value=(data['Claims'].min(), data['Claims'].max())  # Default value
        )

    with selector_2:
        pass




    df_filtered = data[
        (data['Claims'] >= selected_size_range[0]) &
        (data['Claims'] <= selected_size_range[1])
        ]



    fig = go.Figure(go.Scattergeo(
        lat=df_filtered['latitude'],
        lon=df_filtered['longitude'],
        mode='markers',
        marker=dict(
            size=12,
            color=df_filtered['Claims'],
            colorscale='Viridis',
            showscale=True
        ),
        text='',
    ))

    # Set the layout for the map
    fig.update_layout(
        geo=dict(
            projection_type='albers usa',  # Use 'albers usa' projection
            center=dict(lat=39.8283, lon=-98.5795),  # Center on USA
            lataxis=dict(range=[24, 50]),  # Latitude range to zoom
            lonaxis=dict(range=[-125, -66.5]),  # Longitude range to zoom
            scope='usa',  # Limit the map to the USA
        ),
        showlegend=False
    )

    # Display map in Streamlit
    st.plotly_chart(fig)



# # Claim distribution
    st.subtitle("Size distribution of claims")
    hist_data = [data['Claims']]
    group_labels = ['Incurred amount']

    fig_dist = ff.create_distplot(hist_data, group_labels)
    st.plotly_chart(fig_dist)


