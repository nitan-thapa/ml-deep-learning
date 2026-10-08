import numpy as np



#filter 2d array
#2d array

#    id, math , science

data = np.array([
    [1, 80, 75],
    [2, 65, 90],
    [3, 95, 88],
    [4, 45, 60],
    [5, 72, 55]
])

#filtering rows
#find those students rows who score more than 80 in math#find those students rows who score more than 80 in math

print(data[data[:,1]>=80])

#find those students whose score in math and sciens is more than 80%
print(data[(data[:,1]>=80) &(data[:,2]>=80)])





