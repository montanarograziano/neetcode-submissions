-- Write your query below
select c.name
from customers c
where c.id not in (select distinct customer_id from orders)