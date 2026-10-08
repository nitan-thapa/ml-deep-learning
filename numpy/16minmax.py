#min max, sum ,mean
#For one dimension

ar1 = np.array([10,11,12,1])

#minimum, maximum, sum, mean,
print(ar1.min())
print(ar1.max())
print(ar1.sum())
print(ar1.mean())

#argmin, argmax
print(ar1.argmax())#give index of max value
print(ar1.argmin())#give index of min value




import numpy as np
ar1=np.array([[1,2,3],[4,5,6],[7,8,9]])



""" 
[1,2,3]
[4,5,6]
[7,8,9]

 """
print(ar1.min())#1 (gives the minimum value from all element)
print(ar1.max())#9
print(ar1.min(axis=1))#[1,4,7] (gives the minimum value from each row)
print(ar1.max(axis=0))#[7,8,9] (gives the maximum value from each column)
print(ar1.sum())
print(ar1.sum(axis=1))#[6,15,24] sum of each row
print(ar1.sum(axis=0))#[12,15,18] sum of each column
print(ar1.prod())
print(ar1.prod(axis=1))
print(ar1.prod(axis=0))

arr = np.array([1, 2, 3, 4, 5])
print(ar1.mean())
ar1 = np.array([[4,2], [4,6]])

""" 
4  2
4  6 

"""
print(ar1.mean())


print(ar1.mean(axis=1))
print(ar1.mean(axis=0))
