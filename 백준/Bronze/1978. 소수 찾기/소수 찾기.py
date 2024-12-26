# 1978 소수 찾기
def check(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

ans = 0
for num in arr:
    if check(num):
        ans += 1

print(ans)