n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
maxV = 0

for i in range(n):
    for j in range(m):
        for k in range(min(n-i, m-j)):
            if (board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]):
                maxV = max(maxV, (k+1)*(k+1))

print(maxV)