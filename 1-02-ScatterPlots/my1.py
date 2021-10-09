import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random = np.random.randint(1, 101, (2, 100))

data = [go.Scatter(x=random[0], y=random[1], mode='markers')]

pyo.plot(data, filename='plot1.html')
