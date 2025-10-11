import os;os.system('cls')
"""
THE METHOD OF PANDAS
"""
import pandas as p
D=p.read_excel("Pandas.xlsx")
# it is used to info of dataframe
print(D.info())
# for showing the summarize statistics
print(D.describe())
# for Showing the number of rows and columns
print(f"Number of rows: {D.shape[0]}, Number of columns: {D.shape[1]}")
# 0-> rows, 1-> columns
# for showing the names of columns
print("Column names:", D.columns.tolist())
# to get the column names in a list, we use the tolist() method