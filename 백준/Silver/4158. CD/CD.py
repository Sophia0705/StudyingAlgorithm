# 4158. CD
import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    Sang_has = [int(input()) for _ in range(N)]
    Sun_has = [int(input()) for _ in range(M)]
    ans = list(set(Sang_has) & set(Sun_has))
    print(len(ans))