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

#code to find mean and std deviation of 100 data points
dataset = []
for i in range(0, 100):
     random_index= random.randint(0,len(data))
     value = data[random_index]
     dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean of sample data:- ",mean)
print("std_deviation of sample data:- ",std_deviation)