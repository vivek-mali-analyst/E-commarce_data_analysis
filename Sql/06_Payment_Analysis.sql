-- What is the average payment value by payment type?
select payment_type ,round(avg(payment_value)::"numeric",1)
from payments
where payment_type <> 'not_defined'
group by payment_type;


-- Which payment method contributes the most revenue?
select payment_type ,sum(payment_value)*100.0/(select sum(payment_value) from payments) as percentage
from payments
where payment_type <> 'not_defined'
group by payment_type;


-- Does payment type affect review score?
select payment_type ,round(avg(review_score),0) as review_score
from payments as p
join reviews as r on r.order_id = p.order_id
group by payment_type;
