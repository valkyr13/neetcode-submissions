-- Write your query below

-- The golden rule for deciding between them is simple: Use JOIN when you need to retrieve or display data from the related table, and use EXISTS when you only need to filter your main table based on whether matching data exists in the related table


select customer_id, customer_name from customers

where exists 
(select 1 from orders where customers.customer_id = orders.customer_id and product_name='A')
 
and exists
(select 1 from orders where customers.customer_id = orders.customer_id and product_name='B')

and not exists
(select 1 from orders where customers.customer_id = orders.customer_id and product_name='C')

order by customer_name;
