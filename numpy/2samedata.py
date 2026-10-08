#numpy array can only store same type of element
import numpy as np
ar1 = np.array([1, False, "nitan"])
print(ar1)#['1' 'False' 'nitan']

ar2 = np.array([1,False])
print(ar2)#[1,0]

ar3  = np.array([1,3.1])
print(ar3)#[1. 3.1]


""" 
difference between python list and numpy array
python list
    can store element of different type
    slower
numpy array
    store element of same type
    faster

 """


print(np.array([[1],[2]]))#valid  each element has 1d array
print(np.array([[1,2],[3,4]]))#valid each elemnet has 2d array
# print(np.array([[1],[1,2]]))#not valid  one elemnt is 1d and another is 2d