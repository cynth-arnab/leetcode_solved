# Write your MySQL query statement below

select distinct p1.Email 
from person p1 
inner join person p2 
on p1.id != p2.id 
and p1.email = p2.email
