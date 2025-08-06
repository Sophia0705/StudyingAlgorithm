# 1781. 컵라면
import sys
input = sys.stdin.readline
import heapq

N = int(input())    # N: 숙제 개수
problems = []
for _ in range(N):
    dl, cn = map(int, input().split())  # dl: 데드라인, cn:컵라면 수
    problems.append((dl, cn))
problems.sort(key=lambda x: (x[0], -x[1]))

hq = []
for dl, cn in problems:
    heapq.heappush(hq, cn)
    if len(hq) > dl:    # 데드라인보다 크면, 가장 컵라면 적게받는 거 빼기
        heapq.heappop(hq)
print(sum(hq))