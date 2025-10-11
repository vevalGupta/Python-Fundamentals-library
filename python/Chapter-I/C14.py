import os;os.system('cls')
# loops statement's
# /   \       \
# pass  break  continue
# break (exit the loop and forget about it)
for i in range(5): 
    if(i==4): break
    print(i*2)

# continue(skip this particular iteration)
for i in range(10):
    if(i==7): continue
    print(i)

# pass(not whant to complete this loop right now)
for i in range(10):
    pass


# this is next loop that you want to complete before above loop
i=0
while(i<10):
    print(i)
    i+=1
