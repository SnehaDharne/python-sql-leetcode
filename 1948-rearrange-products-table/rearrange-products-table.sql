# Write your MySQL query statement below
select product_id, 
case when store1 is not null then 'store1' end as store, store1 as price
from Products
where store1 is not null

union all 
select product_id, 
case when store2 is not null then 'store2' end as store, store2 as price
from Products
where store2 is not null

union all
select product_id, 
case when store3 is not null then 'store3' end as store, store3 as price
from Products
where store3 is not null