import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv") 
fig = px.bar(x = df["Mobile Brand"].tolist(),y = df["Sr.No"].tolist())
fig1 = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"]) 
fig.show()
fig1.show()