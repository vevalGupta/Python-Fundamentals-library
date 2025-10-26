import os;os.system('cls')
"""
Scatter plot
"""
import matplotlib.pyplot as plt
hour = [1,2,3,4,5,6,7]# in hours
score =[60,71,72,80,85,88,90]
plt.scatter(hour,score,color="red",label="hours of study",marker="*")# always remember to write marker type
plt.xlabel("hours")
plt.ylabel("marks scored")
plt.grid()# use grid for proper understanding of position
plt.show()