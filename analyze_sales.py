import pandas as pd

# Load the sales data
df = pd.read_csv("sales_data.csv")

# Display the first 5 rows
print(df.head())
# Calculate total revenue
total_revenue = df["Revenue"].sum()

print("Total Revenue:", total_revenue)
# Calculate total orders
total_orders = df["Order_ID"].nunique()

print("Total Orders:", total_orders)
# Calculate total units sold
total_units = df["Quantity"].sum()

print("Total Units Sold:", total_units)
# Calculate revenue by product
product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nTop Performing Products:")
print(product_sales)
# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Calculate monthly revenue
monthly_revenue = df.groupby(df["Order_Date"].dt.to_period("M"))["Revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)
# Calculate revenue by category
category_sales = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Category:")
print(category_sales)
# Calculate revenue by region
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Region:")
print(region_sales)
# Export analysis results to Excel

with pd.ExcelWriter("Sales_Revenue_Dashboard.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sales_Data", index=False)
    product_sales.to_excel(writer, sheet_name="Top_Products")
    monthly_revenue.to_excel(writer, sheet_name="Monthly_Revenue")
    category_sales.to_excel(writer, sheet_name="Category_Sales")
    region_sales.to_excel(writer, sheet_name="Region_Sales")

print("\nExcel dashboard data exported successfully!")