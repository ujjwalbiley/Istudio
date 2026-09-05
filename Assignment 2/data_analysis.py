import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TASK 1
print("\n" + "=" * 60)
print("TASK 1: PYTHON BASICS & NUMPY")
print("=" * 60)

print("\n--- 1.1 Python Data Types ---")
integer_value = 25
float_value = 3.14
string_value = "Data Analytics"
boolean_value = True
list_value = [10, 20, 30]
tuple_value = (1, 2, 3)
dictionary_value = {"name": "Aarav", "age": 28}

print("Integer:", integer_value, type(integer_value))
print("Float:", float_value, type(float_value))
print("String:", string_value, type(string_value))
print("Boolean:", boolean_value, type(boolean_value))
print("List:", list_value, type(list_value))
print("Tuple:", tuple_value, type(tuple_value))
print("Dictionary:", dictionary_value, type(dictionary_value))

print("\n--- Arithmetic Operators ---")
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)
print("Floor Division:", a // b)

print("\n--- Comparison Operators ---")

print("a == b:", a == b)
print("a > b:", a > b)
print("a < b:", a < b)

print("\n--- Logical Operators ---")
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)

print("\n--- 1.2 NumPy Operations ---")
sales = np.array([
    125, 138, 142, 155, 168, 180,
    195, 210, 225, 240, 258, 275
])

print("Sales Array:", sales)
print("Shape:", sales.shape)
print("Size:", sales.size)
print("Dtype:", sales.dtype)

print("Sum:", sales.sum())
print("Mean:", sales.mean())
print("Maximum:", sales.max())
print("Minimum:", sales.min())
print("Standard Deviation:", sales.std())

reshaped_sales = sales.reshape(4, 3)

print("\nReshaped Array (4 x 3):")
print(reshaped_sales)

high_sales_indices = np.where(sales > 200)

print("\nIndices where sales > 200:")
print(high_sales_indices)

growth = np.diff(sales)

print("\nMonth-over-month growth:")
print(growth)

# TASK 2:
print("\n" + "=" * 60)
print("TASK 2: PANDAS - DATA LOADING, CLEANING & MERGING")
print("=" * 60)

customers_data = {
    "cust_id": [
        "C01", "C02", "C03", "C04",
        "C05", "C06", "C07", "C08"
    ],

    "name": [
        "Aarav", "Bhavya", "Chirag", "Diya",
        "Eshan", "Farah", "Gaurav", "Hina"
    ],

    "city": [
        "Mumbai", "Delhi", "Bangalore", "Mumbai",
        "Pune", "Delhi", "Bangalore", "Mumbai"
    ],

    "age": [
        28, 32, 26, np.nan,
        30, 29, 40, 27
    ],

    "gender": [
        "M", "F", "M", "F",
        "M", "F", "M", np.nan
    ]
}

customers_df = pd.DataFrame(customers_data)

purchases_data = {
    "purchase_id": [
        "P101", "P102", "P103", "P104", "P105",
        "P106", "P107", "P108", "P109", "P110"
    ],

    "cust_id": [
        "C01", "C02", "C03", "C01", "C05",
        "C02", "C06", "C07", "C03", "C05"
    ],

    "product": [
        "Laptop", "Saree", "Smartphone", "Tablet",
        "Headphones", "Watch", "T-shirt",
        "Backpack", "Mouse", "Charger"
    ],

    "amount": [
        55000, 4500, 32000, 18000, 1500,
        3500, 499, 1800, 899, 650
    ],

    "purchase_date": [
        "2025-02-03", "2025-02-05", "2025-02-09",
        "2025-02-11", "2025-02-12", "2025-02-14",
        "2025-02-18", "2025-02-20", "2025-02-22",
        "2025-02-26"
    ]
}

purchases_df = pd.DataFrame(purchases_data)

print("\n--- Customers DataFrame ---")
print(customers_df.head())

print("\nCustomers Shape:")
print(customers_df.shape)

print("\nCustomers Info:")
customers_df.info()

print("\n--- Purchases DataFrame ---")
print(purchases_df.head())

print("\nPurchases Shape:")
print(purchases_df.shape)

print("\nPurchases Info:")
purchases_df.info()

print("\n--- Missing Values Before Cleaning ---")
print(customers_df.isnull().sum())

