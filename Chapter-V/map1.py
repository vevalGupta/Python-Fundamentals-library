import os ;os.system('cls')
"""
Matplotlib Module
(used for data visualization)
"""
import matplotlib.pyplot as plt
x_axis =[1,2,3,4,5]
y_axis =[10,20,15,20,40]
plt.plot(x_axis,y_axis)
plt.title("first plot")# used to title in plot
plt.xlabel("days")# define what x axis is used 
plt.ylabel("Increasing value")
plt.show()#used to show plot


# you can plot as many graph within 1 code
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
plt.show()