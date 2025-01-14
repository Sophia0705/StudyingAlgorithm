import sys
input = sys.stdin.readline

k, n = map(int, input().split())    # k: 가지고 있는 랜선 개수, n: 필요한 랜선 개수
length = [int(input()) for _ in range(k)]

s, e = 1, max(length)
ans = 0

while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for l in length:
        cnt += l//mid

    if cnt >= n:
        ans = mid
        s = mid+1
    else:
        e = mid-1

print(ans)