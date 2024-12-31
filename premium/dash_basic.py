
#https://dash.plotly.com/tutorial?utm_medium=graphing_libraries&utm_content=python_footer&_gl=1*uo1zsl*_gcl_au*MTc2MjQ4MTkzMy4xNzMyNTA2MzI3*_ga*MTcyNDMyNDcwNS4xNzMyNTA2MzI5*_ga_6G7EE0JNSC*MTczMjUxNTUxOS4yLjAuMTczMjUxNTUxOS42MC4wLjA.
from dash import Dash,html,dash_table,dcc
import pandas as pd
import plotly.express as px

app = Dash()

#app.layout = [html.Div(children='Hello Praveen')]

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
app.layout = [html.Div(children='My First Dash table'),
              dash_table.DataTable(data = df.to_dict('records'),page_size=10 ),
              dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
              dcc.Graph(figure=px.pie(df, values='pop', names='continent', hole = .3, color_discrete_sequence=px.colors.sequential.RdBu,title='Population of European continent'))
              ]

if __name__ == '__main__':
    app.run(debug=True)