"""
A basic bar chart showing the total number of
2018 Winter Olympics Medals won by Country.
Note that the source .csv file is one
directory level higher than this script file.
"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# read a .csv file into a pandas DataFrame:
df = pd.read_csv('../2018WinterOlympics.csv')

data = [go.Bar(
            x=df['NOC'],  # NOC stands for National Olympic Committee
            y=df['Total']
    )]
layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar1.html')
