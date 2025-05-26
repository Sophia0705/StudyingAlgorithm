# 11724. 연결 요소의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

def solve(graph):
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            # 방문처리
            dfs(i)
            cnt += 1
    return cnt

n, m = map(int, input().split())    # n: 정점 수, m: 간선 수
informs = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for u, v in informs:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
print(solve(graph))