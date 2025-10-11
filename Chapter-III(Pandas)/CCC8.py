import os;os.system('cls')
""""
Sorting and Aggregation
"""
# sorting (on column)
import pandas as pd
import random
data = {
    "ID": [i for i in range(1, 6)],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [random.randint(20, 40) for _ in range(5)],
    "Score": [random.randint(50, 100) for _ in range(5)],
    "City": random.choices(["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"], k=5)
}
df = pd.DataFrame(data)
# sort only one column
pd.sort_values(by="Age",ascending=True, inplace= True)
print(df)