import os; os.system('cls')
# conditional Expression
# 1. if else
n=int(input('enter the number'))
if(n%2==0):
    print("Even number")

else:
    print("Odd number")

# elif
if(n>=18):
    print("adult")

elif(n<0):
    print('wrong input')

else:
    print("child")