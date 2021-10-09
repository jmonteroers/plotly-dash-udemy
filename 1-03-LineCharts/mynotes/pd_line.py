import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('../../sourcedata/nst-est2017-alldata.csv')


division_one = df[df['DIVISION'] == '1']
division_one.set_index('NAME', inplace=True)
pop_cols = [col for col in division_one.columns if col.startswith('POP')]
division_one = division_one[pop_cols]
print(division_one.head())
data = [
    go.Scatter(
        x=division_one.columns,
        y=division_one.loc[name],
        mode='lines',
        name=name
    )
    for name in division_one.index
]
pyo.plot(data, filename='pop_line.html')
