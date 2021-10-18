import dash
import dash_html_components as html
import dash_core_components as dcc

# create Flask app
app = dash.Dash()
colors = {'background': '#111111', 'text': '#7FDBFF'}
app.layout = html.Div(children=[
    # style dict gets React-like attrs
    html.H1("Hello Dash!", style={'color': colors['text'], 'textAlign': 'center'}),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [4, 1, 2],
                    'type': 'bar',
                    'name': 'whatever'
                },
                {
                    'x': [1, 2, 3],
                    'y': [5, 2, 1],
                    'type': 'bar',
                    'name': 'whatever 2'
                },
            ],
            'layout': {
                'title': 'Simple Barplots',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {'color': colors['text']},
                }
            }
        )
    ],
    style={'backgroundColor': colors['background']})


if __name__ =="__main__":
    app.run_server(debug=1)
