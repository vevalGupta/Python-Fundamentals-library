import os;os.system('cls')
# function 
def table():
    n =int(input('enter the number :'))
    for i in range(1,11):
        print(i*n)

# you cannot print here for printing at end here this place
table()
print('done')# to print after the function
# function with argument
def greeting(name,ending):
    print("good morning ,"+ name)
    print(ending)
    return "ji" #this is used to return the value of a 

if __name__=="__main__":greeting("veval", 54)# type: ignore # datatype depends upon user
# if you want to provide value variable store in function call ,you can use return
a =greeting("veval", "thanks")
print(a)
print(__name__)
# default argument parameter
# this type of function have predefined parameters value fixed