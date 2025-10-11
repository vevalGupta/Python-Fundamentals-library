import os;os.system("cls")
list=[3,5, 6,98]
print(list)
import numpy as np
# numpy list
numpy_list=np.array([3,6,4,30,78])
print(numpy_list)# numpy is more effeicent in storeage way
# forming a matrix
# Many way of creating array
# 1.coverting from other pyhton structure(like list, etc)-> list to array
matrix = np.array([[1,5,7],
                [5,8,9],
                [9,1,7]])
print(matrix)
# to convert list into array
lis1 =[54,76,24,76,33]
arr=np.array(lis1)
print(arr)
print(matrix.ndim) # one of the attribute from ndarray
