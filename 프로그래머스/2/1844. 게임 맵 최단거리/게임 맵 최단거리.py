from collections import deque

def solution(maps):
    def bfs(x, y):
        # 이동
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # 큐
        Q = deque()
        Q.append((x, y))  # 시작점 추가

        n = len(maps)
        m = len(maps[0])

        # 큐가 빌 때까지
        while Q:
            x, y = Q.popleft()

            # 상하좌우 이동
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 벗어나는지 체크
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                # 벽인지(0) 체크
                if maps[nx][ny] == 0:
                    continue

                # 처음 지나가는 길이면 거리 계산하고 다시 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    Q.append((nx, ny))

        # 상대 팀 진영 (제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[n-1][m-1]

    # 시작점이 벽인 경우
    if maps[0][0] == 0:
        return -1
    
    answer = bfs(0, 0)

    # 상대 팀 진영에 도착할 수 없을 때
    return -1 if answer == 1 else answer
