"""
E-Commerce Order Processing
A small online store wants to analyze customer orders
"""
import os; os.system('cls')
# 1. Accept order details from the user
order_code = input("Enter Order Code: ")
buyer_name = input("Enter Buyer Name: ")
products = input("Enter products : ").split(',')
amounts = list(map(int, input("Enter quantities: ").split(',')))
rates = list(map(float, input("Enter prices : ").split(',')))

# 2. Store data in a dictionary
order_info = {
    "OrderCode": order_code,
    "BuyerName": buyer_name,
    "Products": [product.strip() for product in products],
    "Amounts": amounts,
    "Rates": rates
}

# 6. Calculate line-wise item cost using list comprehension
item_totals = [q * p for q, p in zip(order_info["Amounts"], order_info["Rates"])]

# 3. Calculate total bill using sum()
total_bill = sum(item_totals)

# 4. Apply discount function (using lambda)
discount = lambda amt: amt * 0.9 if amt > 1000 else amt
final_bill = discount(total_bill)

# 5. Display final bill amount with customer details
print("\n--- Order Summary ---")
print(f"Order Code: {order_info['OrderCode']}")
print(f"Buyer Name: {order_info['BuyerName']}")
print("Products Purchased:")
for i, product in enumerate(order_info["Products"]):
    print(f"  {product}: {order_info['Amounts'][i]} x {order_info['Rates'][i]} = {item_totals[i]}")
print(f"Total Bill: {total_bill}")
if total_bill > 1000:
    print("Discount Applied: 10%")
print(f"Final Bill Amount: {final_bill}")