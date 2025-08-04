# 16118. 달빛 여우
import sys
input = sys.stdin.readline
import heapq

def di_fox(s, dist):
    Q = []
    dist[s] = 0
    heapq.heappush(Q, (0, s))
    while Q:
        distance, now = heapq.heappop(Q)
        if distance > dist[now]:
            continue
        for i in G[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))

def di_wolf(s, dist):
    Q = []
    heapq.heappush(Q, (0, s, 0))
    while Q:
        distance, now, state = heapq.heappop(Q)
        if distance > dist[state][now]:
            continue
        for i in G[now]:
            cost = distance + (i[1]//2 if state == 0 else i[1]*2)
            if cost < dist[(state-1)%2][i[0]]:
                dist[(state-1)%2][i[0]] = cost
                heapq.heappush(Q, (cost, i[0], (state-1)%2))

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    G[a].append((b, d*2))   # 늑대연산 편하게(//2, *2)
    G[b].append((a, d*2))
dist_fox = [float('inf')]*(N+1)
dist_wolf = [[float('inf')]*(N+1) for _ in range(2)]
di_fox(1, dist_fox)
di_wolf(1, dist_wolf)

ans = 0
for i in range(2, N+1):
    if dist_fox[i] < min(dist_wolf[0][i], dist_wolf[1][i]):
        ans += 1
print(ans)