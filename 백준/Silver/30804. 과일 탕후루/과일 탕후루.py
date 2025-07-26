# 30804. 과일 탕후루
import sys
input = sys.stdin.readline

N = int(input())
Sn = list(map(int, input().split()))
ans, left, types = 0, 0, 0
cnt = {}

for right in range(N):
    if Sn[right] in cnt:
        cnt[Sn[right]] += 1
    else:
        cnt[Sn[right]] = 1
        types += 1

    while types > 2:
        cnt[Sn[left]] -= 1
        if cnt[Sn[left]] == 0:
            del cnt[Sn[left]]
            types -= 1
        left += 1
        
    ans = max(ans, right - left + 1)
    
print(ans)