customers_df["age"] = customers_df["age"].fillna(
    customers_df["age"].mean()
)

customers_df["gender"] = customers_df["gender"].fillna("Unknown")

customers_df["age"] = customers_df["age"].astype(int)


print("\n--- Customers After Cleaning ---")
print(customers_df)

print("\nMissing Values After Cleaning:")
print(customers_df.isnull().sum())

purchases_df["purchase_date"] = pd.to_datetime(
    purchases_df["purchase_date"]
)

merged_df = pd.merge(
    customers_df,
    purchases_df,
    on="cust_id",
    how="inner"
)

print("\n--- Merged DataFrame ---")
print(merged_df.head())

print("\nMerged Shape:")
print(merged_df.shape)

# TASK 3:
print("\n" + "=" * 60)
print("TASK 3: FILTERING, GROUPING, AGGREGATION & VISUALIZATION")
print("=" * 60)

print("\n--- Purchases from Mumbai ---")

mumbai_purchases = merged_df[
    merged_df["city"] == "Mumbai"
]

print(mumbai_purchases)

print("\n--- Purchases with Amount > 5000 ---")

high_amount_purchases = merged_df[
    merged_df["amount"] > 5000
]

print(high_amount_purchases)

print("\n--- Male Customers Who Made Purchases ---")

male_customers = merged_df[
    merged_df["gender"] == "M"
]

print(male_customers)

print("\n--- Total Purchase Amount Per City ---")

city_totals = merged_df.groupby("city")["amount"].sum()

print(city_totals)

print("\n--- Average Purchase Amount Per Gender ---")

gender_average = merged_df.groupby("gender")["amount"].mean()

print(gender_average)

print("\n--- Number of Purchases Per Customer ---")

purchase_count = merged_df.groupby(
    ["cust_id", "name"]
).size()

print(purchase_count)

print("\n--- Most Active Customers ---")

max_purchase_count = purchase_count.max()

most_active_customers = purchase_count[
    purchase_count == max_purchase_count
]

print("Most active customers:")
print(most_active_customers)

print("Number of purchases:", max_purchase_count)

print("\n--- Top 3 Customers by Total Spending ---")

top3 = (
    merged_df.groupby("name")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print(top3)

print("\n" + "=" * 60)
print("3.3 DATA VISUALIZATION")
print("=" * 60)

plt.figure(figsize=(7, 5))

city_totals.plot(kind="bar")

plt.title("Total Purchase Amount by City")
plt.xlabel("City")
plt.ylabel("Total Amount (INR)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("Figure_1.png", dpi=300, bbox_inches="tight")
plt.show()

gender_totals = merged_df.groupby("gender")["amount"].sum()

plt.figure(figsize=(7, 5))

plt.pie(
    gender_totals,
    labels=gender_totals.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Share of Purchases by Gender")

plt.tight_layout()
plt.savefig("Figure_2.png", dpi=300, bbox_inches="tight")
plt.show()

top3_df = top3.reset_index()

top3_df.columns = ["name", "amount"]

plt.figure(figsize=(7, 5))

sns.barplot(
    data=top3_df,
    x="name",
    y="amount"
)

plt.title("Top 3 Customers by Total Spending")
plt.xlabel("Customer")
plt.ylabel("Total Spending (INR)")

plt.tight_layout()
plt.savefig("Figure_3.png", dpi=300, bbox_inches="tight")
plt.show()

date_amount = (
    merged_df.groupby("purchase_date")["amount"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(9, 5))

plt.plot(
    date_amount.index,
    date_amount.values,
    marker="o"
)

plt.title("Purchase Date vs Amount")
plt.xlabel("Purchase Date")
plt.ylabel("Amount (INR)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Figure_4.png", dpi=300, bbox_inches="tight")
plt.show()

print("\n" + "=" * 60)
print("DATA ANALYSIS SUMMARY")
print("=" * 60)

highest_revenue_city = city_totals.idxmax()
highest_revenue = city_totals.max()

average_spending = merged_df["amount"].mean()

print("Highest revenue city:", highest_revenue_city)
print("Highest revenue:", highest_revenue)

print("Most active customers:")

for customer in most_active_customers.index:
    print("-", customer[1])

print("Number of purchases:", max_purchase_count)

print("Average purchase amount:", average_spending)