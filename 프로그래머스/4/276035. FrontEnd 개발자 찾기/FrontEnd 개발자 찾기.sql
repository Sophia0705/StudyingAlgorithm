-- 코드를 작성해주세요
select distinct d.id, d.email, d.first_name, d.last_name
from developers d, skillcodes s
where s.category = 'Front End' and d.skill_code & s.code != 0
order by d.id
