with q1 as (
    select
        s.student_id,
        s.subject,
        min(s.exam_date) as first_date,
        (select score from scores s2
         where s2.student_id = s.student_id
           and s2.subject = s.subject
           and s2.exam_date = min(s.exam_date)
         limit 1) as first_score
    from
        scores s
    group by
        s.student_id, s.subject
),
q2 as (
    select
        s.student_id,
        s.subject,
        max(s.exam_date) as latest_date,
        (select score from scores s2
         where s2.student_id = s.student_id
           and s2.subject = s.subject
           and s2.exam_date = max(s.exam_date)
         order by s2.exam_date desc -- Optional, but good practice for clarity
         limit 1) as latest_score
    from
        scores s
    group by
        s.student_id, s.subject
)
select
    q1.student_id,
    q1.subject,
    q1.first_score,
    q2.latest_score
from
    q1
join
    q2 on q1.student_id = q2.student_id and q1.subject = q2.subject
where q1.first_score < q2.latest_score and
     q1.first_date != q2.latest_score
order by q1.student_id, q1.subject