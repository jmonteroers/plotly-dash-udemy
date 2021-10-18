import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import subplots
import re
import pandas as pd


filenames = ['2010SantaBarbaraCA.csv', '2010SitkaAK.csv', '2010YumaAZ.csv']
cities = [re.search(r"2010(\w+)[A-Z]{2}.csv", filename).groups()[0] for filename in filenames]
cities = [
    " ".join([word for word in re.split(r"([A-Z][^A-Z]+)", city) if word])
    for city in cities
]
dfs = [
    pd.read_csv(f"../../data/{filename}") for filename in filenames
]
traces = [
    go.Heatmap(
        x=df["DAY"], y=df["LST_TIME"], z=df["T_HR_AVG"], colorscale="Jet",
        zmin=5, zmax=40
    )
    for df in dfs
]
title_pattern = "Hourly Temperatures, June 1-7, in {}"
layout = go.Layout(title="Hourly Temperatures, June 1-7, in Santa Barbara, Sitka and Yuma")
fig = subplots.make_subplots(rows=1, cols=3, subplot_titles=[
                          title_pattern.format(city) for city in cities],
                          shared_yaxes=True)
for idx, trace in enumerate(traces):
    fig.append_trace(trace, 1, idx+1)
fig['layout'].update(title="Hourly Temperatures Heatmap")
pyo.plot(fig, filename="heatmaps.html")
