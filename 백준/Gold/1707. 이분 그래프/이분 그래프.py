import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(start, set):
    visited[start] = set
    
    for i in graph[start]:
        if not visited[i]:
            if not DFS(i, -1 * set):
                return False
        elif visited[i] == visited[start]:
            return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    ans = True
    for i in range(1, V+1):
        if not visited[i]:
            ans = DFS(i, 1)
            if not ans:
                break
    
    if ans == True:
        print('YES')
    else:
        print('NO')