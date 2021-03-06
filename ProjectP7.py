# Project 2018 Part 7 Dividing up Data Set to Iris Class and Assigning Data to Column Headings for Future Analysis

# Import Numpy Library
import numpy

# Import Panda Lbrary
import pandas as pd 

# Import Matplotlib Library for Generating Graphs
import matplotlib.pyplot as plt

# Assigning Headings to Each Column
col_Names=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Class"] # Assigning Headings to Each Colunm
data = pd.read_csv('irisdata/iris.csv',names=col_Names) # Assigning the data set to the pandas library with each column labeled
Setosadata = data.iloc[0:50] # Assigning Setosadata to rows 0 to 49
Versicolor = data.iloc [50:100] # Assigning Versicolor to rows 50 to 100
Virginica = data.iloc [100:150] # Assigning Virginica to rows 100 to 150

data = numpy.genfromtxt('irisdata/iris.csv',delimiter=',') # Assigning Data to numpy library 

SetosadataSepallength = data[0:50:,0] # Assigning the Setos Iris Sepal Length data for 0 to row 50 in the First Column
SetosadataSepalwidth = data[0:50:,1] # Assigning the Setos Iris Sepal Width data for 0 to row 50 in the Second Column
SetosadataPetallength = data[0:50:,2] # Assigning the Setos Iris Petal Length data for 0 to row 50 in the Third Column
SetosadataPetalwidth = data[0:50:,3] # Assigning the Setos Iris Pepal Width data for 0 to row 50 in the Fourth Column
print(Setosadata)
print(Versicolor)
print(Virginica)
print('The Mean of the SetosadataSepallength is',numpy.mean(SetosadataSepallength))
print('The Mean of the SetosadataSepalwidth is',numpy.mean(SetosadataSepalwidth))
print('The Mean of the SetosadataPetallength is',numpy.mean(SetosadataPetallength))
print('The Mean of the SetosadataPetalwidth is',numpy.mean(SetosadataPetalwidth))