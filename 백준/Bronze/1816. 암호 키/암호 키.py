# 1816. 암호 키
import sys
input = sys.stdin.readline

n = int(input())
s = [int(input().rstrip()) for _ in range(n)]
for num in s:
    for divd in range(2, 10**6+1):
        if num % divd == 0:
            print("NO")
            break
        elif divd == 10**6:
            print("YES")