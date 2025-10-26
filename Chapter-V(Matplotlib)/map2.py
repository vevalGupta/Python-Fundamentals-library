import os;os.system('cls')
"""
Type of plots
"""
import matplotlib.pyplot as plt
# 1.Bar Graph
product =['momos','pizza','burger','cold coffee']
sale =[500,1500,1000,800]
plt.barh(product,sale,color='blue')# used for horizontal bar graph
plt.title("bar Graph")
plt.xlabel("product available:" )
plt.ylabel("product's total sale:" )
plt.show()
# 2.pie chart
location =["Delhi","dehradun","up","bihar","j&k"]
time_visited=['5','10','7','2','11']
list1 =["blue","green","red","pink","cyan"]
plt.pie(time_visited,labels=location,colors=list1,autopct="%1.1f%%")
plt.title("Places i have visited")
plt.show()
# 3.histogram
score =[9,11,5,6,12,3,9]
plt.hist(score,bins=5,color="green",label="no. of score they have achieved",edgecolor="black")
plt.grid()
plt.show()