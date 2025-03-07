#%%

import streamlit as st
import pandas as pd
import random
from ydata_profiling import ProfileReport

@st.cache_data
def customer_data_prep():
    def generate_lat_lng_us():
        # Define approximate latitude and longitude ranges
        lat_lng_ranges = [
            # ((31.0, 36.0), (-124.0, -114.0)),  # California and Nevada
            ((32.0, 37.0), (-114.0, -105.0)),  # Arizona and New Mexico
            ((36.0, 42.0), (-124.0, -116.0)),  # Oregon and Washington
            ((40.0, 49.0), (-110.0, -100.0)),  # Montana, Wyoming, and Colorado
            # ((25.0, 31.0), (-85.0, -80.0)),    # Florida
            ((30.0, 37.0), (-95.0, -85.0)),    # Texas and Louisiana
            ((35.0, 41.0), (-90.0, -80.0)),    # Tennessee and North Carolina
            ((37.0, 43.0), (-90.0, -80.0)),    # Illinois and Indiana
            ((39.0, 45.0), (-85.0, -75.0)),    # Ohio and Pennsylvania
            ((42.0, 49.0), (-85.0, -75.0)),    # Michigan and New York
            ((35.0, 40.0), (-120.0, -115.0)),  # Southern California
            ((36.0, 41.0), (-105.0, -95.0)),   # Oklahoma and Kansas
            ((38.0, 44.0), (-100.0, -90.0)),   # Nebraska and Iowa
            ((44.0, 49.0), (-98.0, -88.0)),    # Minnesota and Wisconsin
        ]
        # Select a random range for latitude and longitude
        selected_lat_range, selected_lng_range = random.choice(lat_lng_ranges)
        
        # Generate random latitude and longitude within the selected range
        lat = random.uniform(selected_lat_range[0], selected_lat_range[1])
        lng = random.uniform(selected_lng_range[0], selected_lng_range[1])
        
        return lat, lng


    # Load data --------------------------------------------------------------------

    dt_customer_raw = pd.read_csv('data/Main.csv')
    # scale to get more interesting visualisatoins
    dt_customer_raw['Claims'] = dt_customer_raw['Claims'] * dt_customer_raw.apply(lambda x: random.random(), axis=1)
    # profile = ProfileReport(dt_customer_raw, title="Pandas Profiling Report")
    # profile
    # %%

    dt_claims = dt_customer_raw[[
        'ClaimNb',
        'Exposure',
        'Country',
        'InsuranceType',
        'premiums',
        'Claims',
        'Expenses'
        ]]


    dt_claims.loc[dt_claims['ClaimNb'] == 0, ['Claims', 'Expenses']] = 0


    dt_customer = dt_customer_raw

    dt_motor_loc = dt_customer[(dt_customer['Country'] == 'North America') & 
                            (dt_customer['InsuranceType'] == 'Motor')]
    dt_motor_loc['latitude'], dt_motor_loc['longitude'] = zip(*dt_motor_loc.apply(lambda x: generate_lat_lng_us(), axis=1))


    return dt_claims, dt_motor_loc


# notes
# try delete loss if claim count= 0
# freq = sum(claim count) / sum(exposure)

# bonus malus = extra charge based on claim exp

