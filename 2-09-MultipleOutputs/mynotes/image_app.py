import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import base64
from pathlib import Path

app = dash.Dash(__name__)
df = pd.read_csv("../../data/wheels.csv")
image_datapath = Path(__file__).resolve().parents[2] / "Data" / "Images"

def create_options_from_column(df: pd.DataFrame, colname: str) -> dict:
    return [dict(label=val, value=val) for val in df[colname].unique()]


def encode_image(image_path: str) -> str:
    with open(image_path, 'rb') as fd:
        encoded = base64.b64encode(fd.read())
    return f"data:image/png;base64,{encoded.decode()}"


app.layout = html.Div(
    [
        dcc.RadioItems(
            id="wheels", options=create_options_from_column(df, "wheels"), value=1
        ),
        html.Div(id="wheels-output"),
        html.Hr(),
        dcc.RadioItems(
            id="color", options=create_options_from_column(df, "color"), value="red"
        ),
        html.Div(id="color-output"),
        html.Hr(),
        html.Img(id="image-output", src="children", height=300)
    ],
    style={"fontFamily": "helvetica", "fontSize": 18},
)


@app.callback(Output("wheels-output", "children"), [Input("wheels", "value")])
def update_wheels_text(wheels: int) -> str:
    return f"You chose {wheels} wheels"


@app.callback(Output("color-output", "children"), [Input("color", "value")])
def update_color_text(color: str) -> str:
    return f"You chose {color}"


@app.callback(Output("image-output", "src"), [Input("wheels", "value"), Input("color", "value")])
def update_image(wheel: int, color: str) -> str:
    image_filename = (df[(df["wheels"] == wheel) & (df["color"] == color)]["image"]).iloc[0]
    return encode_image(image_datapath / image_filename)


if __name__ == "__main__":
    app.run_server(debug=True)
