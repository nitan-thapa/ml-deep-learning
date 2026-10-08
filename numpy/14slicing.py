#slicing array

import numpy as np


#slicing of 1d
#ar1[start:end:step]#does not include end index
ar1=np.array([1,2,3,4,5,6])
print(ar1[::-1])

#slicing of 2d array
ar1 = np.array([
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
 ])

#gettin row 
print(ar1[0])#[1,2,3]
print(ar1[1])#[4,5,6]

#getting single elemnet 
#printing 2 
print(ar1[0,1])#row, column
#printing 9
print(ar1[2,2])





#getting column 
print(ar1[:,0])#[1,4,7,10]
print(ar1[:,1])#[2,5,8,11]

#gettin  2 and 3 column 
print (ar1[:,1:3])



#gteting slice person
#printing [[8,9],[11,12]]
print(ar1[2: ,1:])


