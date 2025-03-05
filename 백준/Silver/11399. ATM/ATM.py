import sys
input = sys.stdin.readline

N = int(input())
takes = list(map(int, input().split()))
takes.sort()
temp = 0
answer = 0

for take in takes:
    temp += take
    answer += temp

print(answer)