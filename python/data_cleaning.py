import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

file_path = "data/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("Original Dataset Shape:", df.shape)


# ==========================================
# 2. CHECK DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)


# ==========================================
# 3. REMOVE DUPLICATES
# ==========================================

df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)


# ==========================================
# 4. REMOVE MISSING VALUES
# ==========================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df = df.dropna(subset=["Description", "CustomerID"])

print("\nShape After Removing Missing Values:")
print(df.shape)


# ==========================================
# 5. REMOVE CANCELLED ORDERS
# ==========================================

df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

print("\nShape After Removing Cancelled Orders:")
print(df.shape)


# ==========================================
# 6. REMOVE INVALID QUANTITY
# ==========================================

df = df[df["Quantity"] > 0]

print("\nShape After Removing Invalid Quantity:")
print(df.shape)


# ==========================================
# 7. REMOVE INVALID PRICE
# ==========================================

df = df[df["UnitPrice"] > 0]

print("\nShape After Removing Invalid Prices:")
print(df.shape)


# ==========================================
# 8. CREATE REVENUE COLUMN
# ==========================================

df["Revenue"] = df["Quantity"] * df["UnitPrice"]


# ==========================================
# 9. FINAL DATASET INFORMATION
# ==========================================

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFirst 5 Cleaned Rows:")
print(df.head())


# ==========================================
# 10. SAVE CLEAN DATA
# ==========================================

output_file = "data/cleaned_online_retail.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print(output_file)