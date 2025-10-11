import os;os.system('cls')
"""
HANDLING-THE-MISSING-VALUE 
"""
# Ist method to find the missing value
# n.isnan(array)
import numpy as n
ar=n.array([12,32,43,n.nan])
print(n.isnan(ar))
# replace the missing value with random value
# n.nan_to_num(arr,nan=)
print(n.nan_to_num(ar,nan=100))
# to terminate the infinite value
# n.isinf(array)
ar1=n.array([12,32,43,n.nan,n.inf])
inf = n.isinf(ar)
print(inf)
