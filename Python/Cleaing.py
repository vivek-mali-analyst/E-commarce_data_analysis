# =====================================
# E-Commerce Sales & Customer Analytics
# Data Cleaning
# =====================================

# Objective:
# Clean raw datasets by handling missing values,
# converting data types, and saving cleaned files
# for SQL, Python, and Power BI analysis.

# Data Cleaning Summary
# ---------------------
# Orders:
# - Filled missing delivery dates
# - Converted date columns to datetime
#
# Reviews:
# - Replaced missing review titles and messages
#
# Products:
# - Filled missing category names
# - Converted numeric columns to integer

# ============================
# Import Libraries
# ============================

import pandas as pd


# ============================
# Load Datasets
# ============================

customers = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\customers_dataset.csv")
order_items = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\order_items_dataset.csv")
payments = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\order_payments_dataset.csv")
reviews = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\order_reviews_dataset.csv")
orders = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\orders_dataset.csv")
products = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\products_dataset.csv")
sellers = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\sellers_dataset.csv")
category_translation = pd.read_csv(r"d:\Data_set\28_E-commarce\Data\Bad\category_name_translation.csv")


# ============================
# Clean Orders Dataset
# ============================

# Fill missing delivery dates
orders['order_approved_at'] = orders['order_approved_at'].ffill()
orders['order_delivered_carrier_date'] = orders['order_delivered_carrier_date'].ffill()
orders['order_delivered_customer_date'] = orders['order_delivered_customer_date'].ffill()

# Convert order date columns to datetime
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'], errors='coerce')
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'], errors='coerce')
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'], errors='coerce')
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'], errors='coerce')


# ============================
# Clean Reviews Dataset
# ============================

# Fill missing review title and message
reviews['review_comment_title'] = reviews['review_comment_title'].fillna('No Title')
reviews['review_comment_message'] = reviews['review_comment_message'].fillna('No Message')


# ============================
# Clean Products Dataset
# ============================

# Fill missing product category
products['product_category_name'] = products['product_category_name'].fillna('Missing')

# Fill remaining missing values
products = products.fillna(0)

# Convert numeric columns to integer
numeric_product_columns = [
    'product_description_lenght',
    'product_photos_qty',
    'product_weight_g',
    'product_length_cm',
    'product_height_cm',
    'product_width_cm'
]

for column in numeric_product_columns:
    products[column] = products[column].astype(int)


# ============================
# Save Cleaned Datasets
# ============================

customers.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\customers.csv",
    index=False
)

order_items.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\order_items.csv",
    index=False
)

payments.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\payments.csv",
    index=False
)

reviews.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\reviews.csv",
    index=False
)

orders.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\orders.csv",
    index=False
)

products.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\products.csv",
    index=False
)

sellers.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\sellers.csv",
    index=False
)

category_translation.to_csv(
    r"d:\Data_set\28_E-commarce\Data\Clean\category_name_translation.csv",
    index=False
)


# ============================
# End of Script
# ============================

print("Data cleaning completed successfully.")
print("Clean datasets saved to the Clean folder.")