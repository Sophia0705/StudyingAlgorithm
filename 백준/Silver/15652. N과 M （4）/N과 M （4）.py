# 중복 조합
from itertools import combinations_with_replacement

n, m = map(int, input().split())

numbers = range(1, n+1)

for comb in combinations_with_replacement(numbers, m):
    print(*comb)