import pandas as pd
df=pd.read_csv('milk_data.csv')
df
import dash
from dash import Dash,html, dcc,Input,Output
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json
with urlopen("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson") as response:
    states = json.load(response)

df.loc[len(df.index)] = ['Ladakh',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
app = Dash(__name__)


#fig2 = px.bar(df, x = 'States_Union Territories', y =['2000-01-INC','2011-12-INC'], template = 'plotly_dark')
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2001-02", "value": '01-02'},
                     {"label": "2002-03", "value": '02-03'},
                     {"label": "2003-04", "value": '03-04'},
                     {"label": "2004-05", "value": '04-05'},
                     {"label": "2005-06", "value": '05-06'},
                     {"label": "2006-07", "value": '06-07'},
                     {"label": "2007-08", "value": '07-08'},
                     {"label": "2008-09", "value": '08-09'}
                     ],
                 multi=False,
                 value='01-02',
                 style={'width': "40%"}
                 ),

    html.Div(id="output_container",children=[]),
    html.Br(),
    dcc.Graph(
        id='my_bee_map',
        figure={}

    )

])
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)
    dff = df[['State / UT',option_slctd]]
    fig = px.choropleth(df,
                    geojson= states,
                    featureidkey='properties.ST_NM',
                    locations="State / UT",
                    color = option_slctd,
                    color_continuous_scale='Reds',

                    )
    fig.update_geos(fitbounds="locations", visible=False)
    return container,fig

if __name__ == '__main__':
    app.run_server(debug=True)