import os;os.system('cls')
"""
SUB-PLOTTING
  /         \
subplot()  subplots()
  |           |
  similar     easier way
  for 
  few plots
"""
# I. subplot
import matplotlib.pyplot as plt
# subplot 1
# syntax - plt.subplot(nrows,ncols,index)
plt.subplot(1, 3, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Plot 1")
# subplot 2
plt.subplot(2, 3, 2)
plt.bar([1, 2, 3], [3, 4, 5])
plt.title("Plot 2")
# subplot 3
plt.subplot(1, 3, 3)
plt.scatter([1, 2, 3], [6, 5, 4])
plt.title("Plot 3")

plt.tight_layout()
plt.show()
# II. subplots()
# syntax -fig, axes = plt.subplots(nrow,ncols,figsize=(width,height))
fig, axes = plt.subplots(2, 2)
# subplots1
axes[0, 0].plot([1, 2, 3], [1, 2, 3])
axes[0, 0].set_title("Top Left")
# subplots2
axes[1, 1].bar([1, 2, 3], [3, 2, 1])
axes[1, 1].set_title("Bottom Right")
plt.suptitle("comparison between 2 graphs")
# it make the subplot more presentable
plt.tight_layout()
plt.show()
