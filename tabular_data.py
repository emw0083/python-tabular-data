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
#----------Scatter plot for setosa species-----------
setosa = dataframe[dataframe.species == "Iris_setosa"]
plt.scatter(setosa.petal_length_cm, setosa.sepal_length_cm)
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.savefig("setosa_petal_v_sepal_length.png")

#---------Scatter plot for versicolor species-------------
versicolor = dataframe[dataframe.species == "Iris_versicolor"]
plt.scatter(versicolor.petal_length_cm, versicolor.sepal_length_cm)
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.savefig("versicolor_petal_v_sepal_length.png")

#---------Scatter plot for virginicia species-------------
virginicia = dataframe[dataframe.species == "Iris_virginicia"]
plt.scatter(virginicia.petal_length_cm, virginicia.sepal_length_cm)
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.savefig("virginicia_petal_v_sepal_length.png")

