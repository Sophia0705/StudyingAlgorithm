# 2667 단지 번호 붙이기
from collections import deque
# 방문한 집은 0 으로 만들어서 연결된 집만 찾기(중복 방문X)
def bfs(row, col):
    Q = deque()
    global cnt
    Q.append((row, col))    # 시작점
    cnt += 1
    arr[row][col] = 0

    while Q:
        row, col = Q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:    # 범위, 값 체크
                Q.append((nr, nc))
                cnt += 1
                arr[nr][nc] = 0

N = int(input())     # 지도의 크기
arr = [list(map(int, input())) for _ in range(N)]
# print(N, arr)
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:  # 집일 때만
            cnt = 0
            bfs(i, j)
            result.append(cnt)
result.sort()
print(len(result))
print(*result, sep='\n')