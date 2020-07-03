import plotly.offline as pyo
import plotly.graph_objs as go 

import pandas as pd 

df=pd.read_csv('data/mpg.csv')

data=[go.Histogram(x=df['mpg'])]

layout=go.Layout(title='MPG count')

fig=go.Figure(data,layout)
pyo.plot(fig)