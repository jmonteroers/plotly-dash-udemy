import plotly.offline as pyo
import plotly.graph_objs as go
from typing import Optional

def plot_data(data: list, filename: str,
              layout_kwargs: Optional[dict] = None) -> None:
    layout_kwargs = layout_kwargs or {}
    layout = go.Layout(**layout_kwargs)
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename=filename)

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]


data = [
    go.Box(y=snodgrass, name='Snodgrass'),
    go.Box(y=twain, name='Twain')
]
plot_data(data, 'mark_twain.html')
