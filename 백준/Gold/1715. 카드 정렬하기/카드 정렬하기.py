# 1715. 카드 정렬하기

import sys
input = sys.stdin.readline
import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
H = []
for card in cards:
    heapq.heappush(H, card)
temp = []
# 1. 항상 가장 작은 두 카드 묶음을 먼저 합치고(작은 묶음은 여러 번 재사용 되니까)
# 2. 합친 결과 다시 후보에 넣고
# 3. 모든 카드가 하나의 묶음이 될 때까지 반복
while H:
    if len(H) == 1:
        break
    t1 = heapq.heappop(H)
    t2 = heapq.heappop(H)
    temp.append(t1+t2)
    heapq.heappush(H, t1+t2)
print(sum(temp))