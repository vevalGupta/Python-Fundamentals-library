import os;os.system('cls')
"""
Lambda Function
"""
fruits= ['apple', 'banana', 'kiwi', 'grape']
sorted_words = sorted(fruits, key=lambda x: x[-1])
print("Sorted by last letter:", sorted_words)