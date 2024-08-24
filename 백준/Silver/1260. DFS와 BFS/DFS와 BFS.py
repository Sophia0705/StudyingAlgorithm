# 1260
from collections import deque
import sys

read = sys.stdin.readline

N, M, V = map(int, read().split())     # N: 정점 수, M: 간선 수, V: 시작 정점
graph = [[0] * (N+1) for _ in range(N+1)]
visited1 = [-1] * (N+1)
visited2 = [-1] * (N+1)

def DFS(v):
    visited1[v] = 1
    print(v, end=" ")
    for i in range(1, N+1):
        if visited1[i] == -1 and graph[v][i] == 1:
            DFS(i)

def BFS(v):
    Q = deque()
    Q.append(v)
    visited2[v] = 1
    while Q:
        v = Q.popleft()
        print(v, end=" ")
        for i in range(1, N+1):
            if visited2[i] == -1 and graph[v][i] == 1:
                Q.append(i)
                visited2[i] = 1



for _ in range(M):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1

DFS(V)
print()
BFS(V)