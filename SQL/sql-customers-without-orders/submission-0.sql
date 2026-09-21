-- Write your query below

select C.name from customers C LEFT JOIN orders O ON C.id = O.customer_id where O.customer_id IS NULL;
