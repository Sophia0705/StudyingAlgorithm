# 15663. N과 M(9)

import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()  # 사전순 출력을 위해 정렬
perm_set = set(permutations(nums, M))  # 중복 제거

# 다시 리스트로 바꿔 정렬
result = sorted(perm_set)

for p in result:
    print(' '.join(map(str, p)))