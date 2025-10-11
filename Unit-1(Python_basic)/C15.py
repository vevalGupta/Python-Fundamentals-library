import os;os.system('cls')
# practice 1
l =["shubhra", "khushan", "siddharth", "nikit", "harsh"]
for i in l:
    if(i.startswith("s")): 
       print(f"welcome {i}")

# pratice 2
n =int(input("enter the number: "))
i=sum=0
while(i<n):
    sum += i
    print(sum)
    i+=1
    