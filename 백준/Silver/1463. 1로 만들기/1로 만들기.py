import sys
input = sys.stdin.readline

def solution(N):
    # DP 테이블 초기화 (0부터 N까지의 최소 연산 횟수)
    dp = [0] * (N + 1)

    # 1부터 시작
    for i in range(2, N + 1):
        # 기본적으로 1을 빼는 연산
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[N]

N = int(input())
print(solution(N))