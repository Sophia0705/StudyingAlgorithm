import sys
input = sys.stdin.readline

n = int(input())
for num in range(1, n):
    if sum(map(int, str(num))) + num == n:
        print(num)
        break
else:
    print(0)