import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go

df = pd.read_csv("../../data/mpg.csv")
features_options = [{"value": column, "label": column.title()} for column in df.columns]
dropdown_style = {"width": "50%", "display": "inline-block"}
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.Div(
            [dcc.Dropdown(id="xaxis", options=features_options, value="displacement")],
            style=dropdown_style,
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="yaxis",
                    options=features_options,
                    value="acceleration",
                )
            ],
            style=dropdown_style,
        ),
        dcc.Graph(id="graph"),
    ],
    style={"padding": 10},
)


@app.callback(
    Output("graph", "figure"),
    [
        Input("xaxis", "value"),
        Input("yaxis", "value"),
    ],
)
def update_graph(xaxis_name, yaxis_name):
    # if not xaxis_name or not yaxis_name:
    #     return
    return {
        "data": [
            go.Scatter(
                x=df[xaxis_name],
                y=df[yaxis_name],
                mode="markers",
                marker=dict(size=15, opacity=0.5, line=dict(color="white", width=0.5)),
                text=df["name"],
            )
        ],
        "layout": go.Layout(
            title="Scatterplot with dynamic x and y axes",
            xaxis=dict(title=xaxis_name.capitalize()),
            yaxis=dict(title=yaxis_name.capitalize()),
            hovermode="closest"
        ),
    }


if __name__ == "__main__":
    app.run_server(debug=1)
