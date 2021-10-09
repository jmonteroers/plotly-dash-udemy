import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('../../Data/2010YumaAZ.csv')
weekDays = ("Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday")

data = []
for day in weekDays:
    upper_day = day.upper()
    df_day = df[df["DAY"] == day.upper()]
    df_day.sort_values("LST_TIME", key=lambda x: x.str.split(":").apply(lambda x: x[0]).astype(int),
                       inplace=True)
    data.append(
        go.Scatter(
            x=df_day["LST_TIME"],
            y=df_day["T_HR_AVG"],
            mode="lines",
            name=day
        )
    )

layout = go.Layout(title=dict(
    text='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    x=.5)
)
fig = go.Figure(data, layout=layout)

pyo.plot(fig, filename='exercise_temp_lines.html')
