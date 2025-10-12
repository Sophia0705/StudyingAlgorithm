-- 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회
with done as (select writer_id, sum(price) as total_price from used_goods_board 
              where status = 'DONE'
              group by writer_id having sum(price) >= 700000)

select u.user_id, u.nickname, d.total_price as total_sales
from used_goods_user u
join done d on u.user_id = d.writer_id
order by total_sales