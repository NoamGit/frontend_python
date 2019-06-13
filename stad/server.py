import datetime
import sys
sys.path.append(__file__.split('stad')[0])

from data.toy_data_reader import toy_data_reader
from stad.stad_panel import StadApp
import panel as pn
import jinja2
import holoviews as hv
import pandas as pd
from stad.utils import PATH,TEST_DATA_PATH

# df = toy_data_reader()
# app = StadApp(name="", data=df_raw)
app = StadApp(name="")


panel = pn.Row(pn.Column(
            # pn.Row(title)
              pn.Row(app.autocomplete, align="center")
            , pn.Row(app.DATE_start, align="center")
            , pn.Row(app.DATE_end, align="center")
            , pn.Row(app.BTN_run))
            , pn.Column(app.plot_ts)
)
    # pn.Row(app.daily_shootings, align="center"),
    # pn.Row(instructions, align="center")

# templateLoader = jinja2.FileSystemLoader(searchpath=PATH+r"stad/templates")
# templateEnv = jinja2.Environment(loader=templateLoader)
# template = templateEnv.get_template("test_template.html")
# tmpl = pn.Template(template)

# tmpl.add_panel('select_panel', panel)

# tmpl.servable()

panel.servable()
# panel serve --show server.py