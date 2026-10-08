#note all 1d array length must be same
#note all 2d array length must be same


import numpy as np

a1= np.array([1,2,3])#1d
a2 = np.array([[1,2,3],[4,5,6]])#2d


print(a1)
print(a2)

#shape
print(a1.shape)#(3,) #[1,2,3]
print(a2.shape)#(2,3) [[...],[...],[...]]


#dtype => it gives types of array elemnets
print(a1.dtype)

#1d numpy => vector
#2d numpy => matrix
#3d,4d... numpy => tensor