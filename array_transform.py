from __future__ import division
import numpy as np

array_2d = np.arange(50).reshape((10,5))
# print(array_2d)
# print(array_2d.T)
# array_mu = np.dot(array_2d.T,array_2d)
# print(array_mu)

array_2d = np.arange(50).reshape((5,5,2))
print(array_2d)
array_3d = array_2d.transpose((1,0,2))
arr = np.array([[8,2,9,9]])
arr.swapaxes(0,1)
print(arr)
print(array_3d)
print(arr)


