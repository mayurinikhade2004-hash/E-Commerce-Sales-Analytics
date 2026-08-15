import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("data/cleaned_online_retail.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

import os

os.makedirs("reports/charts", exist_ok=True)


# ==========================================
# CHART 1: MONTHLY REVENUE
# ==========================================

df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = (
    df.groupby("YearMonth")["Revenue"]
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/charts/monthly_revenue.png",
    dpi=300
)

plt.close()


# ==========================================
# CHART 2: TOP 10 PRODUCTS
# ==========================================

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    "reports/charts/top_products.png",
    dpi=300
)

plt.close()


# ==========================================
# CHART 3: TOP 10 COUNTRIES
# ==========================================

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_countries.index,
    top_countries.values
)

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig(
    "reports/charts/top_countries.png",
    dpi=300
)

plt.close()


# ==========================================
# CHART 4: TOP 10 CUSTOMERS
# ==========================================

top_customers = (
    df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_customers.index.astype(str),
    top_customers.values
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Customer ID")

plt.tight_layout()

plt.savefig(
    "reports/charts/top_customers.png",
    dpi=300
)

plt.close()


print("===================================")
print("VISUALIZATION COMPLETED")
print("===================================")

print("\nCharts saved in:")
print("reports/charts/")