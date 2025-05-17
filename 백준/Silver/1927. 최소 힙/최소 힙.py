# 1927. 최소 힙
import heapq
import sys
input = sys.stdin.readline

x = int(input())
minheap = []
for _ in range(x):
    n = int(input())
    if n == 0:
        if minheap:
            print(heapq.heappop(minheap))
        else:
            print(0)
    else:
        heapq.heappush(minheap, n)