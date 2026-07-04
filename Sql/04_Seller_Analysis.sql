-- Which sellers generate the highest revenue?
select oi.seller_id ,round(sum(price)::"numeric",1) as total_revenue
from order_items as oi
join payments as p on oi.order_id = p.order_id
group by oi.seller_id
order by total_revenue desc
limit 10;


-- Which sellers have sold the most products?
select seller_id ,count(product_id) as number_of_product
from order_items
group by seller_id
order by number_of_product desc
limit 5;


-- Which sellers receive the highest average reviews?
select oi.seller_id ,round(avg(review_score),1) avg_reviews
from order_items as oi
join reviews as r on r.order_id = oi.order_id
group by oi.seller_id
order by avg_reviews desc
limit 5;


-- Which states have the most sellers?
select seller_state ,count(seller_id) as number_of_selller
from sellers
group by seller_state
order by number_of_selller desc
limit 5;
