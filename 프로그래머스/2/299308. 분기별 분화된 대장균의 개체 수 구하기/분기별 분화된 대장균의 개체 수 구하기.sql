-- 코드를 작성해주세요
select
    case when month(differentiation_date) between '01' and '03' then '1Q'
        when month(differentiation_date) between '04' and '06' then '2Q'
        when month(differentiation_date) between '07' and '09' then '3Q'
        when month(differentiation_date) between '10' and '12' then '4Q'
    end as quarter, count(id) as ecoli_count
from ecoli_data
group by quarter
order by quarter