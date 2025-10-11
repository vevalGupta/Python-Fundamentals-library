import os;os.system('cls')
"""
This is beginning of indexing and sliecing part within numpy
"""
import numpy as nd
it = nd.array([20,30,40])
print(it[1])
"""
slicing(the next part)
dividing  array into diffferent section
"""
sl = nd.array([10,20,30,40,50,60])
print(sl[1:4])
# slicing jump 
print(sl[:5:4])
# reversing the array
print(sl[::-1])
"""
Fancy indexing (the Sub part)
multiple selection available
"""
fI =nd.array([10,11,1,12,21])
print(fI[[0, 3, 2]])