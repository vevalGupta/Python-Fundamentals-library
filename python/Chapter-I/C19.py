import os;os.system('cls')
# exception handling 
# try and exception as e
try:
    a =int(input("enter the number :"))
    print(f"table of {a} :")
    for i in range(1,11):
        print(f"{a}x{i}= {a*i} ")
except Exception as e: print(e)
finally: print("i will be excueted no matter what")
print("code")
print("ended")
# custom error
value = int(input("Enter the value b/w 2 and 9 :"))
if(value<2 and value>9):
    raise ValueError("wrong input")