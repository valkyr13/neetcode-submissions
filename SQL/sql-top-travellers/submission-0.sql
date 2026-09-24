-- Write your query below

select name, coalesce(travelled_distance, 0) as travelled_distance from users left join

(
    select user_id, sum(distance) 
    as travelled_distance from rides 
    group by user_id 

)  as m
on m.user_id=users.id 

order by travelled_distance desc,
users.name asc