import os;os.system('cls')
# Array modification
import numpy as n
# 1.insertion
ar=n.array([2,54,65,7])
ins = n.insert(ar,2,[12,32,25],axis=0)
print(ins)
# 2. append
ap = n.append(ar, [21,23])
print(ap)
# 3. concatenate 
ar1=n.array([21,64,66])
co=n.concatenate((ar,ar1),axis=0)
print(co)
# 4.removal
re =n.delete(ar1,1,axis=None)
print(re)
# 5.stacking
ar2=n.array([3,1,44])
print(n.vstack((ar1,ar2)))# for vertical stack
print(n.hstack((ar1,ar2)))# for horizontal stack
# 6. splitting
spl_arr=n.array([12,4,3,53,54,22,64,9])
print(n.split(spl_arr, 2))#for equal part 
print(n.hsplit(spl_arr, 2))#for horizontal part 
print(n.vsplit(spl_arr, 2))#for vertical part 
