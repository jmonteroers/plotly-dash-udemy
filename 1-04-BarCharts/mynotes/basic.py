import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../Data/2018WinterOlympics.csv')
print(df.iloc[0])

data = [go.Bar(x=df['NOC'], y=df['Total'])]
layout = go.Layout(title='Medals')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='simple_barplot.html')
