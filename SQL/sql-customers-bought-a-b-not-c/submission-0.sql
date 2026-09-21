-- Write your query below

select c.customer_id, c.customer_name from customers c 

WHERE c.customer_id IN     (SELECT customer_id FROM orders WHERE product_name = 'A')
  AND c.customer_id IN     (SELECT customer_id FROM orders WHERE product_name = 'B')
  AND c.customer_id NOT IN (SELECT customer_id FROM orders WHERE product_name = 'C')

order by c.customer_name;