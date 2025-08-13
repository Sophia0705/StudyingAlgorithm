# 13459. 구슬 탈출
import sys
input = sys.stdin.readline
from collections import deque

def tilt(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by):
    Q = deque()
    visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    Q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

    while Q:
        rx, ry, bx, by, depth = Q.popleft()
        if depth >= 10:
            break

        for dx, dy in dirs:
            nrx, nry, rcnt = tilt(rx, ry, dx, dy)
            nbx, nby, bcnt = tilt(bx, by, dx, dy)

            # 파란 구슬 빠지면 실패
            if board[nbx][nby] == 'O':
                continue
            # 빨간 구슬 빠지면 성공
            if board[nrx][nry] == 'O':
                return 1

            # 같은 위치면 이동거리 큰쪽을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                Q.append((nrx, nry, nbx, nby, depth+1))
    return 0

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            rx, ry = r, c
        elif board[r][c] == 'B':
            bx, by = r, c

print(bfs(rx, ry, bx, by))