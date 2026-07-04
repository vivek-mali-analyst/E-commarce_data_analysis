-- How many orders were delivered, canceled, or unavailable?
select order_status ,count(order_id) as number_of_orders
from orders 
group by order_status;


-- What is the average delivery time?
select avg(order_delivered_customer_date::timestamp - order_purchase_timestamp::timestamp) as delivery_time
from orders 
WHERE order_status='delivered';


-- Which states have the longest delivery time?
select customer_state,
avg(order_delivered_customer_date::timestamp - order_purchase_timestamp::timestamp) as delivery_time
from orders as o
join customers as c
on c.customer_id = o.customer_id
WHERE order_status='delivered'
group by customer_state
order by delivery_time desc
limit 1;


-- Which months have the most canceled orders?
select DATE_TRUNC('month', order_purchase_timestamp::timestamp) as order_purchsed,
count(order_id) as number_of_orders
from orders
where order_status = 'canceled'
group by DATE_TRUNC('month', order_purchase_timestamp::timestamp)
order by number_of_orders desc
limit 3;


-- Which order status generates the highest revenue?
select order_status ,round(sum(p.payment_value)::numeric,1) as total_revenue
from payments as p
join orders as o on o.order_id = p.order_id
group by order_status
order by total_revenue desc
limit 1;
