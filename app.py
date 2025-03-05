#%%
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport


from data_prep_triangle import dt_triangle_all
from data_prep_claim import dt_customer
from container_triangles import create_triangle_tab
from container_claims import create_cla_tab

# global settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)




#%%
### STREAMLIT


st.set_page_config(page_title="Training Streamlit Dashboard")
# st.set_page_config(page_title="Training Streamlit Dashboard", layout="wide")
st.title("Claim Dashboard")
# st.dataframe(dt_customer)


cla_tab, triangle_tab = st.tabs(["Claim Data", "Claim Development"])

with cla_tab:
    create_cla_tab(dt_triangle_all)

with triangle_tab:
    create_triangle_tab(dt_triangle_all)

st.write("this should be under containers")

# df_paid = triangle_all[(triangle_all['trs'] == 'paid') & 
#                        (triangle_all['lob'] == 'Motor') #& 
#                       # (triangle_all['month'] == 'Month1')
#                        ]

# Pivot the DataFrame to prepare it for plotting
# df_pivot = df_paid.pivot_table(index='dev', columns='month', values='value')

# Plot the chart using Streamlit
# st.line_chart(df_pivot)
# st.line_chart(paid_cas, x="Date", y="Price")

# %%
