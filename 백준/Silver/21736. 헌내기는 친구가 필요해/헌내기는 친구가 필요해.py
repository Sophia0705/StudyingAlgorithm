# 21736. 헌내기는 친구가 필요해
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global cnt
    Q = deque()
    visited[x][y] = True
    Q.append((x, y))
    while Q:
        r, c = Q.popleft()
        for dr, dc in move:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if campus[nr][nc] == 'O':
                    visited[nr][nc] = True
                    Q.append((nr, nc))
                elif campus[nr][nc] == 'P':
                    cnt += 1
                    visited[nr][nc] = True
                    Q.append((nr, nc))

N, M = map(int, input().split())
# I: 도연, P: 사람, O: 빈 공간, X: 벽
campus = [input().rstrip() for _ in range(N)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * M for _ in range(N)]
cnt = 0
# 도연이 위치찾기
for i, row in enumerate(campus):
    if 'I' in row:
        x = i
        y = row.index('I')
        break
bfs(x, y)
print(cnt if cnt else "TT")