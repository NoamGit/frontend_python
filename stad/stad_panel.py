from datetime import datetime

import numpy as np
import pandas as pd
import panel as pn
import param as pm
from fastcache import lru_cache
import holoviews as hv

hv.extension('bokeh')
pn.extension()
START = datetime(2009,1,1)
END = datetime(2011,12,22)

class StadApp(pm.Parameterized):
    DB = ['12323', '5421', '78413', '15161']

    autocomplete = pn.widgets.AutocompleteInput(
        name='ID', options=DB,
        placeholder='Enter ID')

    # define interactions

    # the number of days to get data for
    DATE_start = pn.widgets.DatePicker(name='start date', start=START, end=END)

    DATE_end = pn.widgets.DatePicker(name='end date',start=START, end=END)

    BTN_run = pn.widgets.Button(name='Run')

    def __init__(self, *args, **kwargs):
        self.raw_data = kwargs.pop('data', None)
        super(StadApp, self).__init__(*args, **kwargs)

    def get_data(self, start_time, end_time):
        return self.raw_data.iloc[str(start_time.date()):str(end_time.date())]

    @pn.depends("BTN_run.clicks", watch=True)
    def plot_ts(self):
        print(str(self.DATE_start.value))
        return hv.Curve(np.random.randint(0,10,7)).options(line_color="#cfcfcf")
        # df = self.get_data(self.DATE_start,self.DATE_end)
        # print(df)


    # the x-axis selection on the daily shootings chart
