# Write your MySQL query statement below
select u.name, sum(t.amount) as balance
from transactions t left join users u 
    on t.account = u.account
group by t.account 
having balance > 10000