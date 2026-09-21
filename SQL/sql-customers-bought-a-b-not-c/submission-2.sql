-- Write your query below

select c.customer_id, c.customer_name from customers c 

where exists  
( SELECT 1 FROM orders where customer_id = c.customer_id and product_name = 'A')

 and  exists  (SELECT 1 FROM orders where  customer_id = c.customer_id and product_name = 'B')

  and  not exists (SELECT 1 FROM orders where  customer_id = c.customer_id and product_name = 'C')

order by c.customer_name;