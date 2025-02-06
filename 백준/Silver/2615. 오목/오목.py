import sys
input = sys.stdin.readline

def check_win(board, x, y):
    directions = [
        (0, 1),  # 가로
        (1, 0),  # 세로
        (1, 1),  # 대각선 오른쪽 아래
        (1, -1)  # 대각선 왼쪽 아래
    ]

    color = board[x][y]

    for dx, dy in directions:
        count = 1
        px, py = x, y  # 가장 왼쪽 위의 돌 위치 저장

        # 정방향 탐색
        nx, ny = x + dx, y + dy
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            count += 1
            if (ny < py) or (ny == py and nx < px):  # 더 왼쪽에 있는 돌 찾기
                px, py = nx, ny
            nx += dx
            ny += dy

        # 역방향 탐색
        nx, ny = x - dx, y - dy
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            count += 1
            if (ny < py) or (ny == py and nx < px):
                px, py = nx, ny
            nx -= dx
            ny -= dy

        # 정확히 5개인지 체크 (6목 방지)
        if count == 5:
            before_x, before_y = x - dx, y - dy
            after_x, after_y = x + 5 * dx, y + 5 * dy
            if (before_x < 0 or before_x >= 19 or before_y < 0 or before_y >= 19 or board[before_x][before_y] != color) and \
               (after_x < 0 or after_x >= 19 or after_y < 0 or after_y >= 19 or board[after_x][after_y] != color):
                return (color, px, py)

    return None

board = [list(map(int, input().split())) for _ in range(19)]

result = None
for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            res = check_win(board, x, y)
            if res:
                if result is None or (res[2] < result[2]) or (res[2] == result[2] and res[1] < result[1]):
                    result = res  # 가장 왼쪽 위의 돌 갱신

if result:
    print(result[0])
    print(result[1] + 1, result[2] + 1)
else:
    print(0)
