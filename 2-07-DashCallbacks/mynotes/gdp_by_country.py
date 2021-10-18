import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("../../Data/gapminderDataFiveYear.csv")
year_options = [{"value": year, "label": year} for year in df["year"].unique().tolist()]
min_year = df["year"].min()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            id="figure",
        ),
        dcc.Dropdown(id="year-selector", options=year_options, value=min_year),
    ],
)


@app.callback(Output("figure", "figure"), [Input("year-selector", "value")])
def update_figure(selected_year):
    year_df = df[df["year"] == selected_year]
    traces = [
        go.Scatter(
            x=continent_df["gdpPercap"],
            y=continent_df["lifeExp"],
            mode="markers",
            marker=dict(size=5 * continent_df["pop"] / continent_df["pop"].mean()),
            text=continent_df["country"],
            opacity=0.6,
            name=continent,
        )
        for continent, continent_df in year_df.groupby("continent")
    ]
    layout = go.Layout(
        title="Life Expectancy by Continent, with Year Selection",
        xaxis={"title": "GDP Per Capita", "type": "log"},
        yaxis={"title": "Life Expectancy"},
    )
    return {"data": traces, "layout": layout}


if __name__ == "__main__":
    app.run_server(debug=1)
