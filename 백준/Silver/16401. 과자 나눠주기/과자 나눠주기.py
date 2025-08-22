# 16401. 과자 나눠주기
import sys
input = sys.stdin.readline

M, N = map(int, input().split())    # M명 조카, N개 과자
lengths = list(map(int, input().split()))
s, e = 1, max(lengths)
ans = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 0 # 과자 나눠줄 개수
    for leng in lengths:
        cnt += leng // mid
        if cnt >= M:
            break
    if cnt < M:
        e = mid -1
    else:
        ans = mid
        s = mid +1

print(ans)