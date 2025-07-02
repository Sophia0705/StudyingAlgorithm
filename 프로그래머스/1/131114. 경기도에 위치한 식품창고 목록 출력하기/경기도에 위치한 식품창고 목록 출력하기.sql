-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
 case when FREEZER_YN is null then 'N'
 else freezer_yn
 end as freezer_yn
from food_warehouse
where address like '경기도%'
order by warehouse_id;