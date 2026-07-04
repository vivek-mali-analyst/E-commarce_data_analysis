-- What is the overall average review score?
select round(avg(review_score),0)
from reviews;


-- How are review scores distributed?
select review_score ,count(*)
from reviews
group by review_score;


-- Do expensive products receive better reviews?
select product_id ,
round(avg(price)::numeric,1) avg_price,
round(avg(review_score),1) avg_review
from order_items as oi
join reviews as r on r.order_id = oi.order_id
group by product_id
order by avg_price desc
limit 10;


-- Which order status has the highest average review score?
select order_status ,round(avg(review_score),0) as review_score
from orders as o
join reviews as r on r.order_id = o.order_id
where review_score IS NOT NULL
group by order_status
order by review_score desc
limit 1;
