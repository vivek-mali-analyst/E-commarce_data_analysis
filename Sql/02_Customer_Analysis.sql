-- Which states have the most customers?
select customer_state ,count(customer_id) as total_customers
from customers
group by customer_state
order by total_customers desc
limit 1;


-- Which cities generate the highest revenue?
select c.customer_city ,sum(p.payment_value) as total_revenue
from customers as c
join orders as o on o.customer_id = c.customer_id
join payments as p on p.order_id = o.order_id
group by c.customer_city
order by total_revenue desc
limit 1;


-- Which customers spend the most?
select c.customer_unique_id ,sum(p.payment_value) as total_revenue
from customers as c
join orders as o on o.customer_id = c.customer_id
join payments as p on p.order_id = o.order_id
group by c.customer_unique_id
order by total_revenue desc
limit 10;


-- What is the average spending per customer?
with cte as
(select c.customer_unique_id ,sum(p.payment_value) as total_spending
from customers as c
join orders as o on o.customer_id = c.customer_id
join payments as p on p.order_id = o.order_id
group by c.customer_unique_id)
select ROUND(AVG(total_spending)::numeric, 2) AS avg_spending_per_customer
from cte;


-- How many repeat customers are there?
select c.customer_unique_id ,count(DISTINCT o.order_id) as total_order
from customers as c
join orders as o on o.customer_id = c.customer_id
join payments as p on p.order_id = o.order_id
group by c.customer_unique_id
having count(DISTINCT o.order_id) > 1
order by total_order asc;
