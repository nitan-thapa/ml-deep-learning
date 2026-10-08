
#hstack and vstack  and column_stack 


#for 2d array
# hstack and column_stack for 2d is same
# vstack and row_stack for 2d is same

import numpy as np


ar1 = np.array([[1,2,3],[4,5,6]])
ar2 = np.array([[7,8,9],[10,11,12]])


""" 
1 2 3
4 5 6

7 8 9
10 11 12

"""

#after h

print(np.hstack((ar1,ar2)))
""" 
1 2 3 7 8 9
4 5 6 10 11 12

"""
#after v
print(np.vstack((ar1,ar2)))

""" 
1 2 3
4 5 6
7 8 9
10 11 12

"""



#column_stack   
#difference between hstack and column_stack likes in onde dimention array
#column_stack takes 1d array as column 
ar1 = np.array([[1,2,3],[4,5,6]])
""" 
1 2 3
4 5 6
"""

#adding a column (#column_stack takes 1d array as column )
ar2 = np.array([0,0])
print(np.column_stack((ar1,ar2)))
""" 
1 2 3 0
4 5 6 0
"""


#adding a row
ar2 = np.array([0,0,0])
print(np.vstack((ar1,ar2)))
""" 
1 2 3
4 5 6
0 0 0
"""


"""  
note vstack and column stack support one dimention array as well

"""


