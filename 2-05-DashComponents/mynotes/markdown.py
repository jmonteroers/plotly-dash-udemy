import dash_html_components as html
import dash_core_components as dcc
import dash

app = dash.Dash(__name__)

markdown = (
    "## Important note \n"
    """I can write Markdown lists in Dash:
- First item
- Second item
    """
)

app.layout = html.Div([dcc.Markdown(markdown)])

if __name__ == "__main__":
    app.run_server(debug=1)
