import sys
from collections import deque
input = sys.stdin.readline

# 녹는거 확인 --> 주변 바다 개수만큼 녹음
def melt(arr):
    melted = [[0] * M for _ in range(N)]    # 각 빙산이 녹을 양 임시 저장
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                sea_count = 0
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    # 바다(0)이고 배열 범위 내이면
                    if arr[nr][nc] == 0 and 0 <= nr < N and 0 <= nc < M:
                        sea_count += 1
                melted[r][c] = sea_count

    # 빙산 높이 조정
    for r in range(N):
        for c in range(M):
            arr[r][c] = max(0, arr[r][c] - melted[r][c])    # 바다는 0이니까 더 내려가면 안됨
    return arr

# 빙산 덩어리 수 확인
def check(arr):
    visited = [[False] * M for _ in range(N)]
    groups = 0

    def bfs(sr, sc):
        Q = deque([(sr, sc)])
        visited[sr][sc] = True
        while Q:
            r, c = Q.popleft()
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                # 배열 범위 내, 빙산 있고, 방문X
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] > 0 and not visited[nr][nc]:
                    Q.append((nr, nc))
                    visited[nr][nc] = True

    # 모든 빙산 위치 탐색
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0 and not visited[r][c]:
                bfs(r, c)
                groups += 1
    return groups

N, M = map(int, input().split())    # 행, 열 개수
arr = [list(map(int, input().split())) for _ in range(N)]   # 빙산
year = 0 # 다 녹을 때까지 분리 안 되면 0

while True:
    # 모든 빙산 녹았는지 확인
    if sum(sum(row) for row in arr) == 0:
        year = 0
        break

    # 빙산 덩어리 수 확인
    groups = check(arr)
    if groups >= 2:
        break

    # 빙산 녹이기
    arr = melt(arr)
    year += 1

print(year)