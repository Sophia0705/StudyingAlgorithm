# 31464. 초콜릿 괴도 코코(Sweet)
import sys
input = sys.stdin.readline

N = int(input())
grid = [input().strip() for _ in range(N)]

id = [-1] * (N*N)
V = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == '#':
            id[i*N + j] = V
            V += 1

Coords = [None] * V
edges = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == '#':
            cur = id[i*N + j]
            Coords[cur] = (i, j)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == '#':
                    nb = id[ni*N + nj]
                    if cur < nb:
                        edges.append((cur, nb))

# Unionfind
def make_parent(n):
    return list(range(n))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def unite(parent, a, b):
    pa, pb = find(parent, a), find(parent, b)
    if pa == pb:
        return False
    parent[pb] = pa
    return True

# 후보 위치 찾기
candidates = []
for v in range(V):
    parent = make_parent(V)
    added_edges = 0
    cycle_found = False

    for u, w in edges:
        if v in (u, w):
            continue
        if not unite(parent, u, w):
            cycle_found = True
            break
        added_edges += 1

    if cycle_found or added_edges != V - 2:
        continue

    comp = -1
    connected = True
    for i in range(V):
        if i == v:
            continue
        root = find(parent, i)
        if comp == -1:
            comp = root
        elif comp != root:
            connected = False
            break
    if not connected:
        continue

    r, c = Coords[v]
    candidates.append((r + 1, c + 1))

candidates.sort()
print(len(candidates))
for r, c in candidates:
    print(r, c)