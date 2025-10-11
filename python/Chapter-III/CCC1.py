import os;os.system('cls')
"""
PANDAS
"""
import pandas as p
# first step is to read data from  csv file/excel file into databases
dat= p.read_excel("Pandas.xlsx", )
print(dat)

"""
For Read
if you want to read any other file you can simpliy use,.read_filename("path") 
"""