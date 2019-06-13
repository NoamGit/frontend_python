from datetime import datetime

import pandas as pd

from stad.utils import TEST_DATA_PATH


def toy_data_reader():
    df_raw = pd.read_csv(TEST_DATA_PATH)
    col = ['Date', 'Time', 'Longitude', 'Latitude', 'Accident_Severity']
    df_filt = df_raw[col].dropna()
    to_datetime_func = lambda s: datetime.strptime(s, '%d/%m/%Y %H:%M')
    time_datetime = df_filt.apply(lambda row: to_datetime_func(row['Date'] + ' ' + row['Time']), axis=1)
    time_index = pd.Index(time_datetime)
    return df_filt[['Longitude', 'Latitude', 'Accident_Severity']].set_index(time_index)
