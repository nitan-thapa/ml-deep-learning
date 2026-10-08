import numpy as np
ar1=np.array([10,11,12,13])
ar2 = ar1.copy() 
ar3=ar1

ar1[1]=1111
print(ar1)#[10, 1111, 12, 13]
print(ar2)#[10, 11, 12, 13]
print(ar3)#[10, 1111, 12, 13]

# ar2  = ar1[:]  slicing doent do copy