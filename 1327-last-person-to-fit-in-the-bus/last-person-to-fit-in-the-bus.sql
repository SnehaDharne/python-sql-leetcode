# Write your MySQL query statement below
with q1 as (SELECT person_name, SUM(weight) OVER (ORDER BY turn asc) as total_weight
        FROM queue)
select person_name from q1 where total_weight <=1000 order by total_weight desc limit 1