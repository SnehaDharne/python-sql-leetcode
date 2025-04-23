# Write your MySQL query statement below
with q1 as  (select income, case 
    when income < 20000 then 'Low Salary'
    when income >= 20000 and income <= 50000 then 'Average Salary'
    else 'High Salary'
    end as category
    from accounts
),
q2 as (select 'Low Salary' as category
    union all
    select 'Average Salary'
    union all
    select 'High Salary')

select q2.category, ifnull(count(q1.category),0) as accounts_count
from q1 right join q2 on q1.category = q2.category
group by q2.category
