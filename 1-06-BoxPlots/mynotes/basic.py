import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from typing import Optional

def plot_data(data: list, filename: str,
              layout_kwargs: Optional[dict] = None) -> None:
    layout_kwargs = layout_kwargs or {}
    layout = go.Layout(**layout_kwargs)
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename=filename)

# IQR = q3 - q1
# outliers, beyond q1/q3 by more than 1.5 IQR
y = [1,2,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [go.Box(
                y=y,
                # show all y points/ alternative is 'outliers' (default)
                boxpoints='all',
                # the larger pointpos, the more to the right the y points are moved
                pointpos=2.0,
                # the more jitter, the more spread boxpoints will be
                jitter=0.5
                )]

plot_data(data, filename='basic_boxplot.html')
