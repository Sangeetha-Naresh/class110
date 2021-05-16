import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean of raw data:- ",mean)
print("std_deviation of raw data:- ",std_deviation)


#code to show the plot of raw data

fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()