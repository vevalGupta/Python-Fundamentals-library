import os;os.system('cls')

def announce(func):
     def wrapper(*args , **kwargs):
            print(f"running {func.__name__}...")
            return func(*args,**kwargs)
     return wrapper 
@announce
def greets(name):
    """
    greeting program
    """
    return f" hello {name}"
@announce
def add(a,b,c=5):
    """
    Adding Three number
    """
    return a+b+c
print(greets("veval"))
print(add(2,10))
