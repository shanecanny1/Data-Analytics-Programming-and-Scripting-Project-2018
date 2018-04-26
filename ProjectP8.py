# Project 2018 Part 8 Assigning All Iris Classifications with Correct Data and Calulating Means

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

# Assigning Data to the Setosa Iris

SetosadataSepallength = data[0:50:,0] # Assigning the Setosa Iris Sepal Length data for 0 to row 50 in the First Column
SetosadataSepalwidth = data[0:50:,1] # Assigning the Setosa Iris Sepal Width data for 0 to row 50 in the Second Column
SetosadataPetallength = data[0:50:,2] # Assigning the Setosa Iris Petal Length data for 0 to row 50 in the Third Column
SetosadataPetalwidth = data[0:50:,3] # Assigning the Setosa Iris Pepal Width data for 0 to row 50 in the Fourth Column

# Assigning Data to the Versicolor Iris

VersicolordataSepallength = data[50:100:,0] # Assigning the Versicolor Iris Sepal Length data for 50 to row 100 in the First Column
VersicolordataSepalwidth = data[50:100:,1] # Assigning the Versicolor Iris Sepal Width data for 50 to row 100 in the Second Column
VersicolordataPetallength = data[50:100:,2] # Assigning the Versicolor Iris Petal Length data for 50 to row 100 in the Third Column
VersicolordataPetalwidth = data[50:100:,3] # Assigning the Versicolor Iris Pepal Width data for 50 to row 100 in the Fourth Column

# Assigning Data to the Virginica Iris

VirginicadataSepallength = data[100:150:,0] # Assigning the Virginica Iris Sepal Length data for 100 to row 150 in the First Column
VirginicadataSepalwidth = data[100:150:,1] # Assigning the Virginica Iris Sepal Width data for 100 to row 150 in the Second Column
VirginicadataPetallength = data[100:150:,2] # Assigning the Virginica Iris Petal Length data for 100 to row 150 in the Third Column
VirginicadataPetalwidth = data[100:150:,3] # Assigning the Virginica Iris Pepal Width data for 100 to row 150 in the Fourth Column

# Printing each divided data set

print(Setosadata)
print(Versicolor)
print(Virginica)

# Calculating the Mean Values of the Setosa Iris Data Set

print('The Mean of the SetosadataSepallength is',numpy.mean(SetosadataSepallength))
print('The Mean of the SetosadataSepalwidth is',numpy.mean(SetosadataSepalwidth))
print('The Mean of the SetosadataPetallength is',numpy.mean(SetosadataPetallength))
print('The Mean of the SetosadataPetalwidth is',numpy.mean(SetosadataPetalwidth))

# Calculating the Mean Values of the Versicolor Iris Data Set

print('The Mean of the VersicolordataSepallength is',numpy.mean(VersicolordataSepallength))
print('The Mean of the VersicolordataSepalwidth is',numpy.mean(VersicolordataSepalwidth))
print('The Mean of the VersicolordataPetallength is',numpy.mean(VersicolordataPetallength))
print('The Mean of the VersicolordataPetalwidth is',numpy.mean(VersicolordataPetalwidth))

# Calculating the Mean Values of the Virginica Iris Data Set

print('The Mean of the VirginicadataSepallength is',numpy.mean(VirginicadataSepallength))
print('The Mean of the VirginicadataSepalwidth is',numpy.mean(VirginicadataSepalwidth))
print('The Mean of the VirginicadataPetallength is',numpy.mean(VirginicadataPetallength))
print('The Mean of the VirginicadataPetalwidth is',numpy.mean(VirginicadataPetalwidth))