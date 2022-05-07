import csv
import pandas as pd
import plotly.figure_factory as ff


df=pd.read_csv("data.csv")
rating=df["Avg Rating"].tolist()
fig=ff.create_distplot([rating],["rating"],show_hist=False)
fig.show()
