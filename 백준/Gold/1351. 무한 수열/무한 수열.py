import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())
dp = {} # 메모이제이션 하는데 필요한 딕셔너리
def solve(N, P, Q, dp):
    if N == 0:
        return 1

    if N in dp: # 계산된 값 있을 때
        return dp[N]

    # N/P와 N/Q 값 더하는 계산식
    dp[N] = solve(N//P, P, Q, dp) + solve(N//Q, P, Q, dp)
    return dp[N]

print(solve(N, P, Q, dp))