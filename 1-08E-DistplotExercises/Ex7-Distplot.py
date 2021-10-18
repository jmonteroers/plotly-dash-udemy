#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff


# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')

# Define the traces
flowers = ['Iris-setosa','Iris-versicolor','Iris-virginica']
traces = [
 df[df["class"]==flower]["petal_length"] for flower in flowers
]

group_labels = [
    " ".join([word.capitalize() for word in flower.split('-')])
    for flower in flowers
]



# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(traces, group_labels)
pyo.plot(fig, filename="my_solution7.html")
