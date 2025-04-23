# Write your MySQL query statement below
select distinct * 
from stadium 
where people >= 100 and 
      ((id+1 in  (select id from stadium where people >= 100) and 
      id+2 in (select id from stadium where people >= 100) ) or 
        (id-1 in  (select id from stadium where people >= 100) and 
      id-2 in (select id from stadium where people >= 100)) or 
      (id-1 in  (select id from stadium where people >= 100) and 
        id+1 in (select id from stadium where people >= 100) )
      )