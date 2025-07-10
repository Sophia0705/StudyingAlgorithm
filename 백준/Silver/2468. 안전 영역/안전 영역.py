# 2468. 안전 영역
# 장마철에 물에 잠기지 않는 안전 영역의 최대 개수
import sys
input = sys.stdin.readline
from collections import deque

def BFS(row, col, h):
    Q = deque()
    Q.append((row, col))
    visited[row][col] = True
    while Q:
        r, c = Q.popleft()
        for dr, dc in move:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] > h:
                visited[nr][nc] = True
                Q.append((nr, nc))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maxcnt = 0
maxH = max(map(max, arr))

for h in range(0, maxH+1):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > h:
                BFS(r, c, h)
                cnt += 1
    maxcnt = max(maxcnt, cnt)

print(maxcnt)