# 2630. 색종이 만들기

import sys
input = sys.stdin.readline

def solve(x, y, n):
    global cnt0, cnt1
    temp = set()    # 색상 체크

    # 기저 조건
    if n == 1:
        if arr[x][y] == 0:
            cnt0 += 1
        else:
            cnt1 += 1
        return

    for i in range(x, x+n):
        for j in range(y, y+n):
            temp.add(arr[i][j])

    # 같은 색이면
    if len(temp) == 1:
        color = temp.pop()
        if color == 0:
            cnt0 += 1
        elif color == 1:
            cnt1 += 1
    else:
        # 🌟사분면 분할
        next_n = n//2
        solve(x, y, next_n)
        solve(x, y+next_n, next_n)
        solve(x+next_n, y, next_n)
        solve(x+next_n, y+next_n, next_n)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]   # 0: 흰색, 1: 파란색
cnt0, cnt1= 0, 0
solve(0, 0, n)
print(cnt0)
print(cnt1)