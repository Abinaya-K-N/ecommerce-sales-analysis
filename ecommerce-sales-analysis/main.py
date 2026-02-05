import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("visualizations", exist_ok=True)


# Load Dataset

try:
    df = pd.read_csv("data/ecommerce_sales.csv")
except FileNotFoundError:
    print("Error: Dataset not found in data folder.")
    exit()

# Data Exploration & Cleaning

df.dropna(inplace=True)
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

# Rename columns for consistency
df.rename(columns={
    'Product_Category': 'category',
    'Purchase_Amount': 'revenue'
}, inplace=True)

print("Dataset loaded successfully")
print("Number of records:", df.shape[0])
print("Columns:", list(df.columns))
print("Unique product categories:", df['category'].nunique())


# Basic Analysis (Metrics & Patterns)

total_revenue = df['revenue'].sum()
average_order_value = df['revenue'].mean()

print("Total Revenue:", round(total_revenue, 2))
print("Average Order Value:", round(average_order_value, 2))

category_sales = df.groupby('category')['revenue'].sum()
top_category = category_sales.idxmax()

print("Top Performing Category:", top_category)

df['month'] = df['Transaction_Date'].dt.to_period('M')
monthly_sales = df.groupby('month')['revenue'].sum()

best_month = monthly_sales.idxmax()
print("Highest Revenue Month:", best_month)


# Data Visualization


# Bar Chart: Sales by Category
plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("visualizations/bar_sales_by_category.png")
plt.close()

# Line Chart: Monthly Sales Trend
plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visualizations/line_monthly_sales.png")
plt.close()

# Pie Chart: Revenue Distribution
plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Revenue Distribution by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/pie_revenue_distribution.png")
plt.close()

print("Visualizations created successfully.")
print("E-commerce sales analysis completed.")
