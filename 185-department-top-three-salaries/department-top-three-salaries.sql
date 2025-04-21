/* Write your T-SQL query statement below */
with q1 as (select dense_rank() over(partition by departmentid order by salary desc) as rank_salary, 
            salary, 
            name, 
            departmentId
            from employee)

select d.name as Department, q1.name as Employee, Salary
from q1 join department d on q1.departmentId = d.id
where q1.rank_salary < 4

