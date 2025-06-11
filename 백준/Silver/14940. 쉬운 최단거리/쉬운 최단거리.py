# 14940. 쉬운 최단거리

import sys
input = sys.stdin.readline
from collections import deque

# 3. bfs로 각 지점까지 거리 계산(최단거리는 양방향이니까!)
# 큐에 목표지점 좌표와 거리 0을 넣고 시작
# 상하좌우로 이동하면서:
#   - 갈 수 있는 곳(1)이면서 아직 방문 안한 곳이면
#   - 거리를 1 증가시켜서 큐에 추가
def bfs(start_row, start_col):
    Q = deque()
    # 시작점 추가
    Q.append((start_row, start_col, 0)) # 행,열,거리 (거리 0부터 시작)

    # 상하좌우
    while Q:
        row, col, dist = Q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row+dr, col+dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and answer[nr][nc] == -1:  # answer[nr][nc]==-1이면 방문 안한 곳이니까
                answer[nr][nc] = dist + 1
                Q.append((nr, nc, dist+1))

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = []
# 0: X, 1: O, 2: target
# 1. 목표 찾기
# maps를 순회하면서 값이 2인 곳의 좌표를 찾아서 저장
target_row, target_col = None, None
for row in range(n):
    for col in range(m):
        if maps[row][col] == 2: # 목표
            target_row, target_col = row, col
            break
    if target_row is not None:  # 목표 찾았으면 종료
        break

# 2. 결과 배열 초기화
# - 원래 0인 곳: 0으로 유지
# - 목표지점: 0으로 설정
# - 원래 1인 곳: 일단 -1로 설정 (나중에 도달하면 거리로 변경)
for row in range(n):
    temp = []
    for col in range(m):
        if maps[row][col] == 0: # 못가
            temp.append(0)
        elif maps[row][col] == 2: # 목표
            temp.append(0)
        elif maps[row][col] == 1: # 갈 수 있어
            temp.append(-1) # 나중에 바꿀거니까 일단 -1
    answer.append(temp)

bfs(target_row, target_col)
for r in answer:
    print(*r)