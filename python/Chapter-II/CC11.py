import os;os.system('cls')
"""
BROADCASTING-RULES
"""
# 1.matching Dimension
import numpy as s
ar1=s.array([12,34,65])
ar2=s.array([3,6,4])
print(ar1+ar2)#both array should be in same shape
# 2.Expanding single element
print(ar2+10)
# all the operation can be perform on array with single value
# 3.incampatible shape
arr1=s.array([12,34,45])
arr2=s.array([[12,43,54,65],[23,56,7,9]])
print(arr1+arr2)
# this cause array to be in incampatible shape