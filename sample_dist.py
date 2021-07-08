import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
print("Population Mean -> ", population_mean)

def randomMean(counter):

    data_set = []

    for i in range(0,counter):
        number = random.randint(0,len(data)-1)
        value = data[number]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return mean

def setUp():
    meanList = []
    
    for i in range(0,1000):
        setOfMean = randomMean(30)
        meanList.append(setOfMean)

    mean = statistics.mean(meanList)
    print("Sample Mean -> ", mean)
    show_fig(meanList)

def show_fig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["Reading time"], show_hist=False)
    fig.show()

setUp()