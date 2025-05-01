# Write your MySQL query statement below
with q1 as (select p1.product_id as product1_id, p2.product_id as product2_id, count(p1.user_id) as customer_count
from productpurchases p1 inner join productpurchases p2
on p1.user_id = p2.user_id and p1.product_id < p2.product_id

group by p1.product_id, p2.product_id
having customer_count > 2
)

select product1_id, product2_id, 
    (select category from productinfo where product_id = product1_id) as product1_category,
    (select category from productinfo where product_id = product2_id) as product2_category,
    customer_count
from q1
order by customer_count desc, product1_id, product2_id