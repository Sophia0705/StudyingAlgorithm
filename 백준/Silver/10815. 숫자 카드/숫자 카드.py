import sys
input = sys.stdin.readline

n = int(input())
num_cards = set(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))
ans = []

for chk in checks:
    if chk in num_cards:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)
