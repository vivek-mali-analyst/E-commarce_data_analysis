-- Which product categories generate the highest revenue?
select p.product_category_name as category,
sum(p2.payment_value) as total_revenue
from products as p
join order_items as oi on p.product_id = oi.product_id
join payments as p2 on p2.order_id = oi.order_id
group by product_category_name
order by total_revenue desc
limit 5;


-- Which product categories sell the most items?
select p.product_category_name as category,
count(oi.product_id) as number_of_items 
from products as p
join order_items as oi on p.product_id = oi.product_id
group by product_category_name
order by number_of_items desc
limit 5;


-- Which product categories have the highest average price?
select p.product_category_name ,avg(oi.price)
from products as p
join order_items as oi on p.product_id = oi.product_id
group by product_category_name
order by avg(oi.price) desc 
limit 1;


-- Which categories receive the highest review scores?
select p.product_category_name as category,
max(review_score) as max_score
from products as p
join order_items as oi on p.product_id = oi.product_id
join reviews as r on r.order_id = oi.order_id
group by product_category_name;


-- Which categories receive the lowest review scores?
select p.product_category_name as category,
min(review_score) as min_score
from products as p
join order_items as oi on p.product_id = oi.product_id
join reviews as r on r.order_id = oi.order_id
group by product_category_name;


-- Which categories have the largest number of products?
select product_category_name ,count(product_id) as total_products
from products 
group by product_category_name
order by total_products desc
limit 1;
