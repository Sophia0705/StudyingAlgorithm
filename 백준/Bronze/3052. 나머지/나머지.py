import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]
ans = set()
for num in arr:
    ans.add(num%42)

print(len(ans))