n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
cnt = []

# 8x8 체스판 만들기
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        white = black = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if arr[a][b] != 'W':
                        black += 1
                    else:
                        white += 1
        cnt.append(white)
        cnt.append(black)
print(min(cnt))