-- 코드를 작성해주세요
-- 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회
select sum(g.score) as score, e.emp_no, e.emp_name, e.position, e.email
from hr_employees e
join hr_grade g on e.emp_no = g.emp_no
group by emp_no
order by score desc limit 1