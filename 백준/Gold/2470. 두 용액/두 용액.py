import sys
input = sys.stdin.readline

n = int(input())
attrs = list(map(int, input().split()))
attrs.sort()

start, end = 0, n-1
ans = [attrs[start], attrs[end]]
sumV = abs(attrs[0] + attrs[n-1])

while start < end:
    temp = attrs[start] + attrs[end]

    if abs(temp) < sumV:
        sumV = abs(temp)
        ans = [attrs[start], attrs[end]]

    if temp < 0:
        start += 1
    elif temp > 0:
        end -= 1
    elif temp == 0:
        break

print(*ans)