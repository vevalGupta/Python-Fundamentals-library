__import__('os').system('cls' if __import__('os').name == 'nt' else 'clear')
# tuples
T =(1,4,5,6)
print(type(T))
# method
# 1. count()
count = T.count(5)
print(count)
# 2. index
indx = T.index(6)
print(indx)
# operation 
# 1. check whether tuple contain that value
print(5 in T) 
print(7 in T) 
# repeat the tuple 
repeat = T*2
print(repeat)
# return length
print(len(T))