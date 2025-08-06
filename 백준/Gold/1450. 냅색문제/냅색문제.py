# 1450. 냅색문제
import sys
input = sys.stdin.readline
from itertools import combinations

# 부분집합 합
def sum_subset(arr):
    res = []
    for i in range(len(arr)+1):
        for comb in combinations(arr, i):
            res.append(sum(comb))
    return res

# 이분탐색 → 맨 왼쪽 return
def bisearch(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid +1
        else:
            right = mid
    return left

N, C = map(int, input().split())    # N: 물건 개수, C: 가방 최대무게
weights = list(map(int, input().split()))
# weights 반 가르기
left, right = weights[:N//2], weights[N//2:]
L, R = sum_subset(left), sum_subset(right)
R.sort()

# 조합 수 계산
cnt = 0
for l in L:
    remain = C - l
    cnt += bisearch(R, remain)

print(cnt)