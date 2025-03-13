import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or fields[j][i] == 0: # 범위를 벗어나거나 배추 없으면(원래 범위 체크, 값 비교와 반대)
        return False

    fields[j][i] = 0    # 현재 위치 배추 방문 처리

    # 상하좌우 dfs
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i+1, j)
    dfs(i, j-1)

    return True

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split()) # m: 가로 길이, n: 세로 길이, k: 배추 심어진 위치 개수
    fields = [[0]*m for _ in range(n)]  # 배추밭
    for _ in range(k):
        x, y = map(int, input().split())
        fields[y][x] = 1    # 배추 위치 표시
    cnt = 0
    for i in range(m):
        for j in range(n):
            if fields[j][i] == 1:
                if dfs(i, j):
                    cnt += 1
    print(cnt)