import pandas as pd

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

file_path = "data/cleaned_online_retail.csv"

df = pd.read_csv(file_path)

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("===================================")
print("E-COMMERCE EXPLORATORY DATA ANALYSIS")
print("===================================")


# ==========================================
# 2. BASIC INFORMATION
# ==========================================

print("\nDataset Shape:")
print(df.shape)

print("\nNumber of Customers:")
print(df["CustomerID"].nunique())

print("\nNumber of Products:")
print(df["StockCode"].nunique())

print("\nNumber of Countries:")
print(df["Country"].nunique())

print("\nNumber of Orders:")
print(df["InvoiceNo"].nunique())


# ==========================================
# 3. TOTAL REVENUE
# ==========================================

total_revenue = df["Revenue"].sum()

print("\nTotal Revenue:")
print(f"£{total_revenue:,.2f}")


# ==========================================
# 4. TOTAL QUANTITY SOLD
# ==========================================

total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")
print(f"{total_quantity:,}")


# ==========================================
# 5. AVERAGE ORDER VALUE
# ==========================================

order_revenue = df.groupby("InvoiceNo")["Revenue"].sum()

average_order_value = order_revenue.mean()

print("\nAverage Order Value:")
print(f"£{average_order_value:,.2f}")


# ==========================================
# 6. TOP 10 PRODUCTS BY REVENUE
# ==========================================

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Revenue:")
print(top_products)


# ==========================================
# 7. TOP 10 COUNTRIES BY REVENUE
# ==========================================

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Countries by Revenue:")
print(top_countries)


# ==========================================
# 8. TOP 10 CUSTOMERS BY REVENUE
# ==========================================

top_customers = (
    df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Revenue:")
print(top_customers)


# ==========================================
# 9. MONTHLY REVENUE
# ==========================================

df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = (
    df.groupby("YearMonth")["Revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)


# ==========================================
# 10. CATEGORY-LIKE ANALYSIS USING PRODUCT
# ==========================================

top_quantity_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Quantity Sold:")
print(top_quantity_products)


print("\n===================================")
print("EDA COMPLETED SUCCESSFULLY")
print("===================================")