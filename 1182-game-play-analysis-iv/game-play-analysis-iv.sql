-- with q1 as (select  count(distinct a1.player_id) as count1 from activity a1 join activity a2
-- on a2.event_date = DATE_ADD(a1.event_date, INTERVAL 1 DAY))

-- select round(q1.count1/(count(distinct player_id)),2) as fraction
-- from q1, activity

with b1 as (select distinct player_id, min(event_date) 
            as first_login 
            from activity 
            group by player_id),
    b2 as (select b1.player_id 
            from b1 
            where date_add(b1.first_login, interval 1 day) in 
                (select a.event_date 
                from activity a
                where  a.player_id = b1.player_id))

select ifnull(round(count(distinct(b2.player_id)) / count(distinct a2.player_id),2),0) as fraction from b2, activity a2