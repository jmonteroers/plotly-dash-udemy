import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('../../Data/mpg.csv')

# options: xbins
data = [go.Histogram(x=df["mpg"], xbins=dict(start=0, end=50, size=5))]

layout = go.Layout(title="Histogram")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="basic_hist.html")
