import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, set):
    Q = deque([start])  # 시작 정점 같은 큐에
    visited[start] = set    # 시작 정점 set로
    while Q:
        t = Q.popleft()

        for i in graph[t]:  # 해당 정점에서 갈 수 있는 정점들 순회
            if not visited[i]:  # 방문 안했으면
                Q.append(i)
                visited[i] = -1 * visited[t]    # 다른 set로
            elif visited[i] == visited[t]: # 방문한 정점인데 같은 set면
                return False
    return True

K = int(input())    # 테스트 케이스 개수
for _ in range(K):
    V, E = map(int, input().split())    # 정점의 개수, 간선의 개수
    graph = [[] for _ in range(V+1)]    # 그래프
    visited = [False] * (V+1)   # 방문 체크
    for _ in range(E):
        u, v = map(int, input().split())    # 인접한 정점
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1): # 정점 1부터 시작
        if not visited[i]:  # 방문 안 한 정점이면
            ans = BFS(i, 1)
            if not ans:
                break

    if ans == True:
        print('YES')
    else:
        print('NO')