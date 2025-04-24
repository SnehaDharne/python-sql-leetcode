# Write your MySQL query statement below
-- with q1 as (select * from stocks where operation = 'Buy'),
--     q2 as (select * from stocks where operation = 'Sell'),
--     q3 as (select distinct stock_name, sum(price) as buy from q1 group by stock_name),
--     q4 as (select distinct stock_name, sum(price) as sell from q2 group by stock_name)
-- select q3.stock_name, (q4.sell - q3.buy) as capital_gain_loss from q3 join q4 on q3.stock_name = q4.stock_name


select distinct s1.stock_name, 
    ((select sum(s2.price) from stocks s2 where s2.stock_name = s1.stock_name and s2.operation = 'Sell') - 
    (select sum(s3.price) from stocks s3 where s3.stock_name = s1.stock_name and s3.operation = 'Buy')) as capital_gain_loss
 from stocks s1 group by stock_name
