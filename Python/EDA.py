# ============================
# Import Libraries
# ============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')


# ============================
# Load Datasets
# ============================
df_customers_dataset = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Clean\customers.csv")
df_order_items_dataset = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Clean\order_items.csv")
df_order_payments_dataset = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Clean\payments.csv")
df_order_reviews_dataset = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Clean\reviews.csv")
df_orders_dataset = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Clean\orders.csv")
df_products_dataset = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Clean\products.csv")
df_sellers_dataset = pd.read_csv(r'd:\Data_set\28_E-commarce\Data\Clean\sellers.csv')
df_category_name_translation = pd.read_csv(r'd:\Data_set\28_E-commarce\Data\Clean\category_name_translation.csv')


# ============================
# Merge Datasets
# ============================
df = df_order_payments_dataset.merge(df_orders_dataset, on='order_id', how='left')
df = df.merge(df_order_reviews_dataset, on='order_id', how='left')
df = df.merge(df_order_items_dataset, on='order_id', how='left')
df = df.merge(df_products_dataset, on='product_id', how='left')
df = df.merge(df_customers_dataset, on='customer_id', how='left')
df = df.merge(df_sellers_dataset, on='seller_id', how='left')
df = df.merge(df_category_name_translation, on='product_category_name', how='left')


# ============================
# Data Overview
# ============================
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)


# ============================
# Categorical Summary
# ============================
print(df['payment_type'].value_counts())
print(df['review_score'].value_counts())
print(df['order_status'].value_counts())


# ============================
# Payment Analysis
# ============================
# Average payment value by payment type
plt.figure(figsize=(10,6))
sns.barplot(data=df,x='payment_type',y='payment_value',palette='viridis')
plt.title('Average Payment Value by Payment Type',fontsize=14,fontweight='bold')
plt.xlabel("Payment Type")
plt.ylabel("Average Payment Value")
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# Total payment value by order status
plt.figure(figsize=(10,6))
sns.scatterplot(x='review_score', y='payment_value', data=df, palette='blue')
plt.title('Review Score vs Payment Value',fontsize=14,fontweight='bold')
plt.xlabel('Review Score')
plt.ylabel('Payment Value')
plt.show()


# ============================
# Review Analysis
# ============================
# Review score vs payment value
plt.figure(figsize=(10,6))
sns.boxplot(x='review_score', y='payment_value', data=df, palette='magma')
plt.title('Review Score vs Payment Value',fontsize='14',fontweight='bold')
plt.xlabel('Review Score')
plt.ylabel('Payment Value')
plt.show()

# Payment value by review score
plt.figure(figsize=(10,6))
sns.barplot(x='customer_state', y='payment_value', data=df, palette='Purples')
plt.title('Average Payment Value by Customer State',fontsize='14',fontweight='bold')
plt.xlabel('Customer State')
plt.ylabel('Average Payment Value')
plt.grid(axis='y',linestyle='--',alpha=0.4)
plt.show()

# Average review score by payment type
top_catogry = df.groupby('product_category_name_english',as_index=False)['price'].sum().sort_values(by='price',ascending=False).head()
plt.figure(figsize=(10,6))
sns.barplot(data=top_catogry,x='product_category_name_english',y='price',palette='viridis')
plt.title('Sample Product Categories',fontsize=14,fontweight='bold')
plt.xlabel('Product Category')
plt.ylabel('Price')
plt.grid(axis='y',linestyle='--',alpha=0.4)
plt.xticks(fontsize=10)
plt.show()

# Total payment value by order status
Order_payment = df.groupby('order_status',as_index=False)['payment_value'].sum()
plt.figure(figsize=(10,6))
sns.barplot(data=Order_payment,x='order_status',y='payment_value',palette='viridis')
plt.title('Average Payment Value by Order Status',fontsize=14,fontweight='bold')
plt.xlabel('Average Payment Value')
plt.ylabel('Order Status')
plt.grid(axis='y',linestyle='--',alpha=0.4)
plt.show()


# ============================
# Product Analysis
# ============================
# Top 5 product categories by total price
Payment_review = df.groupby('payment_type',as_index=False)['review_score'].mean()
plt.figure(figsize=(10,6))
sns.barplot(data=Payment_review,x='payment_type',y='review_score',palette='viridis')
plt.title('Average Review Score by Payment Type',fontsize = 14,fontweight='bold')
plt.xlabel('Payment Type')
plt.ylabel('Average Review Score')
plt.grid(axis='y',linestyle='--',alpha = 0.4)
plt.show()

# ============================
# Correlation Analysis
# ============================
# Correlation heatmap
df_corr = df[['price', 'payment_value', 'review_score']].dropna().corr()
sns.heatmap(df_corr, annot=True, cmap='Blues')
plt.title('Correlation Matrix',fontsize=14,fontweight='bold')
plt.show()