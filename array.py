from __future__ import division
import numpy as np

# div = 5/2
# print(div)
#
array_2d = np.array([[1,5,8],[2,9,5],[85,6,3]])
print(array_2d)
# print(array_2d[0])
# print(array_2d[1][2])
# print(array_2d[:1])
print(array_2d[:2,1:])
print(array_2d[:2])
array_2d = np.zeros((10,10))

print(array_2d)
array_length = array_2d.shape[1]
print(array_length)
for i in range(array_length):
    array_2d[i] = 1
for i in range(array_length):
    array_2d[i] = i

print(array_2d)
print(array_2d[[9,2,8,]])

# arr = np.arange(0,11)
#
# print(arr)
# print(arr[1:3])
# arr[1:3] = 100
# print(arr[3])
# print(arr)
# array_copy = arr.copy();
# print(array_copy)


