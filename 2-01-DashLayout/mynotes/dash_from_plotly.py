import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()
np.random.seed(42)
x = np.random.randint(1, 101, 100)
y = np.random.randint(1, 101, 100)


def create_graph(id: str, title: str, marker_color: str, xaxis: str = "") -> dcc.Graph:
    return dcc.Graph(
        id=id,
        figure=dict(
            data=[
                go.Scatter(
                    x=x,
                    y=y,
                    mode="markers",
                    marker=dict(
                        size=12,
                        color=marker_color,
                        symbol="pentagon",
                        line=dict(width=2),
                    ),
                )
            ],
            layout=go.Layout(
                title=title, xaxis=dict(title=xaxis)
            ),
        ),
    )


app.layout = html.Div(
    [
        html.H1("Dash Web App with Plotly Graph"),
        create_graph("fig1", "First Scatterplot", "rgb(51, 204, 153)"),
        create_graph("fig2", "Second Scatterplot", "rgb(151, 0, 153)", xaxis="Random Numbers from 1 to 100"),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=1)
