# 11403. 경로 찾기 in DFS(stack)

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = []

for i in range(n):
    visited = [False] * n
    stack = [i]

    while stack:
        cur = stack.pop()
        for next in range(n):
            if arr[cur][next] == 1 and not visited[next]:
                visited[next] = True
                stack.append(next)
    ans.append([1 if visited[j] else 0 for j in range(n)])

for r in ans:
    print(*r)