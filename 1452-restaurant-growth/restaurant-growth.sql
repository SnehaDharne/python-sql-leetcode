SELECT distinct visited_on,
    ( SELECT SUM(AMOUNT)
      FROM CUSTOMER 
      WHERE VISITED_ON BETWEEN DATE_SUB(C.VISITED_ON, INTERVAL 6 DAY) AND C.VISITED_ON )
      AS amount,
    ROUND((SELECT SUM(AMOUNT)/7
      FROM CUSTOMER 
      WHERE VISITED_ON BETWEEN DATE_SUB(C.VISITED_ON, INTERVAL 6 DAY) AND C.VISITED_ON ),2)
      AS average_amount
FROM CUSTOMER C
where visited_on >= (
    select date_add(min(visited_on), interval 6 day)
    from customer
)
group by visited_on