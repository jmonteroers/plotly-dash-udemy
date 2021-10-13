import numpy as np
import plotly.offline as pyo
import plotly.figure_factory as ff

x = np.random.randn(1000)
data = [x]
group_labels = ["distplot"]
fig = ff.create_distplot(data, group_labels=group_labels)
pyo.plot(fig, filename="basic_distplot.html")
