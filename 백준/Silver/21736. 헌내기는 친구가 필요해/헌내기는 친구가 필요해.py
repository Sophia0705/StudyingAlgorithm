# 21736. 헌내기는 친구가 필요해
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(x, y):
    global cnt
    visited[x][y] = True
    # 도연이 위치부터 탐색(x, y)
    for di, dj in move:
        ni, nj = x + di, y + dj
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if campus[ni][nj] == 'O':
                visited[ni][nj] = True
                dfs(ni, nj)
            elif campus[ni][nj] == 'P':
                visited[ni][nj] = True
                cnt += 1
                dfs(ni, nj)
    return cnt

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
dfs(x, y)
print(cnt if cnt else "TT")
