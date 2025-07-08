# 6603. 로또

import sys
input = sys.stdin.readline
from itertools import combinations

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    k = numbers.pop(0)

    comb = combinations(numbers, 6)
    for c in comb:
        print(*c)
    print()
