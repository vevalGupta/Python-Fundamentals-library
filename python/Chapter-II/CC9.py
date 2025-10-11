import os;os.system('cls')
"""
BROADCASTING(PROBLEM-SOLVER)
"""
import numpy as np
# problem (of-discount-given-list)
n =np.array([[10,340,145,330]])
print(f"price list:{n}. ")
discount=10
final_list=[]
for i in n:
    cal_dis=i-(i*discount/100)
    final_list.append(cal_dis)
    
print(final_list)
"""
but all the loop involved to perform operation
take a lot of time the easier way is broadcasting  
"""