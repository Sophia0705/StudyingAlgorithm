# 11403. 경로 찾기
# 모든 정점(i, j)에서 i -> j 가는 길이가 양수인 경로 있는지(1)? 없는지(0)?

import sys
input = sys.stdin.readline

N = int(input())    # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(N)] # 인접 행렬
answer = [[0]*N for _ in range(N)]

for i in range(N):
    visited = [False] * N
    st = [i]
    while st:
        current = st.pop()
        for next in range(N):
            if graph[current][next] == 1 and not visited[next]:
                visited[next] = True
                st.append(next)
                answer[i][next] = 1

for r in answer:
    print(*r)