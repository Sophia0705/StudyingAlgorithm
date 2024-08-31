import sys
input = sys.stdin.readline

N = int(input())     # 전체 사람 수
s, e = map(int, input().split())    # 촌수 계산 할 사람 번호
M = int(input())     # 부모-자식 간 관계의 개수
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)  # 양방향 연결
    G[b].append(a)

visited = [False] * (N+1) # 사람 수만큼 visited 배열 사용(0번 인덱스 버리기)

# s -> e로 가는 동안 촌수 세야 함
def dfs(v, depth):
    if v == e:  # 현재 노드가 목표 노드면 촌수 반환
        return depth
    visited[v] = True
    for i in G[v]:
        if not visited[i]:
            result = dfs(i, depth + 1)  # 촌수 1 증가
            if result != -1:    # 자식 노드 중 하나에서 목표 찾았는지 - dfs 호출 결과가 -1이 아니면 목표 노드 찾은 것
                return result   # 상위 노드로 결과 값 보내기 위한 것
    return -1   # 못찾으면 -1
print(dfs(s, 0))
