-- What is the total revenue generated?
select sum(payment_value) total_revenue
from payments;


-- How many orders have been placed?
select count(order_id) total_orders
from orders;


-- How many unique customers does the business have?
select  DISTINCT count(customer_unique_id) number_of_customers
from customers;


-- How many sellers have completed at least one sale?
select DISTINCT count(seller_id) number_of_seller_whos_atlest_done_order
from order_items;


-- What is the average order value (AOV)?
select avg(payment_value) avg_order_value
from payments;


-- What is the monthly revenue trend?
SELECT
    DATE_TRUNC('month', o.order_delivered_customer_date::timestamp) AS month,
    ROUND(SUM(p.payment_value)::numeric, 1) AS total_revenue,
    ROUND(
        SUM(SUM(p.payment_value)) OVER (
            ORDER BY DATE_TRUNC('month', o.order_delivered_customer_date::timestamp)
        )::numeric,
        1
    ) AS running_total
FROM orders o
JOIN payments p
    ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_TRUNC('month', o.order_delivered_customer_date::timestamp)
ORDER BY month;


-- What is the monthly order trend?
SELECT
    DATE_TRUNC('month', order_delivered_customer_date::timestamp) AS month,
    COUNT(order_id) AS total_orders,
    ROUND(
        SUM(COUNT(order_id)) OVER (
            ORDER BY DATE_TRUNC('month', order_delivered_customer_date::timestamp)
        )::numeric,
        1
    ) AS running_total
FROM orders
WHERE order_status = 'delivered'
GROUP BY DATE_TRUNC('month', order_delivered_customer_date::timestamp)
ORDER BY month;


-- Which states have the highest average order value?
select c.customer_state ,avg(p.payment_value) as total_revenue
from customers as c
join orders as o on o.customer_id = c.customer_id
join payments as p on p.order_id = o.order_id
group by c.customer_state
order by total_revenue desc
limit 1;


-- Which seller has the highest average order value?
select oi.seller_id ,round(avg(price)::numeric,1) as avg_order_value
from order_items as oi
join payments as p on oi.order_id = p.order_id
group by oi.seller_id 
order by avg_order_value desc
limit 1;
