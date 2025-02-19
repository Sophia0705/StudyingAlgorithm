import sys
input = sys.stdin.readline

chr1 = input().strip()
chr2 = input().strip()

# dp 테이블 초기화
n, m = len(chr1), len(chr2)
dp = [[0]*(m+1) for _ in range(n+1)]    # (n+1)*(m+1)

# dp 계산
for i in range(1, n+1):
    for j in range(1, m+1):
        if chr1[i-1] == chr2[j-1]: # 두 문자 같을 때 LCS 연장
            dp[i][j] = dp[i-1][j-1]+1
        else:   # 다를 때 이전 상태 최댓값
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])
