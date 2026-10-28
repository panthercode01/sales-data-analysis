
import pandas as pd

# CSV file ko read karna
df = pd.read_csv("sales.csv")

# Data screen par dikhana
print(df)

# Revenue aur profit calculate karna
df["revenue"] = df["quantity"] * df["unit_price"]

df["profit"] = (
    df["quantity"] * (df["unit_price"] - df["unit_cost"])
)

print("\nTotal Revenue:", df["revenue"].sum())
print("Total Profit:", df["profit"].sum())
print("Total unit sold", (df["quantity"].sum()))

print("\n--- Product-wise Sales Analysis ---")

product_sales = df.groupby("product").agg({
    "quantity": "sum",
    "revenue": "sum",
    "profit": "sum"
})

print(product_sales)

print("\n--- Top Products by Revenue ---")

sorted_sales = product_sales.sort_values(
    by="revenue", #by="revenue" — revenue ke basis par sort karta hai.
    ascending=False #ascending=False — highest value ko pehle rakhta hai.
)

print(sorted_sales)

print("\nMost Profitable Product:")
print(product_sales["profit"].idxmax()) #idxmax() — us product ka naam deta hai jiska profit sabse zyada hai.

print("\n--- Automatic Business Insights ---")

best_revenue = product_sales["revenue"].idxmax()
best_profit = product_sales["profit"].idxmax()
best_selling = product_sales["quantity"].idxmax()

print(f"Highest Revenue Product: {best_revenue}")
print(f"Most Profitable Product: {best_profit}")
print(f"Most Units Sold Product: {best_selling}")

total_revenue = df["revenue"].sum()
total_profit = df["profit"].sum()

profit_margin = (total_profit / total_revenue) * 100

print(f"Total Revenue: {total_revenue}")
print(f"Total Profit: {total_profit}")
print(f"Profit Margin: {profit_margin:.2f}%")

import matplotlib.pyplot as plt

product_sales[["revenue", "profit"]].plot(
    kind="bar",
    figsize=(9, 5),
    title="Sales Revenue vs Profit by Product"
)

plt.xlabel("Product")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.legend(["Revenue", "Profit"])
plt.tight_layout()
plt.show()