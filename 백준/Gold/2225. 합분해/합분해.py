import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1000000000

# dp[k][n] : k개의 수를 더해서 합이 n이 되는 경우의 수
dp = [[0] * (N + 1) for _ in range(K + 1)]

# 초기화: 1개의 수로 n을 만드는 방법은 1가지
dp[1] = [1] * (N + 1)

# k개의 수를 사용하여 n을 만드는 경우
for k in range(2, K + 1):
    for n in range(N + 1):
        # L을 현재 숫자로 사용할 때,
        # dp[k][n] = dp[k-1][0] + dp[k-1][1] + ... + dp[k-1][n]
        for l in range(n + 1):
            dp[k][n] = (dp[k][n] + dp[k-1][n-l]) % MOD

print(dp[K][N])