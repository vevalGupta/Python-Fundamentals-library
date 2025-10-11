__import__('os').system('cls' if __import__('os').name == 'nt' else 'clear')
# string sliecing
name ="This is a string"
print(name[0:7])
# string function 
print(name.endswith("ing"))
# escape sequence 
name1 = "this is second string\a    "
print(name1)
# f string
name2 = "veval"
date="18-02-2006"
print(f''' hi {name2}\n you are good to go\n date- {date}''')