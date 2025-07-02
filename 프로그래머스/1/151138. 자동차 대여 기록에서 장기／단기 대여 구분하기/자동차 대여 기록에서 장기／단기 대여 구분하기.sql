-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, date_format(START_DATE, '%Y-%m-%d') as start_date, date_format(END_DATE, '%Y-%m-%d') as end_date, 
    case when datediff(end_date, start_date) +1 >= 30 then '장기 대여'
    else '단기 대여'
    end
as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date between '2022-09-01' and '2022-09-30'
order by history_id desc;