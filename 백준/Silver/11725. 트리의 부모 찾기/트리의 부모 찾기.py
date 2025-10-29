# 11725. 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, p):
    for nei in graph[node]:
        if nei == p:
            continue
        parents[nei] = node
        dfs(nei, node)

n = int(input())    # 노드 개수
graph = [[] for _ in range(n+1)]
parents = [0]*(n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

for i in range(2, n+1):
    print(parents[i])