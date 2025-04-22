
with q1 as (select user_id, count(user_id) as count_review from movierating group by user_id),
    q2 as (select movie_id, avg(rating) as avg_review 
            from movierating 
            where year(created_at) = 2020 and month(created_at) = 2
            group by movie_id),
    top_user as (select u.name as results 
            from q1 join users u on q1.user_id = u.user_id 
            order by q1.count_review desc, u.name asc limit 1
            ),
    top_movie as (select m.title as results
        from q2 join movies m on q2.movie_id = m.movie_id
        order by q2.avg_review desc, m.title asc limit 1
    )


select * from top_user
union all
select * from top_movie

