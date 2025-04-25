# Write your MySQL query statement below
with q1 as (select employee_id from employees where employee_id not in (select s.employee_id from salaries s)

union all

select employee_id from salaries where employee_id not in (select e.employee_id from employees e))

select * from q1 order by employee_id