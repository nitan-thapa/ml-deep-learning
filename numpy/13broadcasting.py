""" Broadcasting means NumPy automatically 
adjusts smaller arrays so that arithmetic operations 
can be performed with larger arrays.
 """


""" 
Broadcastin is possible if 
rules of broadcasting
      add 1 to the missing dimension form left 
      compare if every pair is compatible 
         pair are compatable if the pairs are same  and if one of the pair is 1 
valid broadcasting 
(3, 4) (4,)
    (3,4), (1,4)  adding 1 from left
        here 4,4 both are same
        and 3,1 one is 1
        thus valid

not valid broadcasting       
(3, 4)  , (3,)
    (3,4), (1,3)
        here 4,3 are not same  (soe broadcast is not possible)

 """

import numpy as np
ar2=np.array([10,11,12,13])
# +,-,*,/
print(ar2)#[10,11,12,13]
print(ar2+10)#[20,21,22,23]
print(ar2-10)#[0,1,2,3]
print(ar2*2)#[20,22,24,26]


ar1 = np.array([[1,2],[3,4]])
ar2 = np.array([[1,1]])



""" 
1 2
3 4

1 1
1 1

 """

""" 
2 3
4 5
"""

print (ar1+ar2)


ar1 = np.array([1,2,3])
ar2 =np.array([3])
print(ar1+ar2)


