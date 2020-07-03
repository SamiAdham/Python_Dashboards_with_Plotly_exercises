import plotly.offline as pyo
import plotly.graph_objs as go 

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data=[go.Box(y=snodgrass,name='Snodgrass',boxpoints='outliers'),
      go.Box(y=twain,name='Twain',boxpoints='outliers') ]
pyo.plot(data)