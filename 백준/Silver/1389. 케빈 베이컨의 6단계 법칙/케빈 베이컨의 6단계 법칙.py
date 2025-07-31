# 1389. 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    Q = deque()
    visited = [False] * (N + 1)
    step = 0
    Q.append((start, 0))
    while Q:
        now, distance = Q.popleft()
        step += distance
        for nei in G[now]:
            if not visited[nei]:
                visited[nei] = True
                Q.append((nei, distance+1))
    return step



N, M = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(M)]
minlist = [0]*(N+1)
G = [[] for _ in range(N+1)]

# 그래프 연결
for a, b in relations:
    G[a].append(b)
    G[b].append(a)

# 순회
for i in range(1, N+1):
    minlist[i] = bfs(i)

minV = min(minlist[1:])
print(minlist.index(minV))