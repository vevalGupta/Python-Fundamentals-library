import os;os.system('cls')
"""
Modify the DataFrame
  /    |   \
add   update  delete
"""
import pandas as p
it_sales_data = [
    {"Sale_ID": "S001", "Date": "2025-07-01", "Service/Product": "Cloud Storage Subscription", "Category": "Cloud Services", "Units_Sold": 20, "Unit_Price": 1500, "Total_Sale": 30000, "Region": "North", "Salesperson": "Ankit Verma"},
    {"Sale_ID": "S002", "Date": "2025-07-02", "Service/Product": "Antivirus Software", "Category": "Software", "Units_Sold": 35, "Unit_Price": 800, "Total_Sale": 28000, "Region": "South", "Salesperson": "Priya Sharma"},
    {"Sale_ID": "S003", "Date": "2025-07-03", "Service/Product": "Website Development", "Category": "IT Services", "Units_Sold": 5, "Unit_Price": 25000, "Total_Sale": 125000, "Region": "West", "Salesperson": "Rohit Singh"},
    {"Sale_ID": "S004", "Date": "2025-07-04", "Service/Product": "CRM Software License", "Category": "Software", "Units_Sold": 10, "Unit_Price": 12000, "Total_Sale": 120000, "Region": "East", "Salesperson": "Neha Gupta"},
    {"Sale_ID": "S005", "Date": "2025-07-05", "Service/Product": "Annual IT Support", "Category": "IT Services", "Units_Sold": 7, "Unit_Price": 18000, "Total_Sale": 126000, "Region": "North", "Salesperson": "Ankit Verma"},
    {"Sale_ID": "S006", "Date": "2025-07-06", "Service/Product": "Cloud Server Hosting", "Category": "Cloud Services", "Units_Sold": 12, "Unit_Price": 4500, "Total_Sale": 54000, "Region": "South", "Salesperson": "Priya Sharma"},
    {"Sale_ID": "S007", "Date": "2025-07-07", "Service/Product": "Network Security Audit", "Category": "IT Services", "Units_Sold": 4, "Unit_Price": 22000, "Total_Sale": 88000, "Region": "West", "Salesperson": "Rohit Singh"},
    {"Sale_ID": "S008", "Date": "2025-07-08", "Service/Product": "ERP Software", "Category": "Software", "Units_Sold": 3, "Unit_Price": 35000, "Total_Sale": 105000, "Region": "East", "Salesperson": "Neha Gupta"},
    {"Sale_ID": "S009", "Date": "2025-07-09", "Service/Product": "Data Backup Solution", "Category": "Cloud Services", "Units_Sold": 15, "Unit_Price": 2000, "Total_Sale": 30000, "Region": "North", "Salesperson": "Ankit Verma"},
    {"Sale_ID": "S010", "Date": "2025-07-10", "Service/Product": "Mobile App Development", "Category": "IT Services", "Units_Sold": 2, "Unit_Price": 40000, "Total_Sale": 80000, "Region": "South", "Salesperson": "Priya Sharma"}
]
F =p.DataFrame(it_sales_data)
print(f" demo : {F}")
F.to_excel("SalesDepart.xlsx",index =False)
"""
1) adding the column 
   /                  \
  without               with 
using insert method       insert method  
"""
# without insert method
F["commission"]=F['Total_Sale']* 0.1
print(F)
# with insert method ( adding a specific index)
F.insert(7,"Deal_Time",[10.00,14.00,12.30,13.5,17.40,20.25,14.48,15.18,9.00,10.00])
print(F)
"""
2) UPDATING  specific value
"""
F.loc[5, "Deal_Time"]=20.20
print(F)
"""
3) deleting /removing the column
"""
F.drop(columns=["Deal_Time"], inplace=True)
# inplace mean making changes in original dataframe
print(F)
# fp=or deleting row use
F.drop(3,inplace=True)
print(F)
# simply to save changes in excel use to_excel()
# which done after all the modification in panda