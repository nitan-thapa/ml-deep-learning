#for insert, apend, delete
#axis=0 for row
#axis=1 for column

#insert for 2d array

import numpy as np 
# np.insert(ar1,index,value,axis)
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(np.insert(A,0,[0,0,0], axis=0))#add one row at 0th index
print(np.insert(A,0,[0,0,0],axis=1))#add one column at 0th index


#delete for 2d array
print(np.delete(A,0, axis=0))#delete one row at 0th index
print(np.delete(A,0, axis=1))#delete one column at 0th index

#np.append(ar1,index,value,axis) #it add value at last
print(np.append(A,[[10,11,12]], axis=0))#add one row at last
print(np.append(A,[[10],[11],[12]], axis=1))#add one column at last






