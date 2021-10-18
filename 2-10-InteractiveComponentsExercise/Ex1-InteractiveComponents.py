#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from typing import Tuple

# Launch the application:
app = dash.Dash(__name__)

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div(
    [
        html.H1("Multiplication Calculator"),
        html.Div(
            [
                html.Div(
                    [
                        dcc.RangeSlider(
                            id="input-slider",
                            min=-5,
                            max=6,
                            value=[-1, 1],
                            marks={n: n for n in range(-5, 7)},
                        )
                    ],
                    style={"margin": "2em"},
                ),
                html.Div(
                    [
                        html.H2(id="output-mult"),
                    ],
                    style={"text-align": "center", "margin-top": "4em"},
                ),
            ],
            style={"width": "50%", "margin": "4em auto"},
        ),
    ]
)


# Create a Dash callback:
@app.callback(
    Output(component_id="output-mult", component_property="children"),
    [Input(component_id="input-slider", component_property="value")],
)
def multiply_bounds_slider(bounds: Tuple[int, int]) -> str:
    min_bound, max_bound = bounds
    return f"The result of multiplying {min_bound} and {max_bound} is {min_bound*max_bound}"


# Add the server clause:
if __name__ == "__main__":
    app.run_server(debug=True)
