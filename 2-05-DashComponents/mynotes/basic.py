import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div(
    [
        "This is the outermost div",
        html.Div(
            ["This is an inner div"], style={"color": "red", "border": "1px red dashed"}
        ),
        html.Div(
            ["This is another inner div!"],
            style={"color": "blue", "border": "2px blue solid"},
        ),
    ],
    style={"color": "green", "border": "2px green solid"},
)

if __name__ == "__main__":
    app.run_server(debug=1)
