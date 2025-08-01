# 1389. 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()
ans = 0
Pn = 'I'+('OI')*N
Plen = len(Pn)

for i in range(M):
    # S에서 N 길이만큼 비교하면서 Pn이랑 일치하면 ans += 1
    if S[i:i+Plen] == Pn:
        ans += 1

print(ans)