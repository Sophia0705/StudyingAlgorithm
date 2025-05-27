# 18870. 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(set(nums))
idxs = []
ans = {}

for i in range(len(sorted_nums)):
    idxs.append(i)

for idx, num in enumerate(sorted_nums):
    ans[num] = idx

result = [ans[num] for num in nums]
print(*result)