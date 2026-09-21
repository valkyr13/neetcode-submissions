-- Write your query below

-- The golden rule for deciding between them is simple: Use JOIN when you need to retrieve or display data from the related table, and use EXISTS when you only need to filter your main table based on whether matching data exists in the related table

select c.customer_id, c.customer_name from customers c 
where exists 

( SELECT 1 FROM orders where customer_id = c.customer_id and product_name = 'A')

and  exists  (SELECT 1 FROM orders where customer_id = c.customer_id and product_name = 'B')

and  not exists (SELECT 1 FROM orders where customer_id = c.customer_id and product_name = 'C')

order by c.customer_name;