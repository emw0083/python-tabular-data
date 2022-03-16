#! /usr/bin/env python3

#Need to make it modular
import sys
import pandas as pd
import matplotlib.pyplot as plt

def ________
"""
Makes a scatter plot that shows the linear regression of sepal length and petal length of various Iris species

"""


dataframe = pd.read_csv("iris.csv")

#Scatter plot for setosa species
setosa = dataframe[dataframe.species == "Iris_setosa"]





versicolor = dataframe[dataframe.species == "Iris_versicolor"]
virginicia = dataframe[dataframe.species == "Iris_virginicia"]


