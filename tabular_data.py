#! /usr/bin/env python3


import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def setosa_scatter():

    """
    Makes a scatter plot that shows the linear regression of sepal length and petal length of of the Iris setosa species


    """

dataframe = pd.read_csv("iris.csv")

#----------Scatter plot for setosa species-----------
if __name__ == '__main__':
    dataframe = pd.read_csv("iris.csv")
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
def versicolor_scatter():

    """
    Makes a scatter plot that shows the linear regression of sepal length and petal length of of the Iris versicolor species
    
    """
if __name__ == '__main__':
    dataframe = pd.read_csv("iris.csv")
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

def virginicia_scatter():
    """
    Makes a scatter plot that shows the linear regression of sepal length and petal length of of the Iris virginicia species
    
    """

if __name__ == '__main__':
    dataframe = pd.read_csv("iris.csv")
    virginica = dataframe[dataframe.species == "Iris_virginica"]
    x = virginica.petal_length_cm
    y = virginica.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("virginica_petal_v_sepal_length_regress.png")

exit()

#need to figure out how to make three separate graphs rather than one graph for all three data sets 
