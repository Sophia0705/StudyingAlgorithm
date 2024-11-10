from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    ans = 1  # 이동 거리
    time = True  # True: 낮, False: 밤

    while q:
        # 현재 큐에 있는 모든 위치를 처리 (같은 시간대의 이동을 한번에 처리)
        for _ in range(len(q)):
            i, j, w = q.popleft()  # 현재 위치와 부순 벽의 개수

            if i == n - 1 and j == m - 1:  # 도착
                print(ans)
                return

            for dy, dx in dir:
                ni, nj = i + dy, j + dx

                # 범위 체크 및 더 적은 벽을 부수고 방문한 경우가 있는지 체크
                if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] <= w:
                    continue

                # 1. 빈 공간인 경우 - 낮/밤 관계없이 이동 가능
                if graph[ni][nj] == '0':
                    q.append((ni, nj, w))
                    visited[ni][nj] = w

                # 2. 벽인 경우 - 벽을 더 부술 수 있을 때만
                elif w < k:
                    if not time:  # 밤이면 현재 위치에서 대기
                        q.append((i, j, w))
                    else:  # 낮이면 벽 부수고 이동
                        visited[ni][nj] = w
                        q.append((ni, nj, w + 1))

        ans += 1
        time = not time  # 낮/밤 전환

    print(-1)
    return


n, m, k = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[k + 1 for _ in range(m)] for _ in range(n)]  # 방문 배열은 부순 벽의 개수만 저장
visited[0][0] = 0
dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
bfs((0, 0, 0))