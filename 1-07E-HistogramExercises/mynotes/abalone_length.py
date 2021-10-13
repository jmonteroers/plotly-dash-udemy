#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('../../Data/abalone.csv')

data = [go.Histogram(y=df["length"], xbins=dict(start=0, end=1, size=0.02))]
layout = go.Layout(title="Distribution of Length in Abalone Dataset")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="abalone_length.html")
