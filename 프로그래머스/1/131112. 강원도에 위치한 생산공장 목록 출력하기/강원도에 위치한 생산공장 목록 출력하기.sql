select FACTORY_ID, FACTORY_NAME, ADDRESS
from FOOD_FACTORY
where address LIKE '강원도%'
order by factory_id;