# 27971. 강아지는 많을수록 좋다
import sys
input = sys.stdin.readline
from collections import deque

N, M, A, B = map(int, input().split())  # N: 키우기 원하는 강아지 수, M: 닫힌 구간 수
dp = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        visited[i] = True

dp[N] = 0
q = deque()
q.append(N)
while q:
    value = q.popleft()
    if value == 0:
        break
    for i in (value-A, value-B):
        if i >= 0:
            if visited[i]:
                continue
            else:
                q.append(i)
                dp[i] = dp[value] +1
                visited[i] = True
if dp[0]:
    print(dp[0])
else:
    print(-1)