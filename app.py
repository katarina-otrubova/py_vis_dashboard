#%%
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

st.set_page_config(page_title="Training Streamlit Dashboard", layout="wide")

from data_prep_triangle import dt_triangle_all
from data_prep_claim import customer_data_prep
from container_triangles import create_triangle_tab
from container_claims import create_cla_tab
from container_motor import create_motor_tab

# global settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# STYLING

st.markdown(
    """
    <style>
    .block-container {
        max-width: 72%;
        margin-left: 3%;
        margin-right: auto;
        
    }
    body {
        background-color: #C9C6B6; 
        background-color: #00FF00;
    }

        .stSlider > div > div > div > input[type=range] {
        accent-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# DATA

dt_claims, dt_motor_loc = customer_data_prep()

### STREAMLIT



st.title("Claim Dashboard")

cla_tab, triangle_tab, motor_tab = st.tabs([
    "Claim Analysis", 
    "Triangle Development",
    "US Motor Claims"
    ])

with cla_tab:
    create_cla_tab(dt_claims)

with triangle_tab:
    create_triangle_tab(dt_triangle_all)

with motor_tab:
    create_motor_tab(dt_motor_loc.head(1000))

