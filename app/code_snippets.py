import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os, sys
import plotly.graph_objs as go



# this works for displaying line graph, good base starting point for any line graph over time 
start =os.path.dirname(os.path.realpath(sys.argv[0])) 
location = os.path.join(start, 'one_month_spreads.csv')
# read data
df = pd.read_csv(location, index_col ='Unnamed: 0')
df.index = pd.to_datetime(df.index)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df_for_dash = pd.DataFrame(index=df.index)
name_array = []
value_array = []
df = df.iloc[:,:4]

for col in df.columns:
	col_name = [col] * len(df[col])
	name_array = name_array + col_name
	value_array = value_array + list(df[col]) 

df_for_dash = pd.DataFrame.from_dict({'Spread_Names':name_array, 'Spread_Values':value_array})
spread_range = 1

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df.index,
                    y=df_for_dash[df_for_dash['Spread_Names'] == i]['Spread_Values'],
                    text=df_for_dash[df_for_dash['Spread_Names'] == i]['Spread_Values'],
                    mode='lines',
                    opacity=0.7,
                    #fill='tozeroy',
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df_for_dash.Spread_Names.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Dates'},
                yaxis={'title': 'Spread'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
