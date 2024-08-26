# 2178
# 최단거리 => BFS!!!
# 이동 방향 처리, 목표 지점 도착 확인 없음
from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
arr = [list(map(int, read().strip())) for _ in range(N)]


def BFS():
    Q = deque([(0, 0)])
    visited = [[0]*M for _ in range(N)]     # 단순 방문 체크X, 시작점으로부터의 거리 저장
    visited[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while Q:
        x, y = Q.popleft()
        if x == N-1 and y == M-1:   # 도착 했으면
            return visited[x][y]    # 도착 했을 때 해당 위치의 visited 값 return

        # 방향 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1     # visited[x][y] +1 : 현재 위치까지의 이동거리에서 한 칸 더 이동
                Q.append((nx, ny))      # 방향 이동하면서 큐 채우기

print(BFS())