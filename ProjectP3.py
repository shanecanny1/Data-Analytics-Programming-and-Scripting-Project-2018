# Project 2018 Part 3 Investigation of Importing Files and Numpy

# Import Numpy Library
import numpy

# Identify data set and set the delimiter of the data as the comma
data = numpy.genfromtxt('irisdata/iris.csv',delimiter=',')


# Assigning column of data a heading
Petallenght = data[:,0]
Petalwidth = data[:,1]
Sepallength = data[:,2]
Sepalwidth = data[:,3]

print (Petallenght)
print (Petalwidth)
print (Sepallength)
print (Sepalwidth)

