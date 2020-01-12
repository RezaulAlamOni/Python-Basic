print("Hello World ! using numpy")
# print 5 + 8
# for i in range(2, 30, 3):
#     print i
# for x in [0, 1, 2]:
#     pass
import numpy as np
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
my_list2 = [3,9,8,9]
my_lists = [my_list1, my_list2]

my_array2 = np.array(my_lists)
my_zerros_array = np.zeros(5)
print(np.ones([5,5]))
print(my_array2.shape)
print(my_array2.dtype)
print(my_zerros_array)
print(my_zerros_array.dtype)
print(np.eye(5))
print(np.arange(5))
print(np.arange(5,50,2))