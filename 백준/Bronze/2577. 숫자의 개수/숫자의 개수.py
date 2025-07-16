# 2577. 숫자의 개수
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
T = str(a*b*c)
ans = [0] * 10

for chr in T:
    if chr.isdigit():
        ans[int(chr)] += 1

for a in ans:
    print(a)