import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os, sys
import plotly.graph_objs as go

start =os.path.dirname(os.path.realpath(sys.argv[0])) 
location = os.path.join(start, 'one_month_spreads.csv')
# read data
df = pd.read_csv(location, index_col ='Unnamed: 0')
df.index = pd.to_datetime(df.index)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

drop_dict = {}
for col in df.columns:
	drop_dict['label'] = col
	drop_dict['value'] = df[col][:5]

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

	
], style={'columnCount': 2})

if __name__ == '__main__':
	app.run_server(debug=True)






"""
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


"""





"""
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([
	dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
	app.run_server(debug=True)

# look at this https://commonmark.org/ 
# and this https://commonmark.org/help/
"""

"""
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv(
	'https://gist.githubusercontent.com/chriddyp/' +
	'5d1ea79569ed194d432e56108a04d188/raw/' +
	'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
	'gdp-life-exp-2007.csv')

app.layout = html.Div([
	dcc.Graph(
		id='life-exp-vs-gdp',
		figure={
			'data': [
				go.Scatter(
					x=df[df['continent'] == i]['gdp per capita'],
					y=df[df['continent'] == i]['life expectancy'],
					text=df[df['continent'] == i]['country'],
					mode='markers',
					opacity=0.7,
					marker={
						'size': 15,
						'line': {'width': 0.5, 'color': 'white'}
					},
					name=i
				) for i in df.continent.unique()
			],
			'layout': go.Layout(
				xaxis={'title': 'Dates'},
				yaxis={'title': 'Life Expectancy'},
				margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
				legend={'x': 0, 'y': 1},
				hovermode='closest'
			)
		}
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)
"""
"""
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
	'background': '#111111',
	'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
	html.H1(
		children='Hello Dash',
		style={
			'textAlign': 'center',
			'color': colors['text']
		}
	),

	html.Div(children='Dash: A web application framework for Python.', style={
		'textAlign': 'center',
		'color': colors['text']
	}),

	dcc.Graph(
		id='example-graph-2',
		figure={
			'data': [
				{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
				{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
			],
			'layout': {
				'plot_bgcolor': colors['background'],
				'paper_bgcolor': colors['background'],
				'font': {
					'color': colors['text']
				}
			}
		}
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)
"""

"""
def generate_table(dataframe, max_rows=10):
	return html.Table(
		# Header
		[html.Tr([html.Th(col) for col in dataframe.columns])] +

		# Body
		[html.Tr([
			html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
		]) for i in range(min(len(dataframe), max_rows))]
	)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
	html.H4(children='US Agriculture Exports (2011)'),
	generate_table(df)
])

if __name__ == '__main__':
	app.run_server(debug=True)

"""
"""
questions,
rendering a fillable pandas dataframe in this


"""
