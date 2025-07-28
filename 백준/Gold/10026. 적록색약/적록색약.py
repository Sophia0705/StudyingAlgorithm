# 10026. 적록색약
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(r, c, target):
    visited[r][c] = True
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if pic[nr][nc] == target:
                dfs(nr, nc, target)

N = int(input())
pic = [list(input().rstrip()) for _ in range(N)]  # str은 immutable이라 수정X -> list!
visited = [[False]*N for _ in range(N)]
cnt1, cnt2 = 0, 0
# 적록색약X
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            dfs(r, c, pic[r][c])
            cnt1 += 1

# 적록색약 탐색 위해 변경
for r in range(N):
    for c in range(N):
        if pic[r][c] == 'G':
            pic[r][c] = 'R'
# 적록색약 탐색 전 원복
visited = [[False]*N for _ in range(N)]

# 적록색약
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            dfs(r, c, pic[r][c])
            cnt2 += 1

print(cnt1, cnt2)