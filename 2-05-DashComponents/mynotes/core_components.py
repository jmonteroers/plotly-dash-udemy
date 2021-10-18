import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()


app.layout = html.Div(
    [
        html.Label("Dropdown"),
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="SF",
        ),
        html.Label("Slider"),
        dcc.Slider(
            min=-10, max=10, step=1, value=0, marks={i: i for i in range(-10, 11)}
        ),
        # Quick Fix! p used to ensure line break, avoid marks overlapping label!
        html.P(html.Label("Some radio items")),
        dcc.RadioItems(options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "San Francisco", "value": "SF"},
        ], value="SF")
    ]
)

if __name__ == "__main__":
    app.run_server(debug=1)
