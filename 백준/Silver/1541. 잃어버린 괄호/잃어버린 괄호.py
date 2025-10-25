# 1541. 잃어버린 괄호
import sys
input = sys.stdin.readline

exp = input().rstrip()
parts = exp.split('-')
# 첫 부분 숫자 다 더함(어차피 - 없어서 더해야 함)
answer = sum(map(int, parts[0].split('+')))
# 나머지는 다 빼기(-를 기준으로 뒤에 숫자는 괄호로 묶을 수 있으니까)
for part in parts[1:]:
    answer -= sum(map(int, part.split('+')))
print(answer)