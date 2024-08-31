# 2667 단지 번호 붙이기
from collections import deque

N, K = map(int, input().split())    # 시작, 목표 위치
max = 100000 # 수빈이랑 동생 점 최대 +1(인덱스 오류나니까 따로 max 잡는 게 낫다)
visited = [0] * (max + 1)   # 각 위치에 도달하는 데 걸리는 최소 시간

def bfs(s):
    Q = deque()
    Q.append(s) # 시작 위치 큐에 추가

    while Q:
        current = Q.popleft()   # 현재 위치
        if current == K:    # 동생 찾았으면
            return visited[current]   # 최소 시간 반환
        for i in (current+1, current-1, current*2): # 수빈이가 움직일 수 있는 범위
            if 0 <= i < (max+1) and not visited[i]:
                visited[i] = visited[current] + 1   # 카운트 더하듯이
                Q.append(i) # 다음 위치 큐에 추가

print(bfs(N))