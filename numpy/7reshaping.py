#resshape
import numpy as np
ar1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#note while reshape total number of elements must be same
print(ar1.reshape((3,4)))#[[1,2,3,4],[5,7,6,8,],[9,10,11,12]]
print(ar1.reshape((4,3)))#[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(ar1.reshape((6,-1)))#1d length is calculated automatically
print(ar1.reshape((-1,6)))#meaing 2d lenght is auto calculated
print(ar1.reshape((-1,3,2)))#meaning 3d length is auto calculated





ar2 = np.array([[1],[2],[3],[4]])
print(ar2.reshape((-1,)))#or
print(ar2.reshape((4)))