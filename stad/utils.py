from panel.widgets.base import Widget
from bokeh.models.widgets import DatePicker as _BkDatePicker
from datetime import datetime
import param
from toolz import isiterable

PATH = __file__.split('stad')[0]
TEST_DATA_PATH = PATH +  r"data/1-6m-accidents-traffic-flow-over-16-years/accidents_2009_to_2011.csv"


class DatePicker(Widget):

    value = param.Date(default=None)

    start = param.Date(default=None)

    end = param.Date(default=None)

    _widget_type = _BkDatePicker

    _rename = {'start': 'min_date', 'end': 'max_date', 'name': 'title'}

    def _process_property_change(self, msg):
        msg = super(DatePicker, self)._process_property_change(msg)
        if msg.get('value',False):
            if not isiterable(msg['value']):
                msg['value'] = datetime.combine(msg['value'], datetime.min.time())
        return msg