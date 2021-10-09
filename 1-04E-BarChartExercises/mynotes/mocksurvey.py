import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


df = pd.read_csv('../../Data/mocksurvey.csv')
print(df.iloc[0])
df.rename(columns={df.columns[0]: 'question'}, inplace=True)
df.set_index('question', inplace=True)
traces = [
    go.Bar(x=df[result], y=df.index, name=result, orientation='h')
    for result in df.columns
]
layout = go.Layout(title='Mock Survey Results by Question',
                   yaxis={'title': 'Proportion of Answers'},
                   barmode='stack',
                   hovermode='y')
fig = go.Figure(data=traces, layout=layout)
pyo.plot(fig, filename='mocksurvey.html')
breakpoint()
