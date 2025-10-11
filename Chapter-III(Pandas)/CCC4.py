import os;os.system('cls')
"""
                           GOALS
-> select specific columns from a DataFrame and save it to a CSV file
-> filter rows based on a condition and save the result to a CSV file
->combine multiple conditions to filter rows .

"""
import pandas as p
data = [
    {"Member_ID": 1, "Name": "Roan", "Flat_No": "A101", "Age": 35, "Role": "Secretary"},
    {"Member_ID": 2, "Name": "Sita", "Flat_No": "A102", "Age": 32, "Role": "Treasurer"},
    {"Member_ID": 3, "Name": "Amit", "Flat_No": "B201", "Age": 40, "Role": "President"},
    {"Member_ID": 4, "Name": "Priya", "Flat_No": "B202", "Age": 29, "Role": "Member"},
    {"Member_ID": 5, "Name": "Karan", "Flat_No": "C301", "Age": 45, "Role": "Member"},
    {"Member_ID": 6, "Name": "Meena", "Flat_No": "C302", "Age": 38, "Role": "Member"},
    {"Member_ID": 7, "Name": "Vikram", "Flat_No": "D401", "Age": 50, "Role": "Vice President"},
    {"Member_ID": 8, "Name": "Anita", "Flat_No": "D402", "Age": 27, "Role": "Member"},
    {"Member_ID": 9, "Name": "Rajesh", "Flat_No": "E501", "Age": 36, "Role": "Member"},
    {"Member_ID": 10, "Name": "Neha", "Flat_No": "E502", "Age": 31, "Role": "Member"},
]
Df =p.DataFrame(data)
Df.to_csv("Members.csv", index=False)
# Display the DataFrame
print(Df)
# -> select specific columns from a DataFrame
select_col = Df['Name']# for returning single selected column
print(select_col) 
# for selecting multiple column
multi_col = Df[["Age","Flat_No"]]# in this one more [] should be add
print(multi_col)
#-> filter rows based on a condition 
filter = Df[Df['Age']<=35]
print(filter)
#->combine multiple conditions to filter rows
com_filter = Df[(Df['Age']>=30) & ( Df['Role']=='Member')]
print(com_filter)
