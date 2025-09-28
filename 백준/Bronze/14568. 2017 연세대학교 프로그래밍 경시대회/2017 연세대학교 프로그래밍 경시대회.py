# 14568. 2017 연세대학교 프로그래밍 경시대회
import sys
input = sys.stdin.readline
from itertools import product

# a, b, c : 택희, 영훈, 남규 -> (a, b, c) 수
n = int(input())    # 사탕의 총 개수
possible = [i for i in range(1, n)]
ans = 0
pros = product(possible, repeat=3)
for pro in pros:
    if sum(pro) != n:
        continue
    a, b, c = pro[0], pro[1], pro[2]
    if c >= b + 2 and a % 2 == 0:
        ans += 1
print(ans)