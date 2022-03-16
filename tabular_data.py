#! /usr/bin/env python3

#Need to make it modular
import sys
import pandas as pd
import matplotlib.pyplot as plt

def ________
"""
Makes a scatter plot that shows the linear regression of sepal length and petal length of various Iris species.

"""


dataframe = pd.read_csv("iris.csv")
#Scatter plot for setosa species
setosa = dataframe[dataframe.species == "Iris_setosa"]
plt.scatter(setosa.petal_length_cm, setosa.sepal_length_cm)
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.savefig("setosa_petal_v_sepal_length.png")



versicolor = dataframe[dataframe.species == "Iris_versicolor"]
virginicia = dataframe[dataframe.species == "Iris_virginicia"]


