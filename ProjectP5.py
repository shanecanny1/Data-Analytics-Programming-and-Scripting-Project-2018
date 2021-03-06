# Project 2018 Part 5 Generating Histograms Using Matplotlib.pyplot

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

# Test for Generating a Histogram Plot for Petal Length
plt.hist(Petallength)
plt.title("Petal Length")
plt.xlabel("Length")
plt.ylabel("Qty")
plt.show()