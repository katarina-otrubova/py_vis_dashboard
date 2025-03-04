#%%

import pandas as pd
from ydata_profiling import ProfileReport


# Load data --------------------------------------------------------------------

dt_customer_raw = pd.read_csv('data/Main.csv')

dt_customer = dt_customer_raw
# %%
