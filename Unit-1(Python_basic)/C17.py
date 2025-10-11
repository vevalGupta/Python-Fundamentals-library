import os;os.system('cls')
def factorial(n):
    if(n==1 or n==0): return 1
    return n * factorial(n-1)

n =int(input("enter the number :"))
print(factorial(n))
# greatest of 3 num
def num_3(a,b,c):
   '''this is a program to find the grreatest the number between the a and b and c'''
   if(a<b and a<c):return a
   elif(b<a and b<c):return b
   elif(c<a and c<b):return c

a = int(input("enter the a:"))
b = int(input("enter the b:"))
c = int(input("enter the c:"))
print(num_3(a,b,c))
print(num_3.__doc__)