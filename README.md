🛒 E-Commerce Sales & Customer Analytics
Analyzing sales, customer behavior, delivery performance, and seller/product trends to support data-driven business decisions using SQL, Python, and Power BI.

📌 Table of Contents
- [Overview](#overview)
- [Business Problem](#business-problem)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [Project Structure](#project-structure)
- [Data Cleaning & Preparation](#data-cleaning--preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Research Questions & Key Findings](#research-questions--key-findings)
- [Dashboard](#dashboard)
- [How to Run This Project](#how-to-run-this-project)
- [Final Recommendations](#final-recommendations)
- [Author & Contact](#author--contact)

## Overview
This project analyzes a multi-table e-commerce dataset (customers, orders, order items, payments, products, reviews, and sellers) to uncover insights on revenue, customer spending, delivery performance, and seller/product performance. A complete data pipeline was built: **Python** for cleaning and EDA, **PostgreSQL** for business-question SQL analysis, and **Power BI** for an interactive dashboard.

## Business Problem
Understanding how customers, sellers, and products drive revenue is critical for growth in e-commerce. This project aims to:
- Measure overall business performance (revenue, orders, AOV, customer base)
- Identify the states, cities, and customers that drive the most revenue
- Determine which product categories sell the most and generate the most revenue
- Evaluate seller performance and geographic concentration
- Analyze delivery times and their impact on cancellations and reviews
- Understand how payment method relates to revenue share and customer satisfaction

## Dataset
- link - https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- 8 relational CSV files located in `/Data/` — `customers`, `orders`, `order_items`, `payments`, `products`, `reviews`, `sellers`, `category_name`
- ~99,441 orders across ~96,096 unique customers and 3,095 active sellers
- Data model documented in `/ER Digram/Database_Schema.png`

## Tools & Technologies
- **Python** (Pandas, Matplotlib, Seaborn) — data cleaning and EDA
- **PostgreSQL** (CTEs, Joins, Window Functions) — business-question SQL analysis
- **Power BI** — interactive dashboard
- **GitHub**

## Project Structure
```
E-commarce_data_analysis_/
│
├── Data/                      # Row data in csv formate
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── payments.csv
│   ├── products.csv
│   ├── reviews.csv
│   ├── sellers.csv
│   └── category_name.csv
│
├── Python/                      # Cleaning and EDA scripts
│   ├── Cleaing.py
│   ├── Insert.py
│   ├── EDA.py
│   └── EDA.ipynb
│
├── Sql/                         # SQL business-question analysis
│   ├── 01_KPI_Analysis.sql
│   ├── 02_Customer_Analysis.sql
│   ├── 03_Product_Analysis.sql
│   ├── 04_Seller_Analysis.sql
│   ├── 05_Order_Analysis.sql
│   ├── 06_Payment_Analysis.sql
│   ├── 07_Review_Analysis.sql
│   └── 08_Advanced_Window_Functions.sql
│
├── ER Digram/                   # Database schema
│   ├── Database_Schema.drawio.xml
│   ├── Database_Schema.png
│   └── Database_Schema.svg
│
├──  Power bi/                   # Dashbored
│   ├── E-commerce Analysis.pbix
│   ├── Executive.png
│   ├── Sales.png
│   ├── Customers.png
│   ├── Products.png
│   ├── Delivery.png
│   ├── Reviews.png
│   ├── Schema.png
│   └── Logo.png
│
├── Project_Report.docx          # Report
├── README.md                    # Readme 
└── Work Flow.png                # End-to-end project workflow
```

## Data Cleaning & Preparation
- **Orders:** forward-filled missing approval/delivery dates, converted all date columns to proper datetime types
- **Reviews:** replaced missing review titles and messages with placeholder labels
- **Products:** filled missing category names, converted description/dimension/weight columns to integer type
- Cleaned datasets exported and loaded into PostgreSQL via `Insert.py` for SQL analysis, and reused directly in Python for EDA

## Exploratory Data Analysis (EDA)
- **Payment behavior:** credit card dominates both order volume and revenue share
- **Review scores:** heavily skewed positive — most orders receive 4 or 5 stars
- **Price vs. review score:** essentially no linear relationship (correlation ≈ **-0.004**) — a higher price does not predict a better or worse review
- **Category revenue:** a small set of categories (bedding/bath, health & beauty, computer accessories) consistently top both revenue and volume charts
- **Geography:** revenue and customer base are heavily concentrated in São Paulo state

## Research Questions & Key Findings

**Overall Performance**
- Total revenue: **R$16.0 million** across **99,441 orders**
- Average order value (AOV): **R$154.10**
- Customer base: **96,096 unique customers**, served by **3,095 active sellers**
- 96,478 of all orders (97%) reached **delivered** status; only 625 were canceled

**Customers**
- São Paulo (SP) leads by customer count with **41,746 customers**, more than 3x the next state (RJ, 12,852)
- São Paulo city alone generates **R$2.2M** in revenue — nearly double Rio de Janeiro, the #2 city
- Average spend per customer is **R$166.59**, but only **2,997 customers (≈3%)** have placed more than one order — repeat purchase behavior is rare
- Paraíba (PB) has the highest average order value at **R$248.33**, well above the national average, despite not being a top-volume state

**Products**
- Top revenue categories: **bed_bath_table (R$1.71M)**, **health_beauty (R$1.66M)**, **computers_accessories (R$1.59M)**, **furniture_decor (R$1.43M)**, **watches_gifts (R$1.43M)**
- The same categories also lead in items sold, showing revenue is volume-driven rather than premium-pricing-driven
- **32,951 unique products** were sold; the single highest-priced item sold for **R$6,735**

**Sellers**
- Seller base is heavily concentrated in **São Paulo state (1,849 of 3,095 sellers, ~60%)**, followed by Paraná (349) and Minas Gerais (244)
- The top seller alone generated **R$244,627.60** in revenue — seller performance is highly uneven across the marketplace

**Delivery & Orders**
- Average delivery time is **12 days 13 hours** from purchase to customer delivery
- Northern states have by far the slowest delivery: **Roraima (29 days)**, **Amapá (27 days)**, **Amazonas (26 days)** — more than double the national average
- Cancellations spike in specific months — **August 2018 (84 cancellations)** and **February 2018 (73 cancellations)** were the worst months
- August 2018 was also the **highest revenue month (R$1.35M)**, suggesting demand spikes can coincide with fulfillment strain

**Payments & Reviews**
- **Credit card** is used for **78.3%** of revenue, followed by boleto (17.9%), voucher (2.4%), and debit card (1.4%)
- Overall average review score is **4.09 / 5** — customers are largely satisfied
- Review scores are similar across payment types (4.0–4.17), except unrecorded/`not_defined` payments, which correlate with a much lower average review (1.67)

## Dashboard
Power BI dashboard (`Power bi/E-commarce Analysis.pbix`) covering:
### Executive summary — revenue, orders, AOV, customer/seller counts
![Executive Dashboard](./Power%20bi/Executive.png)
### Sales trends over time
![Sales Dashboard](./Power%20bi/Sales.png)
### Customer geography and spend
![Customers Dashboard](./Power%20bi/Customers.png)
### Product category performance
![Products Dashboard](./Power%20bi/Products.png)
### Delivery performance
![Delivery Dashboard](./Power%20bi/Delivery.png)
### Review score breakdown
![Reviews Dashboard](./Power%20bi/Reviews.png)

## Database Schema (ER Diagram)
![ER Diagram](./ER%20Digram/Database_Schema.png)

## Project Workflow
![Work Flow](./Work%20Flow.png)

## How to Run This Project
1. Clone the repository:
   ```
   git clone https://github.com/Vivek7ok/E-commarce_data_analysis_.git
   ```
2. Clean the raw data:
   ```
   python Python/Cleaing.py
   ```
3. Load cleaned data into PostgreSQL:
   ```
   python Python/Insert.py
   ```
4. Run the SQL analysis scripts in `Sql/` against the loaded database (in numeric order, 01 → 08) for business-question results.
5. Run exploratory analysis:
   ```
   python Python/EDA.py
   ```
   or open `Python/EDA.ipynb` in Jupyter.
6. Open the dashboard:
   ```
   Power bi/E-commarce Analysis.pbix
   ```

## Final Recommendations
- Invest in customer retention (loyalty offers, targeted re-engagement) since only ~3% of customers currently reorder
- Prioritize logistics improvements in the North region (RR, AP, AM) where delivery times are more than double the national average
- Investigate the August and February cancellation spikes to identify seasonal or operational causes before they recur
- Continue to feature top-performing categories (bed/bath, health & beauty, computer accessories) in promotions, since they drive both volume and revenue
- Reduce reliance on São Paulo-based sellers by recruiting and supporting sellers in other states to diversify fulfillment capacity
- Since price does not drive review score, focus service-quality efforts (delivery speed, product accuracy) rather than pricing to improve satisfaction further

## Author & Contact
**Vivek**
Data Analyst
🔗 [GitHub](https://github.com/Vivek7ok)
