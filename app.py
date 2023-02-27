import dash
from dash import Dash,html, dcc,Input,Output
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json
with urlopen("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson") as response:
    states = json.load(response)
df = pd.read_csv('Statewise_income.csv.csv')
df['States_Union Territories'] = df['States_Union Territories'].replace('Jammu and Kashmir','Jammu & Kashmir')
df.loc[len(df.index)] = ['Ladakh',0,0,0,0,0,0,0,0,0,0,0,0]
app = Dash(__name__)


#fig2 = px.bar(df, x = 'States_Union Territories', y =['2000-01-INC','2011-12-INC'], template = 'plotly_dark')
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2001", "value": '2000-01-INC'},
                     {"label": "2011", "value": '2011-12-INC'},
                     ],
                 multi=False,
                 value='2000-01-INC',
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
    dff = df[['States_Union Territories',option_slctd]]
    fig = px.choropleth(df,
                    geojson= states,
                    featureidkey='properties.ST_NM',
                    locations="States_Union Territories",
                    color = option_slctd,
                    color_continuous_scale='Blues',

                    )
    fig.update_geos(fitbounds="locations", visible=False)
    return container,fig

if __name__ == '__main__':
    app.run_server(debug=True)