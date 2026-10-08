#creting numpy arrays
import numpy as np

#creating zeros element
#1d array
print(np.zeros((3,)))#[0,0,0]
#2d array
print(np.zeros((3,2)))#[[0,0],[0,0],[0,0]]

#creating ones element
#1d array
print(np.ones((3,)))#[1,1,1]
#2d array
print(np.ones((3,2)))#[[1,1],[1,1],[1,1]]

#creating random integers of given range
ar1=np.random.randint(1,7,(10,))
#creates number from 1 to 7 but 1 is inclusive and 7 is exclusive
# (10,) means one dimension array of length 10
print(ar1)

#creating random number from 0 to 1 here 0 is inclusive and 1 is exclusive
#note randdoes not have (())
print(np.random.rand(2,))#generate one dimension array of length 2
print(np.random.rand(2,3))
print(np.random.rand(2,2,3))



#generate same random number using seed 
print(np.random.randint(1,7,(6)))
#np.random.seed(any number) (any number)is not imporant
np.random.seed(2) #seed is used to generate same random number every time,
print(np.random.randint(1,7,(6)))






