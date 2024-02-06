import dash
from dash import dcc, html


app = dash.Dash(__name__)

app.layout = html.Div([
    #Define os componetes do dashboard aqui
])


dcc.Graph(
    id='example-graph',
    figure={
        'data':[
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        ],
        'layout':{
            'title': 'Dash Data Visualization'
            }
        }
    )

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_graph(selected_value):
# Update the chart based on user input
    
   
# You can use Pandas or other libraries to filter and process data
    
   
# and update the chart figure.
# Return the updated figure
    
    if __name__ == '__main__':
        app.run_server(debug=True)