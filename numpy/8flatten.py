import numpy as np

#flatten is used to conver 2d and 3d array to 1d
ar1 = np.array([[1,2],[3,4],[5,6]])
print(ar1.flatten())#[1 2 3 4 5 6]

ar2 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(ar2.flatten())#[1 2 3 4 5 6 7 8]