-- Write your query below

select seller_name from

(select seller.seller_id, seller.seller_name from seller 
where not exists
(
select 1 from orders where orders.seller_id=seller.seller_id and extract(year from orders.sale_date)=2020

)


order by seller_name asc);
