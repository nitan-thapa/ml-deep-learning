
import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
# (m*n).(n*p)=m*p  note the inner dimension must be same 


""" 

 a b      e f    ae+bd  af+bh
 c d      g h    ce+dg  cf+dh

 """
#dot product 
print(A@B)#or
print(np.dot(A,B))#or
print(A.dot(B))



#traspose of a matrix  (row is convert to column and column is convert to row)
A=np.array([[1,2],[3,4]])
print(A.T)


""" 
a b     a  c
c d     b  d

 """
