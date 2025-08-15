# 28069. 김밥천국의 계단
import sys
input = sys.stdin.readline

N, K = map(int, input().split())    # N: 계단 개수, K: 계단 오르는 횟수
dp = [float('inf')]*(N+1)
# N개 계단을 K번만에 올라가 미니김밥 먹으면 minigimbob, else water
dp[0] = 0   # 초기값
for i in range(1, N+1):
    dp[i] = min(dp[i], dp[i-1]+1)
    # 순간이동
    if i + i//2 <= N:
        dp[i + i//2] = min(dp[i + i//2], dp[i]+1)

if dp[-1] <= K:
    print('minigimbob')
else:
    print('water')