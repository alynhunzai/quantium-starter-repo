from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv('pink_morsel_sales.csv')
fig = px.line(df, x='date', y='sales')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),
    html.Div(children=''''
        A simple Dash web application that displays the sales of Pink Morsel.
    '''),
    dcc.Graph(
        id='pink-morsel-sales',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
