import sys
input = sys.stdin.readline

n = int(input())
temp = []
for _ in range(n):
    x, y = map(int, input().split())
    temp.append((x, y))
temp.sort(key=lambda temp: (temp[1], temp[0]))

for x, y in temp:
    print(x, y)