from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_col = [0] * m   # 열별로 석유 저장
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    def bfs(s, e):
        size = 0    # 현재 석유 덩어리 크기 += 포함된 열들
        cols = set()    # 중복 방지
        Q = deque([(s, e)])
        visited[s][e] = True
        
        while Q:
            r, c = Q.popleft()
            size += 1
            cols.add(c) # 현재 열 추가
            
            # 상하좌우
            for dr, dc in move:
                nr = r + dr
                nc = c + dc
                # 범위, 방문 체크
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and land[nr][nc] > 0:
                    visited[nr][nc] = True
                    Q.append((nr, nc))
        # 석유 덩어리 포함된 모든 열에 더하기
        for col in cols:
            oil_col[col] += size
    
    # 석유 탐색
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] > 0:
                bfs(i, j)
    
    return max(oil_col)