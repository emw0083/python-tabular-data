#! /usr/bin/env python3

#Need to make it modular
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


#def ________
"""
Makes a scatter plot that shows the linear regression of sepal length and petal length of various Iris species.

"""


dataframe = pd.read_csv("iris.csv")
#----------Scatter plot for setosa species-----------
setosa = dataframe[dataframe.species == "Iris_setosa"]
x = setosa.petal_length_cm
y = setosa.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("setosa_petal_v_sepal_length_regress.png")


#---------Scatter plot for versicolor species-------------
versicolor = dataframe[dataframe.species == "Iris_versicolor"]
x = versicolor.petal_length_cm
y = versicolor.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("versicolor_petal_v_sepal_length_regress.png")

#---------Scatter plot for virginicia species-------------
virginicia = dataframe[dataframe.species == "Iris_virginicia"]
x = virginicia.petal_length_cm
y = virginicia.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("virginicia_petal_v_sepal_length_regress.png")
