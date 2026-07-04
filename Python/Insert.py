import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Vivek%40123@localhost:5432/E-Commerce Sales & Customer Analytics"
)

folder = r"d:\Data_set\28_E-commarce\Data\Clean"

files = [
    "customers.csv",
    "orders.csv",
    "payments.csv",
    "products.csv",
    "reviews.csv",
    "sellers.csv",
    "order_items.csv",
    "category_name_translation.csv"
]

for file in files:
    path = os.path.join(folder, file)

    df = pd.read_csv(path)

    table_name = file.replace(".csv", "")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} inserted successfully.")