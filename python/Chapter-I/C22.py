import os; os.system('cls')
# lambda function 
# this is an anonymous function without name
add = lambda n,m: n+m
print(add(5,6))
# through this, a function can call our function
def avg(fx, value1,value2):
    return fx(value1,value2)/2

print(avg(add,4,5))
# decorators
def fun_star(fx):
    print( "this function starts here:")
    return fx
    
# for a decorator a fuction/method must have a argument int it

@fun_star
def fun2():
    for i in range(5):
     print(i)
     
fun2()
