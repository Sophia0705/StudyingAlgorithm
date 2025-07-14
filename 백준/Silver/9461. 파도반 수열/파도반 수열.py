# 9461. 파도반 수열
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * 101

    for i in range(101):
        if i < 3:
            dp[i] = 1
        else:
            dp[i] = dp[i-2] + dp[i-3]

    print(dp[N-1])