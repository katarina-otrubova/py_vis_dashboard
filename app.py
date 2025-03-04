#%%
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport


from data_prep_triangle import dt_triangle_all
from data_prep_claim import dt_customer


# global settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)




#%%
### STREAMLIT

st.title("Claim Dashboard")
st.dataframe(dt_customer)





df_paid = triangle_all[(triangle_all['trs'] == 'paid') & 
                       (triangle_all['lob'] == 'Motor') #& 
                      # (triangle_all['month'] == 'Month1')
                       ]

# Pivot the DataFrame to prepare it for plotting
df_pivot = df_paid.pivot_table(index='dev', columns='month', values='value')

# Plot the chart using Streamlit
st.line_chart(df_pivot)
# st.line_chart(paid_cas, x="Date", y="Price")

# %%
