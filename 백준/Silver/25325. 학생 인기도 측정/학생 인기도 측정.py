# 25325. 학생 인기도 측정
import sys
input = sys.stdin.readline

N = int(input())
counts = dict()
names = input().split()
for name in names:
    counts[name] = 0

for _ in range(N):
    S = input().split()
    for name in S:
        counts[name] += 1

ans = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
for name, count in ans:
    print(name, count)