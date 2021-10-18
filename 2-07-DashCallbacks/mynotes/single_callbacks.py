import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Input(
            id="input",
            value="Initial text",
            type="text",
            style={"margin-bottom": "10px"},
        ),
        html.Div(
            id="div1",
            style={"border": "2px solid", "padding": "30px", "white-space": "nowrap"},
        ),
    ],
)


@app.callback(
    Output(component_id="div1", component_property="children"),
    [Input(component_id="input", component_property="value")],
)
def update_output_div(input_value):
    return f"You entered: {input_value}"


if __name__ == "__main__":
    app.run_server(debug=1)
