#%% 

import pandas as pd
from ydata_profiling import ProfileReport

# Load data --------------------------------------------------------------------

paid_cas = pd.read_csv('data/Casualty_paid_adjusted.csv')
inc_cas = pd.read_csv('data/Casualty_incur_adjusted.csv')
paid_mot = pd.read_csv('data/Motor_paid_adjusted.csv')
inc_mot = pd.read_csv('data/Motor_incur_adjusted.csv')
paid_pro = pd.read_csv('data/Property_paid_adjusted.csv')
inc_pro = pd.read_csv('data/Property_incur_adjusted.csv')

# Triangle Data prep --------------------------------------------------------------------

paid_cas['trs'] = 'paid'
paid_mot['trs'] = 'paid'
paid_pro['trs'] = 'paid'
inc_cas['trs'] = 'inc'
inc_mot['trs'] = 'inc'
inc_pro['trs'] = 'inc'

list_dfs = [
    paid_cas,
    inc_cas,
    paid_mot,
    inc_mot,
    paid_pro,
    inc_pro
]

for i, df in enumerate(list_dfs):
    df = df.reset_index()
    df.rename(columns = {'index':'dev'}, inplace=True)
    df = pd.melt(df, id_vars=['trs', 'dev'], var_name='month', value_name='value').reset_index()
    list_dfs[i] = df

# creates dfs of triangles by lob
triangle_casualty = pd.concat([list_dfs[0],list_dfs[1]], ignore_index=True)
triangle_casualty['lob'] = 'Casualty'
triangle_motor = pd.concat([list_dfs[2],list_dfs[3]], ignore_index=True)
triangle_motor['lob'] = 'Motor'
triangle_property = pd.concat([list_dfs[4],list_dfs[5]], ignore_index=True)
triangle_property['lob'] = 'Property'

dt_triangle_all = pd.concat([
    triangle_casualty,
    triangle_motor,
    triangle_property]).drop(columns=['index'])




# profile = ProfileReport(dt_customer_raw, title="Pandas Profiling Report")
# profile
# %%
