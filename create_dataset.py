import pandas as pd
import random
from datetime import datetime, timedelta

# Products and their categories
products = {
    "Laptop": "Electronics",
    "Mobile": "Electronics",
    "Headphones": "Accessories",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Monitor": "Electronics",
    "Tablet": "Electronics",
    "Printer": "Office",
    "Office Chair": "Furniture",
    "Desk": "Furniture"
}

regions = ["North", "South", "East", "West"]

# Starting date
start_date = datetime(2025, 1, 1)

data = []

# Create 200 sales records
for i in range(1, 201):

    product = random.choice(list(products.keys()))
    category = products[product]
    region = random.choice(regions)

    order_date = start_date + timedelta(days=random.randint(0, 364))

    quantity = random.randint(1, 10)

    prices = {
        "Laptop": 55000,
        "Mobile": 25000,
        "Headphones": 2000,
        "Keyboard": 1500,
        "Mouse": 800,
        "Monitor": 12000,
        "Tablet": 18000,
        "Printer": 15000,
        "Office Chair": 8000,
        "Desk": 10000
    }

    unit_price = prices[product]

    revenue = quantity * unit_price

    data.append([
        f"ORD{i:04d}",
        order_date.strftime("%Y-%m-%d"),
        product,
        category,
        region,
        quantity,
        unit_price,
        revenue
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Order_ID",
    "Order_Date",
    "Product",
    "Category",
    "Region",
    "Quantity",
    "Unit_Price",
    "Revenue"
])

# Save as CSV
df.to_csv("sales_data.csv", index=False)

print("Sales dataset created successfully!")
print("Total records:", len(df))
print(df.head())