#%%

import pandas as pd
from ydata_profiling import ProfileReport


# Load data --------------------------------------------------------------------

dt_customer_raw = pd.read_csv('data/Main.csv')

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




# notes
# try delete loss if claim count= 0
# freq = sum(claim count) / sum(exposure)

# bonus malus = extra charge based on claim exp

