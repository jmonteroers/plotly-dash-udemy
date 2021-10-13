"""
Take two random samples from rings column in abelone dataset,
they should look quite similar in a boxplot
"""
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

N = 30
abalone = pd.read_csv("../../Data/abalone.csv")
print(f"The abalone dataset has {len(abalone)} rows")
sample1 = np.random.choice(abalone["rings"], N, replace=False)
sample2 = np.random.choice(abalone["rings"], N, replace=False)

traces = [
    go.Box(y=sample1, name="Sample 1"),
    go.Box(y=sample2, name="Sample 2")
]
layout = go.Layout(
    title=f"Comparison of Two Samples Taken from the Same Population (N={N})"
)
fig = go.Figure(data=traces, layout=layout)
pyo.plot(fig, filename="random_samples.html")
