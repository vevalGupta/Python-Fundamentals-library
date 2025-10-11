__import__('os').system('cls' if __import__('os').name == 'nt' else 'clear')
# practic question 
# 1. enter in list
l = ["banana", "apple"]
print(type(l))
add =input(" enter the fruit :")
l.append(add)
print(l) 
# for sorting
l.sort()
print(l)
# for sum
l1 = ["grapes ", "  waterballon"]
l2 = l1 + l
print(l2)
# for length / count the element
print(len(l2))