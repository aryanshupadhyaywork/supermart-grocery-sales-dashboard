import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "retail_sales.csv"
df = pd.read_csv(DATA, parse_dates=["Order Date"])

print("Rows:", len(df))
print("Total sales:", round(df["Sales"].sum(), 2))
print("Total profit:", round(df["Profit"].sum(), 2))
print("Average discount:", round(df["Discount"].mean() * 100, 2), "%")
print("\nSales and profit by category:")
print(df.groupby("Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False))
print("\nSales and profit by region:")
print(df.groupby("Region")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False))
print("\nTop sub-categories by sales:")
print(df.groupby("Sub Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False).head(10))
