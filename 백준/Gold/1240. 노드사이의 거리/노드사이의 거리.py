# 1240. 노드사이의 거리
import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    Q = deque()
    visited = [False]*(N+1)
    visited[s] = True
    Q.append((s, 0))
    while Q:
        now, distance = Q.popleft()
        if now == e:
            return distance
        
        for i, dist in G[now]:
            if not visited[i]:
                visited[i] = True
                Q.append((i, distance+dist))


N, M = map(int, input().split())    # N:노드개수, M:거리 알려는 노드쌍 개수
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, dist = map(int, input().split())
    G[a].append((b, dist))
    G[b].append((a, dist))

for _ in range(M):
    n1, n2 = map(int, input().split())
    print(bfs(n1, n2))