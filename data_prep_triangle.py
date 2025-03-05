#%% 
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

def skew_value(value, skew_range=0.1):
    """
    Skew the given value by a random percentage within the specified range. 
    To see something, because its not nice triangle data.

    Parameters:
    value (float): The original value to be skewed.
    skew_range (float): The range within which to skew the value, e.g., 0.1 for ±10%.

    Returns:
    float: The skewed value.
    """
    if pd.isna(value):
        return value  # Do not change NaN values
    skew_factor = 1 + np.random.uniform(-skew_range, skew_range)
    return value * skew_factor

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
    month_columns = [col for col in df.columns if col.startswith('Month')]
    df[month_columns] = df[month_columns].replace(0, np.nan)
    df[month_columns] = df[month_columns].cumsum(axis=0)
    df.rename(columns = {'index':'dev'}, inplace=True)
    df.columns = ['dev'] + list(range(2011, 2021)) + ['trs']
    df = pd.melt(df, id_vars=['trs', 'dev'], var_name='year', value_name='value').reset_index()  
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


# Apply the skew_value function to the 'value' column
dt_triangle_all['value'] = dt_triangle_all['value'].apply(skew_value, skew_range=0.2)

# profile = ProfileReport(dt_customer_raw, title="Pandas Profiling Report")
# profile
# %%

