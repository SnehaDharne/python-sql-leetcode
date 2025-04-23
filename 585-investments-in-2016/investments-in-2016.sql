# Write your MySQL query statement below
with q1 as (
    select i1.tiv_2016
    from insurance i1
    where i1.tiv_2015 in (select distinct i2.tiv_2015 from insurance i2 where i1.pid != i2.pid) and 
          i1.lat not in (select distinct i3.lat from insurance i3 where i1.pid != i3.pid and i1.lon = i3.lon) and
          i1.lon not in (select distinct i4.lat from insurance i4 where i4.pid != i4.pid and i1.lat = i4.lat)

    )

select ifnull(round(sum(q1.tiv_2016),2),0) as tiv_2016 from q1 