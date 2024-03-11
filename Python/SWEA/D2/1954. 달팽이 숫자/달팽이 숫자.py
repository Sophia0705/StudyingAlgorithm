T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    d = 0
    row = col = 0
    num = 1
    while num <= N*N:
        arr[row][col] = num
        num += 1
        nr = row + dr[d]
        nc = col + dc[d]
        if nr < 0 or nr >= N or nc <0 or nc >= N or arr[nr][nc] != 0:
            d = (d+1)%4
        row = row + dr[d]
        col = col + dc[d]

    print(f'#{tc}')
    for row in arr:
        print(*row)