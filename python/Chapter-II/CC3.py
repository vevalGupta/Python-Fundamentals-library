import os;os.system('cls')
# array attribute
import numpy as n
arr = n.array([[2,3,4],[5,6,7]])
# 1.attribute is shape
print(arr.shape)
# 2. attribute is size 
print(arr.size)
# 3. attribute is ndim
arr2 = n.array([[3,5,6],[6,78,5]]) 
print(arr2.ndim)
# 4.attribute is dtype 
print(arr2.dtype)
# 5.attribute is astype
print(arr2.astype(str))
