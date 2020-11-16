import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# App layout
app.layout = html.Div([

    html.H1("World map", style={'text-align': 'center'}),

    dcc.Slider(
        id="slider",
        min=1800,
        max=2100,
        value=2020,
        marks={i: '{}'.format(i) for i in range(1800, 2101, 30)}
    ),
    html.Div(id='year_text', children=[], style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_data",
                 options=[
                     {"label": 'World Population', "value": 'World population'},
                     {"label": 'Life Expectancy', "value": 'Life Expectancy'},
                     {"label": 'Internet Users (%)', "value": 'Internet Users'},  # %of county pop
                     {"label": 'Water Access', "value": 'Water Access'},  # overall access %
                     {"label": 'Average Income', "value": 'Average Income'},
                     {"label": 'Military Expenditure (% of GDP)', "value": 'Military Expenditure (% of GDP)'}],
                 multi=False,
                 value='World population',
                 style={'width': "40%",
                        'margin-left': '20px',
                        'margin-top': '20px'}
                 ),

    dcc.Graph(id='world_pop_map', figure={}),
    html.Br()
], style={'backgroundColor': 'white'})


# Connect Plotly graphs w/ Dash comps
# Import and prep data based on input
@app.callback(
    [Output(component_id='slider', component_property='min'),
     Output(component_id='slider', component_property='max'),
     Output(component_id='slider', component_property='step'),
     Output(component_id='slider', component_property='marks'),
     Output(component_id='slider', component_property='value')],
    [Input(component_id='slct_data', component_property='value')])
def update_slider(data_selected):
    if data_selected == 'World population':  # 1800-2100
        minimum = 1800
        maximum = 2100
        value = 2020
        step = 1
        marks = {i: '{}'.format(i) for i in range(1800, 2101, 30)}
    elif data_selected == 'Life Expectancy':  # 1800-2100
        minimum = 1800
        maximum = 2100
        value = 2020
        step = 1
        marks = {i: '{}'.format(i) for i in range(1800, 2101, 30)}
    elif data_selected == 'Internet Users':  # 1960-2018
        minimum = 1990
        maximum = 2018
        value = 1990
        step = 1
        marks = {i: '{}'.format(i) for i in range(1990, 2019, 2)}
    elif data_selected == 'Water Access':  # 2000-2017
        minimum = 2000
        maximum = 2017
        value = 2000
        step = 1
        marks = {i: '{}'.format(i) for i in range(2000, 2018, 2)}
    elif data_selected == 'Average Income':  # 1800-2040
        minimum = 1800
        maximum = 2040
        value = 2020
        step = 1
        marks = {i: '{}'.format(i) for i in range(1800, 2041, 20)}
    elif data_selected == 'Military Expenditure (% of GDP)':  # 1960-2018
        minimum = 1960
        maximum = 2018
        value = 1960
        step = 1
        marks = {i: '{}'.format(i) for i in range(1960, 2019, 5)}

    return minimum, maximum, step, marks, value


@app.callback(
    [Output(component_id='year_text', component_property='children'),
     Output(component_id='world_pop_map', component_property='figure')],
    [Input(component_id='slct_data', component_property='value'),
     Input(component_id="slider", component_property='value')]
)
def update_graph(data_selected, year_selected):
    text = f"Year selected: {year_selected}"

    if data_selected == 'World population':
        df = pd.read_csv("data/population_total.csv")
        clr_cnt_scl = px.colors.sequential.deep
        range_clr_max = 500000000
        range_clr_min = 10000000
    elif data_selected == 'Life Expectancy':
        df = pd.read_csv("data/life_expectancy_years.csv")
        clr_cnt_scl = px.colors.sequential.Plasma
        range_clr_max = None
        range_clr_min = None
    elif data_selected == 'Internet Users':
        df = pd.read_csv("data/internet_users.csv")
        clr_cnt_scl = px.colors.sequential.deep
        range_clr_max = None
        range_clr_min = None
    elif data_selected == 'Water Access':
        df = pd.read_csv("data/at_least_basic_water_source_overall_access_percent.csv")
        clr_cnt_scl = px.colors.sequential.Cividis
        range_clr_max = None
        range_clr_min = None
    elif data_selected == 'Average Income':
        df = pd.read_csv("data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        clr_cnt_scl = px.colors.sequential.algae
        range_clr_max = None
        range_clr_min = None
    elif data_selected == 'Military Expenditure (% of GDP)':
        df = pd.read_csv("data/military_expenditure_percent_of_gdp.csv")
        clr_cnt_scl = px.colors.sequential.amp
        range_clr_max = 0.08
        range_clr_min = 0

    fig = px.choropleth(
        height=600,
        data_frame=df,
        locationmode='country names',
        locations="country",
        color=f"{year_selected}",
        scope="world",
        hover_name=f"{year_selected}",
        hover_data=['country', f"{year_selected}"],
        range_color=(range_clr_min, range_clr_max),
        color_continuous_scale=clr_cnt_scl
    )

    return text, fig


if __name__ == '__main__':
    app.title = "World map"
    app.run_server(debug=True)
