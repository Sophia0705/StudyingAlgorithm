select fh.flavor
from FIRST_HALF fh
join ICECREAM_INFO ii
on fh.flavor = ii.flavor
where TOTAL_ORDER > 3000 
       and INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER desc