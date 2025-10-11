import os;os.system('cls')
"""
handling missing value
"""
import pandas as pus
# here , Nan = not a number
# none = for objective data type
data = [
    {"EmployeeID": 101, "Name": "Raj",    "Department": "IT",      "Salary": 55000, "Age": 28, "JoiningDate": "2019-06-20"},
    {"EmployeeID": 102, "Name": "Priya",  "Department": "HR",      "Salary": None,  "Age": 25, "JoiningDate": "2020-08-14"},
    {"EmployeeID": 103, "Name": "Akash",  "Department": "IT",      "Salary": 60000, "Age": None, "JoiningDate": "2018-11-01"},
    {"EmployeeID": 104, "Name": "Neha",   "Department": "Finance", "Salary": 58000, "Age": 30, "JoiningDate": None},
    {"EmployeeID": 105, "Name": "Manish", "Department": None,      "Salary": 62000, "Age": 32, "JoiningDate": "2017-09-25"},
    {"EmployeeID": 106, "Name": "Ritu",   "Department": "IT",      "Salary": None,  "Age": 29, "JoiningDate": "2021-04-19"},
    {"EmployeeID": 107, "Name": "Sameer", "Department": "HR",      "Salary": 53000, "Age": None, "JoiningDate": "2020-01-10"},
    {"EmployeeID": 108, "Name": "Tanvi",  "Department": "Finance", "Salary": 59000, "Age": 27, "JoiningDate": "2019-12-05"},
    {"EmployeeID": 109, "Name": None,     "Department": "IT",      "Salary": 61000, "Age": 31, "JoiningDate": "2018-07-30"},
    {"EmployeeID": 110, "Name": "Rohit",  "Department": "Finance", "Salary": None,  "Age": 26, "JoiningDate": "2022-03-15"},
]
pf =pus.DataFrame(data)
pf.to_excel("Employee.xlsx", index=False)
print(pf)
# 1) pf.isnull()
# to find whether dataframe contain missing value
print(pf.isnull())
#return in boolean value
print(pf.isnull().sum())
# 2)pf.dropna()
# to delete the missing value within columns/rows
pf.dropna(axis= 0, inplace=True)
# 0-> rows, 1-> column
print(pf)
# 3) pf.fillna()
# to replace the missing value with given value
"""
if you want fill  different value in different column,use
     /          \
    pf.fillna()   df['column_name'].fillna()
"""
# a)pf['column_name'].fillna()
pf['Name'].fillna("sam", inplace=True)
print(pf)
# OR
pf.fillna({"Age:20"},inplace=True)
print(pf)
# b)pf.fillna()
pf.fillna(0, inplace=True)
print(pf)