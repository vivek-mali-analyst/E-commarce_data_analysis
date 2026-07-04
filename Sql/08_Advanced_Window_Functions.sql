-- Which month generated the highest revenue?
SELECT
    DATE_TRUNC('month', o.order_delivered_customer_date::timestamp) AS month,
    ROUND(SUM(p.payment_value)::numeric, 1) AS total_revenue
FROM orders o
JOIN payments p
    ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_TRUNC('month', o.order_delivered_customer_date::timestamp)
ORDER BY total_revenue desc
limit 1;


-- Which month had the highest number of orders?
SELECT
    DATE_TRUNC('month', order_delivered_customer_date::timestamp) AS month,
    COUNT(order_id) AS total_orders
FROM orders
WHERE order_status = 'delivered'
GROUP BY DATE_TRUNC('month', order_delivered_customer_date::timestamp)
ORDER BY total_orders desc
limit 1;


-- What are the top 10 highest-value orders?
select order_id ,payment_value
from payments
order by payment_value desc
limit 10;


-- Highest priced product.
SELECT
    product_id,
    MAX(price) AS highest_price
FROM order_items
GROUP BY product_id
ORDER BY highest_price DESC
LIMIT 5;
