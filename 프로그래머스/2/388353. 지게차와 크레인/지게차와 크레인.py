from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(storage, requests):
    N = len(storage) + 2
    M = len(storage[0]) + 2

    # 패딩 포함한 그래프 생성 ('.': 빈공간, 'A'~'Z': 컨테이너, '0': 외부공기, '1': 내부공기)
    graph = [['0'] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            graph[i][j] = storage[i - 1][j - 1]

    # 외부공기 확장 BFS ('1'을 만나면 '0'으로 바꾸기)
    def update():
        visited = [[False] * M for _ in range(N)]
        q = deque([(0, 0)])
        visited[0][0] = True
        while q:
            y, x = q.popleft()
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    if graph[ny][nx] == '0':
                        q.append((ny, nx))
                        visited[ny][nx] = True
                    elif graph[ny][nx] == '1':
                        graph[ny][nx] = '0'
                        q.append((ny, nx))
                        visited[ny][nx] = True

    # 요청 처리
    for request in requests:
        target = request[0]

        if len(request) == 1:  # 지게차 요청
            remove_list = []
            for i in range(1, N - 1):
                for j in range(1, M - 1):
                    if graph[i][j] == target:
                        for di, dj in dirs:
                            ni, nj = i + di, j + dj
                            if graph[ni][nj] == '0':  # 외부공기 접촉 여부
                                remove_list.append((i, j))
                                break
            for i, j in remove_list:
                graph[i][j] = '0'
            update()

        else:  # 크레인 요청 (2글자)
            for i in range(1, N - 1):
                for j in range(1, M - 1):
                    if graph[i][j] == target:
                        graph[i][j] = '1'
            update()

    # 최종 컨테이너 개수 세기 ('0', '1'이 아닌 것만 셈)
    answer = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if graph[i][j] not in ('0', '1'):
                answer += 1

    return answer