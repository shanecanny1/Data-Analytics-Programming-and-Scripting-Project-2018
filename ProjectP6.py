# Project 2018 Part  Generating Scatter Plots Using Matplotlib.pyplot

# Import Numpy Library
import numpy

# Import Matplotlib Library for Generating Graphs
import matplotlib.pyplot as plt

# Identify data set and set the delimiter of the data as the comma
data = numpy.genfromtxt('irisdata/iris.csv',delimiter=',')


# Assigning column of data a heading
Petallength = data[:,0]
Petalwidth = data[:,1]
Sepallength = data[:,2]
Sepalwidth = data[:,3]

# Assigning x and y values for the scatter plot
x = Sepallength
y = Sepalwidth
# Test for Generating a Scatter Plot for Sepal Data
plt.scatter(x, y,color='red', alpha=0.05)
plt.title("Sepal Data Scatter Plot")
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()