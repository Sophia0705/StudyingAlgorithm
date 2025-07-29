# 1759. 암호 만들기
import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
strs = list(input().split())
strs.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}
ans = []
combs = list(combinations(strs, L))
for c in combs:
    v_cnt = len(set(c) & vowels)    # 모음 개수
    if v_cnt >= 1 and (L-v_cnt) >= 2:
        ans.append(c)

for a in ans:
    print(''.join(a))