#+,-,*.. of two matrix
import numpy as np
ar1 = np.array([1,2,3,4])
ar2 = np.array([1,1,1,1])
#to perform +, -, *, / ,,, it must have same shape
print(ar1+ar2)
print(ar1-ar2)
print(ar1*ar2)
print(ar1/ar2)


# for 2d array
ar2 = np.array([ [1,2], [3,4]])
ar3 = np.array([ [1,1],[0,0]])

print(ar2+ar3)