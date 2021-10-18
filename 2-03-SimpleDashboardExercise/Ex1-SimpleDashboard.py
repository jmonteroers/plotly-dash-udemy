#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc

# Launch the application:
app = dash.Dash(name="old_geyser_dash_app")

# Create a DataFrame from the .csv file:
df = pd.read_csv("../data/OldFaithful.csv")
df["Y"] = df["Y"].astype(float)
# Create a Dash layout that contains a Graph component:
app.layout = html.Div(
    [
        html.H1(
            "Understanding Old Geyser Eruptions in Yellowstone National Park, Wyoming, US"
        ),
        dcc.Graph(
            id="scatter_old_faithful",
            figure={
                "data": [
                    go.Scatter(
                        x=df["X"],
                        y=df["Y"],
                        mode="markers",
                        marker=dict(
                            size=12, symbol="x", color="coral", line=dict(width=1)
                        ),
                    )
                ],
                "layout": go.Layout(
                    title="Waiting Time for Different Duration Times",
                    xaxis=dict(title="Eruption Duration Time"),
                    yaxis=dict(title="Waiting Time Until Next Eruption"),
                    hovermode="closest",
                ),
            },
        ),
    ]
)


# Add the server clause:
if __name__ == "__main__":
    app.run_server(debug=1)
