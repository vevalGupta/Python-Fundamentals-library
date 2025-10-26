import os;os.system('cls')
"""
Saving figures
# can be done by savefig()
"""
import matplotlib.pyplot as plt
# importing old data from map1.py part-2
x=['mon','tues','wed','thur','fri']
y=[2000,1000,5000,2500,1500]
plt.plot(x,y,linestyle="--")
plt.grid()# provide axis's value
plt.xlabel("Days")
plt.ylim(0,8000)
plt.ylabel("Salary amount")
plt.title("Employees Salary")
plt.legend(loc ='upper left')
plt.xticks(['mon','tues','wed','thur','fri'],['M','T','W','TH','F'])# Used to replace x value with keyword
plt.savefig('Plot.png',dpi=300,bbox_inches="tight")
plt.show()