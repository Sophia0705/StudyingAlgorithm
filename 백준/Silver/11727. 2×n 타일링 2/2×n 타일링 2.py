import sys
input = sys.stdin.readline

n = int(input())

# DP 테이블 초기화
dp = [0] * (n + 1)

# 기본 값
if n >= 1:
    dp[1] = 1  # 2×1 크기는 1가지 방법
if n >= 2:
    dp[2] = 3  # 2×2 크기는 3가지 방법

# 점화식을 이용한 DP 계산
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[n])