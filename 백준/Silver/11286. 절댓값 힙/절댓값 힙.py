# 11286. 절댓값 힙
import heapq
import sys
input = sys.stdin.readline

n = int(input())    # n: 연산 개수
absheap = []
# 1. 배열에 정수x 넣기
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(absheap, (abs(x), x))
# 2. 배열에서 절댓값이 가장 작은 값 출력, 그 값 제거
# (절댓값 가장 작은 값 여러 개면 음수 우선 제거) --> 어차피 abs(x) 같으면 원래 값인 x 기준으로 정렬
    else:
        if absheap:
            t = heapq.heappop(absheap)
            print(t[1])
        else:
            print(0)
