-- 코드를 입력하세요
SELECT p.product_id, p.product_name, sum(p.price * o.amount) as total_sales
from food_product p 
join food_order o on o.product_id = p.product_id
where o.produce_date like '2022-05%'
group by p.product_id, p.product_name
order by total_sales desc, o.product_id