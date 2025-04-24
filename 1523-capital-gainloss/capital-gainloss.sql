# Write your MySQL query statement below
with q1 as (select * from stocks where operation = 'Buy'),
    q2 as (select * from stocks where operation = 'Sell'),
    q3 as (select distinct stock_name, sum(price) as buy from q1 group by stock_name),
    q4 as (select distinct stock_name, sum(price) as sell from q2 group by stock_name)
select q3.stock_name, (q4.sell - q3.buy) as capital_gain_loss from q3 join q4 on q3.stock_name = q4.stock_name

