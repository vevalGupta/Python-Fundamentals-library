import os;os.system('cls')
"""
Interpolation
(fill the missing value with value according to previous data)
"""
import pandas as pd
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
pf =pd.DataFrame(data)
print(pf)
# 1. linear interpolation
pf["Salary"]=pf["Salary"].interpolate(method="linear")
print("linear interpolate : \n")
print(pf["Salary"])
# 2. index interpolation
pf["Age"]= pf["Age"].interpolate(method="index")
print("index interpolation :\n")
print(pf["Age"])
# time interpolation
# pf["JoiningDate"]= pf["JoiningDate"].interpolate(method="time")
# print("time interpolation :\n")
# print(pf["JoiningDate"])
