import os;os.system('cls')
"""
BROADCASTING(SOLUTION)
"""
import numpy as np
n =np.array([[10,340,145,330]])
print(f"price list:{n}. ")
discount=10
final_list=[]
prefinal=n-(n*discount/100)
final_list.append(prefinal)
print(final_list)