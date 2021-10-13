import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from typing import Optional

df = pd.read_csv('../../Data/mpg.csv')
data = [
    go.Scatter(
        x=df['weight'],
        y=df['acceleration'],
        text=df['name'],
        mode='markers',
        marker=dict(
            size=(df['model_year']-60.)
        )
    )
]


def plot_data(data: list, filename: str,
              layout_kwargs: Optional[dict] = None) -> None:
    layout_kwargs = layout_kwargs or {}
    layout = go.Layout(**layout_kwargs)
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename=filename)


plot_data(data, filename='bubble_chart_mpg.html',
          layout_kwargs={
          'title': 'Acceleration plotted against Weight, size Model Year',
           'xaxis': dict(title='Weight'),
           'yaxis': dict(title='Acceleration')
           }
           )
