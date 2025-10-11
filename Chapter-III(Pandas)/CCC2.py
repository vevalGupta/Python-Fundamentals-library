import os;os.system('cls')
"""
creating a dataframe then, later sving it as csv file/excel/json file
"""
import pandas as p
data = [
    {'ProductID': 201, 'ProductName': 'Galaxy S21', 'Category': 'Smartphone', 'Brand': 'Samsung', 'Price': 52000, 'Stock': 35, 'Rating': 4.5, 'Warranty (months)': 24, 'LaunchDate': '2021-01-29'},
    {'ProductID': 202, 'ProductName': 'iPhone 13', 'Category': 'Smartphone', 'Brand': 'Apple', 'Price': 72000, 'Stock': 20, 'Rating': 4.7, 'Warranty (months)': 12, 'LaunchDate': '2021-09-24'},
    {'ProductID': 203, 'ProductName': 'Mi Note 10 Pro', 'Category': 'Smartphone', 'Brand': 'Xiaomi', 'Price': 33000, 'Stock': 50, 'Rating': 4.4, 'Warranty (months)': 18, 'LaunchDate': '2020-02-15'},
    {'ProductID': 204, 'ProductName': 'Bravia 55" LED', 'Category': 'Television', 'Brand': 'Sony', 'Price': 68000, 'Stock': 15, 'Rating': 4.6, 'Warranty (months)': 36, 'LaunchDate': '2020-07-20'},
    {'ProductID': 205, 'ProductName': 'Inspiron 15', 'Category': 'Laptop', 'Brand': 'Dell', 'Price': 58000, 'Stock': 25, 'Rating': 4.3, 'Warranty (months)': 24, 'LaunchDate': '2019-11-05'},
    {'ProductID': 206, 'ProductName': 'MacBook Air M1', 'Category': 'Laptop', 'Brand': 'Apple', 'Price': 92000, 'Stock': 10, 'Rating': 4.8, 'Warranty (months)': 12, 'LaunchDate': '2020-11-17'},
    {'ProductID': 207, 'ProductName': 'HP Pavilion x360', 'Category': 'Laptop', 'Brand': 'HP', 'Price': 61000, 'Stock': 18, 'Rating': 4.2, 'Warranty (months)': 24, 'LaunchDate': '2021-04-10'},
    {'ProductID': 208, 'ProductName': 'WH-1000XM4', 'Category': 'Headphones', 'Brand': 'Sony', 'Price': 22000, 'Stock': 40, 'Rating': 4.7, 'Warranty (months)': 12, 'LaunchDate': '2020-08-06'},
    {'ProductID': 209, 'ProductName': 'JBL Flip 5', 'Category': 'Bluetooth Speaker', 'Brand': 'JBL', 'Price': 9500, 'Stock': 55, 'Rating': 4.5, 'Warranty (months)': 12, 'LaunchDate': '2019-09-01'},
    {'ProductID': 210, 'ProductName': 'Kindle Paperwhite', 'Category': 'E-Reader', 'Brand': 'Amazon', 'Price': 12500, 'Stock': 30, 'Rating': 4.6, 'Warranty (months)': 12, 'LaunchDate': '2018-10-16'}
]
# Here, the data has formed and tranfered to datafRAME 
df =p.DataFrame(data)# index = false does'nt work on dataframe
print(df)
# Here, we are going to saving it into file
df.to_excel("panda-I.xlsx",index=False)
# if you,don't want index(in front),use index=false
print("display the first 5 row of the dataframe")
print(df.head(5))
# this method only work on dataframe
print("display the last 5 row of the dataframe")
print(df.tail(5))
