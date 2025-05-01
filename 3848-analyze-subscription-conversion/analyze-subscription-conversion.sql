# Write your MySQL query statement below
with users as (
    select u1.user_id 
    from useractivity u1
    where u1.activity_type = 'paid' and u1.user_id in (select u2.user_id from useractivity u2 where u2.activity_type = 'free_trial')
)
select users.user_id, 
    round(avg(case when activity_type = 'free_trial' then activity_duration end),2) as trial_avg_duration,
    round(avg(case when activity_type = 'paid' then activity_duration end),2) as paid_avg_duration
from users inner join useractivity on users.user_id = useractivity.user_id
group by users.user_id
order by users.user_id