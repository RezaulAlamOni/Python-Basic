# from __future__ import division
import numpy as np
array = np.arange(5)
np.save('myArray1',array)
array = np.arange(10)
array2 = np.load('myArray1.npy')
print(array2)
print(array)
np.savez('ziparray.npz',x=array,y=array2)
zip_array = np.load('ziparray.npz')
print(zip_array['y'])
arr = np.array([[1,2,3],[1,1,3]])
np.savetxt('mynptext.txt',arr,delimiter=',')
text =  np.loadtxt('mynptext.txt',delimiter=',')
print(text)