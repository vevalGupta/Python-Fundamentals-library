import os;os.system('cls')
"""
E-Commerce Order Processing
"""
# ---- INPUT (you can replace these with input() prompts if desired) ----
order = {
    "OrderID": "O1001",
    "CustomerName": "Rahul Sharma",
    "Items": ["Pen", "Notebook", "Bag"],
    "Quantities": [2, 5, 1],
    "Prices": [10.0, 40.0, 500.0],
}

# ---- VALIDATION ----
n_items = len(order["Items"])
assert n_items == len(order["Quantities"]) == len(order["Prices"]), "Item, qty, price length mismatch"

# ---- LINE COSTS USING LAMBDA + map() ----
line_costs = list(map(lambda q_p: q_p[0] * q_p[1], zip(order["Quantities"], order["Prices"])))

# ---- BILL CALCULATION (using a loop, as required) ----
subtotal = 0.0
for cost in line_costs:
    subtotal += cost

def apply_discount(amount: float) -> float:
    """10% discount if total > 1000."""
    return amount * 0.9 if amount > 1000 else amount

final_amount = apply_discount(subtotal)

# ---- OUTPUT ----
print(f"Order ID      : {order['OrderID']}")
print(f"Customer Name : {order['CustomerName']}")
print("\nItems Breakdown:")
for item, qty, price, cost in zip(order["Items"], order["Quantities"], order["Prices"], line_costs):
    print(f"- {item:10s}  qty={qty:2d}  price={price:7.2f}  line_total={cost:8.2f}")

print(f"\nSubtotal: {subtotal:.2f}")
if subtotal > 1000:
    print("Discount : 10% applied")
print(f"Final Bill Amount: {final_amount:.2f}")

