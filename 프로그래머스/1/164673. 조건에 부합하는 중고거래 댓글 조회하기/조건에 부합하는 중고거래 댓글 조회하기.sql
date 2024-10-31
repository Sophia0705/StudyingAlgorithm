select B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, date_format(R.CREATED_DATE, '%Y-%m-%d') as created_date
from USED_GOODS_BOARD B
join USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
where date_format(B.created_date, '%Y-%m') = '2022-10'
order by R.created_date asc, B.title asc;