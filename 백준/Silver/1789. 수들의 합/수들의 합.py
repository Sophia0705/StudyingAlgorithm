# 1789. 수들의 합
import sys
input = sys.stdin.readline

s = int(input())
# n개의 자연수 합 == s
# n의 최댓값?
n, temp = 1, 0

while True:
    temp += n
    if temp > s:
        n -= 1
        break
    elif temp == s:
        break
    n += 1

print(n)