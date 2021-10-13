import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('../../Data/mpg.csv')
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
print(df.head())
print(df.columns)

data = [
    go.Scatter(
        x=df['horsepower'],
        y=df['mpg'],
        # by default, text equals y
        text=df['name'],
        mode='markers',
        marker=dict(
            # modify size of the markers
            size=df['weight']/100,
            color=df['cylinders'],
            showscale=True
        )
    )
]
layout = go.Layout(title='Bubble Chart', hovermode='x')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
