import os;os.system('cls')
# loops
# /   \
# for while
# 1.while loop
n=int(input("Enter the number : "))
print(f"table of {n} is : ")
i=0
while(i<11):
    print(n*i)
    i+=1

print(f"table of {n} ended")
# 2.for loop
print("enter the n")
n1= int(input("Enter the number :"))
print("enter the m")
m= int(input("Enter the number :"))
for i in range(n1):
    for j in range(m):
        print("*", end=" ")
    print()