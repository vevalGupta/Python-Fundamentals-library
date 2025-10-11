__import__('os').system('cls' if __import__('os').name == 'nt' else 'clear')
# list
list1 =["veval", "yash" , 6, 102.4, "sparsh"]
print(list1)
print(list1[0])
list1[0]= "harsh"
print(list1[0])
# list sliecing
print(list1[0:3])
# list method
list2 = [ 23, 4, 56, 41, 5]
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.insert(3, 23)# to add a element into list
print(list2)
# to delete element from list
list2.pop(3)
print(list2)