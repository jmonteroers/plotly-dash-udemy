import numpy as np
import plotly.offline as pyo
import plotly.figure_factory as ff

N = 8
range_means = range(0, N, 2)
data = [
    np.random.randn(100) + mean for mean in range_means
]
group_labels = [f"group_{idx+1}" for idx, mean in enumerate(range_means)]
fig = ff.create_distplot(data, group_labels=group_labels, bin_size=[2, 1, 3, 4])
pyo.plot(fig, filename="multiple_distplots.html")
