import numpy as np
#filter 1d array
ar2=np.array([10,11,12,13])

print(ar2[ar2>10])#[11,12,13]
print(ar2[ar2<=10])#[10]
print(ar2[ar2%2==0])#[10,12]


import numpy as np
ages = np.array([20,30,18,25,17])


#ages between 20 to 30  (use ())
print(ages[(ages>=20) & (ages<=30)])


#ages 20 ,30
print(ages[(ages==20)|(ages==30)])

#age not equal to 30
print(ages[~(ages==30)])


