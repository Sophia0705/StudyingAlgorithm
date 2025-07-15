# 17626. Four Squares
import sys, math
input = sys.stdin.readline

n = int(input())
dp = [0]*50001

for num in range(50001):
    if int(math.sqrt(num))**2 == num:
        dp[num] = 1
    else:
        # num보다 작은 제곱 수 빼고 남은 수 만드는 개수 +1
        dp[num] = float('inf')

        for i in range(1, int(math.sqrt(num))+1):
            dp[num] = min(dp[num], dp[num-i**2]+1)

print(dp[n])