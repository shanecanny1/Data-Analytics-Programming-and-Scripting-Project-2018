# Project 2018 Part 4 Calculating Data from each column using Numpy

# Import Numpy Library
import numpy

# Identify data set and set the delimiter of the data as the comma
data = numpy.genfromtxt('irisdata/iris.csv',delimiter=',')


# Assigning column of data a heading
Petallength = data[:,0]
Petalwidth = data[:,1]
Sepallength = data[:,2]
Sepalwidth = data[:,3]

# Test for Calculating the means of the column data
numpy.mean(Petallength)
numpy.mean(Petalwidth) 
numpy.mean(Sepallength)
numpy.mean(Sepalwidth) 

print("The Combined Petal Length Mean is",numpy.mean(Petallength))
print("The Combined Petal Width Mean is",numpy.mean(Petalwidth)) 
print("The Combined Sepal Length Mean is",numpy.mean(Sepallength)) 
print("The Combined Sepal Width Mean is",numpy.mean(Sepalwidth))  