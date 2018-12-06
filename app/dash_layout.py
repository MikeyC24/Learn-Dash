# standard library
import os, sys

# dash libs
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objs as go

# pydata stack
import pandas as pd
from sqlalchemy import create_engine

# set params
#/home/ebitda/Documents/coding_all/Learn-Dash/dash/soccer-stats.db
#conn = create_engine(os.environ['soccer-stats.db'])
#conn = create_engine('home/ebitda/Documents/coding_all/Learn-Dash/dash/soccer-stats.db')
"""
def fetch_data(q):
    df = pd.read_sql(
        sql=q,
        con=conn
    )
    return df
"""


def fetch_data(q):
	# path for data
	start =os.path.dirname(os.path.realpath(sys.argv[0])) 
	location = os.path.join(start, 'one_month_spreads.csv')
	# read data
	df = pd.read_csv(location, index_col ='Unnamed: 0')
	df.index = pd.to_datetime(df.index)
	return df


# Set up Dashboard and create layout
app = dash.Dash()
app.css.append_css({
	"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

app.layout = html.Div([

	# Page Header
	html.Div([
		html.H1('Project Header')
	]),

])
# line right below is added bc selector id isnt set up yet so this can still run flask 
#app.config['suppress_callback_exceptions']=True
# Template
@app.callback(
	Output(component_id='selector-id', component_property='figure'),
	[
		Input(component_id='input-selector-id', component_property='value')
	]
)
def ctrl_func(input_selection):
	return None


# start Flask server
if __name__ == '__main__':
	app.run_server(
		debug=True,
		host='0.0.0.0',
		port=8050
	)