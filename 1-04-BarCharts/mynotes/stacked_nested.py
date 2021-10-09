import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../Data/2018WinterOlympics.csv')

trace1 = go.Bar(
    x=df['NOC'],
    y=df['Gold'],
    name='Gold',
    marker={'color': '#FFD700'}
)
trace2 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    name='Silver',
    marker={'color': '#9EA0A1'}
)
trace3 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    name='Bronze',
    marker={'color': '#CD7F32'}
)
data = [trace1, trace2, trace3]
# to make stacked, set barmode to "stack"; default is nested
layout = go.Layout(title='Medals', barmode="stack")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stacked_barplot.html')
