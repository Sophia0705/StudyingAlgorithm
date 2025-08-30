# 17271. 리그 오브 레전설 (Small)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 싸움시간, B스킬: M초 (A스킬: 1초)
dp = [1] * (N+1)

for i in range(M, N+1): # M초 보다 작으면 어차피 B스킬 못씀(A만 가능)
    dp[i] = (dp[i-1] + dp[i-M])

print(dp[N] % 1000000007)