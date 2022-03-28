import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import calendar

import plotly.express as px
import plotly.graph_objects as go

import datamodel
order = datamodel.get_data()
df_year = datamodel.get_year()
df_month = datamodel.get_month()

fig_employee = px.bar(order, 
    x='emp_name', y='total', 
    color='type', text='total', title='SALES BY EMPLOYEE',
    color_discrete_sequence=["darkred", "green"],
    template='plotly_dark',
    hover_data=[],
    labels={'total':'Total sales', 'emp_name':'Employee', 'type':'Product Type', 'font': {'color': 'white'}})
fig_employee.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_employee.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

fig_products = px.bar(order, 
    x='productname', y='total', 
    color='type', text='total', title='SALES BY PRODUCTS',
    color_discrete_sequence=["darkred", "green"],
    template='plotly_dark',
    hover_data=[],
    labels={'total':'Total sales', 'productname':'Product', 'type':'Product Type'})
fig_products.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_products.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

dash_app = dash.Dash(__name__)
app = dash_app.server

dash_app.layout = html.Div(style={'backgroundColor':'lightgrey'},
    children=[
        html.Div(className='row',
                children=[
                    html.Div(
                            children=[
                                dcc.Graph(id="sales_employee", figure=fig_employee),
                                dcc.Graph(id="sales_product", figure=fig_products)])
                            ]
                    ),
                ]
        )
if __name__ == '__main__':
    dash_app.run_server(debug=True)
