select BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book
where DATE_FORMAT(published_date, '%Y') = '2021' and category = '인문'
order by published_date;