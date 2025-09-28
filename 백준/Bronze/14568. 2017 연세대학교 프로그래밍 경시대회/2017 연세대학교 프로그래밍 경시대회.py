# 14568. 2017 연세대학교 프로그래밍 경시대회
import sys
input = sys.stdin.readline
from itertools import product

# a, b, c : 택희, 영훈, 남규 -> (a, b, c) 수
n = int(input())    # 사탕의 총 개수
ans = 0
for a in range(1, n):   # 택희
    for b in range(1, n):   # 영훈
        for c in range(1, n):   # 남규
            if a + b + c == n and c >= b+2 and a % 2 == 0:
                ans += 1
print(ans)