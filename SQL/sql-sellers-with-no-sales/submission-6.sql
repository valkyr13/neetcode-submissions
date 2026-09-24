-- Write your query below

select seller.seller_name from seller 
 where not exists
(
select 1 from orders where seller.seller_id=orders.seller_id and extract(year from orders.sale_date)=2020 and sale_date >= '2020-01-01' and sale_date <= '2020-12-31'
)
order by seller_name asc;

