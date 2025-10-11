__import__('os').system('cls' if __import__('os').name =='nt' else 'clear')
# DICTIONARY
# /      \
# empty   filled
# Empty Dictionary
value1={}
# fulled Dictionary
value ={
    "hi": 34,
    "hii": 43,
    "this": 68
}
print(value)
print(type(value))
value["hi"]= 23
print(value)
# return all the item in the dictionary
print(value.items())
# return all the value in the dictionary
print(value.values())
# this method is used to add/change in the dictionary
upd =value.update({"hola": 45})
print(value)
# this method is used to return the key of value stated
print(value.get("hi"))  #return non if no value doesnt exist
print(value["hii"])  # return a error if value doesnt exist